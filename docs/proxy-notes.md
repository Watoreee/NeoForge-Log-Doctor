# Proxy notes (Phase 0, PLAN.md section 4)

Probed with `python scripts/probe_proxy.py` on 2026-10-27 18:35 UTC (two full runs, identical outcomes).
Raw output: `docs/proxy-probe-results.json`. The proxy is LiteLLM in front of an OpenAI-compatible server
(identified from error messages).

## Answers

| Question | Answer | Evidence | Decision / fallback |
|---|---|---|---|
| Exact model id `gemma-4-E4B-it` accepted? | **Yes** | Listed by `models.list()`; a chat call returns `model = gemma-4-E4B-it` | Use it as-is |
| System role accepted? | **Yes** | System + user message call succeeded | Prompts may use a system message |
| Embedding model listed? | **Yes: `bge-m3`** | `models.list()` = `[bge-m3, gemma-4-E4B-it]`; `embeddings.create` returns a **1024-dim** vector | Use proxy `bge-m3` for corpus + query embeddings. Local `sentence-transformers` fallback **not needed**; reduced mode not needed |
| `response_format` JSON mode works? | **No (accepted but ignored)** | `json_object`, `json_schema` and prompt-only all return the *same* output, wrapped in a ```` ```json ```` fence: 0/3 parse raw, 3/3 parse after fence-stripping. The schema required a `confidence` key the prompt never mentioned; it appeared 0/3 times, so the schema is not enforced | **Fallback:** prompt for JSON, strip a markdown fence, parse, validate with pydantic, one repair retry feeding back the error, then regex facts (PLAN 6.3). Don't send `response_format` (it does nothing and would suggest otherwise) |
| Native `tools=[...]` reliable over ~5 trials? | **Yes** | 5/5 calls chose `get_mod_info` with valid JSON args naming the right mod; a full round trip (tool result sent back with `role: tool`) produced a correct final text answer | **Native tool calling** for the agent loop. Still validate name + args with pydantic (allow-list); the JSON text protocol remains the switch-over if the real agent prompts make it flaky |
| Real context window? | **65,536 tokens** (prompt + output) | Server error: "maximum context length is 65536 tokens". Needle at the start was recalled at 58,338 server prompt tokens; 64k cl100k (~77k server tokens) was rejected | Truncation budget well below this (set in `config.py`; leave room for retrieved chunks, the agent transcript, and output). **cl100k undercounts Gemma tokens by ~21%** (server/cl100k = 1.17–1.22), so any cl100k-based budget needs that margin |
| `stream=True` works? | **Yes** | 50 content chunks, first after 0.10 s, total 0.66 s | Not used (we stream events, not tokens) |
| Latency | **Fast** | Tiny calls: median 0.11 s, max 0.13 s (5 sequential). 58k-token prompt: 2.4 s | Eval runtime is not a concern |
| Rate limits | **150 requests, 200,000 tokens per API key** | Headers `x-ratelimit-api_key-limit-requests: 150`, `...-limit-tokens: 200000`. A burst of 8 concurrent calls: 8/8 OK, no 429 | Window is not stated in the headers; **assumed per minute** (LiteLLM's usual rpm/tpm). One near-full-context call uses ~30% of the token budget, so eval runs go sequentially through the response cache (PLAN 7.4), with backoff on 429 |

## Notes and caveats

- Probe calls are tiny or synthetic. Real extraction prompts on long logs may behave differently; the
  pydantic validation + repair path is the guard.
- Embeddings were tested with a single input. Batch size limits for embedding the corpus are untested and are
  checked when `build_index.py` is written.
- Tokenizer for chunking (PLAN 5): the embedding model runs on the proxy, not locally. The choice between
  `tiktoken` cl100k (approximation) and bge-m3's own tokenizer is made with the chunker and recorded in
  `docs/decisions.md`.
