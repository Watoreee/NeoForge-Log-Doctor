"""Scenario-level paired bootstrap (PLAN 7.3): resample scenario groups, not logs, because the logs of one
scenario are not independent. Fixed seed, 1,000 resamples."""

from __future__ import annotations

import random
from collections import defaultdict


def paired_bootstrap(
    scenario_of: dict[str, str], before: dict[str, float], after: dict[str, float], n: int = 1000, seed: int = 0
) -> dict:
    """95% interval of mean(after) - mean(before) over logs, resampling scenario_id groups with replacement."""
    groups: dict[str, list[str]] = defaultdict(list)
    for log_id, sid in scenario_of.items():
        groups[sid].append(log_id)
    sids = sorted(groups)
    rng = random.Random(seed)
    deltas = []
    for _ in range(n):
        logs = [log for sid in (rng.choice(sids) for _ in sids) for log in groups[sid]]
        deltas.append(sum(after[x] - before[x] for x in logs) / len(logs))
    deltas.sort()
    observed = sum(after[x] - before[x] for x in scenario_of) / len(scenario_of)
    lo, hi = deltas[int(0.025 * n)], deltas[int(0.975 * n) - 1]
    return {
        "delta": round(observed, 4),
        "ci95": [round(lo, 4), round(hi, 4)],
        "includes_zero": lo <= 0 <= hi,
        "n_logs": len(scenario_of),
        "n_scenarios": len(sids),
        "resamples": n,
        "seed": seed,
    }
