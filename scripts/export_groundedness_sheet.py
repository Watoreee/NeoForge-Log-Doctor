"""Prepare a hand-judging sheet for groundedness (PLAN 7.1). It only FORMATS outputs; it never judges anything.

Usage:
    python scripts/export_groundedness_sheet.py [--results eval/results/diagnosis_test_....json] [--condition FULL]
                                                [--out data/groundedness/test_FULL.md]

For every log in the results file: the explanation the system gave, the cited documents' excerpts (exactly what the
model was shown for each cited document), and a `[ ]` box. Groundedness = does the cited excerpt support the explanation
(0/1)? Tick `[x]` only if it does. A log with no citation has nothing to support its explanation: the sheet says so,
and the human decides how to count it (state the rule in the report).
Defaults to the most recent test results that contain the condition. Gold labels are not shown, so the judgment
is about the explanation and its sources only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def latest_results(condition: str) -> Path:
    for path in sorted((REPO_ROOT / "eval" / "results").glob("diagnosis_test_*.json"), reverse=True):
        if condition in json.loads(path.read_text(encoding="utf-8"))["per_log"]:
            return path
    sys.exit(f"No test results with condition {condition!r} in eval/results/.")


def sheet(results: dict, condition: str, source: str) -> str:
    rows = results["per_log"][condition]
    manifest = {d["doc_id"]: d for d in json.loads((REPO_ROOT / "data/processed/manifest.json").read_text("utf-8"))}
    out = [
        f"# Groundedness sheet: {condition} on {results['split']} ({len(rows)} logs)",
        "",
        f"Source: `{source}` (git {results['git_sha']}). Produced by `scripts/export_groundedness_sheet.py`; nothing here was judged.",  # noqa: E501
        "",
        "For each log: does the cited excerpt SUPPORT the explanation? Tick `[x]` if yes (judge the excerpt shown,"
        " open the URL only if it does not settle it). Leave `[ ]` if no, or if nothing is cited.",
        "",
    ]
    for r in rows:
        out += [
            "---",
            "",
            f"## {r['log_id']}  (predicted culprit: `{r['pred_culprit']}`, category `{r['pred_category']}`, "
            f"confidence {r.get('confidence')})",
            "",
            f"**Explanation:** {r.get('explanation', '')}",
            "",
        ]
        cites = r.get("citations", [])
        if not cites:
            out += ["**Citations:** none, so there is no source to support this explanation.", ""]
        for doc_id in cites:
            meta = manifest.get(doc_id, {})
            out += [
                f"- **{doc_id}**",
                f"  - {meta.get('title', '')}",
                f"  - {meta.get('url', '')}",
                f"  - excerpt shown to the model: {r.get('cited_excerpts', {}).get(doc_id, '')}",
                "",
            ]
        out += ["**Grounded?**  [ ]", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", default="FULL", choices=("FULL", "RAG1"))
    parser.add_argument("--results", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    path = args.results or latest_results(args.condition)
    results = json.loads(path.read_text(encoding="utf-8"))
    out = args.out or REPO_ROOT / "data" / "groundedness" / f"{results['split']}_{args.condition}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(sheet(results, args.condition, path.name), encoding="utf-8")
    n = len(results["per_log"][args.condition])
    print(
        f"wrote {out}: {n} logs, "
        f"{sum(bool(r.get('citations')) for r in results['per_log'][args.condition])} with a citation"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
