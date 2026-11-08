"""Count the filled-in spot-check (data/spotcheck.md): agreement as counts. Changes nothing.

Usage: python scripts/score_spotcheck.py [data/spotcheck.md]

Per sheet mark (ticked / unticked) and overall: agree, disagree, not yet answered, and (for a section with both or
neither box ticked) invalid. Every disagreement is listed with its sheet and URL. If there is any, STOP: labels are
not changed by this script; the human decides.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def parse(path: Path) -> list[dict]:
    items = []
    for sec in path.read_text(encoding="utf-8").split("\n### ")[1:]:
        head = sec.splitlines()[0]
        mark = "ticked" if "TICKED (relevant)" in sec else "unticked"
        agree = re.search(r"(?<!dis)agree \[([xX])\]", sec) is not None
        disagree = re.search(r"disagree \[([xX])\]", sec) is not None
        if agree and disagree:
            status = "invalid"
        elif agree:
            status = "agree"
        elif disagree:
            status = "disagree"
        else:
            status = "unanswered"
        url = re.search(r"- URL: (.*)", sec)
        items.append({"head": head, "mark": mark, "status": status, "url": url.group(1) if url else ""})
    return items


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "data" / "spotcheck.md"
    items = parse(path)
    print(f"{path.name}: {len(items)} documents")
    print(f"{'sheet mark':<10} {'n':>3} {'agree':>6} {'disagree':>9} {'unanswered':>11} {'invalid':>8}")
    for mark in ("ticked", "unticked", "all"):
        rows = [i for i in items if mark == "all" or i["mark"] == mark]
        c = {s: sum(i["status"] == s for i in rows) for s in ("agree", "disagree", "unanswered", "invalid")}
        print(f"{mark:<10} {len(rows):>3} {c['agree']:>6} {c['disagree']:>9} {c['unanswered']:>11} {c['invalid']:>8}")
    answered = [i for i in items if i["status"] in ("agree", "disagree")]
    print(f"agreement: {sum(i['status'] == 'agree' for i in answered)}/{len(answered)} answered")
    bad = [i for i in items if i["status"] == "disagree"]
    if bad:
        print("\nDISAGREEMENTS (no label was changed; stop and decide):")
        for i in bad:
            print(f"  {i['head']} (sheet mark: {i['mark']}) {i['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
