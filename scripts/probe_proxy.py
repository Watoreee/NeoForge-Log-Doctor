"""Phase 0 proxy probe (PLAN.md section 4).

Answers, against the real class proxy, every question the rest of the build depends on:
model id, embeddings, JSON mode, native tool calling, context window, streaming, latency.

Usage:
    python scripts/probe_proxy.py [--max-context-tokens 131072] [--out docs/proxy-probe-results.json]
    python scripts/probe_proxy.py --only embedding_batches   # rerun some probes, keep the rest

Config comes from the environment only (OPENAI_API_KEY, OPENAI_BASE_URL). A local .env is
loaded with python-dotenv if present. The key and base URL are never printed or written.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from pathlib import Path

MODEL = "gemma-4-E4B-it"  # fixed by the assignment; never change
EMBED_HINTS = ("embed", "bge", "e5", "gte", "nomic", "minilm", "mpnet")
TOOL_TRIAL_MOD_IDS = ["jei", "create", "sodium", "ae2", "curios"]


# ---------------------------------------------------------------- setup


def load_config() -> tuple[str, str]:
    """Read key + base URL from env (after .env). Exit, never guess, if either is missing."""
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    base = os.environ.get("OPENAI_BASE_URL", "").strip()
    missing = [n for n, v in (("OPENAI_API_KEY", key), ("OPENAI_BASE_URL", base)) if not v]
    if missing:
        sys.exit(f"Missing env var(s): {', '.join(missing)}. Copy .env.example to .env and fill them in.")
    return key, base


def use_os_trust_store() -> None:
    """Verify TLS against the OS certificate store; Python's certifi bundle fails on some networks."""
    try:
        import truststore

        truststore.inject_into_ssl()
    except ImportError:
        pass


def make_client(key: str, base: str):
    """One client, no automatic retries, so rate limits and errors are observed as they are."""
    from openai import OpenAI

    return OpenAI(api_key=key, base_url=base, max_retries=0, timeout=180)


class Scrubber:
    """Removes the key and base URL from any text before it is printed or saved."""

    def __init__(self, key: str, base: str):
        self.secrets = [s for s in (key, base, base.rstrip("/")) if s]

    def __call__(self, text: object, limit: int | None = 500) -> str:
        out = str(text)
        for s in self.secrets:
            out = out.replace(s, "<redacted>")
        return out[:limit] if limit else out


def chat(client, messages, **kw):
    """A temperature-0 chat call to the fixed model; returns (response, seconds)."""
    t0 = time.perf_counter()
    resp = client.chat.completions.create(model=MODEL, messages=messages, temperature=0, **kw)
    return resp, time.perf_counter() - t0


# ---------------------------------------------------------------- probes


def probe_models(client, scrub) -> dict:
    """Q1 + Q2 (listing): which model ids does the proxy expose?"""
    try:
        models = client.models.list().data
    except Exception as e:  # noqa: BLE001 - the probe records every failure
        return {"ok": False, "error": scrub(e)}
    ids = sorted(m.id for m in models)
    extra = {m.id: m.model_extra for m in models if getattr(m, "model_extra", None)}
    return {
        "ok": True,
        "ids": ids,
        "target_listed": MODEL in ids,
        "embedding_candidates": [i for i in ids if any(h in i.lower() for h in EMBED_HINTS)],
        "metadata": extra,
    }


def probe_model_accepted(client, scrub) -> dict:
    """Q1: does a real chat call with the exact id succeed?"""
    try:
        resp, secs = chat(client, [{"role": "user", "content": "Reply with exactly: OK"}], max_tokens=10)
    except Exception as e:  # noqa: BLE001
        return {"accepted": False, "error": scrub(e)}
    return {
        "accepted": True,
        "reported_model": resp.model,
        "reply": (resp.choices[0].message.content or "")[:50],
        "seconds": round(secs, 2),
    }


def probe_system_role(client, scrub) -> dict:
    """Some Gemma deployments reject the system role; the prompts need to know."""
    msgs = [
        {"role": "system", "content": "You answer with one word only."},
        {"role": "user", "content": "What colour is the sky on a clear day?"},
    ]
    try:
        resp, _ = chat(client, msgs, max_tokens=10)
        return {"accepted": True, "reply": (resp.choices[0].message.content or "")[:50]}
    except Exception as e:  # noqa: BLE001
        return {"accepted": False, "error": scrub(e)}


