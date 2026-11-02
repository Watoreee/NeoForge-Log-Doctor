"""Format detection and deterministic parsing of Minecraft/NeoForge logs into `RawLogFacts` (PLAN 6.1, 6.2).

Pure functions, no LLM, no I/O. Input must already be redacted (redact.py runs first in the pipeline).
Every parser is a single pass over the lines with anchored regexes and capped output, so a 10 MB log
costs time proportional to its length. Written against the real gold logs, not guessed formats.

Supported formats: NeoForge crash reports, latest.log, debug.log. `hs_err_pid*.log` is NOT supported
(no real example was collected); it is detected and routed to the generic parser. Unknown text with
log-like markers goes to the generic parser; text with none is rejected.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Literal

from crashdoc.config import LOG_TOKEN_BUDGET
from crashdoc.tokens import estimate_llm_tokens

LogFormat = Literal["crash_report", "latest_log", "debug_log", "generic", "rejected"]

MAX_LINE = 2000  # characters of a line that regexes ever see
MAX_EXCEPTIONS = 12
MAX_ERROR_LINES = 40
MAX_ITEMS = 300  # cap for loading issues / dependency issues / mod lists
SNIFF_LINES = 4000  # lines inspected to decide the format

_CRASH_HEADER = re.compile(r"^-{3,} Minecraft Crash Report -{3,}")
_HS_ERR_HEADER = re.compile(r"^# A fatal error has been detected by the Java Runtime Environment")
# "[17:37:04] [main/INFO]: msg" (early launcher) and "[28Oct2026 17:37:44.849] [Render thread/FATAL] [logger/]: msg"
_LOG_LINE = re.compile(
    r"^\[(?:\d{2}:\d{2}:\d{2}|\d{2}[A-Za-z]{3}\d{4} \d{2}:\d{2}:\d{2}(?:\.\d+)?)\] \[([^\]]*?)/([A-Z]+)\](?: \[[^\]]*\])?: ?(.*)$"  # noqa: E501
)
_EXC_LINE = re.compile(
    r"^(?:Caused by: )?((?:[A-Za-z_$][\w$]*\.)+[A-Za-z_$][\w$]*(?:Exception|Error|Throwable))(?:: (.*))?$"
)
_GENERIC_MARKERS = re.compile(
    r"(?:Exception|Error)\b|\b(?:Caused by:|ERROR|FATAL|WARN|INFO|Traceback)\b|\d{2}:\d{2}:\d{2}"
)

_DEP_LINE = re.compile(
    r"Mod ID: '([^']+)', Requested by: '([^']+)', Expected range: '([^']*)', Actual version: '([^']*)'"
)
_THROWABLE_PREFIX = re.compile(r"^\[[\w.$]+:\w+:\d+\]: ")  # "[java.lang.Throwable:printStackTrace:660]: Caused by: ..."
_PRELOAD_ERROR = re.compile(r"Error during pre-loading phase: (.*)")
_INVALID_MOD_FILE = re.compile(r"File (\S+) is not a valid mod file")
_MIXIN_PREPARE = re.compile(r"Mixin prepare for mod (\S+) failed")
_MIXIN_FROM = re.compile(r"Mixin \[[^\]]*? from mod ([\w.-]+)\]")
_MOD_LIST_ROW = re.compile(r"^\t+(.+?) (\S+) \(([a-z][a-z0-9_]*)\)$")  # latest.log: "\t\tName 1.2.3 (modid)"
_CRASH_MOD_ROW = re.compile(r"^\t+(\S+\.jar)\s*\|[^|]*\|([^|]+)\|([^|]+)\|")  # crash report Mod List table
_SUSPECT_ID = re.compile(r"\(([a-z][a-z0-9_]*)\)")
_ARG_VERSION = re.compile(r"--version, ([^,\]]+)")
_JVM_VERSION = re.compile(r"(?:java version|Java Version:|JVM identified as .*? VM) ?(\d+(?:\.\d+)*)")
_XMX = re.compile(r"-Xmx(\d+)([kKmMgG])")
_OOM = re.compile(r"OutOfMemoryError|Java heap space|GC overhead limit exceeded")


@dataclass
class ExceptionInfo:
    type: str
    message: str | None = None


@dataclass
class LoadingIssue:
    """A crash report's "-- Mod loading issue for: X --" block."""

    mod_id: str | None
    failure_message: str | None = None
    mod_file: str | None = None
    mod_version: str | None = None


