"""Redaction (PLAN 6.2, section 8): paths, `Setting user:` capture, --names, IPs, tokens.

All inputs are short synthetic lines written for these tests, not real logs.
"""

from __future__ import annotations

import subprocess
import sys

import pytest

from crashdoc.config import REPO_ROOT
from crashdoc.redact import redact_text

# ---------------------------------------------------------------- paths


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (r"C:\Users\Alice\AppData\Roaming\.minecraft\mods", r"C:\Users\<user>\AppData\Roaming\.minecraft\mods"),
        (r"d:\users\Alice\curseforge\x.jar", r"d:\Users\<user>\curseforge\x.jar"),
        ("C:/Users/Alice/game/logs", "C:/Users/<user>/game/logs"),
        (r"C:\\Users\\Alice\\game", r"C:\\Users\\<user>\\game"),
        (r"C:\Users\John Smith\game", r"C:\Users\<user>\game"),
        ("/home/alice/.minecraft/mods", "/home/<user>/.minecraft/mods"),
        ("/Users/alice/Library/x", "/Users/<user>/Library/x"),
    ],
)
def test_user_paths_are_redacted(raw, expected):
    assert redact_text(raw).text == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Config at /home/cont\n[... truncated]", "Config at /home/<user>\n[... truncated]"),
        ("cd /home/alice && ls", "cd /home/<user> && ls"),
        ('"/Users/alice"', '"/Users/<user>"'),
        ("C:\\Users\\Alice", "C:\\Users\\<user>"),
    ],
)
def test_home_path_cut_off_or_without_trailing_separator_is_redacted(raw, expected):
    assert redact_text(raw).text == expected


def test_account_name_from_path_is_redacted_elsewhere_case_sensitively():
    raw = "C:\\Users\\Bob\\game\nuser.name=Bob\nGPU: ASUS GeForce"
    out = redact_text(raw).text
    assert "Bob" not in out.replace("ASUS", "")
    assert "user.name=<user>" in out
    assert "ASUS GeForce" in out  # different case: a GPU vendor, not the account


# ---------------------------------------------------------------- player names


def test_setting_user_name_is_replaced_everywhere():
    raw = (
        "[12:00:00] [main/INFO]: Setting user: Steve123\n"
        "[12:05:00] [Server thread/INFO]: Steve123 joined the game\n"
        "<steve123> hello\n"
    )
    result = redact_text(raw)
    assert "steve123" not in result.text.lower()
    assert result.text.count("<player>") == 3
    assert result.counts["player_name"] == 3


def test_launcher_username_argument_is_captured():
    out = redact_text("args: --username Alex_99 --version 1.21.1\nAlex_99 died").text
    assert "Alex_99" not in out


def test_names_list_is_replaced_everywhere():
    out = redact_text("[Server thread/INFO]: Notch joined\nKicked notch", extra_names=["Notch"]).text
    assert "notch" not in out.lower()


def test_names_match_whole_tokens_only():
    out = redact_text("Steve joined; Steven left; steve_x stays", extra_names=["Steve"]).text
    assert out == "<player> joined; Steven left; steve_x stays"


def test_name_in_file_path_segment_is_still_whole_token():
    out = redact_text("config/Steve/settings.toml", extra_names=["Steve"]).text
    assert out == "config/<player>/settings.toml"


# ---------------------------------------------------------------- network + secrets


def test_ipv4_addresses_are_redacted_but_versions_and_loopback_kept():
    raw = "Connecting to 192.168.1.20, 25565\n/203.0.113.7:25565 lost\nbind 127.0.0.1 and 0.0.0.0\nNeoForge 21.1.77"
    result = redact_text(raw)
    assert "192.168" not in result.text and "203.0.113.7" not in result.text
    assert "127.0.0.1" in result.text and "0.0.0.0" in result.text
    assert "21.1.77" in result.text  # three-part version, not an IP
    assert result.counts["ipv4"] == 2


def test_mod_list_four_part_versions_are_not_changed():
    """version_mismatch diagnoses depend on these; none may become <ip> (including a 10.x one)."""
    raw = (
        "\t\tjei-1.21.1-neoforge-19.21.0.247.jar                |Just Enough Items             |jei"
        "                           |19.21.0.247         |DONE      |Manifest: NOSIGNATURE\n"
        "\t\twaystones-neoforge-1.21.1-21.1.4.0.jar             |Waystones                     |waystones"
        "                     |21.1.4.0            |DONE      |Manifest: NOSIGNATURE\n"
        "\t\texamplemod-10.2.0.4.jar                            |Example Mod                   |examplemod"
        "                    |10.2.0.4            |DONE      |Manifest: NOSIGNATURE\n"
        "[main/INFO] [net.neoforged.fml.loading.moddiscovery.ModDiscoverer/SCAN]: Found mod file "
        '"sophisticatedcore-1.21.1-1.2.9.104.jar" of type MOD\n'
        "Mod examplemod requires geckolib 4.7.1.2 or above\n"
        "examplemod v10.2.0.4 loaded\n"
    )
    result = redact_text(raw)
    assert result.text == raw
    assert "ipv4" not in result.counts


