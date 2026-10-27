"""Load gold labels and check the rules that span several label files (PLAN 6.1).

Layout: data/gold/{dev,test}/<log_id>.json is the label; the redacted log sits next to it as
<log_id>.<ext> (any extension other than .json). Used by scripts/validate_labels.py and, later, run_eval.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from pydantic import ValidationError

from crashdoc.schemas import GoldLabel

SPLITS = ("dev", "test")


@dataclass
class LabelReport:
    """Validation outcome: errors fail the check; warnings are printed but allowed."""

    labels: dict[str, list[GoldLabel]] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_split(split_dir: Path) -> tuple[list[GoldLabel], list[str]]:
    """Parse every label file in one split directory; schema errors are collected, not raised."""
    labels, errors = [], []
    for path in sorted(split_dir.glob("*.json")):
        try:
            label = GoldLabel.model_validate(json.loads(path.read_text(encoding="utf-8")))
        except (ValidationError, json.JSONDecodeError) as e:
            errors.append(f"{path.name}: {e}")
            continue
        if label.log_id != path.stem:
            errors.append(f"{path.name}: log_id {label.log_id!r} must match the file name")
        if not _log_files(split_dir, path.stem):
            errors.append(f"{path.name}: no log file {path.stem}.<ext> next to the label")
        labels.append(label)
    return labels, errors


def _log_files(split_dir: Path, stem: str) -> list[Path]:
    return [p for p in split_dir.glob(f"{stem}.*") if p.suffix != ".json"]


def check_unique_log_ids(labels: dict[str, list[GoldLabel]]) -> list[str]:
    """A log id may appear once across all splits."""
    seen: dict[str, str] = {}
    errors = []
    for split, items in labels.items():
        for label in items:
            if label.log_id in seen:
                errors.append(f"log_id {label.log_id!r} appears in both {seen[label.log_id]} and {split}")
            seen[label.log_id] = split
    return errors


def check_scenario_leakage(labels: dict[str, list[GoldLabel]]) -> list[str]:
    """All logs of one scenario must be on the same side of the split."""
    splits_of: dict[str, set[str]] = defaultdict(set)
    for split, items in labels.items():
        for label in items:
            splits_of[label.scenario_id].add(split)
    return [
        f"scenario {sid!r} crosses the split ({', '.join(sorted(s))})"
        for sid, s in sorted(splits_of.items())
        if len(s) > 1
    ]


def check_scenario_consistency(labels: dict[str, list[GoldLabel]]) -> list[str]:
    """Relevance is judged per scenario, so its logs must share relevant_doc_ids and support_search."""
    by_scenario: dict[str, list[GoldLabel]] = defaultdict(list)
    for items in labels.values():
        for label in items:
            by_scenario[label.scenario_id].append(label)
    errors = []
    for sid, group in sorted(by_scenario.items()):
        variants = {
            (None if g.relevant_doc_ids is None else tuple(sorted(g.relevant_doc_ids)), g.support_search) for g in group
        }
        if len(variants) > 1:
            ids = ", ".join(g.log_id for g in group)
            errors.append(f"scenario {sid!r}: relevant_doc_ids / support_search differ between logs ({ids})")
    return errors


def check_relevance_judged(labels: dict[str, list[GoldLabel]]) -> list[str]:
    """Logs whose relevance hasn't been judged yet (an error only once annotation must be complete)."""
    return [
        f"{split}/{label.log_id}: relevant_doc_ids not judged yet (null)"
        for split, items in labels.items()
        for label in items
        if not label.relevance_judged
    ]


def check_doc_ids_known(labels: dict[str, list[GoldLabel]], known_doc_ids: set[str]) -> list[str]:
    """Every relevant doc id must exist in the corpus manifest."""
    return [
        f"{split}/{label.log_id}: unknown doc_id {doc_id!r}"
        for split, items in labels.items()
        for label in items
        for doc_id in label.relevant_doc_ids or []
        if doc_id not in known_doc_ids
    ]


def check_category_stratification(labels: dict[str, list[GoldLabel]]) -> list[str]:
    """Every category with >=2 scenario groups should appear in both dev and test."""
    groups: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for split, items in labels.items():
        for label in items:
            groups[label.category.value][split].add(label.scenario_id)
    warnings = []
    for category, per_split in sorted(groups.items()):
        n_groups = sum(len(s) for s in per_split.values())
        missing = [s for s in SPLITS if not per_split.get(s)]
        if n_groups >= 2 and missing:
            warnings.append(f"category {category!r} has {n_groups} scenario groups but none in {', '.join(missing)}")
    return warnings


def load_manifest_doc_ids(manifest_path: Path) -> set[str] | None:
    """Doc ids from data/processed/manifest.json, or None if the corpus isn't built yet."""
    if not manifest_path.exists():
        return None
    rows = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {row["doc_id"] for row in rows}


def validate_gold(gold_dir: Path, manifest_path: Path | None = None, require_relevance: bool = False) -> LabelReport:
    """Run every label check. `require_relevance` turns unjudged relevance into errors (Day 5 gate)."""
    report = LabelReport()
    for split in SPLITS:
        split_dir = gold_dir / split
        items, errors = load_split(split_dir) if split_dir.exists() else ([], [])
        report.labels[split] = items
        report.errors += [f"{split}/{e}" for e in errors]

    report.errors += check_unique_log_ids(report.labels)
    report.errors += check_scenario_leakage(report.labels)
    report.errors += check_scenario_consistency(report.labels)
    unjudged = check_relevance_judged(report.labels)
    (report.errors if require_relevance else report.warnings).extend(unjudged)
    report.warnings += check_category_stratification(report.labels)

    known = load_manifest_doc_ids(manifest_path) if manifest_path else None
    if known is not None:
        report.errors += check_doc_ids_known(report.labels, known)
    return report


def describe_split(items: list[GoldLabel]) -> str:
    """The "N logs from M scenarios" line every results table needs (PLAN 7.1)."""
    return f"{len(items)} logs from {len({i.scenario_id for i in items})} scenarios"
