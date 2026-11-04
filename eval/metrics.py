"""Evaluation metrics (PLAN 7.1). Culprit accuracy is always reported twice (decisions.md):

- **strict**: the prediction equals `culprit_mod_id`;
- **lenient**: the prediction is in `acceptable_culprits`.

Lenient alone would hide "blames the victim" errors, because the acceptable lists of some scenarios are long
(r08 has 12 entries, r17 has 26). For logs with no culprit (`culprit_mod_id = null`, e.g. out of memory), a
prediction is correct only if it is also null/empty, under both metrics.
"""

from __future__ import annotations

from dataclasses import dataclass

from crashdoc.schemas import GoldLabel


def _norm(mod_id: str | None) -> str | None:
    mod_id = (mod_id or "").strip().lower()
    return mod_id or None


def culprit_strict(pred: str | None, gold: GoldLabel) -> bool:
    return _norm(pred) == _norm(gold.culprit_mod_id)


def culprit_lenient(pred: str | None, gold: GoldLabel) -> bool:
    if gold.culprit_mod_id is None:
        return _norm(pred) is None
    return _norm(pred) in {_norm(a) for a in gold.acceptable_culprits}


def category_correct(pred: str | None, gold: GoldLabel) -> bool:
    return (pred or "").strip().lower() == gold.category.value


@dataclass
class Row:
    """One log's outcome under one condition."""

    log_id: str
    scenario_id: str
    pred_culprit: str | None
    pred_category: str | None
    strict: bool
    lenient: bool
    category: bool


def score(log_id: str, pred_culprit: str | None, pred_category: str | None, gold: GoldLabel) -> Row:
    return Row(
        log_id=log_id,
        scenario_id=gold.scenario_id,
        pred_culprit=_norm(pred_culprit),
        pred_category=pred_category,
        strict=culprit_strict(pred_culprit, gold),
        lenient=culprit_lenient(pred_culprit, gold),
        category=category_correct(pred_category, gold),
    )


def summarize(rows: list[Row], has_category: bool = True) -> dict:
    """Counts, never bare percentages: every table states 'N logs from M scenarios' (PLAN 7.1)."""
    n = len(rows)
    out = {
        "n_logs": n,
        "n_scenarios": len({r.scenario_id for r in rows}),
        "culprit_strict": f"{sum(r.strict for r in rows)}/{n}",
        "culprit_lenient": f"{sum(r.lenient for r in rows)}/{n}",
    }
    out["culprit_strict_rate"] = round(sum(r.strict for r in rows) / n, 3) if n else None
    out["culprit_lenient_rate"] = round(sum(r.lenient for r in rows) / n, 3) if n else None
    if has_category:
        out["category"] = f"{sum(r.category for r in rows)}/{n}"
    return out


# --------------------------------------------------------------------------- retrieval metrics (document level)


def recall_at_k(ranked_doc_ids: list[str], relevant: list[str], k: int = 5) -> float:
    """Fraction of the relevant documents that appear in the top k. `ranked_doc_ids` is already one entry per doc."""
    rel = set(relevant)
    return len(rel & set(ranked_doc_ids[:k])) / len(rel)


def reciprocal_rank(ranked_doc_ids: list[str], relevant: list[str]) -> float:
    """1 / rank of the first relevant document, 0 if none is ranked."""
    rel = set(relevant)
    for rank, doc_id in enumerate(ranked_doc_ids, start=1):
        if doc_id in rel:
            return 1.0 / rank
    return 0.0
