"""Format detection and parsing (PLAN 6.1/6.2), on synthetic text and on the real gold logs."""

import time

import pytest

from crashdoc.config import REPO_ROOT
from crashdoc.preprocess import detect_format, parse_log

GOLD = REPO_ROOT / "data" / "gold"


def gold(name: str) -> str:
    path = next(p for p in GOLD.rglob(f"{name}.*") if p.suffix != ".json")
    return path.read_text(encoding="utf-8")


# --- detection -----------------------------------------------------------------------------------


def test_detects_crash_report_latest_log_and_debug_log():
    assert detect_format("---- Minecraft Crash Report ----\n// oops\n") == "crash_report"
    log = "[17:37:04] [main/INFO]: a\n[17:37:05] [main/WARN]: b\n[17:37:06] [main/INFO]: c\n"
    assert detect_format(log) == "latest_log"
    assert detect_format(log + "[17:37:07] [main/DEBUG]: d\n") == "debug_log"
    dated = "".join(f"[28Oct2026 17:37:0{i}.123] [Render thread/INFO] [net.x.Y/]: msg\n" for i in range(4))
    assert detect_format(dated) == "latest_log"


def test_unknown_text_with_log_markers_is_generic_and_flagged_and_plain_text_is_rejected():
    facts = parse_log("something broke\njava.lang.IllegalStateException: boom\n\tat a.b.C.d(C.java:1)\n")
    assert facts.format == "generic" and facts.flagged_generic
    assert facts.exceptions[0].type == "java.lang.IllegalStateException"
    assert parse_log("hello there, what a lovely day").format == "rejected"
    assert parse_log("").format == "rejected"


def test_hs_err_is_recognised_but_unsupported_so_it_goes_generic():
    assert detect_format("# A fatal error has been detected by the Java Runtime Environment:\n#\n") == "generic"


# --- synthetic content ---------------------------------------------------------------------------

CRASH = "\n".join(
    [
        "---- Minecraft Crash Report ----",
        "// Why did you do that?",
        "",
        "Time: 2026-11-02 10:00:00",
        "Description: Exception in server tick loop",
        "",
        'java.lang.NullPointerException: Cannot invoke "x" because "y" is null',
        "\tat a.b.C.d(C.java:1)",
        "Caused by: java.lang.IllegalStateException: inner problem",
        "\tat a.b.E.f(E.java:2)",
        "",
        "-- Mod loading issue for: ars_nouveau --",
        "Details:",
        "\tMod file: /C:/Users/<user>/mods/ars_nouveau-1.21.1-5.11.3.jar",
        "\tFailure message: Mod ars_nouveau requires curios 1.19 or above",
        "\t\tCurrently, curios is not installed",
        "\t",
        "\tMod version: 5.11.3",
        "",
        "-- System Details --",
        "Details:",
        "\tMinecraft Version: 1.21.1",
        "\tJava Version: 21.0.7, Microsoft",
        "\tJVM Flags: 4 total; -Xss1M -Xmx8196m -Xms256m",
        "\tSuspected Mods: Cool Mod (coolmod), Other Mod (othermod)",
        "\tMod List: ",
        "\t\tneoforge-21.1.224-universal.jar |NeoForge |neoforge |21.1.224 |Manifest: NOSI",
        "\t\tfoo-1.0.jar |Foo |foo |1.0 |Manifest: NOSI",
        "",
    ]
)


def test_crash_report_fields():
    f = parse_log(CRASH)
    assert f.format == "crash_report" and f.description == "Exception in server tick loop"
    assert [e.type for e in f.exceptions] == ["java.lang.NullPointerException", "java.lang.IllegalStateException"]
    (issue,) = f.loading_issues
    assert issue.mod_id == "ars_nouveau" and issue.mod_version == "5.11.3"
    assert issue.mod_file == "ars_nouveau-1.21.1-5.11.3.jar"
    assert "requires curios" in issue.failure_message and "curios is not installed" in issue.failure_message
    assert (f.minecraft_version, f.neoforge_version, f.java_version, f.max_heap_mb) == (
        "1.21.1",
        "21.1.224",
        "21.0.7",
        8196,
    )
    assert f.mod_versions["foo"] == "1.0"
    assert f.suspected_mods == ["coolmod", "othermod"]


LOG = "\n".join(
    [
        "[17:37:04] [main/INFO]: ModLauncher running: args [--username, <player>, --version, neoforge-21.1.224, --width, 1]",  # noqa: E501
        "[17:37:04] [main/INFO]: ModLauncher 11.0.5 starting: java version 21.0.7 by Microsoft; OS Windows 11",
        "[17:37:05] [main/INFO]: ",
        "     Mod List:",
        "\t\tName Version (Mod Id)",
        "",
        "\t\tCurios API 9.0.0 (curios)",
        "\t\tMinecraft 1.21.1 (minecraft)",
        "[17:37:35] [main/ERROR]: Missing or unsupported mandatory dependencies:",
        "\tMod ID: 'curios', Requested by: 'ars_nouveau', Expected range: '[1.19,)', Actual version: '[MISSING]'",
        "[28Oct2026 17:37:44.849] [Render thread/FATAL] [net.neoforged.fml.ModLoader/CORE]: "
        "Error during pre-loading phase: Mod ars_nouveau requires curios 1.19 or above",
        "[01Nov2026 14:20:02.040] [Render thread/FATAL] [net.neoforged.fml.ModLoader/CORE]: "
        "Error during pre-loading phase: File mods\\ironfurnaces-neoforge-26.1.2.jar is not a valid mod file",
        "[21:40:07] [main/FATAL]: Mixin prepare for mod cobblemonraiddens failed preparing msd.X in y.json: boom",
        "[21:40:07] [main/INFO]: [java.lang.Throwable:lockedPrintStackTrace:696]: "
        "Caused by: java.lang.NullPointerException: info is null",
        "",
    ]
)


