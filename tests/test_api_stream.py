"""POST /diagnose: limits, SSE format, error events, real incremental delivery, redaction, and the JS SSE parser."""

from __future__ import annotations

import json
import shutil
import socket
import subprocess
import threading
import time

import httpx
import pytest
import uvicorn
from fastapi.testclient import TestClient

from crashdoc import service
from crashdoc.api import create_app
from crashdoc.config import REPO_ROOT

LOG = (
    "[17:37:04] [main/INFO]: a\n[17:37:05] [main/ERROR]: Mod ID: 'curios', Requested by: 'ars_nouveau', "
    "Expected range: '[1,)', Actual version: '[MISSING]'\n[17:37:06] [main/INFO]: c\n"
)
FINAL = {
    "diagnosis": {
        "culprit_mod_id": "curios",
        "category": "missing_dependency",
        "explanation": "x",
        "fix_steps": [],
        "citations": [],
        "confidence": "low",
    },
    "source": "llm",
}


def fake_pipeline(log):
    yield {"event": "facts", "data": {"facts": {"error_category": "missing_dependency", "suspect_mod_ids": ["curios"]}}}
    yield {"event": "tool_call", "data": {"name": "search_docs", "arguments": "{}"}}
    yield {"event": "tool_result", "data": {"name": "search_docs", "ok": True, "preview": "..."}}
    yield {"event": "final", "data": FINAL}


@pytest.fixture
def client():
    return TestClient(create_app(fake_pipeline))


def parse_sse(text: str) -> list[tuple[str, dict]]:
    out = []
    for block in text.strip().split("\n\n"):
        lines = block.split("\n")
        out.append((lines[0].removeprefix("event: "), json.loads(lines[1].removeprefix("data: "))))
    return out


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["status"] == "ok" and "api_key" not in r.text.lower()


def test_streams_the_four_event_kinds_in_order_with_sse_headers(client):
    r = client.post("/diagnose", json={"log": LOG})
    assert r.status_code == 200 and r.headers["content-type"].startswith("text/event-stream")
    events = parse_sse(r.text)
    assert [e for e, _ in events] == ["facts", "tool_call", "tool_result", "final"]
    assert events[-1][1]["diagnosis"]["culprit_mod_id"] == "curios"
    assert '"token"' not in r.text and "delta" not in r.text  # structured events only, no raw model tokens


def test_the_cap_is_10_mb():
    assert service.MAX_LOG_BYTES == 10 * 1024 * 1024


def test_log_over_10mb_is_413(client):
    big = "[17:37:04] [main/INFO]: " + "x" * (service.MAX_LOG_BYTES + 10) + "\n"
    assert client.post("/diagnose", json={"log": big}).status_code == 413
    assert client.post("/diagnose", content=b"x" * (service.MAX_LOG_BYTES + 2 * 1024 * 1024)).status_code == 413


