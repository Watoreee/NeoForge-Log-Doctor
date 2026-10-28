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

**Rate limits are hard constraints.** The proxy allows 150 requests and 200k tokens per key. The window was
measured on Day 2 as at most ~1 minute (3 calls over 11 min; proxy-notes), so the eval budget is per-minute. Embeddings cost requests but not tokens (measured;
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

## Pack facts (Day 2, from the human)

**Gold logs come from the human's test instance of All the Mons (ATMons)**, a CurseForge modpack, run through the
CurseForge app. **NeoForge 21.1.224, Minecraft 1.21.1, Java 21.** PLAN.md's "own NeoForge pack" (6.1) means this
pack; the earlier pack name in PLAN.md is a leftover from a draft and is not used anywhere else. The project
name stays "NeoForge Log Doctor".

## Corpus (Day 2)

**Sources** (`scripts/fetch_corpus.py`):
- NeoForge docs, **1.21.1 version** (`versioned_docs/version-1.21.1` in `neoforged/Documentation`, MIT), plus the
  unversioned **player-facing User Guide** (`user/docs`: install, launchers, client, server, FAQ), which is the most
  relevant part for crash diagnosis. Developer-toolchain pages are left out.
- GitHub issue threads for the human's 15 mods. Three repos were renamed and are fetched under their current
  names: `CaffeineMC/sodium-fabric` → `CaffeineMC/sodium`, `shedaniel/ClothConfig` → `shedaniel/cloth-config`,
  `glisco03/owo-lib` → `wisp-forest/owo-lib`.
- GitHub release notes as changelogs, up to 5 recent ones per repo. Only some of the repos publish GitHub
  releases, so changelog coverage is partial; mods whose changelogs live on CurseForge/Modrinth have none.
- Cobblemon is out of scope (its issues are on GitLab); noted under limitations.

**Issue selection rule (deterministic):** candidates are commented issues from two GitHub searches per repo
(`"1.21"`, and `crash`), ranked by mentions 1.21 → looks crash-related (keyword list in the script) → most
recently updated. An issue is **kept only if a maintainer replied** (comment `author_association` OWNER / MEMBER /
COLLABORATOR, not the issue author, not a bot). Up to 30 per repo; at most 90 candidates checked per repo.

**Long threads are capped.** Each post is cut at 3,000 characters (a pasted full log would otherwise swamp the
corpus), at most 12 comments, issue-template HTML comments removed, and at most 6 chunks per issue/release doc.
Docs pages are not capped.

**GitHub text in the corpus is redacted with the same redactor as gold logs.** Issue threads contain pasted user
logs. On the first fetch, 14 of 461 GitHub docs had user-home paths (123), account names (5) or token-shaped strings
(5, all signed `?jwt=` image links). The text is public on GitHub, but republishing personal paths and tokens in
our repo isn't needed, so `fetch_corpus.py` redacts at save time. Content hashes in the manifest are of the
redacted text.

**Licence notes per doc in `manifest.json`:** docs: MIT (neoforged/Documentation); issues: "user-generated
content under the GitHub Terms of Service; the repo licence does not cover issue text"; releases: the repo's SPDX
licence id, where `NOASSERTION` means a custom or unrecognised licence file.

**Chunking: 400 bge-m3 tokens, 50-token overlap**, each chunk an exact character slice of the source (via token
offsets). BM25 and the embedder both see `title + "\n\n" + chunk text`, so a chunk keeps its mod / issue / page
context. Chunk ids are `<doc_id>#<n>`; doc ids are readable (`gh-issue:mezz/JustEnoughItems#1234`,
`neoforge-docs:docs/1.21.1/gettingstarted/versioning`). No chunking variants yet (PLAN 7.3 #5 is later and optional).

**Embeddings are stored L2-normalised** (`embeddings.npy`, float32), so cosine similarity is a dot product.
`embeddings_meta.json` records the model and the SHA-256 of `chunks.jsonl`, so a mismatch is detectable.
Building is resumable: each vector is cached per chunk (keyed by a hash of its text) in git-ignored
`data/processed/embed_cache/`, so a restart, re-chunking or dropping docs only embeds what is new.

## compat_table.py (Day 2)

**Rules, not a hand-typed list, from two NeoForge docs pages fetched 2026-10-28 (both in the corpus):**
- *Versioning* (docs/1.21.1/gettingstarted/versioning): NeoForge `A.B.n` is for Minecraft `1.A.B`, so 21.1.224 is
  for 1.21.1.
- *User Guide* (user/docs): Minecraft 1.20.2–1.20.4 → Java 17; 1.20.5–"latest" → Java 21. Capped at 1.21.1
  (our pack's version) because "latest" can't be trusted beyond the fetch date.

Only NeoForge majors 20–21 are recognised, so an old Forge version like `47.1.3` isn't misread. Null or
unrecognised inputs come back as `unknown`; a newer Java than required is reported as `newer_than_required`, not
an error.
