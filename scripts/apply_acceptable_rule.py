# ruff: noqa: E501  (the RULE table keeps each run on one line with its reason)
"""Apply the strict acceptable_culprits rule to every gold label and print a before/after table (labelling guide).

Rule: acceptable_culprits = culprit_mod_id + ONLY mods the human actually disabled, removed, swapped or changed
according to the run's notes.txt (including dependents notes.txt says were auto-disabled). Never mods that merely
REPORT the failure (requirers / victims). No-culprit runs (out_of_memory): culprit null, list empty.

Usage:
    python scripts/apply_acceptable_rule.py           # dry run, prints the table
    python scripts/apply_acceptable_rule.py --write   # rewrites the label files

The mapping below was derived by hand from the raw notes.txt files (kept outside the repo); each entry says why.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# run -> (acceptable list, reason from notes.txt)
RULE: dict[str, tuple[list[str], str]] = {
    "r01": (["curios"], "disabled curios; requirers (ars_nouveau, allthearcanistgear, occultism) only report it"),
    "r02": (
        ["geckolib", "theurgy"],
        "disabled geckolib; theurgy auto-disabled as its dependent (notes). ars_nouveau/theurgy_kubejs only report",
    ),
    "r03": (
        ["architectury", "rctapi"],
        "disabled Architectury API; rctapi auto-disabled as its dependent (notes). other requirers only report",
    ),
    "r04": (
        ["simpletms", "cloth_config"],
        "disabled cloth-config (notes), which took simpletms with it; allthemons only reports (NoClassDefFoundError)",
    ),
    "r05": (
        ["kotlinforforge"],
        "disabled KotlinForForge; notes say Cobblemon and dependents 'failed to load', not that they were auto-disabled",
    ),
    "r06": (["ironfurnaces"], "swapped Iron Furnaces to the 26.1 build"),
    "r08": (["create"], "downgraded Create; the 11 mods needing a newer Create only report"),
    "r09": (["trashcans"], "swapped Trash Cans to the mc26.3 build"),
    "r10": ([], "no culprit: max RAM set to 3000 MB (out_of_memory)"),
    "r11": ([], "no culprit: max RAM set to 1000 MB (out_of_memory)"),
    "r12": (["ae2"], "disabled AE2; aeinfinitybooster, ae2ct, ae2importexportcard only report it"),
    "r13": (["extendedae", "megacells"], "ExtendedAE and MEGA Cells were left auto-disabled after the AE2 run (notes)"),
    "r14": (
        ["cobblemonraiddens", "owo", "mega_showdown"],
        "disabled owo-lib (rule b: missing mod accepted); Mega Showdown auto-disabled as a dependent (notes); raiddens' mixin plugin crashed",
    ),
    "r15": (["aquaculture"], "swapped Aquaculture 2 to the 26.1 build"),
    "r16": (["yungsapi"], "swapped YUNG's API to the 1.20.4 build; better* mods only report it as not installed"),
    "r17": (["architectury"], "swapped Architectury for the Fabric build; the 25 requirers only report it"),
    "r18": (["sophisticatedcore"], "swapped Sophisticated Core to the 26.1.2 build; the jei line is a side effect"),
    "r19": (["konkrete"], "swapped Konkrete for the 1.21.11 build"),
    "r20": (["ftbquests"], "disabled FTB Quests; the KubeJS script only reports the missing class"),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    changed = 0
    print(f"{'log':12} {'before':58} {'after':45} reason")
    for path in sorted(p for s in ("dev", "test") for p in (REPO_ROOT / "data" / "gold" / s).glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        after, reason = RULE[path.stem.split("_")[0]]
        culprit = None if not after else after[0]
        if culprit != data["culprit_mod_id"]:
            sys.exit(f"{path.stem}: culprit would change {data['culprit_mod_id']!r} -> {culprit!r}; not allowed here")
        before = data["acceptable_culprits"]
        short = lambda xs: (",".join(xs[:5]) + (f",+{len(xs) - 5}" if len(xs) > 5 else "")) or "[]"  # noqa: E731
        if before != after:
            changed += 1
        print(f"{path.stem:12} {short(before):58} {short(after):45} {reason if before != after else '(unchanged)'}")
        if args.write and before != after:
            data["acceptable_culprits"] = after
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n{changed} label file(s) {'rewritten' if args.write else 'would change'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
