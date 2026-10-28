"""Chunk data/raw/ and embed the chunks (PLAN 6.4). Resumable; safe to run in the background.

Usage:
    python scripts/build_index.py --chunks-only   # data/processed/chunks.jsonl + manifest.json
    python scripts/build_index.py                 # ... then embeddings.npy + embeddings_meta.json

Embedding is resumable: each batch of EMBED_BATCH_SIZE vectors is saved to data/processed/embed_batches/
(git-ignored) as soon as it returns, keyed by a hash of its texts. A rerun skips finished batches, so an
interrupted build never repeats a paid call. Embeddings cost requests, not tokens (docs/proxy-notes.md).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

from crashdoc.config import EMBED_BATCH_SIZE, EMBED_DIM, EMBED_MODEL, REPO_ROOT
from crashdoc.llm import LLM
from crashdoc.retrieval.chunking import chunk_doc, content_hash, index_text, load_tokenizer

RAW_DIR = REPO_ROOT / "data" / "raw"
OUT_DIR = REPO_ROOT / "data" / "processed"
BATCH_DIR = OUT_DIR / "embed_batches"


def load_raw_docs(raw_dir: Path = RAW_DIR) -> list[dict]:
    """Every fetched doc, in a stable order (doc_id), so chunk order and embeddings line up across runs."""
    docs = [json.loads(p.read_text(encoding="utf-8")) for p in raw_dir.rglob("*.json")]
    return sorted((d for d in docs if d.get("text", "").strip()), key=lambda d: d["doc_id"])


def build_chunks(docs: list[dict]) -> tuple[list[dict], list[dict]]:
    """Chunks + one manifest row per doc (with licence note and content hash)."""
    tokenizer = load_tokenizer()
    chunks, manifest = [], []
    for doc in docs:
        doc_chunks = chunk_doc(doc, tokenizer)
        chunks += doc_chunks
        manifest.append(
            {
                "doc_id": doc["doc_id"],
                "url": doc["url"],
                "title": doc["title"],
                "source_type": doc["source_type"],
                "repo": doc.get("repo"),
                "fetched_at": doc["fetched_at"],
                "content_hash": content_hash(doc["text"]),
                "licence": doc["licence"],
                "n_chunks": len(doc_chunks),
            }
        )
    return chunks, manifest


def write_chunks(chunks: list[dict], manifest: list[dict]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / "chunks.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")


def print_stats(chunks: list[dict], manifest: list[dict]) -> None:
    """The corpus stats reported at CHECKPOINT 1."""
    print(f"{len(manifest)} docs, {len(chunks)} chunks")
    docs_by_source = Counter(m["source_type"] for m in manifest)
    chunks_by_source = Counter(c["source_type"] for c in chunks)
    for source in sorted(docs_by_source):
        print(f"  {source:16} {docs_by_source[source]:4} docs  {chunks_by_source[source]:5} chunks")
    by_repo = Counter((m["repo"], m["source_type"]) for m in manifest)
    for repo in sorted({m["repo"] for m in manifest}):
        print(f"  {repo:42} issues={by_repo[(repo, 'github_issue')]:3}  releases={by_repo[(repo, 'github_release')]}")


def load_chunks() -> list[dict]:
    with open(OUT_DIR / "chunks.jsonl", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def batch_key(texts: list[str]) -> str:
    return hashlib.sha256(json.dumps([EMBED_MODEL, texts], ensure_ascii=False).encode("utf-8")).hexdigest()[:24]


def embed_all(chunks: list[dict]) -> np.ndarray:
    """Embed in batches; each finished batch is saved at once, and saved batches are reused."""
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    llm = LLM()
    texts = [index_text(c) for c in chunks]
    parts = []
    n_batches = (len(texts) + EMBED_BATCH_SIZE - 1) // EMBED_BATCH_SIZE
    t0 = time.time()
    for b, start in enumerate(range(0, len(texts), EMBED_BATCH_SIZE)):
        batch = texts[start : start + EMBED_BATCH_SIZE]
        path = BATCH_DIR / f"{batch_key(batch)}.npy"
        if path.exists():
            parts.append(np.load(path))
            continue
        vectors = np.asarray(llm.embed(batch, use_cache=False), dtype=np.float32)
        np.save(path, vectors)
        parts.append(vectors)
        print(f"batch {b + 1}/{n_batches} done ({time.time() - t0:.0f} s)", flush=True)
    matrix = np.vstack(parts)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True)  # unit length: cosine = dot product
    print("usage:", json.dumps(llm.usage.summary()))
    return matrix


def main() -> int:
    parser = argparse.ArgumentParser(description="Chunk the corpus and embed it.")
    parser.add_argument("--chunks-only", action="store_true", help="write chunks.jsonl + manifest.json only")
    args = parser.parse_args()

    chunks, manifest = build_chunks(load_raw_docs())
    write_chunks(chunks, manifest)
    print_stats(chunks, manifest)
    if args.chunks_only:
        return 0

    matrix = embed_all(chunks)
    assert matrix.shape == (len(chunks), EMBED_DIM), matrix.shape
    np.save(OUT_DIR / "embeddings.npy", matrix)
    meta = {
        "model": EMBED_MODEL,
        "dim": EMBED_DIM,
        "n_chunks": len(chunks),
        "normalized": True,
        "chunks_sha256": hashlib.sha256((OUT_DIR / "chunks.jsonl").read_bytes()).hexdigest(),
        "built_at": datetime.now(UTC).isoformat(timespec="seconds"),
    }
    (OUT_DIR / "embeddings_meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
    print(f"wrote embeddings.npy {matrix.shape}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
