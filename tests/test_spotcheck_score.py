"""scripts/score_spotcheck.py: a ticked 'disagree' box must not also count as 'agree'."""

from __future__ import annotations

from scripts.score_spotcheck import parse


def entry(n: int, mark: str, box: str) -> str:
    return (
        f"\n### {n}. sheet 01 (`r02`) `doc{n}`\n\n- URL: https://example.org/{n}\n"
        f"- **Sheet's current mark: {mark}**\n\nYour call:  {box}\n"
    )


def test_agree_disagree_unanswered_and_invalid_are_told_apart(tmp_path):
    p = tmp_path / "s.md"
    p.write_text(
        "# head\n"
        + entry(1, "TICKED (relevant)", "agree [x]   disagree [ ]")
        + entry(2, "TICKED (relevant)", "agree [ ]   disagree [x]")
        + entry(3, "UNTICKED (not relevant)", "agree [ ]   disagree [ ]")
        + entry(4, "UNTICKED (not relevant)", "agree [X]   disagree [x]"),
        encoding="utf-8",
    )
    got = [(i["mark"], i["status"]) for i in parse(p)]
    assert got == [("ticked", "agree"), ("ticked", "disagree"), ("unticked", "unanswered"), ("unticked", "invalid")]
