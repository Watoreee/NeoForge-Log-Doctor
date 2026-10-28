"""Deterministic redaction of personal data in Minecraft logs (PLAN 6.2). No LLM.

Runs before anything is sent to the LLM, written to the cache, or committed. Used by
scripts/redact_logs.py (gold/demo logs) and by preprocessing (pasted logs).

What it claims: every KNOWN name (captured from the log, or passed in) and every MATCHED path,
IP, e-mail, and token is replaced. It does not claim "no player names at all": a name that is
only in chat, and never captured or listed, can survive.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field

# Characters that may NOT touch a name on either side, so "Steve" doesn't match inside "Steven".
_NAME_EDGE = r"A-Za-z0-9_"

# --- Names we can capture from the log itself ---
_SETTING_USER = re.compile(r"Setting user: ([A-Za-z0-9_]{1,32})")
_USERNAME_ARG = re.compile(r"--username[ =]([A-Za-z0-9_]{1,32})")

# --- User folders. The captured folder name is also treated as a known name. ---
# The name must be followed by a separator, or by the end of a line (a path cut off by truncation).
_WIN_USER_PATH = re.compile(r"(?im)\b([a-z]:(?:\\{1,2}|/))Users(\\{1,2}|/)([^\\/:*?\"<>|\r\n]+?)(?=\\|/|$)")
_NIX_USER_PATH = re.compile(r"(?m)(/home/|/Users/)([^/\s:<>\"']+)(?=/|$|\s|[\"'\])])")  # no <> so "<user>" stays

# --- Secrets / network identifiers ---
_TOKEN_ARGS = re.compile(
    r"(?i)(--(?:accessToken|session|uuid|xuid|clientId)[ =])([^\s<]\S*)"
    r"|((?:accessToken|session_?id|clientToken|auth_?token)[\"']?\s*[:=]\s*[\"']?)([^\s\"',}<][^\s\"',}]*)"
)
_SESSION_TOKEN = re.compile(r"token:[A-Za-z0-9._-]{8,}(?::[0-9a-fA-F-]{32,36})?")
_JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}")
_ENV_IDENTITY = re.compile(r"(?m)^(\s*(?:USERNAME|USER|LOGNAME|COMPUTERNAME|HOSTNAME|USERDOMAIN)\s*=\s*)(\S.*)$")
_EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
# IPv4-shaped candidates. Mod versions are often 4-part (1.2.3.4), so a candidate is only redacted
# when its context says it's a network address (see _ipv4_replacement). Loopback / unspecified
# addresses are never redacted: not personal, and useful for diagnosing bind errors.
_IPV4 = re.compile(
    r"(?<![\w.])(?!(?:127\.0\.0\.1|0\.0\.0\.0)(?![\w.]))"
    r"(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}(?![\w.])"
)
_IPV6 = re.compile(
    r"(?<![\w:])(?=[0-9a-fA-F:]*\d)"
    r"((?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,6}:(?:[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4})*)?)"
    r"(?![\w:])"
)
_PORT_AFTER = re.compile(r":\d{1,5}(?!\d)")
_NETWORK_KEYWORD_BEFORE = re.compile(
    r"(?i)(?:connect(?:ing|ed)?\s+to|server[-_ ]?(?:ip|address)|address|host(?:name)?|\bip|\bfrom)[\s:=\"'\[(]*$"
)
_SERVER_ADDRESS_LINE = re.compile(r"(?i)server[-_ ]?(?:ip|address)")
_VERSION_BEFORE = re.compile(r"(?i)(?:[-_@+]|\bv|version[\s:=]*)$")
_VERSION_AFTER = re.compile(r"^[-+_]?[A-Za-z]")
_VERSION_LINE = re.compile(r"(?i)\.jar\b|\||\b(?:mod|mods|version|loader|neoforge|forge|minecraft|requires?)\b")


@dataclass
class RedactionResult:
    """Redacted text plus counts per kind. Counts only: the report never repeats a redacted value."""

    text: str
    counts: Counter = field(default_factory=Counter)
    known_names: int = 0


def capture_names(text: str) -> set[str]:
    """Player names the log itself reveals: `Setting user: X` and launcher `--username X`."""
    return set(_SETTING_USER.findall(text)) | set(_USERNAME_ARG.findall(text))


def capture_user_folders(text: str) -> set[str]:
    """OS account names from user-home paths (C:\\Users\\X\\, /home/X/, /Users/X/)."""
    names = {m.group(3) for m in _WIN_USER_PATH.finditer(text)}
    names |= {m.group(2) for m in _NIX_USER_PATH.finditer(text)}
    return {n for n in names if n.lower() not in {"public", "default", "all users"}}


def redact_text(text: str, extra_names: list[str] | tuple[str, ...] = ()) -> RedactionResult:
    """Redact one log. `extra_names` are known players (e.g. from --names), replaced everywhere."""
    counts: Counter = Counter()
    players = capture_names(text) | {n.strip() for n in extra_names if n.strip()}
    accounts = capture_user_folders(text)

    # Paths first, so the account name inside a path becomes <user> rather than <player>.
    text = _sub(_WIN_USER_PATH, lambda m: f"{m.group(1)}Users{m.group(2)}<user>", text, counts, "path")
    text = _sub(_NIX_USER_PATH, lambda m: f"{m.group(1)}<user>", text, counts, "path")
    text = _sub(_TOKEN_ARGS, _redact_token_arg, text, counts, "token")
    text = _sub(_SESSION_TOKEN, "token:<token>", text, counts, "token")
    text = _sub(_JWT, "<token>", text, counts, "token")
    text = _sub(_ENV_IDENTITY, lambda m: f"{m.group(1)}<redacted>", text, counts, "env_identity")
    text = _sub(_EMAIL, "<email>", text, counts, "email")
    text = _redact_ipv4(text, counts)
    text = _sub(_IPV6, "<ip>", text, counts, "ipv6")

    # Player names: case-insensitive (Minecraft names are), whole-token only.
    text = _replace_names(players, "<player>", text, counts, "player_name", ignore_case=True)
    # Account names: case-sensitive, so an account "Asus" doesn't also erase a GPU vendor "ASUS".
    text = _replace_names(accounts - players, "<user>", text, counts, "account_name", ignore_case=False)
    return RedactionResult(text=text, counts=counts, known_names=len(players | accounts))


def _redact_ipv4(text: str, counts: Counter) -> str:
    """Replace IPv4 candidates that are network addresses; leave version numbers alone."""

    def replace(m: re.Match) -> str:
        if not _ipv4_is_network_address(m):
            return m.group(0)
        counts["ipv4"] += 1
        return "<ip>"

    return _IPV4.sub(replace, text)


def _ipv4_is_network_address(m: re.Match) -> bool:
    """Network evidence wins, then version context, then the private-range fallback.

    Network: a :port after it, "/" right before it, a keyword like "connecting to" / "address"
    right before it, or a server-address line. Version: -, _, @, +, v or "version" right before it,
    letters right after it (1.2.3.4-beta), or a mod-list / loader line. Otherwise only private
    ranges (10/8, 172.16/12, 192.168/16, 169.254/16, 100.64/10) are treated as addresses.
    """
    text = m.string
    line_start = text.rfind("\n", 0, m.start()) + 1
    line_end = text.find("\n", m.end())
    line = text[line_start : line_end if line_end != -1 else len(text)]
    before = text[max(line_start, m.start() - 60) : m.start()]
    after = text[m.end() : m.end() + 8]

    if _PORT_AFTER.match(after) or before.endswith("/") or _NETWORK_KEYWORD_BEFORE.search(before):
        return True
    if _SERVER_ADDRESS_LINE.search(line):
        return True
    if _VERSION_BEFORE.search(before) or _VERSION_AFTER.match(after) or _VERSION_LINE.search(line):
        return False
    return _is_private_ipv4(m.group(0))


def _is_private_ipv4(ip: str) -> bool:
    a, b = (int(x) for x in ip.split(".")[:2])
    return (
        a == 10
        or (a == 172 and 16 <= b <= 31)
        or (a, b) in {(192, 168), (169, 254)}
        or (a == 100 and 64 <= b <= 127)  # carrier-grade NAT
    )


def _replace_names(names: set[str], placeholder: str, text: str, counts: Counter, kind: str, ignore_case: bool) -> str:
    """Replace every whole-token occurrence of any name in one linear pass."""
    names = {n for n in names if len(n) >= 2}
    if not names:
        return text
    alternation = "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True))
    flags = re.IGNORECASE if ignore_case else 0
    pattern = re.compile(rf"(?<![{_NAME_EDGE}])(?:{alternation})(?![{_NAME_EDGE}])", flags)
    return _sub(pattern, placeholder, text, counts, kind)


def _redact_token_arg(m: re.Match) -> str:
    prefix = m.group(1) if m.group(1) is not None else m.group(3)
    return f"{prefix}<token>"


def _sub(pattern: re.Pattern, repl, text: str, counts: Counter, kind: str) -> str:
    """re.subn that also records how many replacements of this kind were made."""
    new_text, n = pattern.subn(repl, text)
    if n:
        counts[kind] += n
    return new_text