@dataclass
class DependencyIssue:
    """One "Mod ID: 'x', Requested by: 'y', Expected range: ..., Actual version: ..." line."""

    mod_id: str
    requested_by: str
    expected: str
    actual: str


@dataclass
class RawLogFacts:
    format: LogFormat
    flagged_generic: bool = False  # not a supported format; best-effort parse (PLAN 6.1)
    description: str | None = None
    exceptions: list[ExceptionInfo] = field(default_factory=list)
    loading_issues: list[LoadingIssue] = field(default_factory=list)
    dependency_issues: list[DependencyIssue] = field(default_factory=list)
    fml_errors: list[str] = field(default_factory=list)  # "Error during pre-loading phase: ..." messages
    invalid_mod_files: list[str] = field(default_factory=list)
    mixin_mods: list[str] = field(default_factory=list)
    suspected_mods: list[str] = field(default_factory=list)
    error_lines: list[str] = field(default_factory=list)
    mod_versions: dict[str, str] = field(default_factory=dict)  # mod id -> version, from the mod list
    minecraft_version: str | None = None
    neoforge_version: str | None = None
    java_version: str | None = None
    max_heap_mb: int | None = None
    out_of_memory: bool = False
    line_count: int = 0

    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def mod_ids(self) -> list[str]:
        return sorted(self.mod_versions)


# --------------------------------------------------------------------------- detection


def detect_format(text: str) -> LogFormat:
    """Cheap regex sniff of the first lines. hs_err is recognised but unsupported, so it goes to `generic`."""
    head = text.split("\n", SNIFF_LINES)[:SNIFF_LINES]
    first = next((ln.strip() for ln in head if ln.strip()), "")
    if _CRASH_HEADER.match(first):
        return "crash_report"
    if _HS_ERR_HEADER.match(first):
        return "generic"
    log_lines = sum(1 for ln in head if _LOG_LINE.match(ln[:MAX_LINE]))
    if log_lines >= 3:
        return "debug_log" if any("/DEBUG]" in ln[:200] for ln in head) else "latest_log"
    if any(_GENERIC_MARKERS.search(ln[:MAX_LINE]) for ln in head):
        return "generic"
    return "rejected"


def parse_log(text: str) -> RawLogFacts:
    """Detect the format and extract facts. Never raises on odd input; unknown formats return best-effort facts."""
    fmt = detect_format(text)
    if fmt == "rejected":
        return RawLogFacts(format="rejected")
    facts = RawLogFacts(format=fmt, flagged_generic=fmt == "generic")
    lines = text.split("\n")
    facts.line_count = len(lines)
    if fmt == "crash_report":
        _parse_crash_report(lines, facts)
    else:
        _parse_log_lines(lines, facts)
    facts.out_of_memory = _OOM.search(text) is not None
    return facts


# --------------------------------------------------------------------------- shared helpers


def _add_exception(facts: RawLogFacts, m: re.Match) -> None:
    info = ExceptionInfo(m.group(1), (m.group(2) or "")[:300] or None)
    if len(facts.exceptions) < MAX_EXCEPTIONS and info not in facts.exceptions:
        facts.exceptions.append(info)


def _add_unique(items: list[str], value: str) -> None:
    if value and value not in items and len(items) < MAX_ITEMS:
        items.append(value)


def _set_versions_from_mods(facts: RawLogFacts) -> None:
    facts.minecraft_version = facts.minecraft_version or facts.mod_versions.get("minecraft")
    facts.neoforge_version = facts.neoforge_version or facts.mod_versions.get("neoforge")


