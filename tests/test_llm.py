"""llm.py: cache, usage counting, 429 backoff, replay mode. A fake client stands in for the proxy."""

from __future__ import annotations

import httpx
import openai
import pytest
from openai.types import CreateEmbeddingResponse
from openai.types.chat import ChatCompletion

from crashdoc.config import EMBED_BATCH_SIZE, Settings
from crashdoc.llm import LLM, CacheMissError, ProxyNotConfiguredError, retry_delay


def _completion(content="hello", tool_calls=None, prompt_tokens=10, completion_tokens=2) -> ChatCompletion:
    message = {"role": "assistant", "content": content}
    if tool_calls:
        message["tool_calls"] = tool_calls
    return ChatCompletion.model_validate(
        {
            "id": "x",
            "object": "chat.completion",
            "created": 0,
            "model": "gemma-4-E4B-it",
            "choices": [{"index": 0, "finish_reason": "stop", "message": message}],
            "usage": {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
            },
        }
    )


def _embedding_response(texts: list[str]) -> CreateEmbeddingResponse:
    # Returned in reverse order on purpose: llm.py must re-sort by index.
    data = [{"object": "embedding", "index": i, "embedding": [float(len(t)), float(i)]} for i, t in enumerate(texts)]
    return CreateEmbeddingResponse.model_validate(
        {
            "object": "list",
            "model": "bge-m3",
            "data": list(reversed(data)),
            "usage": {"prompt_tokens": sum(map(len, texts)), "total_tokens": sum(map(len, texts))},
        }
    )


def _rate_limit_error(retry_after: str | None = None) -> openai.RateLimitError:
    headers = {"retry-after": retry_after} if retry_after else {}
    response = httpx.Response(429, headers=headers, request=httpx.Request("POST", "http://proxy.test"))
    return openai.RateLimitError("rate limited", response=response, body=None)


class FakeClient:
    """Mimics the parts of openai.OpenAI that llm.py uses; can fail the first N calls."""

    def __init__(self, failures: list[Exception] | None = None):
        self.failures = list(failures or [])
        self.chat_calls: list[dict] = []
        self.embed_calls: list[list[str]] = []
        self.chat = self
        self.completions = self
        self.embeddings = _Embeddings(self)

    def create(self, **kwargs):
        self.chat_calls.append(kwargs)
        if self.failures:
            raise self.failures.pop(0)
        return _completion()


class _Embeddings:
    def __init__(self, owner: FakeClient):
        self.owner = owner

    def create(self, model, input):
        self.owner.embed_calls.append(list(input))
        return _embedding_response(list(input))


def _settings(tmp_path, replay=False, configured=True) -> Settings:
    return Settings(
        api_key="test-key" if configured else None,
        base_url="http://proxy.test/v1" if configured else None,
        cache_dir=tmp_path / "cache",
        replay=replay,
    )


MESSAGES = [{"role": "user", "content": "hi"}]


def test_chat_second_call_is_served_from_cache(tmp_path):
    client = FakeClient()
    llm = LLM(settings=_settings(tmp_path), client=client)
    first = llm.chat(MESSAGES, prompt_version="v1")
    second = llm.chat(MESSAGES, prompt_version="v1")
    assert (first.content, first.cached) == ("hello", False)
    assert (second.content, second.cached) == ("hello", True)
    assert len(client.chat_calls) == 1
    assert llm.usage.chat_requests == 1 and llm.usage.chat_cache_hits == 1


def test_cache_survives_a_new_run_so_reruns_resume(tmp_path):
    """A rerun (new LLM instance, same cache dir) must not repeat a paid call."""
    LLM(settings=_settings(tmp_path), client=FakeClient()).chat(MESSAGES, prompt_version="v1")
    client = FakeClient()
    rerun = LLM(settings=_settings(tmp_path), client=client)
    assert rerun.chat(MESSAGES, prompt_version="v1").cached
    assert client.chat_calls == [] and rerun.usage.chat_requests == 0


def test_prompt_version_and_params_change_the_cache_key(tmp_path):
    client = FakeClient()
    llm = LLM(settings=_settings(tmp_path), client=client)
    llm.chat(MESSAGES, prompt_version="v1")
    llm.chat(MESSAGES, prompt_version="v2")
    llm.chat(MESSAGES, prompt_version="v2", max_tokens=50)
    assert len(client.chat_calls) == 3


def test_chat_request_is_temperature_zero_and_fixed_model(tmp_path):
    client = FakeClient()
    LLM(settings=_settings(tmp_path), client=client).chat(MESSAGES, prompt_version="v1")
    assert client.chat_calls[0]["temperature"] == 0
    assert client.chat_calls[0]["model"] == "gemma-4-E4B-it"
    assert "tools" not in client.chat_calls[0]  # None params are not sent


