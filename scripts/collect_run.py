"""Copy one fault-injection run's logs into the raw-log folder and record its labels (PLAN 6.1).

Usage (by hand, right after the game crashed or closed):
    python scripts/collect_run.py --category missing_dependency --culprit jei --broke "removed jei" [--also a,b]
                                  [--since-minutes 15] [--dry-run] [--yes]

- Paths come from the environment only (or the git-ignored .env): CRASHDOC_INSTANCE is the game instance
  folder, CRASHDOC_RAW_DIR the raw-log folder. The raw folder must be OUTSIDE the repo.
- Files are COPIED (never moved) into <raw dir>/r<NN>_<category>_<culprit>/ with their original names.
  An existing run folder is never overwritten.
- Refuses (exit 1) when logs/latest.log is byte-identical (SHA-256) to the latest.log of an earlier run
  folder: the game was probably not relaunched since that run. --force collects it anyway.
- Stdlib only, no network. The category list is read from src/crashdoc/schemas.py (one source of truth)
  with `ast`, so this script needs no third-party packages.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import os
import re
import shutil
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_PATH = REPO_ROOT / "src" / "crashdoc" / "schemas.py"
DOTENV_PATH = REPO_ROOT / ".env"

MOD_ID = re.compile(r"[a-z0-9_-]+")
RUN_DIR = re.compile(r"r(\d+)_")
RUNS_HEADER = "run_id | category | culprit | acceptable | files | what_broke | timestamp"


@dataclass
class Plan:
    """Everything a run would do, computed before anything is written (so --dry-run can print it)."""

    run_id: str
    run_dir: Path
    category: str
    culprit: str | None
    acceptable: list[str]
    what_broke: str
    files: list[Path] = field(default_factory=list)
    stale_latest: bool = False


# ---------------------------------------------------------------- inputs


def load_categories(schemas_path: Path = SCHEMAS_PATH) -> list[str]:
    """String values of `class Category` in schemas.py, read without importing pydantic."""
    tree = ast.parse(schemas_path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Category":
            return [
                stmt.value.value
                for stmt in node.body
                if isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.Constant)
            ]
    raise SystemExit(f"class Category not found in {schemas_path}")


def read_env_paths(environ: dict[str, str], dotenv_path: Path) -> tuple[str, str]:
    """CRASHDOC_INSTANCE and CRASHDOC_RAW_DIR: the real environment wins, then .env. Only these two keys are read."""
    values = {}
    if dotenv_path.is_file():
        for line in dotenv_path.read_text(encoding="utf-8").splitlines():
            key, sep, value = line.partition("=")
            if sep and key.strip() in ("CRASHDOC_INSTANCE", "CRASHDOC_RAW_DIR"):
                values[key.strip()] = value.strip().strip("\"'")
    values.update({k: environ[k] for k in ("CRASHDOC_INSTANCE", "CRASHDOC_RAW_DIR") if environ.get(k)})
    missing = [k for k in ("CRASHDOC_INSTANCE", "CRASHDOC_RAW_DIR") if not values.get(k)]
    if missing:
        raise SystemExit(f"Set {', '.join(missing)} in the environment or .env (see .env.example).")
    return values["CRASHDOC_INSTANCE"], values["CRASHDOC_RAW_DIR"]


def check_raw_dir(raw_dir: Path) -> Path:
    """Raw logs never enter the repo (PLAN 12), so refuse a raw folder inside it."""
    raw_dir = raw_dir.resolve()
    if raw_dir == REPO_ROOT or REPO_ROOT in raw_dir.parents:
        raise SystemExit("CRASHDOC_RAW_DIR is inside the git repo. Raw logs must stay OUTSIDE the repo.")
    if not raw_dir.is_dir():
        raise SystemExit("CRASHDOC_RAW_DIR does not exist. Create it first (no folder is created for you).")
    return raw_dir


def validate_category(value: str, categories: list[str]) -> str:
    value = value.strip().lower()
    if value not in categories:
        raise ValueError(f"unknown category {value!r}; choose one of: {', '.join(categories)}")
    return value


def validate_mod_id(value: str) -> str:
    """Mod ids are lowercase [a-z0-9_-]; anything else is a typo or a display name."""
    value = value.strip()
    if not MOD_ID.fullmatch(value):
        raise ValueError(f"invalid mod id {value!r}: use lowercase letters, digits, '_' or '-' only")
    return value


def parse_culprit(value: str) -> str | None:
    """'none' means no single culprit mod (stored as null)."""
    value = value.strip()
    return None if value.lower() == "none" else validate_mod_id(value)


def acceptable_culprits(culprit: str | None, also: str) -> list[str]:
    """The culprit always comes first; with no culprit the list is empty (the gold-label rule in schemas.py)."""
    if culprit is None:
        return []
    out = [culprit]
    for item in also.split(","):
        if item.strip():
            mod = validate_mod_id(item)
            if mod not in out:
                out.append(mod)
    return out


def ask(prompt: str, check):
    """Prompt until `check` accepts the answer (used only for arguments not given on the command line)."""
    while True:
        try:
            return check(input(prompt))
        except ValueError as exc:
            print(f"  {exc}")


# ---------------------------------------------------------------- planning


def slug(text: str) -> str:
    """Folder-name part: lowercase, hyphens, no spaces ('missing_dependency' -> 'missing-dependency')."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "none"


