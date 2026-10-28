"""scripts/collect_run.py: label validation, numbering, the time window, safety. Temp folders only."""

from __future__ import annotations

import importlib.util
import os
import sys

import pytest

from crashdoc.config import REPO_ROOT
from crashdoc.schemas import Category

_spec = importlib.util.spec_from_file_location("collect_run", REPO_ROOT / "scripts" / "collect_run.py")
collect_run = importlib.util.module_from_spec(_spec)
sys.modules["collect_run"] = collect_run  # dataclasses look the module up
_spec.loader.exec_module(collect_run)

NOW = 1_800_000_000.0  # fixed clock, so file ages are exact


@pytest.fixture
def setup(tmp_path, monkeypatch):
    """A fake instance with a fresh latest.log, an empty raw folder, and no .env lookup."""
    instance, raw = tmp_path / "instance", tmp_path / "raw"
    (instance / "logs").mkdir(parents=True)
    (instance / "crash-reports").mkdir()
    raw.mkdir()
    write(instance / "logs" / "latest.log", age_min=1)
    monkeypatch.setenv("CRASHDOC_INSTANCE", str(instance))
    monkeypatch.setenv("CRASHDOC_RAW_DIR", str(raw))
    monkeypatch.setattr(collect_run, "DOTENV_PATH", tmp_path / "no.env")
    return instance, raw


def write(path, age_min: float, text: str = "synthetic\n"):
    path.write_text(text, encoding="utf-8")
    ts = NOW - age_min * 60
    os.utime(path, (ts, ts))


def run(*argv):
    return collect_run.main(list(argv), now=NOW)


ARGS = ("--category", "missing_dependency", "--culprit", "jei", "--also", "", "--broke", "removed jei")


# ---------------------------------------------------------------- validation


def test_categories_are_read_from_schemas():
    assert collect_run.load_categories() == [c.value for c in Category]


def test_unknown_category_is_rejected(setup):
    with pytest.raises(SystemExit, match="unknown category"):
        run("--category", "crashy", "--culprit", "jei", "--also", "", "--broke", "x")


@pytest.mark.parametrize("bad", ["JEI", "just enough items", "jei!", ""])
def test_invalid_mod_ids_are_rejected(bad):
    with pytest.raises(ValueError):
        collect_run.validate_mod_id(bad)


def test_culprit_is_always_added_to_acceptable():
    assert collect_run.acceptable_culprits("jei", "") == ["jei"]
    assert collect_run.acceptable_culprits("jei", "emi, jei,rei") == ["jei", "emi", "rei"]


def test_culprit_none_means_null_and_empty_acceptable(setup):
    _, raw = setup
    assert run("--category", "out_of_memory", "--culprit", "none", "--also", "", "--broke", "Xmx 512M") == 0
    notes = (raw / "r01_out-of-memory_none" / "notes.txt").read_text(encoding="utf-8")
    assert "culprit_mod_id: null\n" in notes and "acceptable_culprits: \n" in notes


def test_missing_arguments_are_prompted_for(setup, monkeypatch):
    _, raw = setup
    answers = iter(["not_a_category", "version_mismatch", "Create", "create", "flywheel", "downgraded create"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))
    assert run() == 0
    notes = (raw / "r01_version-mismatch_create" / "notes.txt").read_text(encoding="utf-8")
    assert "acceptable_culprits: create, flywheel" in notes and "what_i_broke: downgraded create" in notes


# ---------------------------------------------------------------- numbering and folders


def test_runs_are_numbered_in_order_and_named(setup):
    _, raw = setup
    run(*ARGS)
    run("--category", "duplicate_mod", "--culprit", "create_addition", "--also", "", "--broke", "two jars")
    assert sorted(p.name for p in raw.iterdir() if p.is_dir()) == [
        "r01_missing-dependency_jei",
        "r02_duplicate-mod_create-addition",
    ]


def test_numbering_never_reuses_an_existing_number(setup):
    _, raw = setup
    (raw / "r01_other_none").mkdir()
    (raw / "r03_other_none").mkdir()  # r02 was deleted by hand
    (raw / "notes-folder").mkdir()  # not a run folder
    run(*ARGS)
    assert (raw / "r04_missing-dependency_jei").is_dir()


