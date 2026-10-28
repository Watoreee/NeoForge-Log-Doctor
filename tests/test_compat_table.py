"""compat_table: NeoForge numbering rule, Java table, unknowns stay unknown."""

from __future__ import annotations

import pytest

from crashdoc.agent.compat_table import check_compat, java_major, mc_for_neoforge, required_java


def test_pack_row_neoforge_21_1_is_mc_1_21_1_on_java_21():
    result = check_compat("1.21.1", "21.0.4", "21.1.224")
    assert result == {
        "java": {"status": "ok", "required_java": 21, "java": 21},
        "loader": {"status": "ok", "loader_is_for_mc": "1.21.1", "mc": "1.21.1"},
    }


@pytest.mark.parametrize(
    ("neoforge", "mc"),
    [("21.1.224", "1.21.1"), ("20.2.59", "1.20.2"), ("21.0.167", "1.21"), ("20.4.80-beta", "1.20.4"), ("47.1.3", None)],
)
def test_mc_for_neoforge(neoforge, mc):
    assert mc_for_neoforge(neoforge) == mc


def test_loader_mismatch():
    assert check_compat("1.21.1", loader_version="20.4.80")["loader"]["status"] == "mismatch"


def test_java_too_old_and_newer():
    assert check_compat("1.21.1", "17.0.8")["java"]["status"] == "too_old"
    assert check_compat("1.21.1", "22")["java"]["status"] == "newer_than_required"
    assert check_compat("1.20.4", "17")["java"]["status"] == "ok"


def test_null_and_unknown_inputs_are_reported_unknown():
    result = check_compat(None, None, None)
    assert result["java"]["status"] == "unknown" and result["loader"]["status"] == "unknown"
    assert required_java("1.19.2") is None  # outside the table: not guessed
    assert required_java("24w14a") is None


def test_java_major_parsing():
    assert (java_major("21.0.4"), java_major("1.8.0_311"), java_major("17"), java_major("")) == (21, 8, 17, None)
