import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "export_groundedness_sheet", Path(__file__).resolve().parents[1] / "scripts" / "export_groundedness_sheet.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

SHEET = """# Groundedness sheet

---

## a  (predicted culprit)

**Citations:**

- **d1**

**Grounded?**  [x]

---

## b  (x)

**Citations:** none, so there is no source to support this explanation.

**Grounded?**  not scored (no citation)

---

## c  (x)

- **d2**

**Grounded?**  [ ]
"""


def test_denominator_is_cited_logs_only_and_coverage_is_separate(tmp_path):
    p = tmp_path / "s.md"
    p.write_text(SHEET, encoding="utf-8")
    r = mod.score(p)
    assert r["logs"] == 3 and r["citation_coverage"] == "2/3"
    assert r["grounded"] == "1/2" and r["boxes_still_open"] == 1


def test_a_tick_on_a_log_without_a_citation_is_ignored(tmp_path):
    p = tmp_path / "s.md"
    p.write_text(SHEET.replace("not scored (no citation)", "[x]"), encoding="utf-8")
    assert mod.score(p)["grounded"] == "1/2"


def test_a_judged_no_is_not_an_open_box(tmp_path):
    p = tmp_path / "s.md"
    p.write_text(SHEET.replace("**Grounded?**  [ ]\n", "**Grounded?**  [ ]\n\nJudgment (Claude): no. reason\n"), encoding="utf-8")
    r = mod.score(p)
    assert r["grounded"] == "1/2" and r["boxes_still_open"] == 0
