"""Query construction (PLAN 6.5): one template, three fillings.

(a) the preprocessed log text itself (no template); (b) the template filled from extracted `LogFacts`;
(c) the oracle: the same template as (b) with gold values wherever a gold label exists
(`acceptable_culprits` for the mod ids, gold `category`; `exception_type` stays from extraction).
"""

from __future__ import annotations

from crashdoc.extraction import LogFacts
from crashdoc.preprocess import RawLogFacts
from crashdoc.schemas import Category, GoldLabel

# A small fixed keyword map per category (PLAN 6.5): plain words that docs and issues use for that failure.
CATEGORY_KEYWORDS: dict[str, str] = {
    "missing_dependency": "missing dependency requires mod not found not installed",
    "version_mismatch": "version mismatch incompatible wrong minecraft neoforge version requires",
    "out_of_memory": "OutOfMemoryError java heap space allocate more memory Xmx",
    "mixin_conflict": "mixin conflict apply failed InvalidMixinException",
    "other": "",
}

EMBED_QUERY_CHARS = 6_000  # an embedding input is capped; the preprocessed log puts the diagnosis lines first


def build_query(facts: LogFacts) -> str:
    """The (b) template: exception type + suspect mod ids + the category's keywords."""
    category = facts.error_category.value if isinstance(facts.error_category, Category) else ""
    parts = [facts.exception_type or "", " ".join(facts.suspect_mod_ids), CATEGORY_KEYWORDS.get(category, "")]
    return " ".join(p for p in parts if p).strip()


def oracle_facts(extracted: LogFacts, gold: GoldLabel) -> LogFacts:
    """(c): gold culprit list and category replace the extracted ones; the exception type is kept."""
    return extracted.model_copy(
        update={"suspect_mod_ids": list(gold.acceptable_culprits), "error_category": Category(gold.category)}
    )


def oracle2_facts(raw: RawLogFacts, gold: GoldLabel) -> LogFacts:
    """(c2): gold culprit (the single `culprit_mod_id`) + gold category + the parser's regex-derived exception type.

    Unlike (c), no LLM output is used at all, so the only thing that separates (c2) from the deployed (b) is extraction
    accuracy on culprit, category and exception type.
    """
    return LogFacts(
        exception_type=raw.exceptions[0].type if raw.exceptions else None,
        error_category=Category(gold.category),
        suspect_mod_ids=[gold.culprit_mod_id] if gold.culprit_mod_id else [],
        mc_version=raw.minecraft_version,
        loader_version=raw.neoforge_version,
        java_version=raw.java_version,
    )


def embedding_input(text: str) -> str:
    """Query text for the embedder: the first EMBED_QUERY_CHARS characters."""
    return text[:EMBED_QUERY_CHARS]