def test_usage_counts_tokens(tmp_path):
    llm = LLM(settings=_settings(tmp_path), client=FakeClient())
    llm.chat(MESSAGES, prompt_version="v1")
    summary = llm.usage.summary()
    assert summary["prompt_tokens"] == 10 and summary["completion_tokens"] == 2
    assert summary["total_chat_tokens"] == 12 and summary["total_requests"] == 1


def test_tool_calls_are_returned_and_cached(tmp_path, monkeypatch):
    call = {"id": "c1", "type": "function", "function": {"name": "get_mod_info", "arguments": '{"mod_id": "jei"}'}}
    client = FakeClient()
    monkeypatch.setattr(client, "create", lambda **kw: _completion(content=None, tool_calls=[call]))
    llm = LLM(settings=_settings(tmp_path), client=client)
    live = llm.chat(MESSAGES, prompt_version="v1")
    cached = llm.chat(MESSAGES, prompt_version="v1")
    for result in (live, cached):
        assert result.tool_calls[0]["function"]["name"] == "get_mod_info"
        assert result.message["role"] == "assistant"


def test_429_honours_retry_after_then_succeeds(tmp_path):
    slept = []
    client = FakeClient(failures=[_rate_limit_error("7"), _rate_limit_error()])
    llm = LLM(settings=_settings(tmp_path), client=client, sleep=slept.append)
    assert llm.chat(MESSAGES, prompt_version="v1").content == "hello"
    assert slept == [7.0, 4.0]  # server's retry-after, then exponential backoff (attempt 1 -> 4 s)
    assert llm.usage.chat_requests == 3  # every attempt counts against the request limit
    assert llm.usage.rate_limited == 2 and llm.usage.retries == 2


def test_gives_up_after_max_retries(tmp_path, monkeypatch):
    monkeypatch.setattr("crashdoc.llm.MAX_RETRIES", 2)
    client = FakeClient(failures=[_rate_limit_error()] * 5)
    llm = LLM(settings=_settings(tmp_path), client=client, sleep=lambda s: None)
    with pytest.raises(openai.RateLimitError):
        llm.chat(MESSAGES, prompt_version="v1")
    assert llm.usage.chat_requests == 3


def test_retry_delay_backoff_is_capped():
    assert retry_delay(_rate_limit_error(), 0) == 2.0
    assert retry_delay(_rate_limit_error(), 10) == 60.0
    assert retry_delay(_rate_limit_error("Wed, 21 Oct 2026 07:28:00 GMT"), 1) == 4.0


def test_replay_miss_raises_and_makes_no_network_call(tmp_path, monkeypatch):
    def no_network(*args, **kwargs):
        raise AssertionError("replay mode must not create a client")

    monkeypatch.setattr(openai, "OpenAI", no_network)
    llm = LLM(settings=_settings(tmp_path, replay=True))
    with pytest.raises(CacheMissError):
        llm.chat(MESSAGES, prompt_version="v1")
    with pytest.raises(CacheMissError):
        llm.embed(["query text"])
    assert llm.usage.summary()["total_requests"] == 0


def test_replay_serves_cached_chat_and_embeddings(tmp_path):
    LLM(settings=_settings(tmp_path), client=FakeClient()).chat(MESSAGES, prompt_version="v1")
    LLM(settings=_settings(tmp_path), client=FakeClient()).embed(["query text"])
    replay = LLM(settings=_settings(tmp_path, replay=True))
    assert replay.chat(MESSAGES, prompt_version="v1").cached
    assert replay.embed(["query text"]) == [[10.0, 0.0]]


def test_missing_proxy_config_is_a_clear_error(tmp_path):
    llm = LLM(settings=_settings(tmp_path, configured=False))
    with pytest.raises(ProxyNotConfiguredError):
        llm.chat(MESSAGES, prompt_version="v1")


def test_embed_batches_misses_and_keeps_input_order(tmp_path):
    client = FakeClient()
    llm = LLM(settings=_settings(tmp_path), client=client)
    texts = [f"text number {i}" for i in range(EMBED_BATCH_SIZE + 5)]
    vectors = llm.embed(texts)
    assert [len(b) for b in client.embed_calls] == [EMBED_BATCH_SIZE, 5]
    assert vectors == [[float(len(t)), float(i % EMBED_BATCH_SIZE)] for i, t in enumerate(texts)]
    assert llm.usage.embed_requests == 2 and llm.usage.embed_inputs_sent == len(texts)
    assert llm.usage.embed_reported_usage_chars == sum(map(len, texts))


def test_embed_cache_and_dedup(tmp_path):
    client = FakeClient()
    llm = LLM(settings=_settings(tmp_path), client=client)
    llm.embed(["a", "b", "a"])
    llm.embed(["b", "c"])
    assert client.embed_calls == [["a", "b"], ["c"]]
    assert llm.usage.embed_cache_hits == 1


def test_embed_without_cache_writes_nothing(tmp_path):
    llm = LLM(settings=_settings(tmp_path), client=FakeClient())
    llm.embed(["corpus chunk"], use_cache=False)
    assert not (tmp_path / "cache").exists()