def test_a_log_just_under_the_limit_is_accepted(client):
    line = "[17:37:04] [main/INFO]: " + "y" * 90 + "\n"
    log = line * ((service.MAX_LOG_BYTES - 1000) // len(line))
    assert len(log.encode()) < service.MAX_LOG_BYTES and client.post("/diagnose", json={"log": log}).status_code == 200


def test_a_log_over_200kb_is_accepted_truncated_for_the_model_and_streams_normally(monkeypatch):
    """The real default pipeline (redact -> preprocess -> extraction -> agent) with a scripted model."""
    from tests.test_agent import EXTRACTION, FakeLLM, Reply, final_json, tiny_index, tool

    filler = "".join(f"[17:37:{i % 60:02d}] [main/INFO]: loading number {i} " + "z" * 60 + "\n" for i in range(3000))
    log = filler + LOG + filler
    size = len(log.encode())
    assert size > 200 * 1024
    llm = FakeLLM(Reply(EXTRACTION), tool("check_compat", {}), final_json(citations=[]))
    monkeypatch.setattr(service, "_shared", lambda: (llm, tiny_index()))
    r = TestClient(create_app(service.default_pipeline)).post("/diagnose", json={"log": log})
    assert r.status_code == 200
    events = parse_sse(r.text)
    assert [e for e, _ in events] == ["facts", "tool_call", "tool_result", "final"]
    facts = events[0][1]
    assert facts["truncated"] is True and facts["original_bytes"] == size
    sent = llm.calls[0]["messages"][-1]["content"]  # what the model actually received
    assert len(sent.encode()) < size / 4 and "curios" in sent
    assert events[-1][1]["diagnosis"]["culprit_mod_id"] == "curios"


def test_a_short_log_is_not_marked_truncated(monkeypatch):
    from tests.test_agent import EXTRACTION, FakeLLM, Reply, final_json, tiny_index, tool

    llm = FakeLLM(Reply(EXTRACTION), tool("check_compat", {}), final_json(citations=[]))
    monkeypatch.setattr(service, "_shared", lambda: (llm, tiny_index()))
    events = parse_sse(TestClient(create_app(service.default_pipeline)).post("/diagnose", json={"log": LOG}).text)
    assert events[0][1]["truncated"] is False and events[0][1]["original_bytes"] == len(LOG.encode())


@pytest.mark.parametrize("body", [{"log": ""}, {"log": "hello there, what a lovely day"}, {"log": 5}, {}])
def test_empty_or_non_log_input_is_422(client, body):
    assert client.post("/diagnose", json=body).status_code == 422


def test_malformed_json_is_400(client):
    assert client.post("/diagnose", content=b"{not json").status_code == 400


def test_a_pipeline_failure_after_the_stream_started_is_an_error_event_not_a_stack_trace():
    def boom(log):
        yield {"event": "facts", "data": {"facts": {}}}
        raise RuntimeError("secret internal detail /home/x")

    r = TestClient(create_app(boom)).post("/diagnose", json={"log": LOG})
    events = parse_sse(r.text)
    assert events[-1][0] == "error" and "secret" not in r.text and "Traceback" not in r.text


def test_web_page_and_parser_are_served(client):
    assert "createSseParser" in client.get("/web/sse.js").text
    page = client.get("/").text
    assert "ReadableStream" in page or "getReader" in page and "EventSource" not in page


# --- real server: events must arrive while the pipeline is still running ------------------------------------------


def test_events_arrive_incrementally_over_a_real_connection():
    def slow(log):
        for name in ("facts", "tool_call", "tool_result", "final"):
            yield {"event": name, "data": FINAL if name == "final" else {"name": name}}
            time.sleep(0.4)

    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    server = uvicorn.Server(uvicorn.Config(create_app(slow), host="127.0.0.1", port=port, log_level="error"))
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    try:
        for _ in range(100):
            if server.started:
                break
            time.sleep(0.05)
        assert server.started
        arrivals, start = [], time.perf_counter()
        with httpx.stream("POST", f"http://127.0.0.1:{port}/diagnose", json={"log": LOG}, timeout=20) as resp:
            for line in resp.iter_lines():
                if line.startswith("event: "):
                    arrivals.append((line[7:], time.perf_counter() - start))
    finally:
        server.should_exit = True
        thread.join(timeout=5)
    assert [e for e, _ in arrivals] == ["facts", "tool_call", "tool_result", "final"]
    gaps = [b - a for (_, a), (_, b) in zip(arrivals, arrivals[1:], strict=False)]
    assert all(g > 0.25 for g in gaps), arrivals  # spread out, not delivered in one burst at the end
    assert arrivals[0][1] < arrivals[-1][1] - 0.9  # the first event did not wait for the pipeline to finish


# --- redaction happens before anything reaches the model -------------------------------------------------------------


def test_default_pipeline_redacts_the_log_before_the_agent_sees_it(monkeypatch):
    seen = {}

    def fake_events(llm, index, pre, text, **kw):
        seen["text"], seen["pre"] = text, pre.text
        yield {"event": "facts", "data": {"facts": {}}}
        yield {"event": "final", "data": {"diagnosis": {"citations": []}}}

    monkeypatch.setattr(service, "_shared", lambda: (object(), object()))
    monkeypatch.setattr("crashdoc.agent.loop.run_agent_events", fake_events)
    log = "[17:37:04] [main/INFO]: Setting user: Steve_99\n[17:37:05] [main/ERROR]: C:\\Users\\Bob\\x failed\n[17:37:06] [main/INFO]: z\n"  # noqa: E501
    events = list(service.default_pipeline(log))
    assert "Steve_99" not in seen["text"] and "Bob" not in seen["pre"]
    assert events[0]["data"]["redactions"]["player_name"] >= 1


# --- the JS SSE parser (the page's only non-trivial client code), run under node -------------------------------------


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_js_sse_parser_handles_events_split_across_arbitrary_chunks():
    script = (
        "const {createSseParser}=require('./web/sse.js');const out=[];const p=createSseParser(e=>out.push(e));"
        'const s=\'event: facts\\ndata: {"a":1}\\n\\nevent: final\\r\\ndata: {"b":\\ndata: 2}\\n\\n: comment\\n\\nevent: x\\ndata: z\\n\\n\';'  # noqa: E501
        "for(let i=0;i<s.length;i+=3)p.push(s.slice(i,i+3));"
        "console.log(JSON.stringify(out));"
    )
    res = subprocess.run(["node", "-e", script], capture_output=True, text=True, cwd=REPO_ROOT, timeout=30)
    assert res.returncode == 0, res.stderr
    assert json.loads(res.stdout) == [
        {"event": "facts", "data": '{"a":1}'},
        {"event": "final", "data": '{"b":\n2}'},
        {"event": "x", "data": "z"},
    ]
