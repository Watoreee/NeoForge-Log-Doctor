"""Validate the gold labels in data/gold/{dev,test} (PLAN 6.1).

Usage:
    python scripts/validate_labels.py [--gold-dir data/gold] [--manifest data/processed/manifest.json]
                                      [--strict]

Exit code 1 if any check fails. --strict (Day 3 split freeze, Day 5 gate) also fails on null
relevant_doc_ids and on a category with >=2 scenario groups that is missing from dev or test.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from crashdoc.config import REPO_ROOT
from crashdoc.labels import describe_split, validate_gold


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate gold labels.")
    parser.add_argument("--gold-dir", type=Path, default=REPO_ROOT / "data" / "gold")
    parser.add_argument("--manifest", type=Path, default=REPO_ROOT / "data" / "processed" / "manifest.json")
    parser.add_argument("--strict", action="store_true", help="unjudged relevance + split imbalance are errors")
    args = parser.parse_args()

    report = validate_gold(args.gold_dir, args.manifest, args.strict)
    for split, items in report.labels.items():
        print(f"{split}: {describe_split(items)}")
    for w in report.warnings:
        print(f"WARNING  {w}")
    for e in report.errors:
        print(f"ERROR    {e}")
    print("OK" if report.ok else f"FAILED with {len(report.errors)} error(s)")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