@pytest.mark.parametrize(
    "line",
    [
        "Connecting to 203.0.113.9, 25565",
        "[Server thread/INFO]: Steve[/203.0.113.9:51234] logged in",
        "server-ip=203.0.113.9",
        "Disconnected from 203.0.113.9",
        "remote address: 203.0.113.9",
        "Pinging 192.168.0.12",  # private range, no other context
        "joined via 10.0.0.7",
    ],
)
def test_network_addresses_are_redacted(line):
    result = redact_text(line)
    assert "<ip>" in result.text and result.counts["ipv4"] == 1


def test_public_dotted_number_without_network_context_is_kept():
    assert redact_text("checksum block 203.0.113.9 ok").text == "checksum block 203.0.113.9 ok"


def test_curseforge_instance_path_username_is_redacted():
    raw = r"C:\Users\Alice\curseforge\minecraft\Instances\All the Mons - ATMons_Test\logs\latest.log"
    expected = r"C:\Users\<user>\curseforge\minecraft\Instances\All the Mons - ATMons_Test\logs\latest.log"
    assert redact_text(raw).text == expected


def test_name_ending_in_underscore_is_replaced_as_whole_token():
    out = redact_text("<Alex_> hi\nAlex_ joined\nAlex_x stays", extra_names=["Alex_"]).text
    assert out == "<<player>> hi\n<player> joined\nAlex_x stays"


def test_ipv6_is_redacted_but_timestamps_are_not():
    out = redact_text("[12:00:00] connect /[2001:db8::8a2e:370:7334]:25565").text
    assert "2001:db8" not in out and "[12:00:00]" in out


@pytest.mark.parametrize(
    "raw",
    [
        "--accessToken abcDEF123456789.secretvalue",
        "--uuid 1234567890abcdef1234567890abcdef",
        "--xuid 2535412345678901",
        '"accessToken": "abcDEF1234567890"',
        "accessToken=abcDEF1234567890",
        "Session ID is token:abcdefghij123456:1234567890abcdef1234567890abcdef",
        "auth header eyJhbGciOiJIUzI1.eyJzdWIiOiIxMjM0NTY3.SflKxwRJSMeKKF2QT4",
    ],
)
def test_tokens_are_redacted(raw):
    result = redact_text(raw)
    assert result.counts["token"] >= 1
    for secret in ("abcDEF", "1234567890abcdef", "2535412345678901", "eyJhbGci", "abcdefghij123456"):
        assert secret not in result.text


def test_redacted_text_is_stable_on_a_second_pass():
    """Re-redacting output must find nothing new (redact_logs.py's leftover check relies on this)."""
    raw = (
        "--uuid 1234567890abcdef1234567890abcdef accessToken=abcDEF1234567890 C:\\Users\\Bob\\x 10.0.0.5\n"
        "/home/carol/.minecraft/mods and /Users/dave/Library/x"
    )
    once = redact_text(raw).text
    assert redact_text(once).counts == {}
    assert "/home/<user>/" in once and "/Users/<user>/" in once


def test_hs_err_environment_identity_is_redacted():
    out = redact_text("Environment Variables:\nUSERNAME=bob\nCOMPUTERNAME=BOBS-PC\nOS=Windows_NT").text
    assert "bob" not in out.lower() and "OS=Windows_NT" in out


def test_email_is_redacted_but_java_object_ids_kept():
    out = redact_text("contact me@example.com; object net.minecraft.Foo@1a2b3c").text
    assert "<email>" in out and "Foo@1a2b3c" in out


def test_ordinary_log_lines_are_untouched():
    raw = (
        "[12:00:00] [main/ERROR] [net.neoforged.fml.loading.FMLLoader/]: Missing mod jei 19.0.0\n"
        "java.lang.NoClassDefFoundError: mezz/jei/api/IModPlugin\n"
        "\tat MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.Launcher.run(Launcher.java:108)\n"
    )
    result = redact_text(raw)
    assert result.text == raw and not result.counts


