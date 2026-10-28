"""Fixed-size token chunking with bge-m3's own tokenizer (PLAN 6.4, docs/decisions.md).

Why token windows over the embedding model's tokenizer: chunk sizes are then exact for the model
that embeds them. Each chunk is an exact character slice of the source text (via token offsets),
so the excerpt shown in a citation is real source text, never re-joined tokens.
"""

from __future__ import annotations

import hashlib
from functools import lru_cache
from typing import Any

from crashdoc.config import (
    CHUNK_OVERLAP,
    CHUNK_TOKENS,
    MAX_CHUNKS_PER_THREAD,
    TOKENIZER_REPO,
    TOKENIZER_REVISION,
    use_os_trust_store,
)

# Sources whose docs are capped at MAX_CHUNKS_PER_THREAD (long issue threads / release notes).
CAPPED_SOURCES = {"github_issue", "github_release"}


@lru_cache(maxsize=1)
def load_tokenizer():
    """bge-m3's tokenizer files only (no model weights), at a pinned revision."""
    use_os_trust_store()
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(TOKENIZER_REPO, revision=TOKENIZER_REVISION)


def token_windows(text: str, tokenizer, size: int, overlap: int) -> list[tuple[int, int]]:
    """Character spans of consecutive `size`-token windows that overlap by `overlap` tokens."""
    offsets = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)["offset_mapping"]
    if not offsets:
        return []
    step = size - overlap
    spans = []
    for start in range(0, len(offsets), step):
        window = offsets[start : start + size]
        spans.append((window[0][0], window[-1][1]))
        if start + size >= len(offsets):
            break
    return spans


def chunk_doc(
    doc: dict[str, Any],
    tokenizer,
    size: int = CHUNK_TOKENS,
    overlap: int = CHUNK_OVERLAP,
    max_chunks: int | None = MAX_CHUNKS_PER_THREAD,
) -> list[dict[str, Any]]:
    """Split one raw doc into chunks carrying the metadata citations need (PLAN 6.4)."""
    spans = token_windows(doc["text"], tokenizer, size, overlap)
    if max_chunks is not None and doc["source_type"] in CAPPED_SOURCES:
        spans = spans[:max_chunks]
    return [
        {
            "chunk_id": f"{doc['doc_id']}#{i}",
            "doc_id": doc["doc_id"],
            "url": doc["url"],
            "title": doc["title"],
            "source_type": doc["source_type"],
            "text": doc["text"][start:end].strip(),
        }
        for i, (start, end) in enumerate(spans)
    ]


def index_text(chunk: dict[str, Any]) -> str:
    """What BM25 and the embedder see: the title gives every chunk its context (mod, issue, page)."""
    return f"{chunk['title']}\n\n{chunk['text']}"


def content_hash(text: str) -> str:
    """Drift guard for the manifest (PLAN 6.4): a refetch with a different hash is a different corpus."""
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()
