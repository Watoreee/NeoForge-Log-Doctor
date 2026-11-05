# Final pre-submission audit

Audit only: nothing in code, labels, data or other docs was changed to produce this file (this file and
`docs/defence-notes.md` are the only additions). Audited commit: `ed55b7f` (`origin/main`). Date: 2026-11-05.
Every number below was read from `eval/results/*.json` or printed by the command shown. Nothing is estimated.

## Summary: what I would fix, in order

| # | Issue | Severity | Fix |
|---|---|---|---|
| 1 | **API rejects real logs.** `service.MAX_LOG_BYTES` = 200 KB, but 6 of the 32 gold logs are larger (largest 1,830 KB `r06_latest.log`; then 1,083 / 881 / 796 / 792 KB). The page would answer HTTP 413 to a normal `latest.log`. `PLAN.md` says the limit is 10 MB with server-side truncation and requires a smoke test on a >200 KB log (PLAN 8, "Smoke"). The 200 KB came from a later instruction, which conflicts with PLAN. | High for the demo | Decide: raise `MAX_LOG_BYTES` to 10 MB (one constant, plus the README and the page text), or keep 200 KB and say in the report that larger logs are refused. Add the >200 KB smoke test either way. |
| 2 | **Stale corpus size.** README line 4 and `report-notes.md` say "15 mods / 15 repos". The manifest has **22 GitHub repos + NeoForge docs (689 documents)** because 7 repos were added later. | Medium (a wrong number in the report) | Change "15" to "22 repos (15 original + 7 added after the logs were collected)". |
| 3 | **No LICENSE file.** | Medium if the repo is public and the course expects one | Add one; the choice (e.g. MIT) is yours. |
| 4 | **No architecture diagram.** PLAN section 9 requires one in the report; only a text layout exists in the README. | Medium (report requirement) | Draw one (Mermaid source in `docs/architecture.md` is enough). |
| 5 | **Two wording claims are stronger than the data** (section 4 below). | Medium | Soften as listed. |
| 6 | **Groundedness, spot-check and the 8 unsure documents are unjudged**, so report finding 10 and the groundedness number still say TODO. | Required | See "Still needs you". |
| 7 | README setup: the first command uses `&&` and `source`, which do not work in Windows PowerShell; plain `pip install` failed on this network. | Low | Add a PowerShell line. |
| 8 | Result files record `git_sha 25417e4` for the runs after the r14 relabel, but the label change was still uncommitted then. | Low (provenance) | Say so in the report, or re-run on the committed tree (replay, no cost) and cite those files. |

## 1. Clean clone

Cloned `https://github.com/Watoreee/NeoForge-Log-Doctor.git` (no credentials) into a temp dir at `ed55b7f`,
created a new venv (Python 3.11.9) and ran the README commands.

