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
  case-sensitively, so an account named like a GPU vendor (`Nvidia`) doesn't erase `NVIDIA`.
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

**`collect_run.py` (Day 2, the human runs it, I never do).** After each fault-injection launch it copies that run's
logs into the raw folder and records the labels at the moment they're known, so labelling isn't reconstructed
from memory later.
- **Paths:** `CRASHDOC_INSTANCE` and `CRASHDOC_RAW_DIR` come from the environment (or `.env`); no path is in the
  repo. It refuses a raw folder inside the repo, and does not create a missing one, since that's most likely a typo.
- **Stdlib only.** The category list is read from `schemas.py` with `ast`, so the enum stays the one source of
  truth without importing pydantic.
- **Run numbers:** the highest existing `rNN` + 1, not just a count of folders. These are equal unless a folder was
  deleted by hand; then counting would reuse a number that still exists. An existing folder is never overwritten.
- **Folder names:** category and culprit are lowercased with hyphens (`r03_missing-dependency_jei`), so `_` only
  separates the parts.
- **Copying:** files are copied, not moved. Crash reports and `hs_err_pid*.log` are taken only if modified in the
  last `--since-minutes` (default 15). `latest.log`/`debug.log` are always taken. A missing or older `latest.log`
  prints a loud warning and asks before continuing (`--yes` skips the question).
- **Labels:** `--culprit none` is stored as null with an empty `acceptable_culprits`, which matches the gold-label
  rule. Otherwise the culprit is always first in the list. `--broke` is collapsed to one line. `runs.txt` replaces
  `|` with `/`.
- **notes.txt / runs.txt** are `.txt` files in the raw folder, so `redact_logs.py` also redacts them into
  `data/staging/` together with the logs.

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

**`data/raw/` is committed.** `du -sh data/raw` = **3.4 MB** on Day 2 (529 JSON docs), which is "small (a few
MB)" in PLAN 6.4. Committing it lets a grader rebuild chunks without the GitHub API. Also committed:
`chunks.jsonl` (2.7 MB), `manifest.json` (0.3 MB), `embeddings.npy` (7.3 MB).

**Corpus size: 1,850 chunks, above the ~1,500 target, kept on purpose.** Issue threads are already short (capping
at 4 chunks would save only ~70), and the excess is in the NeoForge modder-API docs (721 chunks: loot tables,
biome modifiers, recipes, models). Dropping docs by topic is a judgment for the human, and PLAN 6.4 says
coverage of the pack's mods matters more than the count (range 500–3,000). Because the embedding cache is per
chunk, dropping docs later costs no re-embedding. `shedaniel/cloth-config` yielded only 16 issues with a
maintainer reply (36 candidates checked); every other repo reached 30.

**Index build cost (Day 2):** 60 embedding requests in total (58 for 1,852 chunks, then 2 to re-embed 51 chunks
changed by corpus redaction), 0 retries, 0 rate-limit responses, ~31 min.

**Incident (Day 2): a truncated path fragment was committed and pushed, then fixed forward.** Commits `479b301` /
`8b9886a` contain a home-directory path cut down to the fragment `cont` in the public Waystones issue #1229. The 3,000-character cap cut a pasted server log
mid-path, and the redactor then required a `/` after the name. It is almost certainly the `container` account, the
default on Pterodactyl game-server hosts, not a person. Cause on our side: the pre-commit scan flagged it,
but its exit status was lost in a shell pipe, so the commit went ahead. Fixes:
- home paths cut off at the end of a line are now redacted (tested);
- the fetcher redacts **before** truncating;
- the scan's exit status gates the commit.
History was not rewritten (no force-push).

## Gold/demo contents and review method (Day 3)

**Deviation from PLAN 6.2: `debug.log` files are not committed, so they are not read.** PLAN 6.2 says the human reads
every committed gold/demo file. The `debug.log` files are 3–6 MB each and mostly repeated startup noise, so gold and
demo items are the **crash report(s) + `latest.log` only**. `debug.log` stays in the git-ignored `data/staging/`
folder (redacted, never moved to `data/gold/` or `data/demo/`).

