"""Static version-compatibility rules for the `check_compat` agent tool (PLAN 6.6).

Data sources (fetched 2026-10-28, both in the corpus):
- NeoForge numbering: NeoForge docs "Versioning", https://docs.neoforged.net/docs/1.21.1/gettingstarted/versioning/
  "The major version is Minecraft's minor version, the minor version is Minecraft's patch version, and the
  patch version is the 'actual' NeoForge version." So NeoForge 21.1.224 -> Minecraft 1.21.1.
- Required Java: NeoForge User Guide, https://docs.neoforged.net/user/docs/
  Table "Minecraft 1.20.2-1.20.4 -> Java 17; 1.20.5-latest -> Java 21".
  "latest" means as of the fetch date; versions released after it are reported as unknown, not guessed.

Our pack (All the Mons - ATMons): NeoForge 21.1.224 -> Minecraft 1.21.1 -> Java 21.
Only MC <-> Java and MC <-> NeoForge are checked here; mod-level compatibility is left to retrieval.
"""

from __future__ import annotations

import re

# (lowest MC version, highest MC version, required Java major), inclusive, from the User Guide table.
JAVA_BY_MC: list[tuple[tuple[int, ...], tuple[int, ...], int]] = [
    ((1, 20, 2), (1, 20, 4), 17),
    ((1, 20, 5), (1, 21, 1), 21),  # "1.20.5-latest"; capped at the newest version this project verified
]


def parse_mc(version: str | None) -> tuple[int, ...] | None:
    """'1.21.1' -> (1, 21, 1); '1.21' -> (1, 21, 0). Anything else (snapshots, junk) -> None."""
    m = re.fullmatch(r"\s*1\.(\d+)(?:\.(\d+))?\s*", version or "")
    return (1, int(m.group(1)), int(m.group(2) or 0)) if m else None


def mc_for_neoforge(neoforge_version: str | None) -> str | None:
    """NeoForge 'A.B.n[-beta]' -> Minecraft '1.A.B' ('1.A' when B is 0). None if it doesn't look like NeoForge.

    Only majors 20 and 21 (Minecraft 1.20.x / 1.21.x) are accepted, so an old Forge version such as
    47.1.3 is not misread as "Minecraft 1.47.1".
    """
    m = re.fullmatch(r"\s*(2[01])\.(\d+)\.\d+(?:[-+.].*)?\s*", neoforge_version or "")
    if not m:
        return None
    major, minor = int(m.group(1)), int(m.group(2))
    return f"1.{major}" if minor == 0 else f"1.{major}.{minor}"


def java_major(java_version: str | None) -> int | None:
    """'21.0.4' -> 21, '17' -> 17, '1.8.0_311' -> 8 (old scheme)."""
    m = re.match(r"\s*(\d+)(?:\.(\d+))?", java_version or "")
    if not m:
        return None
    first = int(m.group(1))
    return int(m.group(2) or 0) if first == 1 else first


def required_java(mc_version: str | None) -> int | None:
    """Required Java major for a Minecraft version, or None if outside the table."""
    mc = parse_mc(mc_version)
    if mc is None:
        return None
    return next((java for low, high, java in JAVA_BY_MC if low <= mc <= high), None)


def check_compat(
    mc_version: str | None, java_version: str | None = None, loader_version: str | None = None
) -> dict[str, dict[str, object]]:
    """Check MC <-> Java and MC <-> NeoForge. Any null or unrecognised input is reported "unknown", never guessed."""
    return {"java": _check_java(mc_version, java_version), "loader": _check_loader(mc_version, loader_version)}


def _check_java(mc_version: str | None, java_version: str | None) -> dict[str, object]:
    need, have = required_java(mc_version), java_major(java_version)
    if need is None or have is None:
        return {"status": "unknown", "required_java": need, "java": have}
    if have < need:
        status = "too_old"
    elif have > need:
        status = "newer_than_required"  # usually runs, but not what the docs list
    else:
        status = "ok"
    return {"status": status, "required_java": need, "java": have}


def _check_loader(mc_version: str | None, loader_version: str | None) -> dict[str, object]:
    implied, mc = mc_for_neoforge(loader_version), parse_mc(mc_version)
    if implied is None or mc is None:
        return {"status": "unknown", "loader_is_for_mc": implied, "mc": mc_version}
    status = "ok" if parse_mc(implied) == mc else "mismatch"
    return {"status": status, "loader_is_for_mc": implied, "mc": mc_version}
