"""Token estimates for the LLM input budget.

Gemma's tokenizer isn't available locally, so we count with tiktoken cl100k and scale by
GEMMA_UNDERCOUNT_FACTOR: the probe measured cl100k undercounting Gemma by ~21%.
"""

from __future__ import annotations

import math
from functools import lru_cache

import tiktoken

from crashdoc.config import GEMMA_UNDERCOUNT_FACTOR, LOG_TOKEN_BUDGET, use_os_trust_store


@lru_cache(maxsize=1)
def _cl100k() -> tiktoken.Encoding:
    use_os_trust_store()  # first use downloads the encoding file over HTTPS
    return tiktoken.get_encoding("cl100k_base")


def estimate_llm_tokens(text: str) -> int:
    """Conservative Gemma token count: cl100k tokens x 1.25, rounded up."""
    return math.ceil(len(_cl100k().encode(text, disallowed_special=())) * GEMMA_UNDERCOUNT_FACTOR)


def fits_log_budget(text: str, budget: int = LOG_TOKEN_BUDGET) -> bool:
    """True if this log text may be sent to the LLM as-is."""
    return estimate_llm_tokens(text) <= budget
