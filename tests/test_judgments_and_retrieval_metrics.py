"""apply_judgments parsing, recall@k / MRR, scenario bootstrap, and the committed sheets <-> labels agreement."""

import importlib.util
import json
import sys

import pytest

from crashdoc.config import REPO_ROOT
from eval.bootstrap import paired_bootstrap
from eval.metrics import recall_at_k, reciprocal_rank

_spec = importlib.util.spec_from_file_location("apply_judgments", REPO_ROOT / "scripts" / "apply_judgments.py")
aj = importlib.util.module_from_spec(_spec)
sys.modules["apply_judgments"] = aj
_spec.loader.exec_module(aj)

SHEET = """# Judging sheet 01: `r99_missing_dependency_x` (dev)

- **Category:** `missing_dependency`

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  {support}

---

- [x] **gh-issue:a/b#1** (github_issue, 2/6 conditions)
  - title
- [ ] **gh-issue:a/b#2** (github_issue, 1/6 conditions)
- [X] **neoforge-docs:docs/x** (neoforge_docs, 1/6 conditions)

## Added by hand

{hand}
"""


def sheet(tmp_path, support="", hand="(none)"):
    p = tmp_path / "01_dev_r99.md"
    p.write_text(SHEET.format(support=support, hand=hand), encoding="utf-8")
    return aj.parse_sheet(p)


def test_checked_boxes_become_relevant_ids_and_unchecked_do_not(tmp_path):
    j = sheet(tmp_path)
    assert j.scenario_id == "r99_missing_dependency_x"
    assert j.relevant == ["gh-issue:a/b#1", "neoforge-docs:docs/x"] and j.support is None


def test_added_by_hand_documents_count(tmp_path):
    j = sheet(tmp_path, hand="- gh-issue:c/d#9 (found by grep)")
    assert j.relevant[-1] == "gh-issue:c/d#9" and j.by_hand == ["gh-issue:c/d#9"]


def test_unfilled_template_line_is_not_a_support_value(tmp_path):
    p = tmp_path / "01_x.md"
    p.write_text(
        "# Judging sheet 01: `s` (dev)\n**Support search:** `none_found` / `uncertain` / (leave blank)  ->  \n",
        encoding="utf-8",
    )
    assert aj.parse_sheet(p).support is None


def test_support_value_is_read_and_inconsistent_sheets_are_flagged(tmp_path):
    p = tmp_path / "01_x.md"
    p.write_text(
        "# Judging sheet 01: `s` (dev)\n**Support search:** `a` ->  none_found\n- [ ] **gh-issue:a/b#2** (x)\n",
        encoding="utf-8",
    )
    j = aj.parse_sheet(p)
    assert j.support == "none_found"
    aj.check(j, known={"gh-issue:a/b#2"})
    assert not j.problems
    both = sheet(tmp_path, support="none_found")
    aj.check(both, known={"gh-issue:a/b#1", "neoforge-docs:docs/x"})
    assert any("AND support_search" in p for p in both.problems)
    unjudged = aj.parse_sheet(p)
    unjudged.support = None
    aj.check(unjudged, known=set())
    assert any("unjudged" in p for p in unjudged.problems)
    unknown = sheet(tmp_path)
    aj.check(unknown, known=set())
    assert any("unknown doc ids" in p for p in unknown.problems)


def test_recall_and_mrr():
    ranked = ["d1", "d2", "d3", "d4", "d5", "d6"]
    assert recall_at_k(ranked, ["d2", "d6"], 5) == 0.5
    assert recall_at_k(ranked, ["d9"], 5) == 0.0
    assert reciprocal_rank(ranked, ["d3", "d6"]) == pytest.approx(1 / 3)
    assert reciprocal_rank(ranked, ["zzz"]) == 0.0


def test_bootstrap_resamples_scenarios_deterministically():
    scen = {"a1": "A", "a2": "A", "b1": "B", "c1": "C"}
    before = dict.fromkeys(scen, 0.0)
    after = dict.fromkeys(scen, 1.0)
    r1 = paired_bootstrap(scen, before, after)
    assert r1 == paired_bootstrap(scen, before, after)  # fixed seed
    assert r1["delta"] == 1.0 and r1["ci95"] == [1.0, 1.0] and not r1["includes_zero"] and r1["n_scenarios"] == 3
    mixed = paired_bootstrap({"a": "A", "b": "B"}, {"a": 0, "b": 1}, {"a": 1, "b": 0})
    assert mixed["includes_zero"]


def test_committed_sheets_agree_with_committed_labels():
    """Every label's relevant_doc_ids / support_search equals what its sheet says (sheets are the source of truth)."""
    sheets = {}
    for p in sorted((REPO_ROOT / "data" / "pool").glob("[0-9][0-9]_*.md")):
        j = aj.parse_sheet(p)
        sheets[j.scenario_id] = j
    for split in ("dev", "test"):
        for lab in (REPO_ROOT / "data" / "gold" / split).glob("*.json"):
            d = json.loads(lab.read_text(encoding="utf-8"))
            j = sheets[d["scenario_id"]]
            assert sorted(d["relevant_doc_ids"]) == sorted(j.relevant), lab.stem
            assert d["support_search"] == (None if j.relevant else j.support), lab.stem
