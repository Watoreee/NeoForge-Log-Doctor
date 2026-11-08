# NeoForge Log Doctor

Paste a Minecraft **NeoForge 1.21.1** crash report or `latest.log`. The service redacts it, reads the facts out of it
with a small LLM (Gemma), searches a corpus of NeoForge docs, GitHub issues and release notes for 22 mod repositories, and returns
a structured diagnosis: the culprit mod, a category, an explanation, fix steps, and citations to the retrieved
documents. It streams its progress to a small web page.

It is a course project (KMITL LLM Applications). It has been evaluated on logs from **one modpack** (see
[Limitations](#limitations)); do not read it as a general NeoForge debugger.

## Setup (3 commands)

Requires **Python 3.11+**.

**bash / zsh / Git Bash**

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pip install -e .
cp .env.example .env        # then fill in OPENAI_API_KEY and OPENAI_BASE_URL
```

**Windows PowerShell** (no `&&` or `source` in PowerShell 5.1)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
Copy-Item .env.example .env   # then fill in OPENAI_API_KEY and OPENAI_BASE_URL
```

If `pip install` fails with `CERTIFICATE_VERIFY_FAILED` (some networks re-sign HTTPS, e.g. a school or company proxy),
use the operating system's certificate store instead, in either shell:

```
pip install --use-feature=truststore -r requirements.txt
pip install --use-feature=truststore --no-build-isolation -e .
```

The corpus index (`data/processed/`) and the LLM/embedding cache (`eval/cache/`) are committed, so a clean clone
needs no fetching and can reproduce every evaluation number **without any API key** (replay mode, below).

### Environment variables (`.env.example`)

Read from the environment only; `.env` is a git-ignored convenience loaded by `python-dotenv`. Never commit it.

| Variable | Purpose |
|---|---|
| `OPENAI_API_KEY`, `OPENAI_BASE_URL` | The class LLM proxy (OpenAI-compatible). Required for live calls, not for replay |
| `CRASHDOC_REPLAY=1` | Serve LLM and embedding calls only from `eval/cache/`; a cache miss is an error |
| `CRASHDOC_CACHE_DIR` | Override the cache location (default `eval/cache/`) |
| `GITHUB_TOKEN` | Optional. Raises the GitHub rate limit for `fetch_corpus.py` |
| `CRASHDOC_INSTANCE`, `CRASHDOC_RAW_DIR` | Only for `collect_run.py` (collecting your own gold logs); the raw folder must be outside the repo |

## Start the server

```bash
uvicorn crashdoc.api:app --port 8000
```

Open <http://127.0.0.1:8000/>. Paste a log, or press **Success example** / **Known failure** to load one of two
redacted sample logs from `data/examples/`. Progress events appear as they happen.

- `GET /health` returns the models and whether a proxy is configured.
- `POST /diagnose` with `{"log": "<text>"}` streams Server-Sent Events: `facts`, `tool_call`, `tool_result`, `final`
  (or `error`). No raw model tokens are streamed. Logs over **10 MB** get HTTP 413 (a hard cap for the server); empty or non-log input gets 422. Logs
  longer than the model budget (about 6,000 tokens) are trimmed to their most informative lines before the model sees
  them; the `facts` event then carries `"truncated": true` and `"original_bytes"`, and the page says so.
  The log is redacted (player name, UUID, tokens, IPs, user folders) before anything else sees it.

```python
import httpx

text = open("data/examples/success_missing_dependency.log", encoding="utf-8").read()
with httpx.stream("POST", "http://127.0.0.1:8000/diagnose", json={"log": text}, timeout=300) as r:
    for line in r.iter_lines():
        print(line)
```

## Evaluation: which command reproduces which number

Add `CRASHDOC_REPLAY=1` to run from the committed cache with no API key (PowerShell: `$env:CRASHDOC_REPLAY=1`).
Every run writes a JSON file to `eval/results/` with the git sha. The **test split is guarded**: it needs `--allow-test`
and should be run once per final configuration (see `docs/decisions.md` for how many times it was run and why).

| What | Command |
|---|---|
| Diagnosis: B0 (LLM only), B1 (regex), RAG-1, Agent. Culprit strict/lenient, category, citation validity (dev) | `python scripts/run_eval.py --split dev --conditions B0,B1,RAG1,FULL` |
| The same on the test split | `python scripts/run_eval.py --split test --allow-test --conditions B0,B1,RAG1,FULL` |
| Retrieval: recall@5, hit@5, MRR for queries (a)/(b)/(c)/(c2), BM25/dense/hybrid, abstention floor, bootstrap CIs (dev, incl. the `min_score` grid) | `python scripts/run_retrieval_eval.py --split dev --grid` |
| The same on test | `python scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.45` |
| **All report tables, rebuilt from the latest result files** (no LLM calls) | `python scripts/report_tables.py --split test` |
| Groundedness sheet for hand judging (test, Agent) | `python scripts/export_groundedness_sheet.py` |
| Groundedness score from the judged sheet (denominator = logs that cite; coverage reported separately) | `python scripts/export_groundedness_sheet.py --score data/groundedness/test_FULL.md` |
| Unit tests (no network), lint | `pytest -q` and `ruff check . && ruff format --check .` |
| Validate the gold labels | `python scripts/validate_labels.py` |

Groundedness (does the cited excerpt support the explanation) is **judged by hand**, never by the code.
Labels live in `data/gold/{dev,test}/*.json`; the rules for them are in `docs/labelling-guide.md`.

## Repository layout

```
src/crashdoc/
  redact.py preprocess.py extraction.py   redact a log, parse/truncate it, extract facts with the LLM
  retrieval/                              chunk index, BM25 + dense + hybrid (RRF), query builders
  rag.py diagnosis.py                     RAG-1 pipeline and the validated Diagnosis (citations only from the retrieved set)
  agent/                                  tool allow-list + pydantic args (tools.py), the JSON-protocol loop (loop.py)
  service.py api.py                       pipeline for the API; FastAPI app (SSE)
  llm.py config.py schemas.py             cached proxy client, settings, pydantic schemas
web/            index.html + sse.js       the page (fetch + ReadableStream, small SSE parser)
data/
  gold/{dev,test}/                        redacted logs with label JSON (dev 7 logs, test 25)
  demo/ data/examples/                    held-out demo logs; the two redacted logs behind the page's example buttons
  processed/                              corpus chunks, manifest, embeddings (committed)
  pool/ groundedness/                     relevance-judging sheets (final); the groundedness sheet
eval/           metrics.py bootstrap.py cache/ results/
scripts/        run_eval, run_retrieval_eval, report_tables, fetch_corpus, build_index, collect_run, redact_logs, ...
docs/           decisions.md (every design choice and when), labelling-guide.md, report-notes.md, proxy-notes.md
tests/
```

Rebuilding the corpus (not needed for evaluation): `python scripts/fetch_corpus.py`,
`python scripts/build_index.py --chunks-only`, then `python scripts/build_index.py` for embeddings through the proxy.
Chunking downloads the bge-m3 tokenizer files (no weights) from Hugging Face; evaluation and serving do not.

Raw logs never enter the repo. `scripts/collect_run.py` writes them to a folder outside it and `scripts/redact_logs.py`
produces reviewed, redacted copies.

## Limitations

The code was built with Claude Code from a written plan (not included in the repository), and the author reviewed it.

- **One modpack, one author.** All 19 usable fault-injection runs (r07 dropped; r10 and r11 count as one scenario, so
  18 scenarios) come from a single modpack, produced by injecting faults into it. 25 test logs from 14 scenarios,
  7 dev logs from 4. Differences of a few logs are noise.
- **The corpus was extended after the logs were collected** (7 repos for the broken mods, before any judgment or
  test result). Some culprits have no tracker in the corpus, so for them nothing relevant exists to retrieve.
- **Relevance labels were made by an LLM**; 8 documents were checked by the author and 30 by a second LLM pass (26/30 agreed); retrieval metrics inherit their errors.
- **Abstention does not work.** The cosine floor (0.45) never triggers on the logs where nothing relevant exists
  (recall 0/7 on test). The system effectively always answers.
- **Citations rarely support the explanation.** The agent cited something on 14 of 25 test logs; on 5 of those 14 the
  cited excerpt supports the explanation (3 of the 5 only in part). This was judged by an LLM (Claude), not by a
  human (`data/groundedness/test_FULL.md`).
- **B0, RAG-1 and the agent are statistically indistinguishable** on this sample. Do not claim that retrieval or the
  agent improves diagnosis from these numbers.
- **Category errors are systematic:** wrong-version jars that dependants report as "not installed" are often labelled
  `missing_dependency` instead of `version_mismatch` (the Known failure example).
- **Fault coverage:** missing dependency, version mismatch, out of memory, and one mixin crash. No duplicate-mod,
  config, Java-version or GPU failures. `hs_err` files are not supported.
- **If a crash report does not name a mod, paste `latest.log` instead.** Some crash reports only show a downstream
  error.
- **Only the first 6,000 tokens of a log's most informative lines are sent to the model.** Longer logs are truncated.
- The model's explanation is generated text. Citations are guaranteed to come from the retrieved set; that they
  *support* the explanation is not guaranteed (this is what the groundedness sheet measures).

Full details, numbers and failure cases: `docs/report-notes.md` and `docs/decisions.md`.
