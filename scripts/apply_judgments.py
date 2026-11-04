"""Turn the annotated judging sheets in data/pool/ into relevant_doc_ids / support_search on the gold labels (PLAN 6.7).

Usage:
    python scripts/apply_judgments.py            # dry run: print what would be written, change nothing
    python scripts/apply_judgments.py --write    # write the label files

Per sheet (one per scenario):
- every `- [x] **<doc_id>**` line is a relevant document; documents under "## Added by hand" count too
  (any `gh-issue:` / `gh-release:` / `neoforge-docs:` id found there);
- `Support search:` value (none_found / uncertain) is read from that line, blank if some doc is relevant.
A log inherits its scenario's judgments. A sheet whose judgments are inconsistent (no [x] and no support value,
or both, or an unknown doc id) is reported as an error and nothing is written for the run.
The sheets are only read, never modified.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
POOL = REPO_ROOT / "data" / "pool"
GOLD = REPO_ROOT / "data" / "gold"

# Sheets are final and keep the ids they were exported with; the two out_of_memory runs were later merged into
# one scenario group (decisions.md), so both sheets feed the same label group and must agree.
SCENARIO_ALIASES = {
    "r10_out_of_memory_none": "r10_r11_out_of_memory_none",
    "r11_out_of_memory_none": "r10_r11_out_of_memory_none",
}

_HEADER = re.compile(r"^# Judging sheet \d+: `([^`]+)`")
_CHECKED = re.compile(r"^- \[[xX]\] \*\*([^*]+)\*\*")
_SUPPORT = re.compile(r"^\*\*Support search:\*\*.*?->\s*(.*)$")
_DOC_ID = re.compile(r"(?:gh-issue|gh-release|neoforge-docs):[^\s`*,;]+")


@dataclass
class Judgment:
    scenario_id: str
    sheet: str
    relevant: list[str] = field(default_factory=list)
    by_hand: list[str] = field(default_factory=list)
    support: str | None = None
    problems: list[str] = field(default_factory=list)


def parse_sheet(path: Path) -> Judgment:
    lines = path.read_text(encoding="utf-8").splitlines()
    m = _HEADER.match(lines[0]) if lines else None
    if not m:
        raise ValueError(f"{path.name}: not a judging sheet")
    j = Judgment(SCENARIO_ALIASES.get(m.group(1), m.group(1)), path.name)
    in_hand = False
    for line in lines[1:]:
        if line.startswith("## Added by hand"):
            in_hand = True
            continue
        if in_hand:
            j.by_hand += _DOC_ID.findall(line)
            continue
        if c := _CHECKED.match(line):
            j.relevant.append(c.group(1).strip())
        elif s := _SUPPORT.match(line):
            value = s.group(1).strip().strip("`").strip()
            # the unfilled template reads "none_found` / `uncertain` / (leave blank ...)"
            j.support = value if value in ("none_found", "uncertain") else None
            if value and value not in ("none_found", "uncertain"):
                j.problems.append(f"unrecognised Support search value {value!r}")
    j.relevant = list(dict.fromkeys(j.relevant + j.by_hand))
    return j


def check(j: Judgment, known: set[str]) -> None:
    unknown = [d for d in j.relevant if d not in known]
    if unknown:
        j.problems.append(f"unknown doc ids: {unknown}")
    if j.relevant and j.support:
        j.problems.append(f"{len(j.relevant)} relevant doc(s) AND support_search={j.support!r}")
    if not j.relevant and not j.support:
        j.problems.append("no relevant doc and no Support search value (unjudged)")


def label_files() -> list[Path]:
    return sorted(p for split in ("dev", "test") for p in (GOLD / split).glob("*.json"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    known = {d["doc_id"] for d in json.loads((REPO_ROOT / "data/processed/manifest.json").read_text("utf-8"))}
    judgments: dict[str, Judgment] = {}
    for sheet in sorted(POOL.glob("[0-9][0-9]_*.md")):
        j = parse_sheet(sheet)
        check(j, known)
        if (prev := judgments.get(j.scenario_id)) is not None:
            if (sorted(prev.relevant), prev.support) != (sorted(j.relevant), j.support):
                prev.problems.append(f"sheets {prev.sheet} and {j.sheet} share a scenario but disagree")
            prev.sheet += f" + {j.sheet[:2]}"
            prev.problems += j.problems
            continue
        judgments[j.scenario_id] = j

    labels = {p: json.loads(p.read_text(encoding="utf-8")) for p in label_files()}
    scenarios = {d["scenario_id"] for d in labels.values()}
    errors = [f"{sid}: {p}" for sid, j in judgments.items() for p in j.problems]
    errors += [f"scenario {sid!r} has labels but no sheet" for sid in sorted(scenarios - judgments.keys())]
    errors += [f"sheet for {sid!r} matches no label" for sid in sorted(judgments.keys() - scenarios)]

    for j in judgments.values():
        shown = ", ".join(j.relevant) if j.relevant else f"(none) support_search={j.support}"
        print(f"{j.sheet[:44]:44} relevant={len(j.relevant)} by_hand={len(j.by_hand)} support={j.support}")
        if j.relevant:
            print(f"    {shown}")
    if errors:
        print("\nERRORS (nothing written):")
        print("\n".join(f"  {e}" for e in errors))
        return 1
    if not args.write:
        print("\nDry run: pass --write to update the label files.")
        return 0
    for path, data in labels.items():
        j = judgments[data["scenario_id"]]
        data["relevant_doc_ids"] = list(j.relevant)
        data["support_search"] = None if j.relevant else j.support
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nWrote {len(labels)} label files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