def test_latest_log_fields():
    f = parse_log(LOG)
    assert f.format == "latest_log"
    assert (f.neoforge_version, f.java_version, f.minecraft_version) == ("21.1.224", "21.0.7", "1.21.1")
    assert f.mod_versions == {"curios": "9.0.0", "minecraft": "1.21.1"}
    assert [(d.mod_id, d.requested_by, d.actual) for d in f.dependency_issues] == [
        ("curios", "ars_nouveau", "[MISSING]")
    ]
    assert len(f.fml_errors) == 2 and f.invalid_mod_files == ["mods\\ironfurnaces-neoforge-26.1.2.jar"]
    assert f.mixin_mods == ["cobblemonraiddens"]
    assert f.exceptions[0].type == "java.lang.NullPointerException"  # found behind a log prefix
    assert any("Mixin prepare" in line for line in f.error_lines)


def test_out_of_memory_marker():
    log = (
        "[17:37:04] [main/INFO]: a\n[17:37:05] [main/INFO]: b\n"
        "[17:37:06] [main/ERROR]: java.lang.OutOfMemoryError: Java heap space\n"
    )
    assert parse_log(log).out_of_memory


def test_odd_input_never_raises():
    for text in ("\x00\x01\x02" * 100, "[" * 50_000, "x" * 1_000_000, "\n" * 10_000, "Caused by: " * 5000):
        parse_log(text)


def test_ten_megabyte_log_parses_in_linear_time():
    line = "[28Oct2026 17:37:44.849] [Render thread/INFO] [net.example.Thing/]: loaded asset number 12345 ok\n"
    dep = (
        "[17:37:35] [main/ERROR]: Mod ID: 'a', Requested by: 'b', Expected range: '[1,)', Actual version: '[MISSING]'\n"
    )
    big = line * (10_500_000 // len(line)) + dep
    start = time.perf_counter()
    facts = parse_log(big)
    elapsed = time.perf_counter() - start
    assert facts.format in ("debug_log", "latest_log")
    assert facts.dependency_issues and elapsed < 10, f"{elapsed:.1f}s"


# --- real gold logs (specific facts) -------------------------------------------------------------


def test_real_missing_dependency_log():
    f = parse_log(gold("r01_latest"))
    requesters = sorted(d.requested_by for d in f.dependency_issues if d.mod_id == "curios")
    assert requesters == ["allthearcanistgear", "ars_nouveau", "occultism"]
    assert (f.minecraft_version, f.neoforge_version) == ("1.21.1", "21.1.224")
    crash = parse_log(gold("r01_crash"))
    assert {i.mod_id for i in crash.loading_issues} == {"ars_nouveau", "allthearcanistgear", "occultism"}


def test_real_mixin_log_names_the_mod_whose_mixin_crashed():
    f = parse_log(gold("r14_latest"))
    assert f.mixin_mods == ["cobblemonraiddens"]
    assert any(e.type.endswith("NullPointerException") for e in f.exceptions)


def test_real_oom_logs():
    assert parse_log(gold("r10_latest")).out_of_memory and parse_log(gold("r11_latest")).out_of_memory
    assert not parse_log(gold("r01_latest")).out_of_memory


def test_real_wrong_loader_jar_is_found_as_invalid_mod_file():
    assert any("ironfurnaces" in n for n in parse_log(gold("r06_latest")).invalid_mod_files)


def test_real_large_crash_report_lists_every_loading_issue():
    assert len(parse_log(gold("r17_crash")).loading_issues) == 26


# --- every committed real log --------------------------------------------------------------------

ALL_LOGS = sorted(
    p for folder in (GOLD, REPO_ROOT / "data" / "demo") for p in folder.rglob("*") if p.suffix in (".log", ".txt")
)


@pytest.mark.parametrize("path", ALL_LOGS, ids=lambda p: f"{p.parent.name}/{p.name}"[:60])
def test_every_real_log_parses_into_a_supported_format_with_some_signal(path):
    f = parse_log(path.read_text(encoding="utf-8"))
    assert f.format in ("crash_report", "latest_log")
    assert f.neoforge_version == "21.1.224" and f.java_version
    signals = (
        f.loading_issues,
        f.dependency_issues,
        f.fml_errors,
        f.exceptions,
        f.invalid_mod_files,
        f.mixin_mods,
        f.error_lines,
    )
    assert any(signals) or f.out_of_memory