def next_run_number(raw_dir: Path) -> int:
    """Next rNN. Uses the highest existing number + 1, which equals the folder count unless one was deleted;
    then counting alone would reuse a number that still exists."""
    numbers = [int(m.group(1)) for p in raw_dir.iterdir() if p.is_dir() and (m := RUN_DIR.match(p.name))]
    return max(numbers, default=0) + 1


def recent_files(paths, since_ts: float) -> list[Path]:
    return sorted(p for p in paths if p.is_file() and p.stat().st_mtime >= since_ts)


def previous_run_timestamp(raw_dir: Path) -> float | None:
    """Epoch seconds of the most recent run recorded in runs.txt (last column), or None if there is none.

    Rows without a timestamp (a dropped run) are skipped. Timestamps are local time, as collect_run writes them.
    """
    runs = raw_dir / "runs.txt"
    if not runs.is_file():
        return None
    stamps = []
    for line in runs.read_text(encoding="utf-8").splitlines()[1:]:
        last = line.rsplit("|", 1)[-1].strip()
        try:
            stamps.append(datetime.fromisoformat(last).timestamp())
        except ValueError:
            continue
    return max(stamps, default=None)


def mods_warnings(instance: Path) -> list[str]:
    """Things in mods/ that usually mean the pack is not in the state the label assumes."""
    mods = instance / "mods"
    if not mods.is_dir():
        return []
    out = []
    disabled = sorted(p.name for p in mods.glob("*.disabled"))
    fabric = sorted(p.name for p in mods.glob("*-fabric*.jar"))
    if disabled:
        out.append(f"mods/ contains {len(disabled)} *.disabled file(s): {', '.join(disabled[:5])}")
    if fabric:
        out.append(f"mods/ contains {len(fabric)} Fabric jar(s) (*-fabric*.jar): {', '.join(fabric[:5])}")
    return out


def files_to_copy(instance: Path, since_ts: float, crash_since_ts: float | None = None) -> tuple[list[Path], bool]:
    """latest.log, debug.log, crash reports and hs_err files. Also: is latest.log stale?

    Crash reports and hs_err files are copied only if modified AFTER `crash_since_ts` (the previous run's
    timestamp in runs.txt); without one they fall back to the `since_ts` window.
    """
    logs = instance / "logs"
    latest = logs / "latest.log"
    files = [p for p in (latest, logs / "debug.log") if p.is_file()]
    if crash_since_ts is None:
        crash = recent_files((instance / "crash-reports").glob("*.txt"), since_ts)
        crash += recent_files(instance.glob("hs_err_pid*.log"), since_ts)
    else:  # strictly after the previous run, so the previous run's own crash report is not collected again
        candidates = [*(instance / "crash-reports").glob("*.txt"), *instance.glob("hs_err_pid*.log")]
        crash = sorted(p for p in candidates if p.is_file() and p.stat().st_mtime > crash_since_ts)
    files += crash
    stale = not latest.is_file() or latest.stat().st_mtime < since_ts
    return files, stale


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def find_duplicate_run(latest: Path, raw_dir: Path) -> Path | None:
    """The earliest run folder whose stored latest.log has the same SHA-256 as `latest`, or None."""
    if not latest.is_file():
        return None
    digest = sha256_file(latest)
    runs = sorted((int(m.group(1)), p) for p in raw_dir.iterdir() if p.is_dir() and (m := RUN_DIR.match(p.name)))
    for _number, run_dir in runs:
        stored = run_dir / "latest.log"
        if stored.is_file() and sha256_file(stored) == digest:
            return run_dir
    return None


def make_plan(args, instance: Path, raw_dir: Path, now: float) -> Plan:
    number = next_run_number(raw_dir)
    run_id = f"r{number:02d}"
    culprit_part = args.culprit or "none"
    run_dir = raw_dir / f"{run_id}_{slug(args.category)}_{slug(culprit_part)}"
    files, stale = files_to_copy(instance, now - args.since_minutes * 60, previous_run_timestamp(raw_dir))
    return Plan(run_id, run_dir, args.category, args.culprit, args.acceptable, args.broke, files, stale)


# ---------------------------------------------------------------- writing


def one_line(text: str) -> str:
    """Free text for the pipe-separated runs.txt: no '|' (it is the separator) and no line breaks."""
    return " ".join(text.replace("|", "/").split())


def notes_text(plan: Plan) -> str:
    return (
        f"what_i_broke: {plan.what_broke}\n"
        f"culprit_mod_id: {plan.culprit if plan.culprit is not None else 'null'}\n"
        f"acceptable_culprits: {', '.join(plan.acceptable)}\n"
        f"category: {plan.category}\n"
        f"files_produced: {', '.join(p.name for p in plan.files)}\n"
    )


