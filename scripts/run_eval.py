"""Run the diagnosis baselines B0 / B1 on a gold split and write a results file (PLAN 7.2, 7.4).

Usage:
    python scripts/run_eval.py --split dev [--conditions B0,B1]
    python scripts/run_eval.py --split test --allow-test     # tune on dev, confirm ONCE on test

Culprit accuracy is reported strict AND lenient (decisions.md). Every table states N logs from M scenarios.
Test is refused unless --allow-test is given, so nothing is tuned on it by accident.
Never reads data/demo or demo answers. Retrieval metrics are added once relevance is judged.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))  # for the top-level `eval` package

from crashdoc.baselines import b0_predict, b1_predict  # noqa: E402
from crashdoc.llm import LLM  # noqa: E402
from crashdoc.preprocess import preprocess_log  # noqa: E402
from crashdoc.schemas import GoldLabel  # noqa: E402
from eval.metrics import score, summarize  # noqa: E402


def load_split(split: str) -> list[tuple[GoldLabel, str]]:
    rows = []
    for label_path in sorted((REPO_ROOT / "data" / "gold" / split).glob("*.json")):
        label = GoldLabel.model_validate(json.loads(label_path.read_text(encoding="utf-8")))
        log = next(p for p in label_path.parent.glob(f"{label_path.stem}.*") if p.suffix != ".json")
        rows.append((label, log.read_text(encoding="utf-8")))
    return rows


def git_sha() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT
        ).stdout.strip()
    except OSError:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=("dev", "test"), required=True)
    parser.add_argument("--conditions", default="B0,B1")
    parser.add_argument("--allow-test", action="store_true")
    args = parser.parse_args()
    if args.split == "test" and not args.allow_test:
        sys.exit("Refusing to run on test without --allow-test (test is never tuned on).")
    conditions = [c.strip().upper() for c in args.conditions.split(",") if c.strip()]

    llm = LLM()
    data = load_split(args.split)
    per_log: dict[str, list[dict]] = {c: [] for c in conditions}
    rows: dict[str, list] = {c: [] for c in conditions}
    for label, text in data:
        pre = preprocess_log(text)
        for cond in conditions:
            if cond == "B1":
                culprit, category = b1_predict(pre.facts), None
            elif cond == "B0":
                r = b0_predict(llm, pre, text)
                culprit, category = r.culprit, r.category
            else:
                sys.exit(f"Unknown condition {cond!r} (B0, B1 here; RAG-1 / Full come later)")
            row = score(label.log_id, culprit, category, label)
            rows[cond].append(row)
            per_log[cond].append(
                {**row.__dict__, "gold_culprit": label.culprit_mod_id, "gold_category": label.category.value}
            )

    summary = {c: summarize(rows[c], has_category=c != "B1") for c in conditions}
    out = {
        "split": args.split,
        "git_sha": git_sha(),
        "utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "summary": summary,
        "per_log": per_log,
        "usage": llm.usage.summary(),
    }
    results_dir = REPO_ROOT / "eval" / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    path = results_dir / f"diagnosis_{args.split}_{out['utc'].replace(':', '')}_{out['git_sha']}.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    for cond, s in summary.items():
        print(
            f"{cond}: {s['n_logs']} logs from {s['n_scenarios']} scenarios | culprit strict {s['culprit_strict']}, "
            f"lenient {s['culprit_lenient']}"
            + (f" | category {s['category']}" if "category" in s else " | category n/a")
        )
    print(f"results: {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
