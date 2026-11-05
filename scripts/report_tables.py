"""Print the report's tables from the latest result files (no new LLM calls, no numbers typed by hand).

Usage: python scripts/report_tables.py [--split test|dev]

Culprit differences use the scenario-level paired bootstrap (eval/bootstrap.py, 1,000 resamples, seed 0).
Also lists every log where a condition missed the strict culprit or the category, with its real log id.
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from eval.bootstrap import paired_bootstrap  # noqa: E402

CONDS = ("B0", "B1", "RAG1", "FULL")
NAMES = {"B0": "B0 (LLM only)", "B1": "B1 (regex heuristic)", "RAG1": "RAG-1", "FULL": "Agent"}


def latest(kind: str, split: str, needs: str | None = None) -> dict:
    for path in sorted(glob.glob(str(REPO_ROOT / "eval" / "results" / f"{kind}_{split}_*.json")), reverse=True):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if needs is None or needs in data.get("per_log", {}):
            data["_file"] = Path(path).name
            return data
    sys.exit(f"no {kind} results for {split}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="test", choices=("dev", "test"))
    split = ap.parse_args().split
    diag = latest("diagnosis", split, "FULL")
    ret = latest("retrieval", split)
    per = diag["per_log"]
    scen = {r["log_id"]: r["scenario_id"] for r in per["B0"]}

    print(f"## Diagnosis, {split} ({diag['_file']}, git {diag['git_sha']})\n")
    print("| Condition | culprit strict | culprit lenient | category | logs with a citation | citations valid |")
    print("|---|---|---|---|---|---|")
    for c in CONDS:
        s = diag["summary"][c]
        n = s["n_logs"]
        print(
            f"| {NAMES[c]} | {s['culprit_strict']} ({s['culprit_strict_rate']:.0%}) | {s['culprit_lenient']} "
            f"({s['culprit_lenient_rate']:.0%}) | {s.get('category', 'n/a')} | "
            f"{s.get('logs_with_a_citation', 'n/a')} | {s.get('citations', 'n/a')} |"
            if c != "B1"
            else f"| {NAMES[c]} | {s['culprit_strict']} ({s['culprit_strict_rate']:.0%}) | {s['culprit_lenient']} "
            f"({s['culprit_lenient_rate']:.0%}) | n/a | n/a | n/a |"
        )
    print(f"\n{n} logs from {diag['summary']['B0']['n_scenarios']} scenarios.\n")

    print("Paired differences in strict culprit accuracy (scenario-level bootstrap, 95% interval):\n")
    print("| Comparison | difference (logs) | 95% CI | includes 0 |")
    print("|---|---|---|---|")
    for a, b in (("B1", "B0"), ("B0", "RAG1"), ("B0", "FULL"), ("RAG1", "FULL")):
        x = {r["log_id"]: float(r["strict"]) for r in per[a]}
        y = {r["log_id"]: float(r["strict"]) for r in per[b]}
        r = paired_bootstrap(scen, x, y)
        lo, hi = r["ci95"]
        print(f"| {NAMES[b]} minus {NAMES[a]} | {r['delta']:+.3f} | [{lo:+.3f}, {hi:+.3f}] | {r['includes_zero']} |")

    print(f"\n## Retrieval, {split} ({ret['_file']})\n")
    print(f"{ret['n_judged_logs']} logs with relevant documents; {ret['n_none_found']} `none_found` logs excluded.\n")
    print("| Query | recall@5 | hit@5 | MRR |")
    print("|---|---|---|---|")
    for k, v in ret["retrieval"].items():
        print(f"| {k} | {v['recall@5_mean']:.3f} | {v['hit@5']} | {v['mrr_mean']:.3f} |")
    print("\n| Difference | delta recall@5 | 95% CI | scenarios |")
    print("|---|---|---|---|")
    for k, v in ret["bootstrap"].items():
        print(f"| {k} | {v['delta']:+.3f} | [{v['ci95'][0]:+.3f}, {v['ci95'][1]:+.3f}] | {v['n_scenarios']} |")
    print("\nAbstention:", json.dumps(ret["abstention"]))

    print("\n## Misses (log id: gold culprit / predicted culprit; gold category / predicted category)\n")
    for c in CONDS:
        miss = [r for r in per[c] if not r["strict"] or (c != "B1" and not r.get("category", True))]
        print(f"**{NAMES[c]}** ({len(miss)} logs)\n")
        for r in miss:
            tags = []
            if not r["strict"]:
                tags.append("culprit")
            if c != "B1" and not r.get("category", True):
                tags.append("category")
            print(
                f"- `{r['log_id']}` [{'+'.join(tags)}]: {r['gold_culprit']} / {r['pred_culprit']}; "
                f"{r['gold_category']} / {r['pred_category']}"
            )
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
