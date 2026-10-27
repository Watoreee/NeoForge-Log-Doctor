"""The only module that talks to the proxy (PLAN 6.0): chat completions and embeddings.

Every call goes: cache lookup -> (replay mode: a miss is an error) -> paid call with backoff on
429 -> response written to the on-disk cache at once -> usage counted.

Why each piece exists:
- Cache: temperature 0 through a proxy isn't guaranteed deterministic, so cached responses make
  eval numbers reproducible (PLAN 7.4). Each paid response is saved as soon as it returns, so an
  interrupted eval resumes from the cache and never repeats a paid call.
- Usage counting + backoff: the proxy allows 150 requests / 200k tokens per window per key
  (docs/proxy-notes.md), so every run reports what it spent and waits politely on 429s.
- Replay mode (CRASHDOC_REPLAY=1): live-defence fallback; serves only from the cache (PLAN 6.9).

Callers must only pass redacted text: whatever is sent here is written to the cache, which is committed.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import openai

from crashdoc.config import (
    BACKOFF_BASE_S,
    BACKOFF_MAX_S,
    CHAT_MODEL,
    EMBED_BATCH_SIZE,
    EMBED_MODEL,
    MAX_RETRIES,
    REQUEST_TIMEOUT_S,
    Settings,
    get_settings,
    use_os_trust_store,
)

RETRYABLE_ERRORS = (openai.RateLimitError, openai.APIConnectionError, openai.InternalServerError)


class CacheMissError(RuntimeError):
    """Replay mode needed a response that isn't in the cache."""


class ProxyNotConfiguredError(RuntimeError):
    """A paid call was needed but OPENAI_API_KEY / OPENAI_BASE_URL aren't set."""


@dataclass
class Usage:
    """What one run spent. `*_requests` count every HTTP attempt, retries included."""

    chat_requests: int = 0
    chat_cache_hits: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    embed_requests: int = 0
    embed_inputs_sent: int = 0
    embed_cache_hits: int = 0
    # The proxy reports embedding usage as a character count, and doesn't charge it to the token limit.
    embed_reported_usage_chars: int = 0
    retries: int = 0
    rate_limited: int = 0

    def summary(self) -> dict[str, int]:
        """Flat dict for the results file, with the two numbers the rate limits are about."""
        out = asdict(self)
        out["total_requests"] = self.chat_requests + self.embed_requests
        out["total_chat_tokens"] = self.prompt_tokens + self.completion_tokens
        return out


@dataclass
class ChatResult:
    """One assistant turn. `message` is the dict to append to the conversation in an agent loop."""

    content: str | None
    tool_calls: list[dict[str, Any]]
    message: dict[str, Any]
    cached: bool