def test_large_log_is_linear_enough():
    """A multi-MB log must redact quickly (PLAN 6.2: linear-time scanning)."""
    line = "[12:00:00] [Render thread/INFO] [minecraft/Minecraft]: Loaded chunk section without errors.\n"
    raw = "Setting user: Steve\n" + line * 60_000  # ~5.6 MB
    import time

    t0 = time.perf_counter()
    redact_text(raw, extra_names=["Alex", "Notch"])
    assert time.perf_counter() - t0 < 10


# ---------------------------------------------------------------- script safety


def test_script_refuses_a_source_folder_inside_the_repo(tmp_path):
    proc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "redact_logs.py"), str(REPO_ROOT / "data"), str(tmp_path)],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0 and "OUTSIDE the repo" in proc.stderr


def test_script_redacts_a_folder_and_reports_counts_only(tmp_path):
    src, dest = tmp_path / "raw", tmp_path / "out"
    (src / "logs").mkdir(parents=True)
    (src / "logs" / "latest.log").write_text("Setting user: Steve\nSteve joined from 10.1.2.3", encoding="utf-8")
    (src / "notes.png").write_bytes(b"\x89PNG")
    proc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "redact_logs.py"), str(src), str(dest), "--names", "Alex"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    out = (dest / "logs" / "latest.log").read_text(encoding="utf-8")
    assert "Steve" not in out and "10.1.2.3" not in out
    report = (dest / "redaction_report.json").read_text(encoding="utf-8")
    assert "Steve" not in report and "Steve" not in proc.stdout
    assert "1 non-log file(s) skipped" in proc.stdout


MODLAUNCHER_ARGS = (
    "[16:21:44] [main/INFO] [cpw.mods.modlauncher.Launcher/MODLAUNCHER]: ModLauncher running: args "
    r"[--username, Fakeplayer_, --version, neoforge-21.1.224, --gameDir, C:\Users\Bob\curseforge\minecraft\Instances\Pack, "  # noqa: E501
    "--assetIndex, 17, --uuid, 0123456789abcdef0123456789abcdef, --accessToken, ey0notajwtjustsecretvalue99, "
    "--clientId, ZmFrZWNsaWVudGlkZmFrZWNsaWVudGlkZmFrZWNsaWVudA, --xuid, 2535400000000001, "
    "--userType, msa, --versionType, release, --width, 1024]"
)


def test_modlauncher_args_line_is_redacted():
    """A real ModLauncher args line is a comma-separated list, not 'flag value' pairs."""
    result = redact_text(MODLAUNCHER_ARGS)
    for secret in (
        "0123456789abcdef0123456789abcdef",
        "ey0notajwtjustsecretvalue99",
        "ZmFrZWNsaWVudGlkZmFrZWNsaWVudGlkZmFrZWNsaWVudA",
        "2535400000000001",
        "Fakeplayer_",
        "Bob",
    ):
        assert secret not in result.text
    # Non-secret arguments survive, and the list structure is intact.
    assert "--version, neoforge-21.1.224" in result.text and "--userType, msa" in result.text
    assert result.text.rstrip().endswith("--width, 1024]")
    assert result.counts["token"] == 4


def test_names_option_redacts_extra_player_everywhere():
    out = redact_text("<Fakeplayer_> hi\nFakeplayer_ joined the game", extra_names=["Fakeplayer_"]).text
    assert "Fakeplayer_" not in out and "<player>" in out


def test_player_uuid_is_redacted_outside_the_args_line_too():
    """authlib timeouts print the player's UUID in a sessionserver URL, far from the launcher args."""
    uuid = "0123456789abcdef0123456789abcdef"
    raw = (
        f"ModLauncher running: args [--username, Bob, --uuid, {uuid}, --userType, msa]\n"
        f"MinecraftClientException: Failed to read from https://sessionserver.mojang.com/session/minecraft/profile/{uuid}?unsigned=false"
    )
    assert uuid not in redact_text(raw).text
    only_url = "https://sessionserver.mojang.com/session/minecraft/profile/01234567-89ab-cdef-0123-456789abcdef?x=1"
    assert "01234567" not in redact_text(only_url).text
    assert "unsigned" not in redact_text(only_url).text or "?x=1" in redact_text(only_url).text


def test_authlib_profile_lookup_uuid_is_redacted_without_an_args_line():
    raw = "YggdrasilMinecraftSessionService/]: Couldn't look up profile properties for 01234567-89ab-cdef-0123-456789abcdef"  # noqa: E501
    assert "01234567" not in redact_text(raw).text
