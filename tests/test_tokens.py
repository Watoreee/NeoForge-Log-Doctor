"""Token budget estimate: cl100k x 1.25, rounded up (docs/decisions.md)."""

from __future__ import annotations

import math

from crashdoc.tokens import _cl100k, estimate_llm_tokens, fits_log_budget


def test_estimate_scales_cl100k_by_1_25():
    text = "java.lang.NoClassDefFoundError: mezz/jei/api/IModPlugin " * 10
    raw = len(_cl100k().encode(text))
    assert estimate_llm_tokens(text) == math.ceil(raw * 1.25)


def test_special_token_text_in_a_log_does_not_crash():
    assert estimate_llm_tokens("<|endoftext|>") > 0


def test_budget_check():
    assert fits_log_budget("short log line")
    assert not fits_log_budget("word " * 10_000)