def probe_embeddings(client, scrub, candidates: list[str]) -> dict:
    """Q2: does any listed embedding model actually return vectors?"""
    results = {}
    for name in candidates:
        try:
            resp = client.embeddings.create(model=name, input=["NoClassDefFoundError mixin jei"])
            results[name] = {"ok": True, "dim": len(resp.data[0].embedding)}
        except Exception as e:  # noqa: BLE001
            results[name] = {"ok": False, "error": scrub(e)}
    return {"tried": results, "any_working": any(r["ok"] for r in results.values())}


JSON_PROMPT = (
    "Classify this Minecraft log line. Respond with a JSON object with keys "
    '"category" (one of "missing_dependency", "mixin_conflict", "other") and "mod_ids" (list of strings).\n'
    "Log: Mod jei requires mod_x 1.2 or above, which is not installed."
)


def _load_object(text: str | None, strip_fences: bool = False) -> dict | None:
    """Parse a JSON object; optionally strip a ```json ... ``` markdown fence first."""
    text = (text or "").strip()
    if strip_fences and text.startswith("```"):
        text = text.split("\n", 1)[-1].rsplit("```", 1)[0]
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


def probe_json_mode(client, scrub, trials: int = 3) -> dict:
    """Q3: response_format json_object / json_schema, vs. prompt-only JSON (the fallback).

    The schema requires a "confidence" key the prompt never mentions, so its presence
    shows the proxy actually enforces the schema rather than ignoring response_format.
    """
    schema = {
        "name": "facts",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "category": {"type": "string"},
                "mod_ids": {"type": "array", "items": {"type": "string"}},
                "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
            },
            "required": ["category", "mod_ids", "confidence"],
            "additionalProperties": False,
        },
    }
    variants = {
        "json_object": {"response_format": {"type": "json_object"}},
        "json_schema": {"response_format": {"type": "json_schema", "json_schema": schema}},
        "prompt_only": {},
    }
    out = {}
    for name, kw in variants.items():
        raw_ok, stripped_ok, has_confidence, errors, sample = 0, 0, 0, [], None
        for _ in range(trials):
            try:
                resp, _ = chat(client, [{"role": "user", "content": JSON_PROMPT}], max_tokens=200, **kw)
                text = resp.choices[0].message.content
                sample = (text or "")[:200]
                raw_ok += _load_object(text) is not None
                obj = _load_object(text, strip_fences=True)
                stripped_ok += obj is not None
                has_confidence += bool(obj and "confidence" in obj)
            except Exception as e:  # noqa: BLE001
                errors.append(scrub(e))
        out[name] = {
            "parsed_raw": raw_ok,
            "parsed_after_fence_strip": stripped_ok,
            "has_schema_only_key": has_confidence,
            "trials": trials,
            "sample": sample,
            "errors": errors[:1],
        }
    return out


TOOL_SPEC = [
    {
        "type": "function",
        "function": {
            "name": "get_mod_info",
            "description": "Look up whether a mod is installed in the user's modpack.",
            "parameters": {
                "type": "object",
                "properties": {"mod_id": {"type": "string", "description": "The mod id, e.g. 'jei'."}},
                "required": ["mod_id"],
            },
        },
    }
]


def _tool_trial(client, scrub, mod_id: str) -> dict:
    """One native tool-call attempt; valid = right tool name + parseable args naming the mod."""
    msgs = [{"role": "user", "content": f"A crash log mentions the mod '{mod_id}'. Check whether it is installed."}]
    try:
        resp, secs = chat(client, msgs, tools=TOOL_SPEC, max_tokens=200)
    except Exception as e:  # noqa: BLE001
        return {"mod_id": mod_id, "valid": False, "error": scrub(e)}
    calls = resp.choices[0].message.tool_calls or []
    if not calls:
        return {
            "mod_id": mod_id,
            "valid": False,
            "reason": "no tool_calls",
            "content": (resp.choices[0].message.content or "")[:200],
        }
    fn = calls[0].function
    try:
        args = json.loads(fn.arguments or "")
    except json.JSONDecodeError:
        return {"mod_id": mod_id, "valid": False, "reason": "args not JSON", "raw_args": fn.arguments[:200]}
    valid = fn.name == "get_mod_info" and str(args.get("mod_id", "")).lower() == mod_id
    return {"mod_id": mod_id, "valid": valid, "name": fn.name, "args": args, "seconds": round(secs, 2)}


