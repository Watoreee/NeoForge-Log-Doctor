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

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure the LLM proxy
cp .env.example .env      # then fill in OPENAI_API_KEY and OPENAI_BASE_URL
```

Configuration is read from environment variables only. `.env` is a local convenience loaded with
`python-dotenv` and is git-ignored. Never commit it.

**TLS note:** if `pip install` fails with `CERTIFICATE_VERIFY_FAILED` (some networks re-sign HTTPS),
use `pip install --use-feature=truststore -r requirements.txt`, which verifies certificates against
the OS trust store. The app does the same at runtime via `truststore`.

## Check the proxy (Phase 0)

```bash
python scripts/probe_proxy.py
```

Writes raw results to `docs/proxy-probe-results.json`. The summary and chosen fallbacks are in
`docs/proxy-notes.md`.