def _heap_mb(flags: str) -> int | None:
    m = _XMX.search(flags)
    if not m:
        return None
    n, unit = int(m.group(1)), m.group(2).lower()
    return n // 1024 if unit == "k" else n * 1024 if unit == "g" else n


# --------------------------------------------------------------------------- latest.log / debug.log / generic


def _parse_log_lines(lines: list[str], facts: RawLogFacts) -> None:
    in_mod_list = False
    seen_errors: set[str] = set()
    for raw in lines:
        line = raw[:MAX_LINE].rstrip("\r")
        m = _LOG_LINE.match(line)
        level, body = (m.group(2), m.group(3)) if m else (None, line)

        # The mod list is a block of tab-indented rows under a "Mod List:" header; any other line ends it.
        if in_mod_list:
            row = _MOD_LIST_ROW.match(line)
            if row:
                if len(facts.mod_versions) < 2000:
                    facts.mod_versions.setdefault(row.group(3), row.group(2))
                continue
            if not line.strip() or line.strip() == "Name Version (Mod Id)":
                continue  # blank line and column header between "Mod List:" and the rows
            in_mod_list = False
        if body.strip() == "Mod List:":
            in_mod_list = True
            continue

        if (d := _DEP_LINE.search(line)) and len(facts.dependency_issues) < MAX_ITEMS:
            issue = DependencyIssue(*d.groups())
            if issue not in facts.dependency_issues:
                facts.dependency_issues.append(issue)
        if "pre-loading phase" in body and (p := _PRELOAD_ERROR.search(body)):
            _add_unique(facts.fml_errors, p.group(1).strip()[:400])
        if (v := _INVALID_MOD_FILE.search(body)) is not None:
            _add_unique(facts.invalid_mod_files, v.group(1))
        if "Mixin" in body:
            for rx in (_MIXIN_PREPARE, _MIXIN_FROM):
                if mx := rx.search(body):
                    _add_unique(facts.mixin_mods, mx.group(1))
        if facts.neoforge_version is None and "ModLauncher running: args" in body and (a := _ARG_VERSION.search(body)):
            facts.neoforge_version = a.group(1).removeprefix("neoforge-")
        if facts.java_version is None and (j := _JVM_VERSION.search(body)):
            facts.java_version = j.group(1)
        if (e := _EXC_LINE.match(_THROWABLE_PREFIX.sub("", body.strip()))) is not None:
            _add_exception(facts, e)
        if level in ("ERROR", "FATAL") and len(facts.error_lines) < MAX_ERROR_LINES:
            key = body[:160]
            if key not in seen_errors:
                seen_errors.add(key)
                facts.error_lines.append(f"[{level}] {body[:300]}")
    _set_versions_from_mods(facts)


# --------------------------------------------------------------------------- crash report