| Step | Result |
|---|---|
| `pip install -r requirements.txt` (plain) | **FAILED**: `CERTIFICATE_VERIFY_FAILED`, "No matching distribution found for openai==2.54.0". This network re-signs HTTPS. |
| Same with `--use-feature=truststore` (the README's TLS note) | OK |
| `pip install --use-feature=truststore --no-build-isolation -e .` | OK |
| `pytest -q`, with no `.env`, no key, no `CRASHDOC_REPLAY` | **267 passed** |
| `scripts/run_eval.py --split dev ...` (replay, from cache) | B0 4/7, 5/7, cat 6/7; B1 4/7, 4/7; RAG-1 4/7, 5/7, cat 7/7; Agent 4/7, 6/7, cat 7/7 |
| `scripts/run_eval.py --split test --allow-test ...` | B0 17/25, 19/25, cat 19/25; B1 7/25, 7/25; RAG-1 18/25, 18/25, cat 19/25; Agent 19/25, 20/25, cat 19/25 |
| `scripts/run_retrieval_eval.py --split dev --grid` | ran; per-log table and max-cosine lines printed |
| `scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.45` | recall@5: (a) 0.167, (b) 0.597, (c) 0.458, (c2) 0.458, B2 0.028; abstention 0/7, specificity 18/18 |
| `scripts/validate_labels.py` | OK (dev 7 logs / 4 scenarios, test 25 / 14) |
| `uvicorn crashdoc.api:app` | `/health` 200; `/`, `/web/sse.js`, both `/examples/*.log` 200 |
| `POST /diagnose` on both examples | success example: `missing_dependency`, `create`; known failure: `missing_dependency`, `cobblemon`; events `facts, tool_call, tool_result, final` |

All numbers match the tables in `report-notes.md`. Replay needed no network.

Unclear or unverified README points:
- **Windows:** line 1 of the setup block (`python -m venv .venv && source ...`) does not run in PowerShell 5.1 (`&&` is not valid there, and `source` is a bash command). I ran my own equivalent, not the literal line.
- **Plain `pip install` can fail** behind a re-signing network; the workaround is in a later paragraph, not in the 3-command block.
- I did not run `cp .env.example .env` (no key was needed in replay), and I started the server with `python -m uvicorn`, not the bare `uvicorn` command.
- During the server check my shell may have had the proxy variables set (`/health` printed `proxy_configured: true`); pytest and the evals ran with them cleared. Replay makes no network call either way.
- A live (non-replay) call from a clean clone was not tested; it needs your key.

## 2. Public repo

| Check | Result |
|---|---|
| Unauthenticated access | `git ls-remote https://github.com/Watoreee/NeoForge-Log-Doctor.git HEAD` returned `ed55b7f...`; HTTP GET of the repo page returned **200**. The repository **is public**. |
| `.env` tracked? | No (0 tracked files match; `.env.example` only) |
| `data/staging` tracked? | No (0) |
| Raw logs tracked? | No. The raw folder is outside the repo; 0 tracked `*.raw.log`, `raw_logs/`, `debug.log` or `hs_err*` files |
| `.gitignore` covers | `.env`, `.env.*` (except `.env.example`), `data/staging/`, `*.raw.log`, `raw_logs/`, `.venv/`, caches. It does **not** list `debug.log` or `hs_err*`; they are safe only because they never leave `data/staging/`. Optional hardening. |
| LICENSE | **Missing** (`LICENSE*` not found at the root). |
| Note | `data/raw/` is tracked: it is the fetched public GitHub/NeoForge corpus, not user logs. The name may confuse a reader; the README layout does not mention it. |
| History | The Windows username remains in 12 earlier commits already on GitHub (decided: not rewritten). |

## 3. Rubric audit

| Item | Verdict | Evidence |
|---|---|---|
| Runs from README | **PASS** (with the TLS workaround here) | Section 1 |
| Layering api -> service -> llm/retrieval/agent | **PASS** | `api.py` imports only `service` and `config`; `service.py` calls `agent.loop`, `llm`, `retrieval.index` lazily; 0 imports of `api`/`service` in `agent/`, `rag.py`, `retrieval/`, `llm.py` |
| Env-based config | **PASS** | `os.environ` is read only in `config.py` (lines 61-73); `.env.example`; README env table |
| Validated structured output | **PASS** | pydantic `Diagnosis` + `parse_with_repair`; invalid category rejected (`tests/test_agent.py`); fallback never needed in the runs (0/25 test, 0/7 dev) |
| Allow-listed tool calls | **PASS** | `agent/tools.py`: `TOOL_NAMES` allow-list, `extra="forbid"` arg models, unknown tool / bad args become errors (tests for both and for injection text) |
| README clarity | **PARTIAL** | Works, but items 2 and 7 above |
| At least 3 capability families incl. evaluation and an agentic one | **PASS** | (1) retrieval/RAG (hybrid BM25+dense, RRF); (2) agentic tool loop (`agent/loop.py`); (3) evaluation (`scripts/run_eval.py`, `run_retrieval_eval.py`, bootstrap); plus extraction/structured output, redaction, streaming API |
| About 30 labelled examples | **PASS** | 32 gold logs (`data/gold`: 7 dev + 25 test) from 18 scenarios; labelling guide |
| Named baselines | **PASS** | B0 (LLM only), B1 (regex heuristic), B2 (BM25 on the log) |
| Reproducible numbers from the repo | **PASS** | Section 1; committed cache and index; `scripts/report_tables.py` |
| One measured improvement with a before/after number | **PASS** | Query (a) -> (b): recall@5 0.167 -> 0.597, +0.431, 95% CI [0.222, 0.681], 9 scenarios |
| Corpus or fetch script committed | **PASS** | `data/processed/` (689 docs, embeddings) and `scripts/fetch_corpus.py` |
| Incremental commit history | **PASS** | 43 commits on 5 days (2026-10-28 to 11-05) |
| Report: problem | **PARTIAL** | README opening; the report itself is not written (`report-notes.md` is notes) |
| Report: architecture diagram source | **FAIL** | None in the repo |
| Report: design | **PASS** (as notes) | `docs/decisions.md` |
| Report: eval | **PASS** (as notes) | `docs/report-notes.md`, `scripts/report_tables.py` |
| Report: failure cases | **PASS** | `report-notes.md`, real log ids |
| Report: limitations | **PASS** | README and `report-notes.md` |
| Items in PLAN not done (cut list) | **PARTIAL** | citation gate, `sweep.py`, chunking experiment, tool-call panel, replay-mode test of `run_eval.py`, "browser parser checked under throttling"; the PLAN "Smoke" test on a >200 KB log (see issue 1); the per-log before/after tables the PLAN lists for the report (they can be built from the result files) |

## 4. Consistency of numbers and claims

I checked every number in `README.md` and `docs/report-notes.md` against the result files with
`python scripts/report_tables.py --split test|dev` and the raw JSON.

**Matches** (all of these): the test and dev tables for B0, B1, RAG-1 and the agent; the bootstrap intervals; retrieval recall@5, hit@5 and MRR
for (a), (b), (c), (c2) and B2; abstention 0/7 and 18/18; max-cosine ranges; citation counts (14/14, 14/15; 14 of 25 logs; 26 tool calls); the
per-log predictions in the failure cases (r01, r03, r04, r05, r09, r14, r16, r17, B1 `None` on r04_latest, r14_latest, r20_latest); agent `high` confidence on
all 6 strict misses and all 7 `none_found` logs; 7 dev logs / 4 scenarios; 25 test logs / 14 scenarios; 19 usable runs and 18 scenarios.

**Mismatches and stale items**
1. README line 4, `report-notes.md` lines 149 and 151: "15 mods" and "15 repos". Actual: 22 GitHub repos plus NeoForge docs (23 sources, 689 documents).
2. README (API section): "Logs over 200 KB get HTTP 413" is true of the code but contradicts PLAN and rejects 6 of the 32 gold logs (issue 1).
3. `report-notes.md` finding 8: "the test split was therefore run three times in total". For retrieval and B0/B1 this is right (three runs). RAG-1 and the agent were first run on test in the second pass, so they have two runs. State it per condition.
4. `report-notes.md` header cites `..._25417e4.json` files; the dirty-tree issue (8) applies to them. The clean-clone re-run (`ed55b7f`) gave identical numbers.
5. `report-notes.md` "Groundedness" and finding 10 contain TODO placeholders. `decisions.md` has the same TODO.

**Claims without a reproducing command**: the corpus size and per-repo counts (add: `python scripts/build_index.py --chunks-only` prints them), and the "6,000 tokens" truncation budget (reproduced only by reading `config.py`).

**Claims stronger than the data**
- *Finding 5, "the model itself is a better abstainer than the floor ... the agent cited nothing in all 7".* An empty citation list is not abstention: the agent still gave a confident (`high`) wrong or unsupported diagnosis on the same logs (r04). Rewrite as: "the agent cited nothing on the 7 `none_found` logs, but it still diagnosed them with high confidence".
- *README Limitations, "often cites loosely related documents".* Groundedness is not judged yet, so this is my impression, not a measurement. Reword or delete until the groundedness sheet is scored.
- *Finding 1, "LLM beats the B1 heuristic".* True and the interval excludes 0, but B1 is a deliberately simple regex baseline; do not generalise to "LLM beats heuristics".
- *Finding 2, "the measured improvement".* It is a retrieval-metric improvement, not a diagnosis improvement (finding 3 shows no significant diagnosis gain); keep both statements together. Also (b) depends on the LLM's extraction.
- *Findings 3 and 4 are worded correctly*: the report does not claim agent or RAG-1 beat B0, and says (c) and (c2) are not upper bounds (both are significantly worse than (b): -0.139, CIs exclude 0). No sentence calls an oracle an upper bound.
- *Known-failure label:* it is described as the system finding "the right mod but the wrong category". Verified on the clean clone: `cobblemon`, `missing_dependency` (gold: `version_mismatch`).

## 5. Security and PII (HEAD, `ed55b7f`, working tree clean)

All gated on printed matches (0 printed lines = 0 matches), not on exit status.

| Scan | Result |
|---|---|
| The Windows username, the player name, API-key and token shapes (`ghp_`, `github_pat_`, `sk-`, long Bearer strings), the author's local drive path, the student id | **0 matches** |
| `C:\Users\<name>` (not `<user>`), outside `data/pool`, `data/processed`, `data/raw` | 11 matches, all fake test names: Alice, Bob, John, X, Nvidia (`tests/test_redact.py`, `tests/test_api_stream.py`, `redact.py` docstring) |
| `C:\Users\?????` | in third-party issue text inside `data/raw`, `data/processed`, `data/pool` (not this project's users) |
| Emails | `example@gmail.com` (2), `me@example.com` (1): placeholders in third-party docs and tests |
| Redactor re-run over the committed files | 0 files would change: `data/gold` (32), `data/demo` (8), `data/examples` (2), pool sheets (19) |
| UUID-shaped strings in `data/gold` | 12: Mekanism's fixed fake-player UUID, Nature's Aura's UUID and crash-report ids. No player UUID. `data/demo` and `data/examples`: 0 |
| Commit metadata | all 43 commits authored as `Watoreee` with the GitHub noreply address |

Not covered: the 12 earlier commits on GitHub still contain the Windows username (a test fixture); your decision was not to rewrite history.
Player-name redaction covers captured and listed names only (stated in the limitations).

## 6. Defence notes

Written to `docs/defence-notes.md`.

## 7. Still needs you

| Item | Where |
|---|---|
| Fill the 30 spot-check boxes, then `python scripts/score_spotcheck.py` (any disagreement: list and stop) | `data/spotcheck.md` |
| Judge groundedness (tick `[x]` only if the excerpt supports the explanation), then `python scripts/export_groundedness_sheet.py --score data/groundedness/test_FULL.md` | `data/groundedness/test_FULL.md` (14 of 25 logs have a citation) |
| The 8 unsure documents | I do not have them listed. The sheets are marked final and contain no "unsure" flag; tell me the ids or the sheet numbers. |
| The spot-check count for finding 10 | `report-notes.md` finding 10, `decisions.md`; by my arithmetic 8 + 30 = 38, but you decide how to count |
| Decide issue 1 (200 KB vs 10 MB), issue 3 (LICENSE), issue 4 (diagram) | above |
| Demo recording (3-6 min: success case on a cache-cold log from `data/demo/`, one honest failure, a tool-call trace, the query-construction number) | not done; note the PLAN wants a tool-call trace but the tool-call panel was cut, so the trace has to come from the progress events (`tool_call` and `tool_result`) |
| Report editing (4-8 pages; `report-notes.md` is the skeleton) | the report itself is not written |

## 8. Fix status (after this audit)

Fixed in the commit that follows this audit: issue 1 (10 MB cap, `truncated` and `original_bytes` in the `facts` event,
tests), issue 2 (22 repos), issue 3 (MIT LICENSE), issue 5 (both overclaims reworded; finding 8 per condition) and
issue 7 (README bash and PowerShell blocks, truststore note). **Not fixed:** issue 4 (architecture diagram), issue 6
(groundedness, spot-check, unsure documents: yours), issue 8 (provenance of the result files' git sha). Sections 1-5
above describe the audited commit `ed55b7f` and were not edited, so the 200 KB and "15" statements there are the
state before the fixes.
