"""Write redacted copies of raw Minecraft logs (PLAN 6.2).

Usage:
    python scripts/redact_logs.py <src_dir> [<dest_dir>] [--names a,b,c]

- <src_dir> holds the raw logs and must be OUTSIDE the repo. It is only read, never modified.
- <dest_dir> defaults to data/staging/ (git-ignored). Files move to data/gold/ or data/demo/ only
  after the human has read every redacted file.
- Reads *.log, *.txt and *.log.gz (decompressed), recursively, keeping relative paths.
- Prints and saves counts only (redaction_report.json); never prints log content or redacted values.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path

from crashdoc.config import REPO_ROOT
from crashdoc.redact import capture_names, capture_user_folders, redact_text

LOG_SUFFIXES = (".log", ".txt", ".log.gz")


def read_text(path: Path) -> str:
    """Raw bytes -> text. Logs are usually UTF-8; undecodable bytes become U+FFFD rather than failing."""
    data = path.read_bytes()
    if path.name.endswith(".gz"):
        data = gzip.decompress(data)
    return data.decode("utf-8", errors="replace")


def output_name(rel: Path, names: list[str]) -> Path:
    """Destination path: drop .gz, and redact known names in the file name too (no <> on Windows)."""
    parts = [redact_text(p, names).text.replace("<", "").replace(">", "") for p in rel.parts]
    out = Path(*parts)
    return out.with_name(out.name[: -len(".gz")]) if out.name.endswith(".gz") else out


def _has_token(text: str, name: str, ignore_case: bool) -> bool:
    pattern = rf"(?<![A-Za-z0-9_]){re.escape(name)}(?![A-Za-z0-9_])"
    return len(name) >= 2 and re.search(pattern, text, re.IGNORECASE if ignore_case else 0) is not None


def leftovers(text: str, players: set[str], accounts: set[str]) -> list[str]:
    """Self-check on the redacted output, using the same matching rules as redaction itself."""
    found = []
    if any(_has_token(text, n, ignore_case=True) for n in players) or any(
        _has_token(text, n, ignore_case=False) for n in accounts
    ):
        found.append("known name")
    if capture_user_folders(text):
        found.append("user path")
    if redact_text(text).counts.keys() & {"ipv4", "ipv6", "token", "email"}:
        found.append("ip/token/email")
    return found


def check_dirs(src: Path, dest: Path) -> None:
    """Raw logs live outside the repo (PLAN 6.2), and output must never land inside the raw folder."""
    if not src.is_dir():
        sys.exit(f"Source folder not found: {src}")
    if src == REPO_ROOT or REPO_ROOT in src.parents:
        sys.exit("Refusing: the raw-log folder must be OUTSIDE the repo.")
    if dest == src or src in dest.parents:
        sys.exit("Refusing: the destination must not be inside the raw-log folder.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Write redacted copies of raw logs.")
    parser.add_argument("src_dir", type=Path)
    parser.add_argument("dest_dir", type=Path, nargs="?", default=REPO_ROOT / "data" / "staging")
    parser.add_argument("--names", default="", help="comma-separated known player names to replace everywhere")
    args = parser.parse_args()

    src, dest = args.src_dir.resolve(), args.dest_dir.resolve()
    check_dirs(src, dest)
    names = [n.strip() for n in args.names.split(",") if n.strip()]

    report, skipped, problems = [], 0, 0
    for path in sorted(p for p in src.rglob("*") if p.is_file()):
        if not path.name.lower().endswith(LOG_SUFFIXES):
            skipped += 1
            continue
        raw = read_text(path)
        result = redact_text(raw, names)
        out_rel = output_name(path.relative_to(src), names)
        out = dest / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.text, encoding="utf-8")

        left = leftovers(result.text, capture_names(raw) | set(names), capture_user_folders(raw))
        problems += bool(left)
        report.append(
            {
                "file": out_rel.as_posix(),
                "bytes": len(result.text.encode("utf-8")),
                "redactions": dict(sorted(result.counts.items())),
                "known_names_used": result.known_names,
                "leftover_check": left or "clean",
            }
        )
        print(
            f"{out_rel.as_posix()}: {dict(sorted(result.counts.items())) or 'nothing to redact'}"
            f"{'  LEFTOVER: ' + ', '.join(left) if left else ''}"
        )

    dest.mkdir(parents=True, exist_ok=True)
    (dest / "redaction_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(
        f"\n{len(report)} file(s) redacted into {dest}; {skipped} non-log file(s) skipped; "
        f"{problems} with leftovers. Report: redaction_report.json"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
