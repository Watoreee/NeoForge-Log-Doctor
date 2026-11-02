"""Structured extraction of `LogFacts` from a preprocessed log (PLAN 6.3).

The proxy ignores `response_format`, so we ask for JSON in the prompt, strip a markdown fence, validate with
pydantic, and retry once with the validation error fed back. If that also fails, fall back to facts derived by
regex from `RawLogFacts` (never crash, missing fields stay null). Every `suspect_mod_id` must then appear in the
**whole** log as a whole token, or it is dropped and counted.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Literal

from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

from crashdoc.llm import LLM
from crashdoc.preprocess import Preprocessed, RawLogFacts
from crashdoc.schemas import Category

EXTRACT_PROMPT_VERSION = "extract-v2"  # bump whenever EXTRACT_SYSTEM / the user template changes

# Categories the model may choose. duplicate_mod / config_error were dropped (decisions.md).
ALLOWED_CATEGORIES = ("missing_dependency", "version_mismatch", "out_of_memory", "mixin_conflict", "other")

EXTRACT_SYSTEM = """You read a Minecraft NeoForge 1.21.1 crash report or log and extract facts. Reply with ONE JSON object and nothing else:
{
  "exception_type": the main Java exception class name (e.g. "java.lang.NullPointerException"), or null,
  "error_category": one of "missing_dependency", "version_mismatch", "out_of_memory", "mixin_conflict", "other",
  "suspect_mod_ids": [mod ids (lowercase, e.g. "create", "ae2") that most likely CAUSED the failure, best first],
  "mc_version": Minecraft version string or null,
  "loader_version": NeoForge version string or null,
  "java_version": Java version string or null
}
Rules:
- Label the CAUSE, not the symptom. A jar skipped because it is for the wrong Minecraft/NeoForge version or the
  wrong loader (e.g. Fabric) is "version_mismatch" even if other mods then report it as "not installed".
- "missing_dependency": a required mod is not installed. The suspect is the MISSING mod. In lines like
  "Mod A requires B" with "B is not installed" (or "Requested by: 'A'" with "Actual version: [MISSING]"), A is only
  the victim that needs B: put B in suspect_mod_ids, not A.
- "version_mismatch": a mod or jar is for the wrong version or loader. If mod A "requires neoforge/minecraft/java
  X or above" and the pack has an older one, the suspect is A (its jar was built for another version). If a jar
  was skipped as "not a valid mod file" / wrong loader, or other mods report a mod as missing although its jar
  is present but skipped, the suspect is that skipped mod, not the mods that need it.
- "mixin_conflict": a mixin failed to apply. The suspect is the mod whose mixin crashed.
- "out_of_memory": java.lang.OutOfMemoryError or heap exhaustion. Use an empty suspect list.
- A KubeJS script that fails with "class could not be found", "Unknown type" or "plugin ... does not have required
  mod" because some mod is not loaded is "missing_dependency"; the suspect is the mod whose classes or types are
  missing, not KubeJS and not the script.