def _tool_round_trip(client, scrub) -> dict:
    """Agent loops send the tool result back; check the model then answers in text."""
    msgs = [
        {"role": "user", "content": "A crash log mentions the mod 'jei'. Check whether it is installed, then tell me."}
    ]
    try:
        resp, _ = chat(client, msgs, tools=TOOL_SPEC, max_tokens=200)
        calls = resp.choices[0].message.tool_calls or []
        if not calls:
            return {"ok": False, "reason": "no tool call on first turn"}
        msgs.append(resp.choices[0].message.model_dump(exclude_none=True))
        msgs.append({"role": "tool", "tool_call_id": calls[0].id, "content": json.dumps({"installed": False})})
        resp2, _ = chat(client, msgs, tools=TOOL_SPEC, max_tokens=200)
        msg2 = resp2.choices[0].message
        return {"ok": bool(msg2.content) and not msg2.tool_calls, "final_text": (msg2.content or "")[:200]}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": scrub(e)}


def probe_tools(client, scrub) -> dict:
    """Q4: is native tools=[...] calling reliable over 5 trials (+ one full round trip)?"""
    trials = [_tool_trial(client, scrub, m) for m in TOOL_TRIAL_MOD_IDS]
    return {
        "valid": sum(t["valid"] for t in trials),
        "trials": len(trials),
        "details": trials,
        "round_trip": _tool_round_trip(client, scrub),
    }


NEEDLE = "The secret code word is HEMATITE-417."
FILLER_LINE = "[12:00:00] [Render thread/INFO] [minecraft/Minecraft]: Loaded chunk section without errors.\n"