@dataclass
class LLM:
    """Cached, usage-counted access to the proxy. One instance per run, so `usage` is per run."""

    settings: Settings = field(default_factory=get_settings)
    client: Any = None  # an openai.OpenAI; created lazily so /health and replay never need a key
    sleep: Any = time.sleep  # injectable so tests don't actually wait
    usage: Usage = field(default_factory=Usage)

    # ------------------------------------------------------------ chat

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        prompt_version: str,
        tools: list[dict[str, Any]] | None = None,
        max_tokens: int = 1024,
    ) -> ChatResult:
        """One temperature-0 chat completion, served from the cache when possible.

        `prompt_version` is part of the cache key: bump it whenever the prompt template changes.
        """
        request = {
            "model": CHAT_MODEL,
            "messages": messages,
            "tools": tools,
            "max_tokens": max_tokens,
            "temperature": 0,
        }
        path = self._cache_path("chat", {**request, "prompt_version": prompt_version})
        cached = _read_json(path)
        if cached is not None:
            self.usage.chat_cache_hits += 1
            return _chat_result(cached["message"], cached=True)
        self._refuse_in_replay("chat", prompt_version)

        kwargs = {k: v for k, v in request.items() if v is not None}
        resp = self._with_retries(lambda: self._client().chat.completions.create(**kwargs), "chat_requests")
        message = resp.choices[0].message.model_dump(exclude_none=True)
        if resp.usage:
            self.usage.prompt_tokens += resp.usage.prompt_tokens or 0
            self.usage.completion_tokens += resp.usage.completion_tokens or 0
        _write_json(path, {"prompt_version": prompt_version, "model": resp.model, "message": message})
        return _chat_result(message, cached=False)

    # ------------------------------------------------------------ embeddings

    def embed(self, texts: list[str], *, use_cache: bool = True) -> list[list[float]]:
        """Embed texts in order. Misses are sent in batches of EMBED_BATCH_SIZE.

        Query embeddings use the cache (needed for replay). Corpus embeddings pass use_cache=False:
        they are saved once as embeddings.npy instead of thousands of cache files.
        """
        vectors: dict[str, list[float]] = {}
        misses: list[str] = []
        for text in dict.fromkeys(texts):  # dedupe, keep order
            cached = _read_json(self._cache_path("embed", _embed_key(text))) if use_cache else None
            if cached is not None:
                vectors[text] = cached["embedding"]
                self.usage.embed_cache_hits += 1
            else:
                misses.append(text)
        if misses:
            self._refuse_in_replay("embedding", f"{len(misses)} input(s)")
        for start in range(0, len(misses), EMBED_BATCH_SIZE):
            batch = misses[start : start + EMBED_BATCH_SIZE]
            for text, vector in zip(batch, self._embed_batch(batch), strict=True):
                vectors[text] = vector
                if use_cache:
                    entry = {"model": EMBED_MODEL, "embedding": vector}
                    _write_json(self._cache_path("embed", _embed_key(text)), entry)
        return [vectors[t] for t in texts]

    def _embed_batch(self, batch: list[str]) -> list[list[float]]:
        """One paid embeddings call; vectors re-sorted by `index` to match the input order."""
        resp = self._with_retries(
            lambda: self._client().embeddings.create(model=EMBED_MODEL, input=batch), "embed_requests"
        )
        self.usage.embed_inputs_sent += len(batch)
        if resp.usage:
            self.usage.embed_reported_usage_chars += resp.usage.prompt_tokens or 0
        return [d.embedding for d in sorted(resp.data, key=lambda d: d.index)]

    # ------------------------------------------------------------ plumbing

    def _client(self):
        """Create the OpenAI client on first paid call only."""
        if self.client is None:
            if not self.settings.proxy_configured:
                raise ProxyNotConfiguredError("Set OPENAI_API_KEY and OPENAI_BASE_URL (see .env.example).")
            use_os_trust_store()
            self.client = openai.OpenAI(
                api_key=self.settings.api_key,
                base_url=self.settings.base_url,
                max_retries=0,  # we retry ourselves, so every attempt is counted
                timeout=REQUEST_TIMEOUT_S,
            )
        return self.client

    def _with_retries(self, call, counter: str):
        """Run a paid call; on 429 honour retry-after, else back off exponentially. Counts every attempt."""
        for attempt in range(MAX_RETRIES + 1):
            setattr(self.usage, counter, getattr(self.usage, counter) + 1)
            try:
                return call()
            except RETRYABLE_ERRORS as e:
                if attempt == MAX_RETRIES:
                    raise
                if isinstance(e, openai.RateLimitError):
                    self.usage.rate_limited += 1
                self.usage.retries += 1
                self.sleep(retry_delay(e, attempt))
        raise AssertionError("unreachable")

    def _refuse_in_replay(self, kind: str, detail: str) -> None:
        if self.settings.replay:
            raise CacheMissError(f"Replay mode: no cached {kind} response ({detail}). No proxy call was made.")

    def _cache_path(self, kind: str, key_material: dict[str, Any]) -> Path:
        digest = hashlib.sha256(_canonical(key_material).encode("utf-8")).hexdigest()
        return self.settings.cache_dir / kind / digest[:2] / f"{digest}.json"


def retry_delay(error: Exception, attempt: int) -> float:
    """Seconds to wait: the server's retry-after if it sent one, else 2, 4, 8 ... capped at 60."""
    response = getattr(error, "response", None)
    header = response.headers.get("retry-after") if response is not None else None
    try:
        if header is not None:
            return max(0.0, float(header))
    except ValueError:
        pass  # an HTTP-date retry-after; fall back to backoff
    return min(BACKOFF_MAX_S, BACKOFF_BASE_S * 2**attempt)


def _embed_key(text: str) -> dict[str, str]:
    return {"model": EMBED_MODEL, "input": text}


def _chat_result(message: dict[str, Any], cached: bool) -> ChatResult:
    return ChatResult(
        content=message.get("content"),
        tool_calls=message.get("tool_calls") or [],
        message=message,
        cached=cached,
    )


def _canonical(obj: Any) -> str:
    """Stable JSON for cache keys: sorted keys, no whitespace differences."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None


def _write_json(path: Path, data: dict[str, Any]) -> None:
    """Atomic write (temp file + rename), so an interrupted run never leaves a half-written cache entry."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)