- Only use mod ids that literally appear in the log. If unsure, return fewer ids, not guesses.
- Use null for anything the log does not state."""


class LogFacts(BaseModel):
    model_config = ConfigDict(extra="ignore")

    exception_type: str | None = None
    error_category: Category | None = None
    suspect_mod_ids: list[str] = []
    mc_version: str | None = None
    loader_version: str | None = None
    java_version: str | None = None

    @field_validator("suspect_mod_ids", mode="before")
    @classmethod
    def _clean_ids(cls, v):
        if v is None:
            return []
        if not isinstance(v, list):
            raise ValueError("suspect_mod_ids must be a list of strings")
        ids = [str(x).strip().lower() for x in v if str(x).strip()]
        return list(dict.fromkeys(ids))


Source = Literal["llm", "llm_repaired", "regex_fallback"]


@dataclass
class ExtractionResult:
    facts: LogFacts
    source: Source
    dropped_ids: list[str] = field(default_factory=list)  # hallucinated ids removed by the whole-token check
    errors: list[str] = field(default_factory=list)  # validation problems seen on the way (for the results file)


# --------------------------------------------------------------------------- JSON handling


def parse_json_object(text: str | None) -> dict:
    """Strip a ```json fence and parse the first JSON object. Raises ValueError if there is none."""
    if not text:
        raise ValueError("empty reply")
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.IGNORECASE).strip()
    start, end = t.find("{"), t.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object in reply")
    obj = json.loads(t[start : end + 1])
    if not isinstance(obj, dict):
        raise ValueError("reply is not a JSON object")
    return obj


def is_whole_token_in(mod_id: str, text: str) -> bool:
    """Case-insensitive whole-token search: neighbours must not be [A-Za-z0-9_-] (so 'ae2' is not in 'tae2x')."""
    if not mod_id:
        return False
    return re.search(rf"(?<![A-Za-z0-9_-]){re.escape(mod_id)}(?![A-Za-z0-9_-])", text, re.IGNORECASE) is not None


# --------------------------------------------------------------------------- regex fallback

_REQUIRES = re.compile(r"^Mod ([A-Za-z0-9_]+) requires ([A-Za-z0-9_]+) ")
_JAR_ID = re.compile(r"([A-Za-z][A-Za-z_]*)")


def regex_facts(raw: RawLogFacts) -> LogFacts:
    """Facts derived only from RawLogFacts: used when the LLM reply can't be validated (PLAN 6.3)."""
    exc = raw.exceptions[0].type if raw.exceptions else None
    category: Category | None = None
    suspects: list[str] = []
    missing = [d.mod_id for d in raw.dependency_issues if d.actual == "[MISSING]"]
    messages = [i.failure_message or "" for i in raw.loading_issues] + raw.fml_errors
    if raw.out_of_memory:
        category = Category.OUT_OF_MEMORY
    elif raw.mixin_mods:
        category, suspects = Category.MIXIN_CONFLICT, list(raw.mixin_mods)
    elif raw.invalid_mod_files:
        category = Category.VERSION_MISMATCH
        suspects = [m.group(1).lower() for n in raw.invalid_mod_files if (m := _JAR_ID.match(n.rsplit("\\", 1)[-1]))]
    elif missing or any("is not installed" in m for m in messages):
        category = Category.MISSING_DEPENDENCY
        suspects = list(dict.fromkeys(missing)) or [
            m.group(2) for msg in messages if (m := _REQUIRES.match(msg)) and "is not installed" in msg
        ]
    elif raw.dependency_issues or any(_REQUIRES.match(m) for m in messages):
        category = Category.VERSION_MISMATCH
        suspects = list(dict.fromkeys(d.requested_by for d in raw.dependency_issues)) or [
            m.group(1) for msg in messages if (m := _REQUIRES.match(msg))
        ]
    return LogFacts(
        exception_type=exc,
        error_category=category,
        suspect_mod_ids=list(dict.fromkeys(s.lower() for s in suspects))[:5],
        mc_version=raw.minecraft_version,
        loader_version=raw.neoforge_version,
        java_version=raw.java_version,
    )


# --------------------------------------------------------------------------- extraction


def extract_facts(llm: LLM, pre: Preprocessed, full_text: str) -> ExtractionResult:
    """LLM extraction with one repair retry, whole-token check on the ids, and a regex fallback."""
    messages = [
        {"role": "system", "content": EXTRACT_SYSTEM},
        {"role": "user", "content": f"Log:\n{pre.text}\n\nReturn the JSON object."},
    ]
    errors: list[str] = []
    source: Source = "llm"
    facts: LogFacts | None = None
    reply = None
    for attempt in range(2):
        reply = llm.chat(messages, prompt_version=EXTRACT_PROMPT_VERSION, max_tokens=400).content
        try:
            facts = LogFacts.model_validate(parse_json_object(reply))
            break
        except (ValueError, ValidationError) as exc:  # json.JSONDecodeError is a ValueError
            errors.append(f"attempt {attempt + 1}: {str(exc)[:300]}")
            messages = messages + [
                {"role": "assistant", "content": reply or ""},
                {
                    "role": "user",
                    "content": f"That reply was invalid: {str(exc)[:300]}\nReturn ONLY the corrected JSON object.",
                },
            ]
            source = "llm_repaired"
    if facts is None:
        return ExtractionResult(regex_facts(pre.facts), "regex_fallback", errors=errors)

    kept = [m for m in facts.suspect_mod_ids if is_whole_token_in(m, full_text)]
    dropped = [m for m in facts.suspect_mod_ids if m not in kept]
    facts = facts.model_copy(update={"suspect_mod_ids": kept})
    return ExtractionResult(facts, source, dropped_ids=dropped, errors=errors)