def runs_line(plan: Plan, timestamp: str) -> str:
    fields = [
        plan.run_id,
        plan.category,
        plan.culprit if plan.culprit is not None else "null",
        ",".join(plan.acceptable),
        ",".join(p.name for p in plan.files),
        one_line(plan.what_broke),
        timestamp,
    ]
    return " | ".join(fields)


def execute(plan: Plan, raw_dir: Path, now: float) -> None:
    """Create the run folder (never an existing one), copy files, write notes.txt, append to runs.txt."""
    plan.run_dir.mkdir(exist_ok=False)
    for src in plan.files:
        shutil.copy2(src, plan.run_dir / src.name)
    (plan.run_dir / "notes.txt").write_text(notes_text(plan), encoding="utf-8")

    runs = raw_dir / "runs.txt"
    timestamp = datetime.fromtimestamp(now).isoformat(timespec="seconds")
    with runs.open("a", encoding="utf-8") as f:
        if runs.stat().st_size == 0:
            f.write(RUNS_HEADER + "\n")
        f.write(runs_line(plan, timestamp) + "\n")


def print_plan(plan: Plan, dry_run: bool) -> None:
    verb = "Would copy" if dry_run else "Copied"
    print(f"{plan.run_id}: {plan.run_dir.name}")
    print(f"  category={plan.category} culprit={plan.culprit or 'null'} acceptable=[{', '.join(plan.acceptable)}]")
    print(f"{verb} {len(plan.files)} file(s):")
    for p in plan.files:
        print(f"  {p.parent.name}/{p.name}")


def warn_stale(since_minutes: float) -> None:
    bar = "!" * 70
    print(f"{bar}\nWARNING: logs/latest.log is missing or older than {since_minutes:g} minutes.")
    print(f"The game probably did not launch in this run.\n{bar}")


# ---------------------------------------------------------------- main


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Copy a fault-injection run's logs into the raw-log folder.")
    p.add_argument("--category")
    p.add_argument("--broke", help="what you did to break the pack")
    p.add_argument("--culprit", help="mod id, or 'none'")
    p.add_argument("--also", help="comma-separated other acceptable culprit mod ids")
    p.add_argument("--since-minutes", type=float, default=15)
    p.add_argument("--dry-run", action="store_true", help="print the plan and write nothing")
    p.add_argument("--yes", action="store_true", help="continue past the stale-latest.log warning without asking")
    p.add_argument("--force", action="store_true", help="collect even if latest.log duplicates an earlier run's")
    return p


def resolve_args(args, categories: list[str]) -> None:
    """Validate given arguments; prompt for missing ones. Invalid command-line values are an error, not a prompt."""
    try:
        if args.category is None:
            args.category = ask(f"Category ({', '.join(categories)}): ", lambda v: validate_category(v, categories))
        else:
            args.category = validate_category(args.category, categories)
        if args.culprit is None:
            args.culprit = ask("Culprit mod id (or 'none'): ", parse_culprit)
        else:
            args.culprit = parse_culprit(args.culprit)
        if args.also is None:
            args.also = "" if args.culprit is None else ask("Also acceptable (comma list, blank for none): ", str)
        args.acceptable = acceptable_culprits(args.culprit, args.also)
        if args.broke is None:
            args.broke = ask("What did you break? ", lambda v: v.strip() or _raise("please describe it"))
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    args.broke = " ".join(args.broke.split())  # one line, so notes.txt stays one field per line
    if args.culprit is None and args.also and args.also.strip():
        print("Note: --culprit none, so --also is ignored (acceptable_culprits must be empty).")


def _raise(message: str):
    raise ValueError(message)


def main(argv: list[str] | None = None, now: float | None = None) -> int:
    args = build_parser().parse_args(argv)
    now = time.time() if now is None else now

    instance_str, raw_str = read_env_paths(dict(os.environ), DOTENV_PATH)
    raw_dir = check_raw_dir(Path(raw_str))
    instance = Path(instance_str)
    if not instance.is_dir():
        raise SystemExit("CRASHDOC_INSTANCE does not exist or is not a folder.")

    for warning in mods_warnings(instance):
        print(f"WARNING: {warning}")
    resolve_args(args, load_categories())
    plan = make_plan(args, instance, raw_dir, now)

    if plan.stale_latest:
        warn_stale(args.since_minutes)
        if not (args.yes or args.dry_run) and input("Continue anyway? [y/N] ").strip().lower() != "y":
            print("Nothing written.")
            return 1

    duplicate = find_duplicate_run(instance / "logs" / "latest.log", raw_dir)
    if duplicate is not None:
        print(f"logs/latest.log is identical (SHA-256) to the one already stored in {duplicate.name}/.")
        if not args.force:
            print("The game was probably not relaunched since that run. Nothing written (--force collects it anyway).")
            return 1
        print("--force given: collecting it anyway.")

    if args.dry_run:
        print_plan(plan, dry_run=True)
        print("Dry run: nothing written.")
        return 0

    execute(plan, raw_dir, now)
    print_plan(plan, dry_run=False)
    print(f"Wrote notes.txt and appended to runs.txt in {raw_dir.name}/.")
    print("REMINDER: restore the mod / config you broke before the next run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
