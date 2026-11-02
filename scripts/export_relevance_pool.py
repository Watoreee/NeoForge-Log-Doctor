"""Export the relevance pool for human judging (PLAN 6.7).

Usage:
    python scripts/export_relevance_pool.py [--out data/pool] [--top 10]

For every gold log, run the six pooled retrieval conditions with NO cosine floor (min_score=None):
    hybrid (a) preprocessed log | hybrid (b) extracted fields | hybrid (c) oracle
    BM25 (a) | BM25 (b) | dense (b)
take the top-N documents (deduplicated by doc_id) from each ranking, union them PER SCENARIO, and write one
judging sheet per scenario to <out>/<scenario_id>.md (test scenarios are numbered first: 01_..., then dev).
Also writes <out>/pool.json (machine-readable, incl. what extraction returned) and <out>/README.md.

Needs the proxy (extraction + query embeddings); both are cached on disk, so a rerun costs nothing.
The pool only ever holds redacted log text and corpus text. It never reads data/demo or demo answers.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

from crashdoc.config import REPO_ROOT
from crashdoc.extraction import LogFacts, extract_facts
from crashdoc.llm import LLM
from crashdoc.preprocess import preprocess_log
from crashdoc.retrieval.index import Index, top_docs
from crashdoc.retrieval.query import build_query, embedding_input, oracle_facts
from crashdoc.schemas import GoldLabel

GOLD = REPO_ROOT / "data" / "gold"
CONDITIONS = ("hybrid_a", "hybrid_b", "hybrid_c", "bm25_a", "bm25_b", "dense_b")
EXCERPT_CHARS = 600


def load_gold() -> list[tuple[str, GoldLabel, Path]]:
    """(split, label, log path), test split first, then dev (PLAN 6.7 order)."""
    rows = []
    for split in ("test", "dev"):
        for label_path in sorted((GOLD / split).glob("*.json")):
            label = GoldLabel.model_validate(json.loads(label_path.read_text(encoding="utf-8")))
            log = next(p for p in label_path.parent.glob(f"{label_path.stem}.*") if p.suffix != ".json")
            rows.append((split, label, log))
    return rows


def run_conditions(index: Index, llm: LLM, label: GoldLabel, text: str, top: int):
    """Rankings for one log: {condition: [DocHit]} plus the extraction result (for the record)."""
    pre = preprocess_log(text)
    ext = extract_facts(llm, pre, text)
    facts_b: LogFacts = ext.facts
    facts_c = oracle_facts(facts_b, label)
    q_a, q_b, q_c = pre.text, build_query(facts_b), build_query(facts_c)

    to_embed = [t for t in dict.fromkeys(embedding_input(x) for x in (q_a, q_b, q_c) if x.strip())]
    vectors = dict(zip(to_embed, llm.embed(to_embed), strict=True))

    def vec(q: str):
        return np.array(vectors[embedding_input(q)], dtype=np.float32) if q.strip() else None

    plan = {  # condition -> (mode, query text)
        "hybrid_a": ("hybrid", q_a),
        "hybrid_b": ("hybrid", q_b),
        "hybrid_c": ("hybrid", q_c),
        "bm25_a": ("bm25", q_a),
        "bm25_b": ("bm25", q_b),
        "dense_b": ("dense", q_b),
    }
    rankings = {}
    for name, (mode, q) in plan.items():
        if not q.strip():
            rankings[name] = []  # nothing to search with (e.g. extraction found nothing)
            continue
        result = index.search(mode, query_text=q, query_vec=vec(q), min_score=None)
        rankings[name] = top_docs(result.hits, top)
    return rankings, ext, pre


def build_sheets(index: Index, llm: LLM, top: int) -> tuple[dict, dict]:
    chunk_text = {c["chunk_id"]: c["text"] for c in index.chunks}
    manifest = {d["doc_id"]: d for d in json.loads((REPO_ROOT / "data/processed/manifest.json").read_text("utf-8"))}
    scenarios: dict[str, dict] = {}
    order: list[str] = []
    for split, label, path in load_gold():
        text = path.read_text(encoding="utf-8")
        rankings, ext, pre = run_conditions(index, llm, label, text, top)
        sc = scenarios.setdefault(
            label.scenario_id,
            {
                "split": split,
                "category": label.category.value,
                "culprit": label.culprit_mod_id,
                "acceptable": label.acceptable_culprits,
                "notes": label.notes,
                "logs": [],
                "docs": {},
            },
        )
        if label.scenario_id not in order:
            order.append(label.scenario_id)
        sc["logs"].append(
            {
                "log_id": label.log_id,
                "source_file_type": label.source_file_type,
                "truncated": pre.truncated,
                "extraction_source": ext.source,
                "extracted": ext.facts.model_dump(mode="json"),
                "dropped_ids": ext.dropped_ids,
                "errors": ext.errors,
            }
        )
        for cond, docs in rankings.items():
            for rank, d in enumerate(docs, start=1):
                entry = sc["docs"].setdefault(d.doc_id, {"appearances": [], "best_chunk_id": d.best_chunk_id})
                entry["appearances"].append(
                    {"log": label.log_id, "condition": cond, "rank": rank, "cos": round(d.cos, 3)}
                )
    # finalise: metadata, excerpt, ordering
    for sc in scenarios.values():
        docs = []
        for doc_id, e in sc["docs"].items():
            meta = manifest.get(doc_id, {})
            best = min(e["appearances"], key=lambda a: a["rank"])
            docs.append(
                {
                    "doc_id": doc_id,
                    "title": meta.get("title", ""),
                    "url": meta.get("url", ""),
                    "source_type": meta.get("source_type", ""),
                    "best_chunk_id": e["best_chunk_id"],
                    "excerpt": chunk_text.get(e["best_chunk_id"], "")[:EXCERPT_CHARS],
                    "appearances": e["appearances"],
                    "n_conditions": len({a["condition"] for a in e["appearances"]}),
                    "best_rank": best["rank"],
                }
            )
        docs.sort(key=lambda d: (-d["n_conditions"], d["best_rank"], d["doc_id"]))
        sc["docs"] = docs
    return {sid: scenarios[sid] for sid in order}, manifest


def sheet_markdown(num: int, sid: str, sc: dict) -> str:
    out = [f"# Judging sheet {num:02d}: `{sid}` ({sc['split']})", ""]
    out += [
        f"- **Category:** `{sc['category']}`  |  **Culprit:** `{sc['culprit']}`  |  **Acceptable:** {', '.join(sc['acceptable']) or '(none)'}",  # noqa: E501
        f"- **What was broken:** {sc['notes']}",
        f"- **Logs in this scenario:** {', '.join(log['log_id'] for log in sc['logs'])}",
        f"- **Documents to judge:** {len(sc['docs'])}",
        "",
        "Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).",
        "Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of"  # noqa: E501
        " six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here:"
        " add it by hand under *Added by hand* (and note how you found it).",
        "",
        "If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.",
        "",
        "**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  ",
        "",
        "---",
        "",
    ]
    for d in sc["docs"]:
        apps = ", ".join(
            f"{a['condition']}#{a['rank']}@{a['log'].split('_')[0]}{a['log'].split('_')[-1][0]}"
            for a in d["appearances"]
        )
        excerpt = " ".join(d["excerpt"].split())
        out += [
            f"- [ ] **{d['doc_id']}** ({d['source_type']}, {d['n_conditions']}/6 conditions)",
            f"  - {d['title']}",
            f"  - {d['url']}",
            f"  - retrieved by: {apps}",
            f"  - excerpt: {excerpt}",
            "",
        ]
    out += ["## Added by hand", "", "(none)", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export the relevance pool for judging.")
    parser.add_argument("--out", type=Path, default=REPO_ROOT / "data" / "pool")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    llm, index = LLM(), Index.load()
    scenarios, _ = build_sheets(index, llm, args.top)
    args.out.mkdir(parents=True, exist_ok=True)
    for old in args.out.glob("[0-9][0-9]_*.md"):
        old.unlink()
    summary = []
    for num, (sid, sc) in enumerate(scenarios.items(), start=1):
        name = f"{num:02d}_{sc['split']}_{sid}.md"
        (args.out / name).write_text(sheet_markdown(num, sid, sc), encoding="utf-8")
        summary.append((name, sc["split"], len(sc["logs"]), len(sc["docs"])))
    (args.out / "pool.json").write_text(
        json.dumps({"top_n": args.top, "scenarios": scenarios}, indent=1), encoding="utf-8"
    )
    readme = [
        "# Relevance pool",
        "",
        "One sheet per scenario, test scenarios first (PLAN 6.7). Judge each once.",
        "",
        "| sheet | split | logs | docs to judge |",
        "|---|---|---|---|",
    ]
    readme += [f"| {n} | {s} | {nl} | {nd} |" for n, s, nl, nd in summary]
    readme += ["", f"Total documents to judge: {sum(r[3] for r in summary)}"]
    (args.out / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    print("\n".join(f"{n}: {nl} logs, {nd} docs" for n, _, nl, nd in summary))
    print(f"\nusage: {json.dumps(llm.usage.summary())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
