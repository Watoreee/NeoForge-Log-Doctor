"""Fetch the retrieval corpus into data/raw/ (PLAN 6.4). Resumable: already-fetched docs are skipped.

Sources:
- NeoForge docs for Minecraft 1.21.1 (neoforged/Documentation, versioned_docs/version-1.21.1) plus the
  unversioned player-facing user guide (user/docs).
- GitHub issue threads for the pack's mods (REPOS). Preference order: mentions 1.21, looks crash-related,
  most recently updated. An issue is kept only if a maintainer (OWNER / MEMBER / COLLABORATOR, not the
  issue author, not a bot) replied in it.
- GitHub release notes (changelogs) where a repo publishes releases.

Usage:
    python scripts/fetch_corpus.py [--issues-per-repo 30] [--releases-per-repo 5]

GitHub text (issues, release notes) goes through crashdoc.redact before it is saved: users paste logs
that contain their home paths, player names and launcher tokens. Docs pages are saved as-is.

Each raw doc is one JSON file with url, title, source_type, fetched_at and licence/terms note.
GITHUB_TOKEN (optional, from the environment / .env) raises the API limit from 60 to 5,000 requests/hour.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

import httpx

from crashdoc.config import REPO_ROOT, get_settings, use_os_trust_store
from crashdoc.redact import redact_text

RAW_DIR = REPO_ROOT / "data" / "raw"
API = "https://api.github.com"
DOCS_REPO = "neoforged/Documentation"
DOCS_VERSION = "1.21.1"
DOCS_SITE = "https://docs.neoforged.net"

# The pack's ~15 mods (human's choice, Day 2). Renamed repos are listed under their current name.
REPOS = [
    "Creators-of-Create/Create",
    "mezz/JustEnoughItems",
    "embeddedt/ModernFix",
    "malte0811/FerriteCore",
    "CaffeineMC/sodium",  # was CaffeineMC/sodium-fabric
    "bernie-g/geckolib",
    "TheIllusiveC4/Curios",
    "architectury/architectury-api",
    "shedaniel/cloth-config",  # was shedaniel/ClothConfig
    "wisp-forest/owo-lib",  # was glisco03/owo-lib
    "thedarkcolour/KotlinForForge",
    "P3pp3rF1y/SophisticatedStorage",
    "TwelveIterations/Waystones",
    "mrh0/createaddition",
    "AppliedEnergistics/Applied-Energistics-2",
]

MAINTAINER_ROLES = {"OWNER", "MEMBER", "COLLABORATOR"}
CRASH_WORDS = re.compile(
    r"(?i)crash|exception|error|mixin|incompatib|missing|requires|failed to load|not load|freez|out of memory"
)
MAX_POST_CHARS = 3_000  # a pasted full log in an issue would otherwise swamp the corpus
MAX_COMMENTS = 12
CANDIDATES_PER_KEPT = 3  # check at most 3x as many issues as we keep, per repo


class GitHub:
    """Small GitHub REST client: spaces out requests and waits out rate limits instead of failing."""

    def __init__(self, token: str | None):
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.http = httpx.Client(headers=headers, follow_redirects=True, timeout=60)
        self.requests = 0

    def get(self, path: str, **params) -> httpx.Response:
        """GET with a polite delay (search: 30/min) and up to 5 waits on 403/429 rate-limit responses."""
        url = path if path.startswith("http") else f"{API}{path}"
        for _ in range(5):
            time.sleep(2.2 if "/search/" in url else 0.25)
            self.requests += 1
            resp = self.http.get(url, params=params or None)
            if resp.status_code not in (403, 429) or "rate limit" not in resp.text.lower():
                resp.raise_for_status()
                return resp
            wait = _rate_limit_wait(resp)
            print(f"  rate limited; waiting {wait:.0f} s", flush=True)
            time.sleep(wait)
        resp.raise_for_status()
        return resp

    def json(self, path: str, **params):
        return self.get(path, **params).json()


def _rate_limit_wait(resp: httpx.Response) -> float:
    """Seconds to wait: retry-after, else until x-ratelimit-reset, else a minute."""
    if resp.headers.get("retry-after"):
        return float(resp.headers["retry-after"]) + 1
    reset = resp.headers.get("x-ratelimit-reset")
    if reset and resp.headers.get("x-ratelimit-remaining") == "0":
        return max(1.0, int(reset) - time.time() + 2)
    return 60.0


def now_utc() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def save(path: Path, doc: dict) -> None:
    """Write one raw doc. GitHub text is redacted first: users paste logs with their paths and tokens."""
    if doc["source_type"] != "neoforge_docs":
        doc = {**doc, "text": redact_text(doc["text"]).text}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", text)


# ---------------------------------------------------------------- NeoForge docs


def docs_url(rel_path: str, prefix: str) -> str:
    """Docusaurus URL for a markdown file: strip .md/.mdx, `index` maps to its folder, trailing slash."""
    stem = re.sub(r"\.mdx?$", "", rel_path)
    stem = re.sub(r"(^|/)index$", "", stem)
    return f"{DOCS_SITE}/{prefix}/{stem}/".replace("//", "/").replace("https:/", "https://")


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Docusaurus front matter (--- key: value ---) -> (fields, body)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    fields = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.MULTILINE))
    return fields, text[m.end() :]


def fetch_docs(gh: GitHub, licence: str) -> int:
    """Every markdown page of the 1.21.1 docs and the user guide."""
    tree = gh.json(f"/repos/{DOCS_REPO}/git/trees/main", recursive=1)["tree"]
    sections = [(f"versioned_docs/version-{DOCS_VERSION}/", f"docs/{DOCS_VERSION}"), ("user/docs/", "user/docs")]
    count = 0
    for src_prefix, url_prefix in sections:
        for item in tree:
            path = item["path"]
            if item["type"] != "blob" or not path.startswith(src_prefix) or not path.endswith((".md", ".mdx")):
                continue
            rel = path[len(src_prefix) :]
            doc_id = re.sub(r"\.mdx?$", "", f"neoforge-docs:{url_prefix}/{rel}")
            out = RAW_DIR / "neoforge_docs" / f"{safe_name(doc_id)}.json"
            count += 1
            if out.exists():
                continue
            raw = gh.get(f"https://raw.githubusercontent.com/{DOCS_REPO}/main/{path}").text
            fields, body = split_front_matter(raw.replace("\r\n", "\n"))
            heading = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            title = fields.get("title") or (heading.group(1).strip() if heading else rel)
            url = docs_url(fields["slug"].lstrip("/"), url_prefix) if "slug" in fields else docs_url(rel, url_prefix)
            save(
                out,
                {
                    "doc_id": doc_id,
                    "url": url,
                    "title": f"NeoForge docs: {title.strip(chr(34))}",
                    "source_type": "neoforge_docs",
                    "repo": DOCS_REPO,
                    "fetched_at": now_utc(),
                    "licence": licence,
                    "text": body.strip(),
                },
            )
    return count


# ---------------------------------------------------------------- GitHub issues


def clean_post(body: str | None) -> str:
    """Drop issue-template HTML comments, redact, then cap the length (pasted logs can be 100k+ characters).

    Redacting before the cut matters: a cut can split a user path mid-name, so redaction no longer sees it.
    """
    text = re.sub(r"<!--.*?-->", "", body or "", flags=re.DOTALL).strip()
    text = redact_text(text).text
    if len(text) > MAX_POST_CHARS:
        text = text[:MAX_POST_CHARS].rstrip() + "\n[... truncated]"
    return text


def candidate_issues(gh: GitHub, repo: str) -> list[dict]:
    """Commented issues, best first: mentions 1.21, then crash-related, then most recently updated."""
    seen: dict[int, dict] = {}
    for query in (f'repo:{repo} is:issue comments:>0 "1.21"', f"repo:{repo} is:issue comments:>0 crash"):
        for page in (1, 2):
            items = gh.json("/search/issues", q=query, sort="updated", order="desc", per_page=100, page=page)["items"]
            for it in items:
                seen.setdefault(it["number"], it)
            if len(items) < 100:
                break

    def rank(it: dict) -> tuple:
        text = f"{it['title']}\n{it.get('body') or ''}"
        return ("1.21" in text, bool(CRASH_WORDS.search(text)), it["updated_at"])

    return sorted(seen.values(), key=rank, reverse=True)


def maintainer_replied(issue: dict, comments: list[dict]) -> bool:
    author = issue["user"]["login"]
    return any(
        c["author_association"] in MAINTAINER_ROLES and c["user"]["login"] != author and c["user"]["type"] != "Bot"
        for c in comments
    )


def fetch_issues(gh: GitHub, repo: str, keep: int, terms: str) -> tuple[int, int]:
    """Keep up to `keep` issues with a maintainer reply. Returns (kept, checked)."""
    folder = RAW_DIR / "github_issues" / safe_name(repo)
    kept = len(list(folder.glob("*.json"))) if folder.exists() else 0
    if kept >= keep:
        return kept, 0
    checked = 0
    for issue in candidate_issues(gh, repo):
        if kept >= keep or checked >= keep * CANDIDATES_PER_KEPT:
            break
        out = folder / f"{issue['number']}.json"
        if out.exists():
            continue
        checked += 1
        comments = gh.json(f"/repos/{repo}/issues/{issue['number']}/comments", per_page=100)
        if not maintainer_replied(issue, comments):
            continue
        posts = [f"[issue by {issue['user']['login']}]\n{clean_post(issue.get('body'))}"]
        posts += [
            f"[comment by {c['user']['login']} ({c['author_association'].lower()})]\n{clean_post(c['body'])}"
            for c in comments[:MAX_COMMENTS]
        ]
        save(
            out,
            {
                "doc_id": f"gh-issue:{repo}#{issue['number']}",
                "url": issue["html_url"],
                "title": f"{repo.split('/')[1]} issue #{issue['number']}: {issue['title']}",
                "source_type": "github_issue",
                "repo": repo,
                "state": issue["state"],
                "created_at": issue["created_at"],
                "fetched_at": now_utc(),
                "licence": terms,
                "text": "\n\n".join(posts),
            },
        )
        kept += 1
    return kept, checked


# ---------------------------------------------------------------- releases (changelogs)


def fetch_releases(gh: GitHub, repo: str, limit: int, licence: str) -> int:
    """The most recent non-empty release notes."""
    kept = 0
    for rel in gh.json(f"/repos/{repo}/releases", per_page=20):
        if kept >= limit:
            break
        body = (rel.get("body") or "").strip()
        if rel.get("draft") or len(body) < 80:
            continue
        kept += 1
        out = RAW_DIR / "github_releases" / safe_name(repo) / f"{safe_name(rel['tag_name'])}.json"
        if out.exists():
            continue
        save(
            out,
            {
                "doc_id": f"gh-release:{repo}@{rel['tag_name']}",
                "url": rel["html_url"],
                "title": f"{repo.split('/')[1]} release {rel.get('name') or rel['tag_name']}",
                "source_type": "github_release",
                "repo": repo,
                "created_at": rel.get("published_at"),
                "fetched_at": now_utc(),
                "licence": licence,
                "text": clean_post(body) if len(body) > MAX_POST_CHARS * 2 else body,
            },
        )
    return kept


def repo_licence(gh: GitHub, repo: str) -> str:
    """SPDX id from the API; NOASSERTION means a custom or unrecognised licence file."""
    info = gh.json(f"/repos/{repo}")
    spdx = (info.get("license") or {}).get("spdx_id") or "none"
    note = " (custom or unrecognised licence; see the repo's LICENSE file)" if spdx == "NOASSERTION" else ""
    return f"{spdx}{note}"


def redact_existing() -> int:
    """Re-redact GitHub docs already on disk (idempotent), so older fetches get the same treatment."""
    changed = 0
    for path in RAW_DIR.glob("github_*/*/*.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        if redact_text(doc["text"]).counts:
            save(path, doc)
            changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch the retrieval corpus into data/raw/.")
    parser.add_argument("--issues-per-repo", type=int, default=30)
    parser.add_argument("--releases-per-repo", type=int, default=5)
    args = parser.parse_args()

    print(f"Re-redacted {redact_existing()} already-fetched GitHub doc(s)")
    use_os_trust_store()
    gh = GitHub(get_settings().github_token)
    if not get_settings().github_token:
        print("No GITHUB_TOKEN: limited to 60 requests/hour; the fetch will be slow.", file=sys.stderr)

    docs_licence = f"{repo_licence(gh, DOCS_REPO)} (neoforged/Documentation)"
    print(f"NeoForge docs: {fetch_docs(gh, docs_licence)} pages")
    for repo in REPOS:
        licence = repo_licence(gh, repo)
        terms = (
            "GitHub issue thread: user-generated content under the GitHub Terms of Service; "
            f"the repo licence ({licence.split(' ')[0]}) does not cover issue text"
        )
        kept, checked = fetch_issues(gh, repo, args.issues_per_repo, terms)
        rels = fetch_releases(gh, repo, args.releases_per_repo, f"Release notes; repo licence {licence}")
        print(f"{repo}: {kept} issues (checked {checked} new), {rels} releases", flush=True)
    print(f"Done. {gh.requests} GitHub requests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