def test_existing_run_folder_is_never_overwritten(setup, monkeypatch):
    _, raw = setup
    monkeypatch.setattr(collect_run, "next_run_number", lambda _raw: 1)
    run(*ARGS)
    with pytest.raises(FileExistsError):
        run(*ARGS)


# ---------------------------------------------------------------- safety


def test_refuses_a_raw_folder_inside_the_repo(setup, monkeypatch):
    monkeypatch.setenv("CRASHDOC_RAW_DIR", str(REPO_ROOT / "data"))
    with pytest.raises(SystemExit, match="inside the git repo"):
        run(*ARGS)


def test_refuses_without_the_env_paths(setup, monkeypatch):
    monkeypatch.delenv("CRASHDOC_RAW_DIR")
    with pytest.raises(SystemExit, match="CRASHDOC_RAW_DIR"):
        run(*ARGS)


def test_dry_run_writes_nothing(setup, capsys):
    _, raw = setup
    assert run(*ARGS, "--dry-run") == 0
    assert list(raw.iterdir()) == []
    assert "Would copy 1 file(s)" in capsys.readouterr().out


# ---------------------------------------------------------------- copying and the time window


def test_copies_recent_crash_reports_and_hs_err_only(setup):
    instance, raw = setup
    write(instance / "logs" / "debug.log", age_min=1)
    write(instance / "crash-reports" / "crash-new-client.txt", age_min=5)
    write(instance / "crash-reports" / "crash-old-client.txt", age_min=60)
    write(instance / "hs_err_pid111.log", age_min=2)
    write(instance / "hs_err_pid222.log", age_min=600)
    run(*ARGS)
    run_dir = raw / "r01_missing-dependency_jei"
    copied = sorted(p.name for p in run_dir.iterdir())
    assert copied == ["crash-new-client.txt", "debug.log", "hs_err_pid111.log", "latest.log", "notes.txt"]
    assert (instance / "logs" / "latest.log").exists()  # copied, not moved


def test_since_minutes_widens_the_window(setup):
    instance, raw = setup
    write(instance / "crash-reports" / "crash-old-client.txt", age_min=60)
    run(*ARGS, "--since-minutes", "90")
    assert (raw / "r01_missing-dependency_jei" / "crash-old-client.txt").exists()


def test_stale_latest_log_warns_and_can_continue(setup, capsys):
    instance, raw = setup
    write(instance / "logs" / "latest.log", age_min=120)
    assert run(*ARGS, "--yes") == 0
    assert "WARNING" in capsys.readouterr().out
    assert (raw / "r01_missing-dependency_jei" / "latest.log").exists()


def test_stale_latest_log_stops_when_declined(setup, monkeypatch):
    instance, raw = setup
    write(instance / "logs" / "latest.log", age_min=120)
    monkeypatch.setattr("builtins.input", lambda _prompt: "n")
    assert run(*ARGS) == 1
    assert list(raw.iterdir()) == []


# ---------------------------------------------------------------- notes.txt and runs.txt


def test_notes_and_runs_line_with_pipe_escaping(setup):
    _, raw = setup
    run("--category", "mixin_conflict", "--culprit", "sodium", "--also", "iris", "--broke", "added A | B\nthen ran")
    notes = (raw / "r01_mixin-conflict_sodium" / "notes.txt").read_text(encoding="utf-8")
    assert notes.splitlines() == [
        "what_i_broke: added A | B then ran",
        "culprit_mod_id: sodium",
        "acceptable_culprits: sodium, iris",
        "category: mixin_conflict",
        "files_produced: latest.log",
    ]
    lines = (raw / "runs.txt").read_text(encoding="utf-8").splitlines()
    assert lines[0] == collect_run.RUNS_HEADER
    fields = lines[1].split(" | ")
    assert fields[:6] == ["r01", "mixin_conflict", "sodium", "sodium,iris", "latest.log", "added A / B then ran"]
    assert len(fields) == 7


def test_runs_header_is_written_once(setup):
    _, raw = setup
    run(*ARGS)
    run(*ARGS)
    lines = (raw / "runs.txt").read_text(encoding="utf-8").splitlines()
    assert lines.count(collect_run.RUNS_HEADER) == 1 and len(lines) == 3
