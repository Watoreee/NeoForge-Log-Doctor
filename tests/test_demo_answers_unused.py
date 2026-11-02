"""data/demo/answers.json is for the live defence only; evaluation code must never read it (decisions.md)."""

from crashdoc.config import REPO_ROOT


def test_no_code_reads_demo_answers():
    offenders = [
        str(p.relative_to(REPO_ROOT))
        for folder in ("src", "scripts")
        for p in (REPO_ROOT / folder).rglob("*.py")
        if "answers.json" in p.read_text(encoding="utf-8", errors="replace")
    ]
    assert not offenders, f"must not reference demo answers: {offenders}"


def test_demo_answers_file_has_no_personal_identifiers():
    text = (REPO_ROOT / "data" / "demo" / "answers.json").read_text(encoding="utf-8").lower()
    for needle in ("users\\", "/home/", "uuid", "token", "@"):
        assert needle not in text, needle