**Stale crash reports removed from staging.** Some raw run folders held crash reports from earlier runs. Staging keeps
only the crash reports listed in that run's `files` column of `runs.txt` (demo: the one named in `notes.txt`).
Deleted (15): r08 `15.44.58`; r09 `15.44.58`, `15.59.51`, `16.03.47`, `16.05.00`; r10 and r11 each `15.44.58`,
`15.59.51`, `16.03.47`, `16.05.00`, `16.13.04`. The raw folder itself is untouched.

**Review method (human).** Instead of reading every committed file line by line: (1) a find-in-files search of the
committed gold/demo files for known identifiers (player name, uuid, xuid, clientId, account name, IPs); (2) a full
read of every crash report and of the header (first part) of every `latest.log`. This is what the "read before
committing" rule in PLAN 6.2 means here.

**Redaction fixes found while preparing the gold set.** (a) ModLauncher's `args [--uuid, X, --xuid, N, ...]` list is
comma-separated; the old `flag value` patterns matched nothing, so uuid/xuid/clientId/accessToken and `--username`
all survived. (b) The player UUID also appears outside the args line (authlib timeouts: `sessionserver…/profile/<uuid>`,
"Couldn't look up profile properties for <uuid>"), including in logs with no args line. The UUID is now captured from
`--uuid` and replaced everywhere, and those two URL/message shapes are redacted generically. Tests added.

## Categories and gold set (Day 3)

