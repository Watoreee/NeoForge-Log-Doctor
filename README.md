# NeoForge Log Doctor

Paste a Minecraft (NeoForge) crash report or `latest.log` and get a structured diagnosis, fix steps, and cited sources.

> Work in progress. See `PLAN.md` for the full spec and `docs/decisions.md` for design choices.

## Setup

Requires **Python 3.11+**.

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (Git Bash):    source .venv/Scripts/activate
# macOS / Linux:         source .venv/bin/activate

# 2. Install dependencies and the crashdoc package (editable)
pip install -r requirements.txt
pip install -e .

# 3. Configure the LLM proxy
cp .env.example .env      # then fill in OPENAI_API_KEY and OPENAI_BASE_URL
```

Configuration is read from environment variables only. `.env` is a local convenience loaded with
`python-dotenv` and is git-ignored. Never commit it.

| Variable | Purpose |
|---|---|
| `OPENAI_API_KEY`, `OPENAI_BASE_URL` | Class LLM proxy (required for live calls) |
| `GITHUB_TOKEN` | Optional, raises the GitHub API rate limit for corpus fetching |
| `CRASHDOC_REPLAY=1` | Serve LLM + embedding calls only from the on-disk cache; a miss is an error |
| `CRASHDOC_CACHE_DIR` | Override the cache location (default `eval/cache/`) |
| `CRASHDOC_INSTANCE` | Game instance folder, read by `collect_run.py` |
| `CRASHDOC_RAW_DIR` | Raw-log folder OUTSIDE the repo, written by `collect_run.py`, read by `redact_logs.py` |

**TLS note:** if `pip install` fails with `CERTIFICATE_VERIFY_FAILED` (some networks re-sign HTTPS),
use `pip install --use-feature=truststore -r requirements.txt` and `pip install --no-build-isolation -e .`.
These verify certificates against the OS trust store. The app does the same at runtime via `truststore`.

## Run

```bash
uvicorn crashdoc.api:app --reload        # then open http://127.0.0.1:8000/health
pytest -q                                 # unit tests (no network)
ruff check . && ruff format --check .     # lint
python scripts/validate_labels.py         # check gold labels in data/gold/{dev,test} (--strict at freeze/gates)
```

## Preparing gold logs (raw logs never enter the repo)

```bash
# After each fault-injection launch: copy that run's logs into the raw folder and record its labels.
# Writes <raw>/r<NN>_<category>_<culprit>/ (latest.log, debug.log, crash reports and hs_err files from the
# last --since-minutes, notes.txt) and appends a line to <raw>/runs.txt. Prompts for anything missing.
python scripts/collect_run.py --category missing_dependency --culprit jei --broke "removed jei" [--also a,b] [--dry-run]

# Raw logs stay in a folder OUTSIDE the repo. This writes redacted copies to data/staging/ (git-ignored):
python scripts/redact_logs.py /path/outside/repo/raw_logs --names Name1,Name2
```

Read every file in `data/staging/`, then move it into `data/gold/{dev,test}/` or `data/demo/`.

## Corpus and index

The chunked corpus (`data/processed/chunks.jsonl`, `manifest.json`) and its embeddings (`embeddings.npy`) are
committed, so a clean clone does not need to refetch. To rebuild:

```bash
python scripts/fetch_corpus.py            # NeoForge 1.21.1 docs + GitHub issues/releases for 15 mods -> data/raw/
python scripts/build_index.py --chunks-only   # chunk -> chunks.jsonl + manifest.json, prints corpus stats
python scripts/build_index.py             # + embeddings via the proxy (resumable; ~1 s per chunk)
```

Both scripts are resumable: rerunning skips what is already fetched or embedded.

## Check the proxy (Phase 0)

```bash
python scripts/probe_proxy.py
```

Writes raw results to `docs/proxy-probe-results.json`. The summary and chosen fallbacks are in
`docs/proxy-notes.md`.