def _context_prompt(target_tokens: int, enc) -> str:
    """A needle at the start + filler up to ~target tokens, so we test real use of the window."""
    per_line = len(enc.encode(FILLER_LINE))
    lines = max(1, (target_tokens - 100) // per_line)
    question = "What is the secret code word stated at the very start? Reply with the code word only."
    return f"{NEEDLE}\n{FILLER_LINE * lines}\n{question}"


def probe_context(client, scrub, max_tokens: int) -> dict:
    """Q5: grow the prompt until the proxy refuses; record server-counted prompt tokens + needle recall."""
    import tiktoken

    enc = tiktoken.get_encoding("cl100k_base")
    ladder = [t for t in (2_000, 8_000, 16_000, 32_000, 48_000, 64_000, 100_000, 128_000, 200_000) if t <= max_tokens]
    steps = []
    for target in ladder:
        prompt = _context_prompt(target, enc)
        try:
            resp, secs = chat(client, [{"role": "user", "content": prompt}], max_tokens=20)
            answer = resp.choices[0].message.content or ""
            steps.append(
                {
                    "target_cl100k": target,
                    "server_prompt_tokens": getattr(resp.usage, "prompt_tokens", None),
                    "needle_found": "HEMATITE-417" in answer.upper(),
                    "seconds": round(secs, 2),
                }
            )
        except Exception as e:  # noqa: BLE001
            steps.append({"target_cl100k": target, "error": scrub(e)})
            break
    ok = [s for s in steps if "error" not in s]
    return {"steps": steps, "largest_ok_server_tokens": max((s["server_prompt_tokens"] or 0 for s in ok), default=0)}


def probe_streaming(client, scrub) -> dict:
    """Q6: does stream=True yield incremental chunks?"""
    t0 = time.perf_counter()
    try:
        stream = client.chat.completions.create(
            model=MODEL,
            temperature=0,
            stream=True,
            max_tokens=60,
            messages=[{"role": "user", "content": "Count from 1 to 20, separated by spaces."}],
        )
        first, chunks, text = None, 0, []
        for ev in stream:
            if ev.choices and ev.choices[0].delta.content:
                first = first or time.perf_counter() - t0
                chunks += 1
                text.append(ev.choices[0].delta.content)
    except Exception as e:  # noqa: BLE001
        return {"works": False, "error": scrub(e)}
    return {
        "works": chunks > 1,
        "content_chunks": chunks,
        "time_to_first_s": round(first or 0, 2),
        "total_s": round(time.perf_counter() - t0, 2),
        "text": "".join(text)[:120],
    }


def _one_small_call(client, scrub) -> dict:
    """A tiny call that also captures rate-limit headers, if the proxy sends any."""
    t0 = time.perf_counter()
    try:
        raw = client.chat.completions.with_raw_response.create(
            model=MODEL, temperature=0, max_tokens=5, messages=[{"role": "user", "content": "Reply with OK"}]
        )
        headers = {k: v for k, v in raw.headers.items() if "ratelimit" in k.lower() or k.lower() == "retry-after"}
        return {"ok": True, "seconds": time.perf_counter() - t0, "headers": headers}
    except Exception as e:  # noqa: BLE001
        status = getattr(e, "status_code", None)
        return {"ok": False, "seconds": time.perf_counter() - t0, "status": status, "error": scrub(e)}


def probe_latency(client, scrub, sequential: int = 5, burst: int = 8) -> dict:
    """Q7: typical latency (sequential) and whether a small concurrent burst hits 429s."""
    seq = [_one_small_call(client, scrub) for _ in range(sequential)]
    with ThreadPoolExecutor(max_workers=burst) as pool:
        bursts = list(pool.map(lambda _: _one_small_call(client, scrub), range(burst)))
    secs = [r["seconds"] for r in seq if r["ok"]]
    return {
        "sequential_ok": len(secs),
        "sequential_median_s": round(statistics.median(secs), 2) if secs else None,
        "sequential_max_s": round(max(secs), 2) if secs else None,
        "burst_size": burst,
        "burst_ok": sum(r["ok"] for r in bursts),
        "burst_statuses": sorted({str(r.get("status")) for r in bursts if not r["ok"]}),
        "burst_errors": [r["error"] for r in bursts if not r["ok"]][:2],
        "rate_limit_headers": next((r["headers"] for r in seq + bursts if r.get("headers")), {}),
    }


# ---------------------------------------------------------------- main


EMBED_MODEL = "bge-m3"
EMBED_BATCH_SIZES = (8, 32, 64)


def _chunk_like_text(i: int) -> str:
    """A distinct ~300-token text, roughly the size of one corpus chunk."""
    body = " ".join(
        f"Mod{i}_{j} failed to load because dependency lib{j} version {i}.{j} is missing." for j in range(20)
    )
    return f"Chunk {i}. {body}"


def probe_embedding_batches(client, scrub, sizes=EMBED_BATCH_SIZES) -> dict:
    """How many inputs does one embeddings call accept? Grow the batch; stop at the first failure."""
    steps = []
    for size in sizes:
        texts = [_chunk_like_text(i) for i in range(size)]
        t0 = time.perf_counter()
        try:
            resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
        except Exception as e:  # noqa: BLE001
            steps.append({"batch": size, "ok": False, "error": scrub(e)})
            break
        indices = [d.index for d in resp.data]
        steps.append(
            {
                "batch": size,
                "ok": len(resp.data) == size,
                "vectors": len(resp.data),
                "in_order": indices == list(range(size)),
                "dim": len(resp.data[0].embedding),
                "prompt_tokens": getattr(resp.usage, "prompt_tokens", None),
                "seconds": round(time.perf_counter() - t0, 2),
            }
        )
    return {"model": EMBED_MODEL, "steps": steps, "largest_ok": max((s["batch"] for s in steps if s["ok"]), default=0)}


def run_all(client, scrub, max_context_tokens: int, only: set[str] | None = None, previous: dict | None = None) -> dict:
    """Run the probes in a fixed order; each records its own errors instead of aborting.

    With `only`, run just those probes and merge into `previous`, so earlier results are kept.
    """
    results = dict(previous or {}) if only else {"model": MODEL}
    results["run_at_utc" if not only else "partial_run_at_utc"] = datetime.now(UTC).isoformat(timespec="seconds")
    steps = [
        ("models", lambda: probe_models(client, scrub)),
        ("model_accepted", lambda: probe_model_accepted(client, scrub)),
        ("system_role", lambda: probe_system_role(client, scrub)),
        ("embeddings", lambda: probe_embeddings(client, scrub, results["models"].get("embedding_candidates", []))),
        ("json_mode", lambda: probe_json_mode(client, scrub)),
        ("tools", lambda: probe_tools(client, scrub)),
        ("streaming", lambda: probe_streaming(client, scrub)),
        ("latency", lambda: probe_latency(client, scrub)),
        ("context", lambda: probe_context(client, scrub, max_context_tokens)),
        ("embedding_batches", lambda: probe_embedding_batches(client, scrub)),
    ]
    for name, fn in steps:
        if only and name not in only:
            continue
        print(f"[probe] {name} ...", flush=True)
        results[name] = fn()
        print(scrub(json.dumps(results[name], indent=2, default=str), limit=1500), flush=True)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-context-tokens", type=int, default=131_072)
    parser.add_argument("--out", default="docs/proxy-probe-results.json")
    parser.add_argument("--only", help="comma-separated probe names to (re)run, merged into --out")
    args = parser.parse_args()

    key, base = load_config()
    use_os_trust_store()
    scrub = Scrubber(key, base)
    out = Path(args.out)
    only = set(args.only.split(",")) if args.only else None
    previous = json.loads(out.read_text(encoding="utf-8")) if only and out.exists() else None
    results = run_all(make_client(key, base), scrub, args.max_context_tokens, only, previous)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(scrub(json.dumps(results, indent=2, default=str), limit=None), encoding="utf-8")
    print(f"[probe] wrote {out}")


if __name__ == "__main__":
    main()