**Dropped categories: `duplicate_mod` and `config_error`.** Fault injection did not give a usable log for either
(human's decision), so they are removed from the report and the label set rather than left empty. Categories in use:
`missing_dependency`, `version_mismatch`, `out_of_memory`, `mixin_conflict`. The enum in `schemas.py` still lists
them. Run r07 was dropped as invalid.

**Gold = crash report + `latest.log` per run, each its own gold log.** 19 runs gave 33 gold logs in 19 scenarios (one
`scenario_id` per run), above PLAN's 24–30 target because a run's crash report and `latest.log` are counted
separately. r10, r11, r13, r14 and r20 have no crash report (`latest.log` only). Log ids are `rNN_crash` /
`rNN_latest`. Demo: d1, d2, d3, d6 keep their original file names under `data/demo/`.

**Draft split (stratified by scenario, to be confirmed):** dev = r02, r13, r15, r18, r10 (8 logs, 5 scenarios);
test = the other 14 scenarios (25 logs). `missing_dependency`, `version_mismatch` and `out_of_memory` have scenarios on
both sides. `mixin_conflict` has only one scenario (r14), so it sits in test only.

**Confirmed by the human (Day 3).** Acceptable lists for r02, r08, r12, r17 as drafted (cascades excluded). Rule (d2)
for r04/r05 accepted. Split accepted as drafted, with r14 (`mixin_conflict`) in test only.

**Culprit accuracy is reported twice: strict and lenient, for every condition including B1.** Strict = the predicted
mod equals `culprit_mod_id`; lenient = it is in `acceptable_culprits`. Reason: the large acceptable lists (r08 has 12
entries, r17 has 26) would otherwise hide "blames the victim" errors, where the model names a mod that only
reported the problem instead of the mod that caused it. Lenient alone would score those as correct.

**`data/demo/answers.json` (live defence only).** Built from the demo `notes.txt` files: demo id, culprit, category,
acceptable list, what was broken. `run_eval.py` and all evaluation code must never read it; a test
(`tests/test_demo_answers_unused.py`) fails if any file under `src/` or `scripts/` mentions it. Checked: no player
name, uuid, path or token in it.

## preprocess.py (Day 3)

**Format detector + parsers, written against the real gold logs.** `detect_format` sniffs the first 4,000 lines:
`---- Minecraft Crash Report ----` -> `crash_report`; 3+ timestamped log lines -> `latest_log` (or `debug_log` if a
`/DEBUG]` line is present); an `hs_err` header or other text with log markers (timestamps, levels, `...Exception`) ->
`generic`, flagged in the facts; no markers -> `rejected`. `hs_err` stays **unsupported** (no real example was
collected), so it only gets the generic parse. Two timestamp styles occur in the same log (`[17:37:04]` early
launcher, `[28Oct2026 17:37:44.849]` once the game is up); both are handled.

**What `RawLogFacts` holds:** crash-report description, exception + `Caused by` chain, "Mod loading issue" blocks
(mod id, file, failure message, version), `Suspected Mods` (none of the gold logs has one, tested on synthetic text only),
FML `Missing or unsupported mandatory dependencies` lines (dependency, requested-by, expected, actual),
"Error during pre-loading phase" messages, `is not a valid mod file` names, mods named in `Mixin prepare ... failed`,
ERROR/FATAL lines (first 40, deduplicated), the mod list (id -> version), Minecraft / NeoForge / Java versions,
`-Xmx`, and an out-of-memory flag. Exceptions inside redirected stack traces
(`[java.lang.Throwable:printStackTrace:660]: Caused by: ...`) are found behind their log prefix.

**Linear time.** One pass over the lines, anchored regexes, each line cut at 2,000 characters, every list capped. A 6 MB
`debug.log` parses in about 150 ms; a synthetic 10.5 MB log in well under the 10 s test limit.

**Parser output is not the label.** The parser reports what the log says; it does not pick a culprit or a category.
`scripts/check_parser.py` (CHECKPOINT 1) prints `culprit_in_facts` only as a sanity signal.

**r06_crash dropped from gold (human's decision).** The crash report shows only a downstream
`IllegalStateException: Registry is already frozen` and never names the culprit (`ironfurnaces`). A label is only
valid if the log supports it, so `r06_latest` stays as the gold item for scenario r06 and the crash report was deleted
(never committed). Gold is now **32 logs in 19 scenarios** (test: 24 logs, 14 scenarios; dev: 8 logs, 5 scenarios).
Advice for users, to repeat in the README: *if a crash report doesn't name a mod, paste `latest.log` instead.*

## Truncation, extraction, retrieval, baselines, pool (Day 3)

**Corpus status (reported to the human).** 529 docs (436 GitHub issue threads / 25 release notes / 68 docs pages, per
`manifest.json`; 15 issue repos, 30 each except `cloth-config` 16), 1,850 chunks (1,092 issue, 37 release, 721 NeoForge
docs), `data/raw/` committed (3.4 MB), `chunks.jsonl`, `manifest.json`, `embeddings.npy` (bge-m3, 1024-d, normalised)
committed, `data/processed` 26 MB in total including the git-ignored embed cache. The rate-limit window was measured on 2026-10-28
(proxy-notes.md). The "Placebo/Balm/ResourcefulLib swap" was **not applied**: nothing in the repo, PLAN or notes records
it, and the corpus is the 15 repos listed in `fetch_corpus.py`.

**Truncation to the token budget (`preprocess_log`).** Logs of 12,000 characters or less are sent whole. Longer ones become
a one-line header (versions) plus selected lines, most informative first and in original order: exception lines
and their top 3 frames, FML dependency / loading-error / mixin / OOM / "Failure message" lines (tier 0), other ERROR/FATAL
(tier 1), frames (2), version/system lines (3), KubeJS "does not have required mod" warnings (4, often benign). The mod list
and startup noise are dropped. Selection stops at 6,000 Gemma tokens minus a 250-token margin, so the assembled text fits.
Check on all 32 gold logs: the culprit id is still in the text for every one. Because diagnosis lines come first,
cutting this text to 6,000 characters for the embedder keeps them.

**Extraction (`extraction.py`).** Prompt for JSON, strip the fence, pydantic, one repair retry that feeds the error back,
then regex-derived facts. Each suspect id must be a whole token in the whole log, else dropped and counted. **The prompt
was tuned once on dev only (v1 -> v2):** v1 blamed the mods that need a missing mod (r02) and called a KubeJS failure `other`
(r13). v2 adds general rules (victim vs missing mod, skipped jar, KubeJS), with no gold mod names. r13 still extracts the
wrong mod: left as is, because overfitting 8 dev logs would hide the very error that the oracle condition (c) measures.
A prompt change bumps `EXTRACT_PROMPT_VERSION`; prompt text is part of the cache key, so `E501` is ignored for the two
files that hold prompts rather than reflowing them.

**Retrieval (`retrieval/index.py`).** Dense (normalised cosine), BM25 (rank-bm25; ids like `cobblemon_battle_tower` also
index their parts; a BM25 score of 0 is not a candidate), hybrid = RRF (k=60) over the survivors of the cosine floor.
Top-k per retriever is 50 before the floor. `min_score=None` means no floor. BM25-only candidates removed by the floor are
returned in `dropped_bm25_only` (PLAN 6.4). Queries: (a) preprocessed log, (b) template of exception type + suspect ids +
category keywords, (c) oracle = (b) with gold `acceptable_culprits` and gold category (`retrieval/query.py`).

**Baselines.** B1 is one fixed rule (`Suspected Mods`, else the mod named in the first FML loading error, else null), so it
names the *reporting* mod; on missing-dependency logs that is the victim, and the strict metric exposes it. B0 is one LLM call
on the preprocessed log. Both report strict and lenient culprit accuracy. `scripts/run_eval.py` refuses `--split test` without
`--allow-test`. **No test-split numbers have been looked at**; B0/B1 were run on dev only.

**Relevance pool (`scripts/export_relevance_pool.py`, `data/pool/`).** Six pooled conditions (hybrid a/b/c, BM25 a/b, dense b),
all with `min_score=None`, top 10 documents per ranking, unioned per scenario; one markdown sheet per scenario, test scenarios
first. Pooling bias applies (PLAN 6.7): a relevant document no condition ranked in the top 10 can only be added by hand.
The pool was regenerated after the last truncation change, so it matches the final code.

## Corpus extended to cover the broken mods (Day 3)

**The corpus now covers the culprits broken during collection (PLAN 6.4: corpus mods are chosen from the mods broken).**
Seven repos were added to the original 15, which stay as distractors: `Qelifern/IronFurnacesNeoForge`,
`SuperMartijn642/TrashCans`, `GlodBlock/ExtendedAE` (listed by the human as `GlodBlock/ExPatternProvider`, the old name;
GitHub redirects it), `TeamMetallurgy/Aquaculture`, `YUNG-GANG/YUNGs-API` (was `yungnickyoung/YUNGs-API`; redirected),
`Keksuccino/Konkrete`, `TwelveIterations/Balm`. **This was done before any relevance judgment and before any test-split
result** (no test number has been computed or viewed; B0/B1 ran on dev only). The earlier note that "Placebo/Balm/
ResourcefulLib" would be swapped in was never sent by the human and is void.

**Culprits still not covered by the corpus:** `simpletms` (no tracker), `cobblemonraiddens` (no tracker),
`sophisticatedcore` (no tracker; only `SophisticatedStorage` is in the corpus), `ftbquests` (not on GitHub),
`cobblemon` (GitLab). Scenarios with these culprits are expected to end up with `support_search = "none_found"`
(abstention recall).

**Small side effects of re-running the fetch:** two existing GitHub docs (FerriteCore #189, KotlinForForge #85) were
re-redacted with the improved redactor (it now catches the comma-separated launcher args), so their text changed and
their chunks were re-embedded; two newer AE2 release notes were added because the repo published them since the first
fetch. Existing docs were otherwise untouched. Fewer than 30 issues were kept for some new repos
(IronFurnacesNeoForge 6, TrashCans 17, Konkrete 11, YUNGs-API 29): the maintainer-reply filter and the small trackers.

**Pool depth cut to top-5 per condition, dev sheets first (human's decision; deviation from PLAN 6.7's top-10 and
test-first order).** At top-10 the pool had 952 documents to judge (709 test, 243 dev), too many to judge carefully.
At top-5 it has **532** (389 test, 143 dev), 17 to 44 per scenario. Consequences to state in the report: (1) pooling bias
is larger: a relevant document ranked 6th to 10th by every pooled condition can only be found by hand; so recall@k at
k >= 5 is measured against a shallower pool, and recall@5, the headline metric, is the least affected; (2) the dev
sheets are numbered first (`01_` to `05_`), then test (`06_` to `19_`). The change is only the `--top` default and the
split order in `scripts/export_relevance_pool.py`; the six conditions and `min_score=None` are unchanged.

## Labels finalised (Day 4)

**Relevance labels were produced by an LLM (Claude) from each document's title + the one excerpt shown in the sheet, then
the human reviewed the unsure ones; the human did not open every URL.** Number of documents the human checked:
**8** (see "Spot-check result" below for the 30 checked by a second LLM pass). The sheets in `data/pool/` are final and are never edited. `scripts/apply_judgments.py`
turns them into `relevant_doc_ids` / `support_search` (a log inherits its scenario's judgments; the dry run lists every
judgment; inconsistent sheets are errors).

**Strict `acceptable_culprits` rule (replaces the "Requested by" rule).** culprit + only mods the human disabled,
removed, swapped or changed per `notes.txt` (+ dependents `notes.txt` says were auto-disabled); never mods that merely
report the failure. Applied by `scripts/apply_acceptable_rule.py` (the per-run reason is in the script and the before/after
table printed there). Effect: r08 and r17 shrink from 12 / 26 entries to 1, so strict and lenient culprit accuracy now
differ only where a cascade is listed (r02, r03, r13, r14). The strict metric is still reported next to the
lenient one. The rule has a second condition, added after the human's review: an extra mod must also be **absent or faulty according to the
log** (`apply_acceptable_rule.py` refuses an extra that the log shows loaded). So r04 lists only `simpletms`: the notes say
cloth-config was disabled, but the log shows `cloth_config` loaded via fightorflight. r14 lists `mega_showdown` (notes:
auto-disabled dependent); r05 lists no Cobblemon dependents (notes say only "failed to load").

**r10 and r11 are one scenario group** (`r10_r11_out_of_memory_none`) and sit together in **test** (r10 moved from dev).
Both sheets are `none_found`, so the group's judgments agree. Dev is now 7 logs from 4 scenarios; test 25 logs from 14.
r03's culprit is `architectury` (never `architectury_api`).

**`duplicate_mod` dropped for a second reason:** NeoForge 21.1 tolerates identical duplicate jars (no error), so a
duplicate could not be injected as a failure (human's finding). **Dev is thin:** only 2 dev scenarios (r02, r13) have
relevant documents, the other two (r15, r18) are `none_found`, so dev experiments (min_score choice, query tuning)
rest on very few logs.

## Label correction, oracle (c2), RAG-1, agent, API (Day 4)

**Labels were corrected after the first test run, and no number changed.** The first test run (B0/B1 and retrieval, with
r04's list `simpletms, cloth_config`) was followed by the human's review: the log shows `cloth_config` loaded via
fightorflight, so r04 lists only `simpletms`, and `apply_acceptable_rule.py` now refuses an extra the log shows healthy.
The test split was therefore run **twice** (retrieval) and B0/B1 twice; the second run is the reported one. Before -> after:

| Condition (test) | before | after |
|---|---|---|
| B0 culprit strict / lenient / category | 17/25 / 19/25 / 20/25 | 17/25 / 19/25 / 20/25 |
| B1 culprit strict / lenient | 7/25 / 7/25 | 7/25 / 7/25 |
| hybrid (a) / (b) / (c) recall@5 | 0.167 / 0.597 / 0.458 | 0.167 / 0.597 / 0.458 |
| hybrid (c2) recall@5 | not run | 0.458 |

Nothing moved because r04 has no relevant documents (`none_found`) and neither model named `cloth_config`. Commands:
`python scripts/run_eval.py --split test --allow-test --conditions B0,B1[,RAG1,FULL]`,
`python scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.45`.

**r14 relabelled `mixin_conflict` -> `other` (human's decision, after the second test run).** The log shows one mixin
plugin (`CobblemonRaidDensNeoForgeMixinPlugin.isModAndNewerThan`) throwing a NullPointerException while preparing the
`msd.BattlePokemonStateMixin` (the Mega Showdown compat mixin) because Mega Showdown was disabled; no two mixins
conflict. Culprit `cobblemonraiddens`, acceptable culprits `cobblemonraiddens, owo, mega_showdown` (unchanged).
This leaves `mixin_conflict` with **no logs at all**, so the category is never evaluated (it has no gold example).
Re-run from the cache (no new LLM calls; this is the third test run, label-only change). **One number changed:**
category accuracy on test fell for B0, RAG-1 and the agent, because all three said `mixin_conflict` for r14.

| Test | before (r14 = `mixin_conflict`) | after (r14 = `other`) |
|---|---|---|
| B0 category | 20/25 | 19/25 |
| RAG-1 category | 20/25 | 19/25 |
| Agent category | 20/25 | 19/25 |
| culprit strict / lenient, all conditions | unchanged | unchanged |
| retrieval recall@5, MRR, abstention | unchanged | unchanged |

Dev numbers are unchanged (r14 is a test log). Reproduce: `python scripts/run_eval.py --split test --allow-test
--conditions B0,B1,RAG1,FULL` and `python scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.45`.
Like r04's, this label was corrected after test results had been seen. It lowered the scores, so it was not chosen
to flatter them.

**Oracle (c2).** (c) = LLM-extracted `exception_type` + gold `acceptable_culprits` + gold category keywords. (c2) = gold
`culprit_mod_id` + gold category + the parser's regex exception type (no LLM output). Reported side by side; neither is an
upper bound (test: both score below (b)). Note the (b) query itself uses the LLM exception type, not a regex one.

**Cosine floor `min_score = 0.45`.** Chosen on dev as the middle of the specificity plateau (0.30-0.60), per PLAN 7.3. It
does not discriminate: on dev the `none_found` logs have *higher* max cosine (0.675-0.747) than logs with relevant docs
(0.617-0.698), so abstention recall is 0 until a floor that also kills specificity. At 0.45 the system effectively never
abstains (test abstention recall 0/7). The honest reading is that a similarity floor does not detect "the corpus has
nothing", and the report should say so.

**RAG-1 (`rag.py`).** extraction -> query (b) -> hybrid retrieval with the floor, top 4 documents (best chunk, 700 chars)
-> one Diagnosis call at temperature 0. Citations are doc_ids and may only be ones retrieved; the others are dropped and
counted; with no usable document the diagnosis is still produced with empty citations and confidence `low`. A culprit
that is not a whole token of the log is nulled. One repair retry, then a regex fallback (never observed in the runs).

**Agent: JSON text protocol, not native tool calling.** Measured on this proxy: with the real long prompt and the JSON
answer format the model made **0 native tool calls on 7/7 dev logs**, and `tool_choice="required"` returned an empty tool
call (`finish_reason=tool_calls`, no calls, ~195 tokens spent). A minimal prompt did call the tool, so the failure is
specific to the long prompt. Each turn is one JSON object (`{"action":"tool",...}` or `{"action":"final",...}`); the
allow-list, pydantic argument models, untrusted-data delimiters and max_steps=5 with a forced final call are unchanged. A
final answer before any search gets one nudge to call `search_docs`, then is accepted. Prompt `agent-v4` was tuned on
dev only (v1-v3 were native-protocol attempts). Tools: `search_docs` (hybrid + floor), `get_mod_info` (what this log says
about a mod), `check_compat` (the static NeoForge/Java table). Retrieved set = union of all `search_docs` results.

**API/UI.** `POST /diagnose` takes `{"log": ...}` (limit 200 KB -> 413; empty or no log markers -> 422), redacts the log
first, and streams SSE events `facts`, `tool_call`, `tool_result`, `final`, `error` (structured events only). `GET
/health`. `web/index.html` reads the stream with `fetch` + `ReadableStream` and a small parser (`web/sse.js`, tested under
node); model text is inserted with `textContent` only. A test with a real uvicorn server checks the events arrive spread
over time, not in one burst. The page was later exercised in a real (headless) Chrome, see "Example logs on the page" below.

**Groundedness scoring (human's decision).** The denominator is only the logs that have a citation (14 of 25);
citation coverage (14/25 logs) is a separate number. A log with no citation has no box on the sheet.
`python scripts/export_groundedness_sheet.py --score data/groundedness/test_FULL.md` counts the ticks; the script
refuses to overwrite a sheet that already has ticks. The human judges; the code never does.
**Example logs on the page.** `data/examples/` holds two redacted demo logs (d6 and d3, never in dev or test), checked
unchanged by the redactor (`tests/test_examples.py`). "Success example" is d6 (the system names `create`, category
right). "Known failure" is d3 (Cobblemon replaced by its Fabric build): culprit right, category `missing_dependency`
instead of `version_mismatch`. Checked in a headless Chrome 156 over the DevTools protocol: on an uncached log the
progress events reached the page about 4.5 s, 8.4 s, 8.4 s and 11.4 s after the click.
**Not done (cut list):** (d) the rule-based citation gate (human: skip for now), the retriever comparison beyond what `run_retrieval_eval.py`
prints, the chunking experiment, the tool-call panel, a `sweep.py`, and the replay-mode test of `run_eval.py`.
Groundedness is for the human: `scripts/export_groundedness_sheet.py` writes `data/groundedness/test_FULL.md`.

## History scan and spot-check (Day 5)
**Git history scanned (42 commits, all refs, file contents and commit messages) for the player name, the Windows
username, local paths, tokens (`ghp_`, `github_pat_`, `sk-`, `Bearer`) and emails.** The only identifier found was the
default Windows username, in a test fixture (13 commits) and in two explanatory comments (32 commits). No player name,
token or local drive path was found. The fixture and comments are removed from HEAD (neutral example names are used
now). **History was left unchanged** to avoid a force-push before submission; 12 of the 22 commits already on
`origin/main` contain the username.
**Spot-check of the LLM relevance judgments.** `scripts/make_spotcheck.py` draws 15 ticked + 15 unticked (sheet,
document) pairs with seed 42 into `data/spotcheck.md`, excluding the 8 doc ids in `data/spotcheck_exclude.txt` (already
reviewed by the human; all were unticked, 19 sheet entries removed). The human fills the agree/disagree boxes and
`scripts/score_spotcheck.py` counts them. No label is changed by either script. The number the human spot-checked
(for `report-notes.md` finding 10) is those 8 plus the 30 in the sample, once answered.

## Pre-submission fixes (Day 5)

- **Request size limit: 10 MB, not 200 KB.** The 200 KB figure was a mistake: it contradicted `PLAN.md` (10 MB limit,
  server-side truncation, smoke test on a log over 200 KB) and made the API answer HTTP 413 to 6 of the 32 gold logs
  (largest 1,830 KB). `service.MAX_LOG_BYTES` is now 10 MB, a hard cap that protects the server. The model budget is
  unchanged: `preprocess_log` still trims the log to about 6,000 Gemma tokens of the most informative lines. The `facts`
  SSE event now carries `truncated` (true/false) and `original_bytes`; the page shows a line when the log was trimmed.
  Tests: a log over 200 KB is accepted, trimmed for the model and streams the four event kinds; a short log is not
  marked truncated; a log over 10 MB gets 413. No evaluation number is affected (eval does not go through the API).
- **Wording corrected** (no data changed): the report no longer calls the agent "a better abstainer" (it cited nothing
  on the 7 `none_found` logs but still answered with `high` confidence); the README no longer says the system "often
  cites loosely related documents" (groundedness is not judged yet, TODO marker left for the author); finding 8 now
  says retrieval, B0 and B1 ran three times on test and RAG-1 and the agent twice; the corpus count is 22 GitHub repos
  (15 from the pack + 7 added) plus the NeoForge docs. Older entries above that say "15 repos" describe the state at
  the time and were left as written.
- **LICENSE** added (MIT, 2026, copyright holder from `git config user.name`). README setup now has bash and PowerShell
  blocks and the `--use-feature=truststore` note.

## Spot-check result (2026-11-09)

At the author's request, Claude filled in the 30 boxes of `data/spotcheck.md` (2026-11-09), reading the document text
from `data/processed/chunks.jsonl` and, for r03, r09 and r17, the gold log. It did not open the URLs. The file header
says so, and each entry has a one-line reason. Result (`python scripts/score_spotcheck.py`): **26/30 agree** (ticked
11/15, unticked 15/15). Disagreements, all ticked: ExtendedAE #422 (r13), architectury-api #542 (r03), #528 and
#664 (r17). In each, the thread shares the mod and error words but has a different cause. For example, #528 and #664
are a runtime "Mod 'architectury' is not available" caused by omegaconfig, while r17's log shows architectury skipped
as a Fabric jar and reported `[MISSING]`. **Decision (author): keep the labels.** No number changes. The report counts
8 author-checked documents and 30 LLM-checked documents separately, never 38 human ones.

Scorer bug found and fixed before scoring: `agree \[x\]` also matched inside `disagree [x]`, so a disagreement would
have been counted as invalid. Fixed with a look-behind and tested in `tests/test_spotcheck_score.py`.
