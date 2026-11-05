"""Draw the human spot-check sample from the FINAL relevance sheets. Changes no label.

Usage: python scripts/make_spotcheck.py [--seed 42] [--n 15] [--exclude-file data/spotcheck_exclude.txt]
                                        [--raw-dir <crashdoc-raw-logs>] [--out data/spotcheck.md]

Samples n ticked and n unticked (sheet, doc) pairs with random.Random(seed) from `data/pool/*.md`, minus the
documents listed in the exclude file (one doc id per line, optionally `NN:doc_id` to exclude only one sheet; `#`
comments allowed). For each: sheet, doc id, title, URL, the sheet's mark, the run's `what_i_broke` from notes.txt
(redacted), and an agree/disagree box. Score the filled file with scripts/score_spotcheck.py.
"""

from __future__ import annotations

import argparse
import os
import random
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from crashdoc.redact import redact_text  # noqa: E402

ENTRY = re.compile(r"^- \[( |x|X)\] \*\*(.+?)\*\*")


def parse_sheets(pool_dir: Path) -> list[dict]:
    docs = []
    for sheet in sorted(pool_dir.glob("[0-9][0-9]_*.md")):
        lines = sheet.read_text(encoding="utf-8").splitlines()
        run = re.search(r"_(r\d\d)_", sheet.name).group(1)
        for i, line in enumerate(lines):
            m = ENTRY.match(line)
            if not m:
                continue
            title = lines[i + 1].strip()[2:] if i + 1 < len(lines) else ""
            url = lines[i + 2].strip()[2:] if i + 2 < len(lines) else ""
            docs.append(
                {
                    "sheet": sheet.name,
                    "num": sheet.name[:2],
                    "run": run,
                    "doc_id": m.group(2),
                    "mark": "x" if m.group(1).lower() == "x" else " ",
                    "title": title,
                    "url": url,
                }
            )
    return docs


def load_exclusions(path: Path) -> tuple[set[str], set[tuple[str, str]]]:
    any_sheet: set[str] = set()
    one_sheet: set[tuple[str, str]] = set()
    if path.exists():
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = re.split(r"\s#", raw, maxsplit=1)[0].strip()  # ids contain '#', so only ' #...' starts a comment
            if line.startswith("#"):
                continue
            if not line:
                continue
            if re.match(r"^\d\d:", line):
                one_sheet.add((line[:2], line[3:].strip()))
            else:
                any_sheet.add(line)
    return any_sheet, one_sheet


def what_i_broke(raw_dir: Path | None, run: str) -> str:
    if raw_dir and raw_dir.is_dir():
        for folder in sorted(raw_dir.glob(f"{run}_*")):
            notes = folder / "notes.txt"
            if notes.exists():
                for line in notes.read_text(encoding="utf-8").splitlines():
                    if line.startswith("what_i_broke:"):
                        return redact_text(line.split(":", 1)[1].strip()).text
    return "(notes.txt not found)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n", type=int, default=15)
    ap.add_argument("--exclude-file", type=Path, default=REPO_ROOT / "data" / "spotcheck_exclude.txt")
    ap.add_argument(
        "--raw-dir",
        type=Path,
        default=Path(os.environ["CRASHDOC_RAW_DIR"]) if os.environ.get("CRASHDOC_RAW_DIR") else None,
    )
    ap.add_argument("--out", type=Path, default=REPO_ROOT / "data" / "spotcheck.md")
    args = ap.parse_args()

    docs = parse_sheets(REPO_ROOT / "data" / "pool")
    any_sheet, one_sheet = load_exclusions(args.exclude_file)
    eligible = [d for d in docs if d["doc_id"] not in any_sheet and (d["num"], d["doc_id"]) not in one_sheet]
    ticked = [d for d in eligible if d["mark"] == "x"]
    unticked = [d for d in eligible if d["mark"] != "x"]
    if len(ticked) < args.n or len(unticked) < args.n:
        sys.exit(f"not enough eligible documents: {len(ticked)} ticked, {len(unticked)} unticked")
    rng = random.Random(args.seed)
    sample = rng.sample(ticked, args.n) + rng.sample(unticked, args.n)
    sample.sort(key=lambda d: (d["sheet"], d["doc_id"]))

    excl_note = (
        f"**exclusion list applied** (`{args.exclude_file.name}`: {len(any_sheet) + len(one_sheet)} doc ids, "
        f"{len(docs) - len(eligible)} sheet entries removed, i.e. the documents already reviewed by the human)"
        if args.exclude_file.exists()
        else f"**NO exclusion list applied** (`{args.exclude_file.name}` does not exist): the documents you already "
        "reviewed may appear below. Put their ids in that file and re-run"
    )
    out = [
        "# Spot-check of the relevance judgments",
        "",
        f"Seed {args.seed}; {args.n} ticked + {args.n} unticked, drawn from {len(ticked)} ticked and {len(unticked)} "
        f"unticked eligible (sheet, document) pairs in `data/pool/` ({len(docs)} judged in total); {excl_note}. "
        "Produced by `scripts/make_spotcheck.py`. Nothing here changes a label.",
        "",
        "For each: open the URL if the excerpt/title does not settle it. **agree** = the sheet's mark is right "
        "(ticked: it helps diagnose or fix THIS failure; unticked: it does not). **disagree** = it is wrong. "
        "Tick exactly one box. Then run `python scripts/score_spotcheck.py`.",
        "",
    ]
    for i, d in enumerate(sample, 1):
        out += [
            "---",
            "",
            f"### {i}. sheet {d['num']} (`{d['run']}`) `{d['doc_id']}`",
            "",
            f"- Sheet: `{d['sheet']}`",
            f"- Title: {d['title']}",
            f"- URL: {d['url']}",
            f"- **Sheet's current mark: {'TICKED (relevant)' if d['mark'] == 'x' else 'UNTICKED (not relevant)'}**",
            f"- What was broken (notes.txt): {what_i_broke(args.raw_dir, d['run'])}",
            "",
            "Your call:  agree [ ]   disagree [ ]",
            "",
        ]
    args.out.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {args.out}: {args.n} ticked + {args.n} unticked; {excl_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