def _parse_crash_report(lines: list[str], facts: RawLogFacts) -> None:
    section = ""  # "", "issue", "mods", "system"
    issue: LoadingIssue | None = None
    in_message = False
    seen_first_exception = False
    suspect_indent: int | None = None  # indent of a "Suspected Mods:" header while its rows are read
    for raw in lines:
        line = raw[:MAX_LINE].rstrip("\r")
        stripped = line.strip()

        if line.startswith("Description: ") and facts.description is None:
            facts.description = line[len("Description: ") :].strip()[:300]
        if _EXC_LINE.match(stripped) and (not seen_first_exception or stripped.startswith("Caused by: ")):
            _add_exception(facts, _EXC_LINE.match(stripped))
            seen_first_exception = True

        if line.startswith("-- "):
            section, in_message, issue = "", False, None
            if line.startswith("-- Mod loading issue"):
                mod = re.match(r"-- Mod loading issue(?: for: (\S+))? --", line)
                issue = LoadingIssue(mod.group(1) if mod else None)
                if len(facts.loading_issues) < MAX_ITEMS:
                    facts.loading_issues.append(issue)
                section = "issue"
            elif line.startswith("-- System Details"):
                section = "system"
            continue
        if stripped.startswith("Suspected Mods:"):
            suspect_indent = len(line) - len(line.lstrip("\t"))
            _collect_suspects(facts, stripped[len("Suspected Mods:") :])
            continue
        if suspect_indent is not None:
            indent = len(line) - len(line.lstrip("\t"))
            if stripped and indent > suspect_indent and "|" not in line and "(" in line:
                _collect_suspects(facts, stripped)
                continue
            suspect_indent = None

        if section == "issue" and issue is not None:
            if stripped.startswith("Mod file:"):
                issue.mod_file = stripped[len("Mod file:") :].strip().rsplit("/", 1)[-1][:200]
                in_message = False
            elif stripped.startswith("Failure message:"):
                issue.failure_message = stripped[len("Failure message:") :].strip()[:400]
                in_message = True
            elif stripped.startswith("Mod version:"):
                issue.mod_version = stripped[len("Mod version:") :].strip()
                in_message = False
            elif stripped.startswith(("Mod issues URL:", "Exception message:", "Stacktrace:")):
                in_message = False
            elif in_message and stripped and issue.failure_message is not None:
                issue.failure_message = f"{issue.failure_message} {stripped}"[:400]
            continue

        if section == "system":
            _parse_system_line(line, stripped, facts)
            if stripped == "Mod List:":
                section = "mods"
        elif section == "mods":
            row = _CRASH_MOD_ROW.match(line)
            if row:
                if len(facts.mod_versions) < 2000:
                    facts.mod_versions.setdefault(row.group(2).strip(), row.group(3).strip())
            elif stripped and not line.startswith("\t\t"):
                section = "system"
                _parse_system_line(line, stripped, facts)
    _set_versions_from_mods(facts)


def _collect_suspects(facts: RawLogFacts, text: str) -> None:
    for mod_id in _SUSPECT_ID.findall(text):
        _add_unique(facts.suspected_mods, mod_id)


def _parse_system_line(line: str, stripped: str, facts: RawLogFacts) -> None:
    if stripped.startswith("Minecraft Version:") and facts.minecraft_version is None:
        facts.minecraft_version = stripped.split(":", 1)[1].strip()
    elif stripped.startswith("Java Version:") and (j := _JVM_VERSION.search(stripped)):
        facts.java_version = j.group(1)
    elif stripped.startswith("JVM Flags:"):
        facts.max_heap_mb = _heap_mb(stripped)


# --------------------------------------------------------------------------- truncation to the LLM budget

SHORT_LOG_CHARS = 12_000  # about 3k tokens: always sent whole, no selection needed
SELECTION_MARGIN = 250  # tokens held back so the assembled text, not just the sum of lines, fits the budget
MAX_KEPT_LINE = 400  # characters kept per selected line
FRAMES_PER_EXCEPTION = 3  # "at ..." lines kept after each exception line (PLAN 6.2: top N frames)

_KEY_LINE = re.compile(
    r"Requested by:|Missing or unsupported|pre-loading phase|Mixin prepare|OutOfMemoryError|Java heap space|"
    r"GC overhead|is not a valid mod file|Failure message:|Currently, .* is not installed|Mod loading has failed|"
    r"Unknown type|Failed to load Java class|Class could not be found"
)
_SYSTEM_LINE = re.compile(
    r"^\s*(?:Minecraft Version:|Java Version:|JVM Flags:|Memory:|ModLauncher running|JVM identified|ModLauncher \d)"
)


@dataclass
class Preprocessed:
    """The log text that goes to the LLM / the (a) retrieval query, plus what produced it."""

    text: str
    facts: RawLogFacts
    truncated: bool
    omitted_lines: int = 0
    tokens: int = 0


