# Proxy notes (Phase 0, PLAN.md section 4)

Probed with `python scripts/probe_proxy.py` on 2026-10-27 18:35 UTC (two full runs, identical outcomes).
Embedding batches probed on 2026-10-28 with `python scripts/probe_proxy.py --only embedding_batches`.
Raw output: `docs/proxy-probe-results.json`. The proxy is LiteLLM in front of an OpenAI-compatible server
(identified from its error messages).

## Summary

| Question | Answer | Decision |
|---|---|---|
| Model id `gemma-4-E4B-it` accepted? | Yes | Use as-is |
| System role accepted? | Yes | Prompts may use a system message |
| Embedding model listed? | Yes: `bge-m3`, 1024-dim | Use the proxy's `bge-m3`; no local fallback, no reduced mode |
| Embedding batch limit? | 64 inputs per call OK (largest tried) | Batch size 32 in `build_index.py` |
| `response_format` JSON mode? | No: accepted but ignored | Prompt for JSON, strip fence, pydantic, one repair |
| Native `tools=[...]` reliable? | Yes: 5/5, plus a full round trip | Native tool calling (allow-list still enforced) |
| Context window? | 65,536 tokens (prompt + output) | Log text budget: 6k Gemma tokens (see below) |
| `stream=True` works? | Yes | Not used (we stream events, not tokens) |
| Latency? | Chat: ~0.1 s small, 2.4 s at 58k tokens. Embeddings: ~1 s per input | Fine for chat; corpus embedding is slow, so batch |
| Rate limits? | 150 requests and 200,000 tokens per API key | Hard constraint: count, back off, cache, resume (below) |

## Details

**Model id.** `models.list()` returns exactly `[bge-m3, gemma-4-E4B-it]`. A chat call with `model="gemma-4-E4B-it"`
succeeds and reports `model = gemma-4-E4B-it`.

**Embeddings.** `embeddings.create(model="bge-m3", ...)` returns 1024-dim vectors.
- Batch probe: 8, 32 and 64 inputs per call all succeeded, with every vector returned and `index` in input order.
  Larger batches were not tried. Inputs were ~370 bge-m3 tokens each (~1,440 characters), about one chunk.
- Time grows linearly with batch size: 9.4 s for 8, 32.2 s for 32, 63.5 s for 64 (about 1 s per input). A corpus
  of ~3,000 chunks therefore takes ~50 min to embed. Chosen batch size: **32**. That keeps each call well under
  any proxy timeout and needs only ~94 requests for 3,000 chunks.
- **The proxy's `usage.prompt_tokens` for embeddings equals the input's character count, not tokens** (11,504 /
  46,918 / 94,246 reported, matching the character totals exactly; the real bge-m3 counts are 2,869 / 11,617 /
  23,623). `llm.py` records this number under a separate name and never adds it to chat tokens.
- Rate-limit accounting, measured from the `x-ratelimit-api_key-remaining-*` headers: a 4,999-character embedding
  call reduced remaining *tokens* by only 1, but reduced remaining *requests* by 1, while a 13-token chat call
  reduced remaining tokens by 14. So **embeddings cost requests, not tokens**; chat costs both.

**JSON mode.** `json_object`, `json_schema` and prompt-only all return the *same* output, wrapped in a
```` ```json ```` markdown fence: 0/3 parse as-is, 3/3 parse after stripping the fence. The `json_schema` variant
required a `confidence` key that the prompt never mentioned; it appeared 0/3 times, so the schema is not enforced.
Fallback (PLAN 6.3): ask for JSON in the prompt, strip a markdown fence, parse, validate with pydantic, one repair
retry that feeds back the validation error, then regex-derived facts. `response_format` is not sent (it does
nothing, and sending it would suggest otherwise).

**Tool calling.** 5/5 trials chose `get_mod_info` with valid JSON args naming the right mod (`jei`, `create`,
`sodium`, `ae2`, `curios`). A full round trip (assistant tool call, then a `role: tool` result) produced a correct
text answer. Decision: native tool calling, still validating tool name and args with pydantic against the
allow-list. If the real agent prompts are flaky, switch to the JSON text protocol (PLAN 6.6) at once.

**Context window.** The proxy's error message states "maximum context length is 65536 tokens" (prompt + output).
A needle at the start of the prompt was recalled at 58,338 server-counted prompt tokens.
- `tiktoken` cl100k **undercounts Gemma tokens by ~21%** (server/cl100k = 1.17 to 1.22 across the ladder).
- **Budget (set by the human):** the log text sent to the LLM is at most **~6,000 Gemma tokens**, counted as
  cl100k tokens × 1.25. We never budget anywhere near the 65k window; the rest is headroom for instructions,
  retrieved chunks, the agent transcript and output. See `docs/decisions.md`.

**Streaming.** 50 content chunks, first after 0.10 s, total 0.66 s. Not needed.

**Rate limits.**
- Response headers: `x-ratelimit-api_key-limit-requests: 150` and `x-ratelimit-api_key-limit-tokens: 200000`.
- A burst of 8 concurrent chat calls all succeeded (no 429).
- **Window: not stated by the proxy and not yet confirmed. Assumed to be per minute (LiteLLM's usual rpm/tpm
  default) until course staff confirm.** Evidence for a short window: remaining requests were back at 149 of 150
  a few minutes after runs that had used 20+ requests. This does not prove a 1-minute window.
- Until the window is confirmed, the limits are treated as hard constraints:
  - `llm.py` counts requests and tokens per run (chat and embeddings separately) for the results file.
  - It honours `retry-after` on 429 errors, else exponential backoff.
  - Every paid response is written to the on-disk cache immediately, so a rerun of `run_eval.py` resumes
    from the cache and never repeats a paid call.
  - Before any eval run, the full eval matrix's requests and tokens are estimated and checked with the human.

## Caveats

- **Tool calling depends on the prompt.** In a Day 1 smoke test of `llm.py` (2026-10-28), the bare prompt "Is the
  mod 'jei' installed? Check." with the same tool and no system message got a text refusal ("I do not have the
  capability to check…") instead of a tool call. The probe's 5/5 used "A crash log mentions the mod '…'. Check
  whether it is installed." So the agent's system prompt must say that it has tools and when to use them, and the
  agent tests must cover a turn that ends with no tool call and no diagnosis.
- Probe prompts are tiny or synthetic. Real extraction prompts on long logs may behave differently; pydantic
  validation + repair is the guard.
- The probe run itself used several 10k–60k-token chat calls. Do not rerun the full probe casually.
