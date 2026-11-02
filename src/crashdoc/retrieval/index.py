"""Dense + BM25 + hybrid search over the committed chunks and embeddings, with the cosine floor (PLAN 6.4).

The abstention rule is one rule with one threshold:
1. dense and BM25 each return their top-k chunks;
2. the dense cosine similarity is computed for EVERY candidate from either retriever (embeddings are in memory);
3. candidates with cosine < `min_score` are dropped. The floor applies to chunks, BEFORE fusion and dedupe;
4. nothing left -> abstain;
5. otherwise the survivors' two rankings are fused with RRF.
`min_score=None` means no floor: the relevance pool (6.7) and the retrieval metrics (7.1) use it.
BM25-only candidates that the floor dropped are reported, so the trade-off is measured, not assumed (6.4).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import numpy as np
from rank_bm25 import BM25Okapi

from crashdoc.config import REPO_ROOT
from crashdoc.retrieval.chunking import index_text

Mode = Literal["dense", "bm25", "hybrid"]
RRF_K = 60
DEFAULT_TOP_K = 50  # candidates per retriever before the floor / fusion

_TOKEN = re.compile(r"[a-z0-9_]+")


def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric tokens; an id like `cobblemon_battle_tower` also yields its parts."""
    out: list[str] = []
    for tok in _TOKEN.findall(text.lower()):
        out.append(tok)
        if "_" in tok:
            out.extend(p for p in tok.split("_") if p)
    return out


@dataclass(frozen=True)
class Hit:
    chunk_id: str
    doc_id: str
    cos: float  # dense cosine to the query (computed for every candidate)
    score: float  # the ranking score: RRF (hybrid), cosine (dense) or BM25 (bm25)
    in_dense: bool
    in_bm25: bool


@dataclass
class SearchResult:
    hits: list[Hit]  # ranked best first, after the floor
    abstained: bool  # a floor was set and nothing survived
    dropped_bm25_only: list[Hit] = field(default_factory=list)  # BM25-only candidates the floor removed


@dataclass
class DocHit:
    doc_id: str
    best_chunk_id: str
    score: float
    cos: float


class Index:
    def __init__(self, chunks: list[dict], embeddings: np.ndarray):
        if len(chunks) != len(embeddings):
            raise ValueError("chunks and embeddings are out of step: rebuild the index")
        self.chunks = chunks
        self.emb = embeddings.astype(np.float32, copy=False)
        self.bm25 = BM25Okapi([tokenize(index_text(c)) for c in chunks])

    @classmethod
    def load(cls, processed_dir: Path = REPO_ROOT / "data" / "processed") -> Index:
        lines = (processed_dir / "chunks.jsonl").read_text(encoding="utf-8").splitlines()
        return cls([json.loads(line) for line in lines], np.load(processed_dir / "embeddings.npy"))

    # ------------------------------------------------------------------ rankers

    def _dense_scores(self, query_vec: np.ndarray) -> np.ndarray:
        q = np.asarray(query_vec, dtype=np.float32)
        return self.emb @ (q / (np.linalg.norm(q) or 1.0))  # corpus vectors are L2-normalised

    def _bm25_scores(self, query_text: str) -> np.ndarray:
        tokens = list(dict.fromkeys(tokenize(query_text)))  # a repeated query term must not count twice
        return self.bm25.get_scores(tokens) if tokens else np.zeros(len(self.chunks))

    @staticmethod
    def _top(scores: np.ndarray, k: int) -> list[int]:
        return [int(i) for i in np.argsort(-scores, kind="stable")[:k]]

    # ------------------------------------------------------------------ search

    def search(
        self,
        mode: Mode,
        *,
        query_text: str = "",
        query_vec: np.ndarray | None = None,
        k: int = DEFAULT_TOP_K,
        min_score: float | None = None,
    ) -> SearchResult:
        if mode in ("dense", "hybrid") and query_vec is None:
            raise ValueError(f"{mode} search needs a query vector")
        if min_score is not None and query_vec is None:
            raise ValueError("a cosine floor needs a query vector")
        cos = self._dense_scores(query_vec) if query_vec is not None else None
        dense_top = self._top(cos, k) if mode in ("dense", "hybrid") else []
        bm25_scores = self._bm25_scores(query_text) if mode in ("bm25", "hybrid") else None
        bm25_top: list[int] = []
        if bm25_scores is not None:  # a BM25 score of 0 means no query term matched: not a candidate
            bm25_top = [i for i in self._top(bm25_scores, k) if bm25_scores[i] > 0]

        candidates = list(dict.fromkeys(dense_top + bm25_top))
        survivors = [i for i in candidates if min_score is None or cos[i] >= min_score]
        keep = set(survivors)
        dense_set, bm25_set = set(dense_top), set(bm25_top)

        def hit(i: int, score: float) -> Hit:
            c = self.chunks[i]
            cosine = float(cos[i]) if cos is not None else 0.0
            return Hit(c["chunk_id"], c["doc_id"], cosine, float(score), i in dense_set, i in bm25_set)

        dropped_bm25_only: list[Hit] = []
        if bm25_scores is not None:
            dropped_bm25_only = [
                hit(i, bm25_scores[i]) for i in candidates if i not in keep and i in bm25_set and i not in dense_set
            ]
        if not survivors:
            return SearchResult([], abstained=min_score is not None, dropped_bm25_only=dropped_bm25_only)

        if mode == "dense":
            hits = [hit(i, cos[i]) for i in dense_top if i in keep]
        elif mode == "bm25":
            hits = [hit(i, bm25_scores[i]) for i in bm25_top if i in keep]
        else:  # hybrid: RRF over the survivors' two rankings
            rrf: dict[int, float] = {}
            for ranking in ([i for i in dense_top if i in keep], [i for i in bm25_top if i in keep]):
                for rank, i in enumerate(ranking, start=1):
                    rrf[i] = rrf.get(i, 0.0) + 1.0 / (RRF_K + rank)
            ordered = sorted(rrf.items(), key=lambda kv: (-kv[1], -float(cos[kv[0]])))
            hits = [hit(i, s) for i, s in ordered]
        return SearchResult(hits, abstained=False, dropped_bm25_only=dropped_bm25_only)


def top_docs(hits: list[Hit], n: int) -> list[DocHit]:
    """Collapse ranked chunks to ranked documents (best chunk per doc_id), keeping the first n."""
    seen: dict[str, DocHit] = {}
    for h in hits:
        if h.doc_id not in seen:
            seen[h.doc_id] = DocHit(h.doc_id, h.chunk_id, h.score, h.cos)
            if len(seen) == n:
                break
    return list(seen.values())
