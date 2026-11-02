"""CHECKPOINT 1: run the parser on every real log and report what it extracted (PLAN 6.2, Day 2-3 gate).

Usage:  python scripts/check_parser.py [--big-dir data/staging]

Covers every gold + demo log. With --big-dir it also times the multi-MB debug.log files (not committed).
Exit code 1 if any log is rejected, raises, or yields no signal at all. It prints facts, never log content
beyond short error lines (the logs are already redacted).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from crashdoc.config import REPO_ROOT
from crashdoc.preprocess import RawLogFacts, parse_log

SIGNALS = (
    "loading_issues",
    "dependency_issues",
    "fml_errors",
    "exceptions",
    "invalid_mod_files",
    "mixin_mods",
    "error_lines",
)


def signal_count(f: RawLogFacts) -> int:
    return sum(len(getattr(f, name)) for name in SIGNALS) + f.out_of_memory


def gold_logs() -> list[tuple[str, Path, str | None]]:
    """(log_id, path, culprit) for every gold log, then demo logs (demo answers are never read)."""
    rows = []
    for split in ("dev", "test"):
        for label in sorted((REPO_ROOT / "data" / "gold" / split).glob("*.json")):
            data = json.loads(label.read_text(encoding="utf-8"))
            log = next(p for p in label.parent.glob(f"{label.stem}.*") if p.suffix != ".json")
            rows.append((f"{split}/{label.stem}", log, data["culprit_mod_id"]))
    for log in sorted((REPO_ROOT / "data" / "demo").rglob("*")):
        if log.is_file() and log.suffix in (".log", ".txt"):
            rows.append((f"demo/{log.parent.name[:2]}/{log.name[:18]}", log, None))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--big-dir", type=Path, default=None, help="folder with large debug.log files to time")
    args = parser.parse_args()

    failures, rows = 0, gold_logs()
    for name, path, culprit in rows:
        text = path.read_text(encoding="utf-8", errors="replace")
        t0 = time.perf_counter()
        try:
            f = parse_log(text)
        except Exception as exc:  # the checkpoint must report, not crash
            print(f"{name}: RAISED {type(exc).__name__}: {exc}")
            failures += 1
            continue
        ms = (time.perf_counter() - t0) * 1000
        n = signal_count(f)
        blob = json.dumps(f.to_dict()).lower()
        in_facts = "-" if culprit is None else ("yes" if culprit.lower() in blob else "NO")
        bad = f.format in ("rejected", "generic") or n == 0
        failures += bad
        print(
            f"{name:28} {f.format:12} load={len(f.loading_issues):2} dep={len(f.dependency_issues):2} "
            f"fml={len(f.fml_errors):2} exc={len(f.exceptions):2} mixin={len(f.mixin_mods)} mods={len(f.mod_versions):3} "  # noqa: E501
            f"mc={f.minecraft_version} nf={f.neoforge_version} java={f.java_version} heap={f.max_heap_mb} "
            f"oom={int(f.out_of_memory)} culprit_in_facts={in_facts} {ms:5.0f}ms{'  <-- PROBLEM' if bad else ''}"
        )
    print(f"\n{len(rows)} committed logs parsed, {failures} problem(s)")

    if args.big_dir:
        for path in sorted(args.big_dir.rglob("debug.log")):
            text = path.read_text(encoding="utf-8", errors="replace")
            t0 = time.perf_counter()
            f = parse_log(text)
            print(
                f"big {path.parent.name[:30]:30} {len(text) / 1e6:5.1f} MB {f.format:10} {(time.perf_counter() - t0) * 1000:6.0f} ms"  # noqa: E501
            )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
