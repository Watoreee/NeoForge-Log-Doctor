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

**Ruff line length 120.** Set explicitly on the command line for now; it moves to `pyproject.toml` with the skeleton.

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
