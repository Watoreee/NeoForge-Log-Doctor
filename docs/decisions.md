# Design decisions and deviations

PLAN.md is frozen. Every deviation, clarification, and design choice is recorded here (2–3 lines each).

## Setup (Day 1)

**Repo root = project root, not `crashdoc/`.** PLAN 6.0 shows the layout under a `crashdoc/` folder; the
repo root *is* that folder (README, PLAN.md, `src/crashdoc/`, ... sit at the top level). The Python package
is still `src/crashdoc/`.

**`.env` loaded with python-dotenv.** Config stays env-only (PLAN 2): code reads `os.environ`; `python-dotenv`
just copies a local, git-ignored `.env` into the environment for convenience. Real env vars take precedence.

**TLS via the OS trust store (`truststore`).** On the dev machine, Python's bundled `certifi` CAs fail to verify
HTTPS (`CERTIFICATE_VERIFY_FAILED`) while the OS store succeeds (curl/git work), so something on the network
re-signs TLS. We call `truststore.inject_into_ssl()` instead of disabling verification. Verification stays on.

**Exact version pins in `requirements.txt`.** They are the versions development and evaluation ran on, so a clean
clone reproduces the same environment.

**Ruff line length 120, rules E/F/W/I/UP/B.** Configured in `pyproject.toml`.

## Phase 0 outcomes (details in `docs/proxy-notes.md`)

**Embedding model: proxy `bge-m3` (1024-dim); reduced mode not needed.** The proxy lists and serves `bge-m3`, so
dense retrieval, the cosine floor and hybrid fusion all run as planned. The local `sentence-transformers` fallback
stays a documented fallback only; it was not needed or exercised.

**Native tool calling.** 5/5 trials produced the right tool with valid args, and a full tool-result round trip
worked. The agent uses `tools=[...]`, still validating name + args against the allow-list with pydantic. If real
agent prompts turn out flaky, switch to the JSON text protocol (PLAN 6.6) at once.

