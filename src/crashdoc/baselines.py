"""Diagnosis baselines B0 and B1 (PLAN 7.2). Neither uses retrieval.

B1 is one fixed rule, applied to every log and never tuned: the first mod in "Suspected Mods", else the mod named in
the FML loading-error line, else null. It names the mod that REPORTS a problem ("Mod A requires B" names A), so it is
expected to "blame the victim" on missing-dependency logs; the strict metric shows that.

B0 is one LLM call on the preprocessed log, no retrieval.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from pydantic import ValidationError

from crashdoc.extraction import is_whole_token_in, parse_json_object
from crashdoc.llm import LLM
from crashdoc.preprocess import Preprocessed, RawLogFacts

B0_PROMPT_VERSION = "b0-v1"

_MOD_IN_ERROR = re.compile(r"^Mod ([A-Za-z0-9_]+) ")
_JAR_IN_ERROR = re.compile(r"File (?:\S*[\\/])?([A-Za-z][A-Za-z_]*)\S*\.jar is not a valid mod file")


def b1_predict(raw: RawLogFacts) -> str | None:
    """Suspected Mods first, else the mod named in the first FML loading error, else None."""
    if raw.suspected_mods:
        return raw.suspected_mods[0]
    messages = raw.fml_errors or [i.failure_message or "" for i in raw.loading_issues]
    for message in messages:
        if m := _MOD_IN_ERROR.match(message) or _JAR_IN_ERROR.search(message):
            return m.group(1).lower()
    for issue in raw.loading_issues:  # a crash report's "Mod loading issue for: X" block names X directly
        if issue.mod_id:
            return issue.mod_id.lower()
    return None


B0_SYSTEM = """You diagnose Minecraft NeoForge 1.21.1 crashes from a crash report or log. Reply with ONE JSON object only:
{"culprit_mod_id": the lowercase id of the mod whose fault caused the failure, or null if no mod is at fault,
 "category": one of "missing_dependency", "version_mismatch", "out_of_memory", "mixin_conflict", "other",
 "explanation": one or two sentences}
Label the CAUSE, not the symptom. For a missing dependency the culprit is the MISSING mod, not the mods that need it.
A jar skipped for the wrong version or loader is "version_mismatch". Out of memory has no culprit mod.
Only use mod ids that literally appear in the log."""


@dataclass
class B0Result:
    culprit: str | None
    category: str | None
    explanation: str
    valid: bool  # False if the reply could not be parsed even after one repair


def b0_predict(llm: LLM, pre: Preprocessed, full_text: str) -> B0Result:
    messages = [
        {"role": "system", "content": B0_SYSTEM},
        {"role": "user", "content": f"Log:\n{pre.text}\n\nReturn the JSON object."},
    ]
    for _ in range(2):  # one repair retry, as for extraction
        reply = llm.chat(messages, prompt_version=B0_PROMPT_VERSION, max_tokens=300).content
        try:
            obj = parse_json_object(reply)
            culprit = obj.get("culprit_mod_id")
            culprit = str(culprit).strip().lower() if culprit not in (None, "", "null") else None
            if culprit is not None and not is_whole_token_in(culprit, full_text):
                culprit = None  # a mod id that is not in the log is a hallucination
            category = obj.get("category")
            return B0Result(culprit, str(category) if category else None, str(obj.get("explanation", ""))[:500], True)
        except (ValueError, ValidationError) as exc:
            messages = messages + [
                {"role": "assistant", "content": reply or ""},
                {"role": "user", "content": f"That reply was invalid: {str(exc)[:200]}\nReturn ONLY the JSON object."},
            ]
    return B0Result(None, None, "", False)
