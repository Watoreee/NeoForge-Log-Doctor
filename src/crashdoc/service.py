"""Application logic behind the API routes (PLAN 6.0: api.py -> service.py -> llm/retrieval/agent)."""

from __future__ import annotations

import threading
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from functools import lru_cache

from crashdoc.config import CHAT_MODEL, EMBED_MODEL, get_settings
from crashdoc.preprocess import parse_log, preprocess_log
from crashdoc.redact import redact_text

MAX_LOG_BYTES = 10 * 1024 * 1024  # hard cap protecting the server (PLAN 10 MB); preprocessing trims to the model budget

Pipeline = Callable[[str], Iterator[dict]]


def health() -> dict[str, object]:
    """Liveness plus the config facts worth seeing at a glance. Never includes the key or base URL."""
    settings = get_settings()
    return {
        "status": "ok",
        "chat_model": CHAT_MODEL,
        "embed_model": EMBED_MODEL,
        "proxy_configured": settings.proxy_configured,
        "replay": settings.replay,
    }


@dataclass
class Rejected(Exception):
    """Input the pipeline will not process (the API turns it into a 4xx before any stream starts)."""

    status: int
    message: str


def check_input(log: str) -> str:
    """Size and content checks. Returns the log text, or raises Rejected (413 too big, 422 not a log)."""
    if not log or not log.strip():
        raise Rejected(422, "The log is empty.")
    if len(log.encode("utf-8", errors="replace")) > MAX_LOG_BYTES:
        raise Rejected(
            413, f"The log is larger than {MAX_LOG_BYTES // 2**20} MB. Paste the crash report or the relevant part."
        )
    if parse_log(log).format == "rejected":
        raise Rejected(
            422, "This does not look like a Minecraft crash report or log (no timestamps, levels or exceptions)."
        )
    return log


_lock = threading.Lock()


@lru_cache(maxsize=1)
def _shared():
    """The LLM and the index, created once on first use (the index load takes a moment)."""
    from crashdoc.llm import LLM
    from crashdoc.retrieval.index import Index

    return LLM(), Index.load()


@lru_cache(maxsize=1)
def _manifest() -> dict[str, dict]:
    import json

    from crashdoc.config import REPO_ROOT

    rows = json.loads((REPO_ROOT / "data" / "processed" / "manifest.json").read_text(encoding="utf-8"))
    return {r["doc_id"]: r for r in rows}


def citation_links(doc_ids: list[str]) -> list[dict]:
    """doc_id -> title + url for the page. Unknown ids (the backend never produces any) are skipped."""
    rows = _manifest()
    return [{"doc_id": d, "title": rows[d]["title"], "url": rows[d]["url"]} for d in doc_ids if d in rows]


def default_pipeline(log: str) -> Iterator[dict]:
    """redact -> preprocess -> extraction -> agent loop. Yields facts / tool_call / tool_result / final events."""
    from crashdoc.agent.loop import run_agent_events

    with _lock:
        llm, index = _shared()
    original_bytes = len(log.encode("utf-8", errors="replace"))
    redacted = redact_text(log)
    pre = preprocess_log(redacted.text)
    for event in run_agent_events(llm, index, pre, redacted.text):
        if event["event"] == "facts":
            event["data"]["redactions"] = dict(redacted.counts)  # counts only, never the values
            event["data"]["original_bytes"] = original_bytes  # "truncated" is set by the agent loop
        if event["event"] == "final":
            event["data"]["citation_links"] = citation_links(event["data"]["diagnosis"]["citations"])
        yield {"event": event["event"], "data": event["data"]}
