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

**TLS note:** if `pip install` fails with `CERTIFICATE_VERIFY_FAILED` (some networks re-sign HTTPS),
use `pip install --use-feature=truststore -r requirements.txt` and `pip install --no-build-isolation -e .`.
These verify certificates against the OS trust store. The app does the same at runtime via `truststore`.

## Run

```bash
uvicorn crashdoc.api:app --reload        # then open http://127.0.0.1:8000/health
pytest -q                                 # unit tests (no network)
ruff check . && ruff format --check .     # lint
python scripts/validate_labels.py         # check gold labels in data/gold/{dev,test}
```

## Check the proxy (Phase 0)

```bash
python scripts/probe_proxy.py
```

Writes raw results to `docs/proxy-probe-results.json`. The summary and chosen fallbacks are in
`docs/proxy-notes.md`.