def preprocess_log(text: str, budget: int = LOG_TOKEN_BUDGET) -> Preprocessed:
    """Parse, then cut the log to `budget` Gemma tokens (PLAN 6.2).

    Short logs pass through whole. Longer ones keep a one-line header (versions), then the exception chain with
    its top frames, the FML dependency / loading-error lines, mixin and OOM lines, and other ERROR/FATAL lines,
    **most informative first** and in their original order, until the budget is full. The mod list and
    repeated startup noise are dropped. Because the useful lines come first, truncating this text again
    (e.g. for an embedding input) still keeps the diagnosis lines.
    """
    facts = parse_log(text)
    if facts.format == "rejected" or len(text) <= SHORT_LOG_CHARS:
        return Preprocessed(text=text, facts=facts, truncated=False, tokens=estimate_llm_tokens(text))

    lines = text.split("\n")
    chosen = _select_lines(lines, facts)  # [(priority, index, text)]
    header = _header(facts)
    used = estimate_llm_tokens(header) + SELECTION_MARGIN  # room for newlines and the [...] gap markers
    kept: list[tuple[int, str]] = []
    for _priority, idx, line in sorted(chosen):  # most informative first, original order within a tier
        cost = estimate_llm_tokens(line) + 1
        if used + cost > budget:
            break
        used += cost
        kept.append((idx, line))
    kept.sort()
    body, previous = [], -1
    for idx, line in kept:
        if previous != -1 and idx - previous > 1:
            body.append("[...]")
        body.append(line)
        previous = idx
    out = header + "\n" + "\n".join(body)
    return Preprocessed(
        text=out, facts=facts, truncated=True, omitted_lines=len(lines) - len(kept), tokens=estimate_llm_tokens(out)
    )


def _header(f: RawLogFacts) -> str:
    parts = [
        f"[{f.format}]",
        f"minecraft {f.minecraft_version}",
        f"neoforge {f.neoforge_version}",
        f"java {f.java_version}",
    ]  # noqa: E501
    if f.mod_versions:
        parts.append(f"{len(f.mod_versions)} mods loaded")
    return "; ".join(parts)


def _select_lines(lines: list[str], facts: RawLogFacts) -> list[tuple[int, int, str]]:
    """(priority, line index, text). Priority 0 is the most informative. Linear, one pass."""
    crash = facts.format == "crash_report"
    chosen: list[tuple[int, int, str]] = []
    frames_left = 0
    in_mod_list = in_system = False
    system_kept = 0
    seen: set[str] = set()
    for i, raw in enumerate(lines):
        line = raw[:MAX_LINE].rstrip("\r")
        stripped = line.strip()
        if not stripped:
            continue
        if in_mod_list:  # the mod list (header, blank, rows) is dropped: it is huge and names no failure
            if line.startswith("\t") or stripped.startswith("Name Version"):
                continue
            in_mod_list = False
        if stripped == "Mod List:":
            in_mod_list = True
            continue
        if line.startswith("-- System Details"):
            in_system = True
        m = _LOG_LINE.match(line)
        level, body = (m.group(2), m.group(3)) if m else (None, stripped)
        body = _THROWABLE_PREFIX.sub("", body.strip())

        if _EXC_LINE.match(body):
            frames_left, prio = FRAMES_PER_EXCEPTION, 0
        elif body.startswith("at "):
            if frames_left <= 0:
                continue
            frames_left, prio = frames_left - 1, 2
        elif _KEY_LINE.search(line):
            prio = 0
        elif level in ("ERROR", "FATAL"):
            prio = 1
        elif "does not have required mod" in body:
            prio = 4  # a KubeJS plugin skipped for an optional mod: often benign, so lowest priority
        elif _SYSTEM_LINE.match(line):
            if system_kept >= 8:
                continue
            system_kept, prio = system_kept + 1, 3
        elif crash and not in_system:
            prio = 1  # a crash report's body above "System Details" is small and names the failure
        else:
            continue
        if body[:160] in seen and prio != 2:
            continue
        seen.add(body[:160])
        chosen.append((prio, i, line[:MAX_KEPT_LINE]))
    return chosen