**No `response_format`; prompt-for-JSON + fence strip + pydantic + one repair.** The proxy accepts
`response_format` but does not enforce it (a schema-only key never appeared; output is always ```` ```json ````
fenced). So `llm.py` asks for JSON in the prompt, strips a markdown fence, and validates with pydantic (PLAN 6.3).

**Context window 65,536 tokens; cl100k undercounts Gemma by ~21%.** Truncation budgets get a safety margin
for this whenever they are counted with `tiktoken`.

**Tool calling is prompt-sensitive.** A bare user prompt got a text refusal instead of a tool call (proxy-notes,
caveats). The agent prompt will state the available tools and when to use them. A run that ends with neither a
tool call nor a diagnosis is handled like any other turn: it counts toward `max_steps`, and the forced final call follows.

## Rate limits and budgets (set by the human, Day 1)

**Rate limits are hard constraints until the window is confirmed.** The proxy allows 150 requests and 200k tokens
per key; the window is unknown and assumed per minute. Embeddings cost requests but not tokens (measured;
proxy-notes). So:
- `llm.py` counts every HTTP attempt (retries included) and chat tokens per run, in `Usage.summary()`. `run_eval.py`
  will write it into each results file.
- On 429 it honours `retry-after`, else waits 2, 4, 8 … s (capped at 60), up to 6 retries.
- Each paid response is written to the cache immediately with an atomic write. A rerun after a crash or a
  429 give-up resumes from the cache and never repeats a paid call (tested: a new `LLM` instance with the same
  cache dir makes zero requests).
- **Before any eval run (Day 5)**, estimate requests and tokens for the full eval matrix and stop to check with
  the human if it exceeds the limits, saying what to cut.

**Log text budget: at most 6,000 Gemma tokens, counted as cl100k × 1.25.** The window is 65,536, but we never
budget near it. A small log input leaves room for instructions, retrieved chunks and the agent transcript, keeps
each call far below the 200k-token rate limit, and suits a 4B model, which is weak on long inputs.
`tokens.estimate_llm_tokens()` implements the count and `config.LOG_TOKEN_BUDGET` holds the number.

**Embedding batch size 32.** 8, 32 and 64 inputs per call all worked. Time is ~1 s per input, so 32 keeps a call
at ~30 s, and 3,000 chunks need ~94 requests. Corpus embeddings skip the per-text cache (`use_cache=False`) and are
saved once as `embeddings.npy`. Query embeddings are cached, so replay works.

## Code layout and data conventions (Day 1)

**Chunking tokenizer: bge-m3's own, tokenizer files only.** `AutoTokenizer.from_pretrained("BAAI/bge-m3")` downloads
only the tokenizer files plus a 687-byte `config.json`, with no model weights (checked in the HF cache), so PLAN 5's
"embedding model's own tokenizer" option applies. It is pinned to revision `5617a9f61b028005a4858fdac845db406aefb181`
in `config.py`. Chunk token counts are therefore exact for the embedding model. The LLM budget still uses
cl100k × 1.25 (Gemma's tokenizer isn't available).

**`pip install -e .` (src layout).** Scripts, tests and uvicorn all import `crashdoc` the same way, with no
`sys.path` hacks. Use `--no-build-isolation` on networks where pip's TLS fails (setuptools is already installed).

**Label logic lives in `src/crashdoc/labels.py`; `scripts/validate_labels.py` is a thin CLI.** This adds a module
not shown in PLAN 6.0. It keeps the checks unit-testable and reusable by `run_eval.py`.

**Gold layout: `data/gold/<split>/<log_id>.json` + `<log_id>.<ext>`.** The label file name must equal `log_id`,
and the redacted log sits next to it. The validator checks both.

**`relevant_doc_ids: null` means "not judged yet."** PLAN fills relevance on Day 3–4, but labels exist earlier. So
`null` = unjudged (allowed, warned) and `[]` = judged with nothing relevant, which needs `support_search`. With
`--strict` (Day 3 split freeze, Day 5 gate), unjudged is an error. The rule that copies per-scenario judgments into every
log (PLAN 6.7) is added with the pool export on Day 3.

**Category stratification is a warning, an error under `--strict`.** A category with ≥2 scenario groups missing from dev or
test is flagged. Whether the split can satisfy it depends on the real logs, so the human decides.

## Redaction (Day 2)

**Redacted output goes to git-ignored `data/staging/` first, not `data/gold/`.** `redact_logs.py` writes there by
default; files move to `data/gold/` or `data/demo/` only after the human has read each one. A redaction miss
therefore can't be committed by accident. (PLAN 6.2 writes straight into gold/demo; this adds a review buffer.)

**Redaction logic lives in `src/crashdoc/redact.py`; `scripts/redact_logs.py` is a thin CLI.** Preprocessing will
also redact pasted logs before any LLM call or cache write, so both share one implementation.

**What gets redacted, beyond PLAN 6.2's list:**
- Player names come from `Setting user:` **and** launcher `--username` args, plus `--names`. They are replaced
  case-insensitively (Minecraft names are) and as whole tokens only, so `Steve` doesn't hit `Steven`.
- OS account names are captured from user-home paths and also replaced elsewhere (e.g. `user.name=`), but
  case-sensitively, so an account `Asus` doesn't erase a GPU vendor `ASUS`.
- `hs_err` environment identity lines (`USERNAME=`, `COMPUTERNAME=`, …) and e-mail addresses are also redacted.
- `127.0.0.1` / `0.0.0.0` are kept: they aren't personal and help diagnose bind errors.
- **IPv4 only in network context (human's request, before the first real run).** Mod versions are often 4-part
  (`19.21.0.247`), and version_mismatch diagnoses depend on them, so an IPv4-shaped number is redacted only if:
  - it has a `:port` after it, a `/` right before it, or a keyword like `connecting to` / `address` / `from`
    right before it;
  - or it is on a `server-ip` / server-address line;
  - otherwise, it is in a private range (10/8, 172.16/12, 192.168/16, 169.254/16, 100.64/10), **unless** it is in
    a version context (`-`, `_`, `@`, `+`, `v` or `version` before it; letters after it; or a `.jar` / `|` /
    mod / loader line).
  A test checks that real-format mod-list lines with 4-part versions (including a `10.x` one) come out unchanged.
- Known limits: a public IP with no network context is kept (e.g. one pasted bare in chat); names that
  appear only in chat and are never captured or listed survive (both stated in the report).

**Self-check and counts-only reporting.** After redacting, the script re-scans each output for known names, user
paths, IPs, tokens and e-mails, using the same matching rules, and exits non-zero on any leftover. The printed
summary and `redaction_report.json` contain counts only, never a redacted value. The raw folder must be outside
the repo (enforced) and is only read.

**`validate_labels.py --strict`** (Day 3 split freeze, Day 5 gate) replaces `--require-relevance`. It turns both
warnings into errors: null `relevant_doc_ids`, and a category with ≥2 scenario groups missing from dev or test.
A category with a single scenario group can't be in both splits and is exempt.
