"""Chunking: token windows, exact source slices, per-thread cap. A whitespace tokenizer stands in for bge-m3."""

from __future__ import annotations

import re

from crashdoc.retrieval.chunking import chunk_doc, content_hash, index_text, token_windows


class WordTokenizer:
    """One token per whitespace-separated word, with character offsets like a fast HF tokenizer."""

    def __call__(self, text, add_special_tokens=False, return_offsets_mapping=True):
        return {"offset_mapping": [m.span() for m in re.finditer(r"\S+", text)]}


TOK = WordTokenizer()


def _doc(n_words: int, source_type="neoforge_docs") -> dict:
    return {
        "doc_id": "d1",
        "url": "https://example.test/d1",
        "title": "Doc one",
        "source_type": source_type,
        "text": " ".join(f"w{i}" for i in range(n_words)),
    }


def test_windows_overlap_and_cover_everything():
    text = " ".join(f"w{i}" for i in range(10))
    spans = token_windows(text, TOK, size=4, overlap=1)
    chunks = [text[a:b].split() for a, b in spans]
    assert chunks == [["w0", "w1", "w2", "w3"], ["w3", "w4", "w5", "w6"], ["w6", "w7", "w8", "w9"]]


def test_short_and_empty_text():
    assert token_windows("only three words", TOK, size=4, overlap=1) == [(0, 16)]
    assert token_windows("   ", TOK, size=4, overlap=1) == []


def test_chunks_are_exact_slices_with_metadata():
    doc = _doc(9)
    chunks = chunk_doc(doc, TOK, size=4, overlap=0, max_chunks=None)
    assert [c["chunk_id"] for c in chunks] == ["d1#0", "d1#1", "d1#2"]
    assert all(c["text"] in doc["text"] for c in chunks)
    assert {c["url"] for c in chunks} == {doc["url"]} and chunks[0]["source_type"] == "neoforge_docs"


def test_cap_applies_to_issue_threads_only():
    assert len(chunk_doc(_doc(100, "github_issue"), TOK, size=4, overlap=0, max_chunks=3)) == 3
    assert len(chunk_doc(_doc(100, "neoforge_docs"), TOK, size=4, overlap=0, max_chunks=3)) == 25


def test_index_text_includes_title_and_hash_is_stable():
    chunk = chunk_doc(_doc(3), TOK, size=4, overlap=0)[0]
    assert index_text(chunk).startswith("Doc one\n\n")
    assert content_hash("abc") == content_hash("abc") != content_hash("abd")
