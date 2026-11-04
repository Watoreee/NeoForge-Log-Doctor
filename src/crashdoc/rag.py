"""RAG-1: extraction -> retrieval -> one Diagnosis call, temperature 0 (PLAN 6.6, 7.2)."""

from __future__ import annotations

import numpy as np

from crashdoc.diagnosis import (
    DIAGNOSIS_RULES,
    DiagnosisResult,
    Evidence,
    excerpt,
    facts_summary,
    format_documents,
    parse_with_repair,
)
from crashdoc.extraction import extract_facts
from crashdoc.llm import LLM
from crashdoc.preprocess import Preprocessed
from crashdoc.retrieval.index import Index, top_docs
from crashdoc.retrieval.query import build_query, embedding_input

RAG_PROMPT_VERSION = "rag1-v1"
MIN_SCORE = 0.45  # cosine floor: middle of the dev specificity plateau (decisions.md)
TOP_DOCS = 4

RAG_SYSTEM = (
    "You diagnose Minecraft NeoForge 1.21.1 crashes from a crash report or log, helped by retrieved documents "
    "(GitHub issues, release notes, NeoForge docs).\n" + DIAGNOSIS_RULES
)


def retrieve_evidence(index: Index, llm: LLM, query_text: str, k: int = TOP_DOCS, min_score: float | None = MIN_SCORE):
    """Hybrid search with the cosine floor, collapsed to documents. Returns (evidence list, abstained)."""
    if not query_text.strip():
        return [], True
    vec = np.array(llm.embed([embedding_input(query_text)])[0], dtype=np.float32)
    res = index.search("hybrid", query_text=query_text, query_vec=vec, min_score=min_score)
    out = []
    for d in top_docs(res.hits, k):
        chunk = index.chunk(d.best_chunk_id)
        out.append(Evidence(d.doc_id, chunk.get("title", ""), excerpt(chunk["text"])))
    return out, res.abstained


def rag1(
    llm: LLM, index: Index, pre: Preprocessed, full_text: str, min_score: float | None = MIN_SCORE
) -> DiagnosisResult:
    ext = extract_facts(llm, pre, full_text)
    evidence, _abstained = retrieve_evidence(index, llm, build_query(ext.facts), min_score=min_score)
    user = (
        f"Log:\n{pre.text}\n\n{facts_summary(pre.facts, ext.facts)}\n\nRetrieved documents:\n{format_documents(evidence)}"  # noqa: E501
        "\n\nReturn the JSON object."
    )
    messages = [{"role": "system", "content": RAG_SYSTEM}, {"role": "user", "content": user}]
    retrieved = {e.doc_id: e.excerpt for e in evidence}
    return parse_with_repair(llm, messages, RAG_PROMPT_VERSION, full_text, retrieved, ext.facts)
