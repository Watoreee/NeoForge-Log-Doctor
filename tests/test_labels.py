"""Gold-label schema rules and the cross-file checks in labels.py (PLAN 6.1, section 8)."""

from __future__ import annotations

import json

import pytest
from pydantic import ValidationError

from crashdoc.labels import validate_gold
from crashdoc.schemas import GoldLabel


def _label(**overrides) -> dict:
    base = {
        "log_id": "log01",
        "scenario_id": "s1",
        "source_file_type": "latest_log",
        "culprit_mod_id": "jei",
        "acceptable_culprits": ["jei"],
        "category": "missing_dependency",
    }
    return {**base, **overrides}


# ---------------------------------------------------------------- per-label schema rules


def test_valid_label_parses():
    assert GoldLabel.model_validate(_label()).relevance_judged is False


def test_acceptable_culprits_must_include_culprit():
    with pytest.raises(ValidationError, match="must include culprit_mod_id"):
        GoldLabel.model_validate(_label(acceptable_culprits=["create"]))


def test_null_culprit_needs_empty_acceptable_list():
    GoldLabel.model_validate(_label(culprit_mod_id=None, acceptable_culprits=[], category="out_of_memory"))
    with pytest.raises(ValidationError, match="must be \\[\\]"):
        GoldLabel.model_validate(_label(culprit_mod_id=None, acceptable_culprits=["jei"]))


def test_empty_relevant_docs_require_support_search():
    with pytest.raises(ValidationError, match="support_search must be"):
        GoldLabel.model_validate(_label(relevant_doc_ids=[]))
    GoldLabel.model_validate(_label(relevant_doc_ids=[], support_search="none_found"))


def test_non_empty_relevant_docs_forbid_support_search():
    with pytest.raises(ValidationError, match="must be null"):
        GoldLabel.model_validate(_label(relevant_doc_ids=["doc1"], support_search="uncertain"))
    GoldLabel.model_validate(_label(relevant_doc_ids=["doc1"]))


def test_support_search_without_judged_relevance_is_rejected():
    with pytest.raises(ValidationError, match="has not been judged"):
        GoldLabel.model_validate(_label(support_search="none_found"))


def test_unknown_fields_and_categories_are_rejected():
    with pytest.raises(ValidationError):
        GoldLabel.model_validate(_label(extra_field=1))
    with pytest.raises(ValidationError):
        GoldLabel.model_validate(_label(category="not_a_category"))


# ---------------------------------------------------------------- cross-file checks


def _write(gold, split, log_text="[12:00:00] [main/ERROR]: boom", **overrides):
    data = _label(**overrides)
    d = gold / split
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{data['log_id']}.json").write_text(json.dumps(data), encoding="utf-8")
    if log_text is not None:
        (d / f"{data['log_id']}.log").write_text(log_text, encoding="utf-8")


def test_clean_gold_set_passes(tmp_path):
    _write(tmp_path, "dev", log_id="a", scenario_id="s1")
    _write(tmp_path, "test", log_id="b", scenario_id="s2")
    report = validate_gold(tmp_path)
    assert report.ok, report.errors


def test_empty_gold_dir_is_ok(tmp_path):
    assert validate_gold(tmp_path).ok


def test_scenario_crossing_the_split_is_an_error(tmp_path):
    _write(tmp_path, "dev", log_id="a", scenario_id="s1")
    _write(tmp_path, "test", log_id="b", scenario_id="s1")
    assert any("crosses the split" in e for e in validate_gold(tmp_path).errors)


def test_scenario_logs_must_share_relevance_labels(tmp_path):
    _write(tmp_path, "test", log_id="a", scenario_id="s1", relevant_doc_ids=["d1"])
    _write(tmp_path, "test", log_id="b", scenario_id="s1", relevant_doc_ids=["d2"])
    assert any("differ between logs" in e for e in validate_gold(tmp_path).errors)


def test_same_relevance_in_any_order_is_consistent(tmp_path):
    _write(tmp_path, "test", log_id="a", scenario_id="s1", relevant_doc_ids=["d1", "d2"])
    _write(tmp_path, "test", log_id="b", scenario_id="s1", relevant_doc_ids=["d2", "d1"])
    assert validate_gold(tmp_path).ok


def test_unjudged_relevance_is_warning_then_error_when_required(tmp_path):
    _write(tmp_path, "test", log_id="a")
    assert validate_gold(tmp_path).ok
    assert validate_gold(tmp_path).warnings
    assert not validate_gold(tmp_path, require_relevance=True).ok


def test_label_needs_matching_log_file_and_name(tmp_path):
    _write(tmp_path, "dev", log_id="a", log_text=None)
    assert any("no log file" in e for e in validate_gold(tmp_path).errors)
    d = tmp_path / "dev"
    (d / "wrong.json").write_text(json.dumps(_label(log_id="other")), encoding="utf-8")
    (d / "wrong.txt").write_text("x", encoding="utf-8")
    assert any("must match the file name" in e for e in validate_gold(tmp_path).errors)


def test_schema_errors_are_reported_not_raised(tmp_path):
    _write(tmp_path, "dev", log_id="a", acceptable_culprits=[])
    report = validate_gold(tmp_path)
    assert not report.ok and "a.json" in report.errors[0]


def test_duplicate_log_id_across_splits(tmp_path):
    _write(tmp_path, "dev", log_id="a", scenario_id="s1")
    _write(tmp_path, "test", log_id="a", scenario_id="s2")
    assert any("appears in both" in e for e in validate_gold(tmp_path).errors)


def test_relevant_doc_ids_must_exist_in_manifest(tmp_path):
    _write(tmp_path, "test", log_id="a", relevant_doc_ids=["known", "ghost"])
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([{"doc_id": "known"}]), encoding="utf-8")
    errors = validate_gold(tmp_path, manifest).errors
    assert errors == ["test/a: unknown doc_id 'ghost'"]


def test_category_missing_from_a_split_is_warned(tmp_path):
    _write(tmp_path, "test", log_id="a", scenario_id="s1")
    _write(tmp_path, "test", log_id="b", scenario_id="s2")
    assert any("none in dev" in w for w in validate_gold(tmp_path).warnings)
