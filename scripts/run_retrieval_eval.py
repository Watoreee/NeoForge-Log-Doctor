"""Retrieval evaluation at DOCUMENT level (PLAN 7.1, 7.3): the query-construction experiment, B2, abstention.

Usage:
    python scripts/run_retrieval_eval.py --split dev --grid            # dev: metrics + abstention over a cosine grid
    python scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.55   # test, once, at the chosen floor

Conditions (all ranked with NO floor, min_score=None; chunks are collapsed to documents by doc_id):
    hybrid_a  hybrid, preprocessed log as the query          bm25_a  = B2 (BM25 only, preprocessed log)
    hybrid_b  hybrid, extracted-fields query                 bm25_b, dense_b  retriever comparison at query (b)
    hybrid_c  hybrid, oracle query (gold culprits + category; exception type kept from extraction)
Recall@5 and MRR are computed only on logs with non-empty relevant_doc_ids. Logs with support_search = "none_found"
are reported separately under abstention (the floor is applied to hybrid_b, the deployed retrieval); "uncertain" logs
are counted and excluded. Never reads data/demo. Test needs --allow-test (tune on dev, confirm once on test).
Extraction and query embeddings are cached, so a rerun costs nothing and CRASHDOC_REPLAY=1 works.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from crashdoc.extraction import extract_facts  # noqa: E402
from crashdoc.llm import LLM  # noqa: E402
from crashdoc.preprocess import preprocess_log  # noqa: E402
from crashdoc.retrieval.index import Index, top_docs  # noqa: E402
from crashdoc.retrieval.query import build_query, embedding_input, oracle_facts  # noqa: E402
from crashdoc.schemas import GoldLabel  # noqa: E402
from eval.bootstrap import paired_bootstrap  # noqa: E402
from eval.metrics import recall_at_k, reciprocal_rank  # noqa: E402

CONDITIONS = ("hybrid_a", "hybrid_b", "hybrid_c", "bm25_a", "bm25_b", "dense_b")
GRID = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
K = 5
DEPTH = 1000  # documents kept per ranking (effectively all candidates)


def load_split(split: str) -> list[tuple[GoldLabel, str]]:
    rows = []
    for label_path in sorted((REPO_ROOT / "data" / "gold" / split).glob("*.json")):
        label = GoldLabel.model_validate(json.loads(label_path.read_text(encoding="utf-8")))
        log = next(p for p in label_path.parent.glob(f"{label_path.stem}.*") if p.suffix != ".json")
        rows.append((label, log.read_text(encoding="utf-8")))
    return rows


def rank_conditions(index: Index, llm: LLM, label: GoldLabel, text: str) -> tuple[dict, dict]:
    pre = preprocess_log(text)
    facts_b = extract_facts(llm, pre, text).facts
    q = {"a": pre.text, "b": build_query(facts_b), "c": build_query(oracle_facts(facts_b, label))}
    inputs = list(dict.fromkeys(embedding_input(x) for x in q.values() if x.strip()))
    vectors = dict(zip(inputs, llm.embed(inputs), strict=True))

    def vec(x: str):
        return np.array(vectors[embedding_input(x)], dtype=np.float32) if x.strip() else None

    plan = {
        "hybrid_a": ("hybrid", "a"),
        "hybrid_b": ("hybrid", "b"),
        "hybrid_c": ("hybrid", "c"),
        "bm25_a": ("bm25", "a"),
        "bm25_b": ("bm25", "b"),
        "dense_b": ("dense", "b"),
    }
    rankings, results = {}, {}
    for name, (mode, which) in plan.items():
        if not q[which].strip():
            rankings[name] = []
            continue
        res = index.search(mode, query_text=q[which], query_vec=vec(q[which]), min_score=None)
        results[name] = res
        rankings[name] = [d.doc_id for d in top_docs(res.hits, DEPTH)]
    return rankings, {"results": results, "query_b": q["b"], "vec_b": vec(q["b"]), "text_b": q["b"]}


def abstain_info(index: Index, extra: dict, floor: float | None) -> dict:
    """Does hybrid (b) abstain at this floor, and which BM25-only candidates would it drop?"""
    if not extra["text_b"].strip():
        return {"abstained": True, "max_cos": None, "dropped_bm25_only": []}
    res = index.search("hybrid", query_text=extra["text_b"], query_vec=extra["vec_b"], min_score=floor)
    full = extra["results"]["hybrid_b"]
    return {
        "abstained": res.abstained,
        "max_cos": round(max((h.cos for h in full.hits), default=0.0), 3),
        "dropped_bm25_only": [h.doc_id for h in res.dropped_bm25_only],
    }


def mean(xs: list[float]) -> float | None:
    return round(sum(xs) / len(xs), 3) if xs else None


def git_sha() -> str:
    out = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
    return out.stdout.strip() or "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=("dev", "test"), required=True)
    parser.add_argument("--allow-test", action="store_true")
    parser.add_argument("--grid", action="store_true", help="abstention over a cosine grid (dev only)")
    parser.add_argument("--min-score", type=float, default=None, help="floor for the abstention numbers")
    args = parser.parse_args()
    if args.split == "test" and not args.allow_test:
        sys.exit("Refusing to run on test without --allow-test (tune on dev, confirm once on test).")
    if args.grid and args.split == "test":
        sys.exit("The cosine grid is for dev only: choosing the floor from test would tune on test.")

    llm, index = LLM(), Index.load()
    per_log, extras = {}, {}
    for label, text in load_split(args.split):
        rankings, extra = rank_conditions(index, llm, label, text)
        per_log[label.log_id] = {"label": label, "rankings": rankings}
        extras[label.log_id] = extra

    judged = {k: v for k, v in per_log.items() if v["label"].relevant_doc_ids}  # non-empty relevant_doc_ids
    none_found = {k: v for k, v in per_log.items() if v["label"].support_search == "none_found"}
    uncertain = [k for k, v in per_log.items() if v["label"].support_search == "uncertain"]
    scen = lambda d: len({v["label"].scenario_id for v in d.values()})  # noqa: E731

    print(
        f"split={args.split}: {len(per_log)} logs from {scen(per_log)} scenarios | with relevant docs: "
        f"{len(judged)} logs from {scen(judged)} scenarios | none_found: {len(none_found)} logs from "
        f"{scen(none_found)} scenarios | uncertain (excluded): {len(uncertain)}"
    )
    summary, rr, rc = {}, {}, {}
    print(f"\nRetrieval, document level, no floor (N={len(judged)} logs from {scen(judged)} scenarios)")
    print(f"{'condition':10} {'recall@5':>9} {'hit@5':>7} {'MRR':>7}")
    for cond in CONDITIONS:
        rec = {k: recall_at_k(v["rankings"][cond], v["label"].relevant_doc_ids, K) for k, v in judged.items()}
        rrk = {k: reciprocal_rank(v["rankings"][cond], v["label"].relevant_doc_ids) for k, v in judged.items()}
        rc[cond], rr[cond] = rec, rrk
        hits = sum(r > 0 for r in rec.values())
        summary[cond] = {
            "recall@5_mean": mean(list(rec.values())),
            "hit@5": f"{hits}/{len(rec)}",
            "mrr_mean": mean(list(rrk.values())),
        }
        print(
            f"{cond:10} {summary[cond]['recall@5_mean']!s:>9} {summary[cond]['hit@5']:>7} {summary[cond]['mrr_mean']!s:>7}"
        )  # noqa: E501
    scenario_of = {k: v["label"].scenario_id for k, v in judged.items()}
    boot = {}
    if judged:
        boot = {
            "b_minus_a": paired_bootstrap(scenario_of, rc["hybrid_a"], rc["hybrid_b"]),
            "c_minus_b": paired_bootstrap(scenario_of, rc["hybrid_b"], rc["hybrid_c"]),
        }
        for name, b in boot.items():
            print(
                f"recall@5 {name}: delta {b['delta']:+.3f}, 95% CI {b['ci95']} "
                f"({'includes 0: exploratory' if b['includes_zero'] else 'excludes 0'}; {b['n_scenarios']} scenarios)"
            )  # noqa: E501

    print("\nPer-log recall@5 (a / b / c) and first relevant rank under hybrid (b):")
    for k, v in judged.items():
        print(
            f"  {k:12} {v['label'].scenario_id[:30]:30} a={rc['hybrid_a'][k]:.2f} b={rc['hybrid_b'][k]:.2f} "
            f"c={rc['hybrid_c'][k]:.2f} B2(bm25_a)={rc['bm25_a'][k]:.2f}"
        )

    abstain = {}
    floors = GRID if args.grid else ([args.min_score] if args.min_score is not None else [])
    for floor in floors:
        info = {k: abstain_info(index, extras[k], floor) for k in per_log}
        rec_n = sum(info[k]["abstained"] for k in none_found)
        spec_n = sum(not info[k]["abstained"] for k in judged)
        dropped = sum(len(info[k]["dropped_bm25_only"]) for k in per_log)
        dropped_rel = sum(
            d in per_log[k]["label"].relevant_doc_ids for k in judged for d in info[k]["dropped_bm25_only"]
        )
        abstain[str(floor)] = {
            "abstention_recall": f"{rec_n}/{len(none_found)}",
            "abstention_specificity": f"{spec_n}/{len(judged)}",
            "bm25_only_dropped": dropped,
            "bm25_only_dropped_relevant": dropped_rel,
        }
        print(
            f"floor {floor:.2f}: abstention recall {rec_n}/{len(none_found)} | specificity {spec_n}/{len(judged)} "
            f"| BM25-only candidates dropped {dropped} (relevant: {dropped_rel})"
        )
    maxcos = {k: extras[k] and abstain_info(index, extras[k], None)["max_cos"] for k in per_log}
    print(
        "\nmax cosine of any candidate (hybrid b), none_found logs:",
        {k: maxcos[k] for k in none_found},
        "\n  logs with relevant docs:",
        {k: maxcos[k] for k in judged},
    )

    out = {
        "split": args.split,
        "git_sha": git_sha(),
        "utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "n_logs": len(per_log),
        "n_judged_logs": len(judged),
        "n_none_found": len(none_found),
        "n_uncertain_excluded": len(uncertain),
        "retrieval": summary,
        "bootstrap": boot,
        "per_log_recall5": {c: rc[c] for c in CONDITIONS},
        "per_log_rr": {c: rr[c] for c in CONDITIONS},
        "abstention": abstain,
        "max_cosine_hybrid_b": maxcos,
        "usage": llm.usage.summary(),
    }
    path = (
        REPO_ROOT / "eval" / "results" / f"retrieval_{args.split}_{out['utc'].replace(':', '')}_{out['git_sha']}.json"
    )  # noqa: E501
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nresults: {path.relative_to(REPO_ROOT)}   usage: {json.dumps(out['usage'])[:160]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
