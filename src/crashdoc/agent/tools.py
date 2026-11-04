"""Agent tools (PLAN 6.6): search_docs, get_mod_info, check_compat.

Safety rules, enforced here and tested:
- an allow-list: a tool name not in TOOL_NAMES is answered with an error and never executed;
- arguments are validated with pydantic (extra keys forbidden); bad JSON or bad args -> an error, never executed;
- every tool result is wrapped in <untrusted_data> and the closing tag is defanged inside it;
- `search_docs` records every document it returns in `ctx.retrieved`, so the retrieved set the citations are
  checked against is the union of all search_docs results.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from crashdoc.agent.compat_table import check_compat
from crashdoc.diagnosis import Evidence
from crashdoc.llm import LLM
from crashdoc.preprocess import RawLogFacts
from crashdoc.rag import MIN_SCORE, retrieve_evidence
from crashdoc.retrieval.index import Index

MAX_RESULT_CHARS = 3000


class SearchDocsArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str = Field(min_length=2, max_length=300, description="what to look for: mod id, error text, exception")
    k: int = Field(default=4, ge=1, le=6, description="how many documents to return")


class GetModInfoArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")
    mod_id: str = Field(pattern=r"^[A-Za-z][A-Za-z0-9_\-]{1,63}$", description="mod id as written in the log")


class CheckCompatArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")
    minecraft_version: str | None = Field(default=None, max_length=32)
    java_version: str | None = Field(default=None, max_length=32)
    neoforge_version: str | None = Field(default=None, max_length=32)


ARG_MODELS: dict[str, type[BaseModel]] = {
    "search_docs": SearchDocsArgs,
    "get_mod_info": GetModInfoArgs,
    "check_compat": CheckCompatArgs,
}
TOOL_NAMES = frozenset(ARG_MODELS)
_DESCRIPTIONS = {
    "search_docs": "Search the corpus of NeoForge docs, GitHub issues and release notes. Returns documents with ids.",
    "get_mod_info": "What THIS log says about one mod: loaded or not, version, who requires it, errors that name it.",
    "check_compat": "Check Minecraft / Java / NeoForge version compatibility (defaults to the versions in the log).",
}


def tool_specs() -> list[dict[str, Any]]:
    """OpenAI-style tool definitions, generated from the pydantic models so schema and validation cannot drift."""
    specs = []
    for name, model in ARG_MODELS.items():
        schema = model.model_json_schema()
        schema.pop("title", None)
        specs.append(
            {"type": "function", "function": {"name": name, "description": _DESCRIPTIONS[name], "parameters": schema}}
        )
    return specs


@dataclass
class ToolContext:
    index: Index
    llm: LLM
    raw: RawLogFacts
    min_score: float | None = MIN_SCORE
    retrieved: dict[str, str] = field(default_factory=dict)  # doc_id -> excerpt: union of all search_docs results
    titles: dict[str, str] = field(default_factory=dict)


def wrap_untrusted(tool: str, text: str) -> str:
    """Delimit tool output as data. The closing tag is removed from the content so it cannot end the block early."""
    body = re.sub(r"</?untrusted_(?:data|document)[^>]*>", "[tag removed]", text)[:MAX_RESULT_CHARS]
    return f'<untrusted_data tool="{tool}">\n{body}\n</untrusted_data>'


def execute_tool(name: str, raw_args: str | dict | None, ctx: ToolContext) -> tuple[bool, str]:
    """Run one tool call. Returns (ok, text). Unknown tools and invalid args are errors that are NOT executed."""
    if name not in TOOL_NAMES:
        return False, f"error: unknown tool {name!r}. Allowed tools: {sorted(TOOL_NAMES)}"
    try:
        data = json.loads(raw_args) if isinstance(raw_args, str) and raw_args.strip() else (raw_args or {})
        if not isinstance(data, dict):
            raise ValueError("arguments must be a JSON object")
        args = ARG_MODELS[name].model_validate(data)
    except (ValueError, ValidationError) as exc:
        return False, f"error: invalid arguments for {name}: {str(exc)[:300]}"
    return True, _RUNNERS[name](args, ctx)


def _search_docs(args: SearchDocsArgs, ctx: ToolContext) -> str:
    evidence, abstained = retrieve_evidence(ctx.index, ctx.llm, args.query, k=args.k, min_score=ctx.min_score)
    if not evidence:
        return "no documents found" + (" (nothing scored above the relevance floor)" if abstained else "")
    lines = []
    for e in evidence:
        ctx.retrieved.setdefault(e.doc_id, e.excerpt)
        ctx.titles.setdefault(e.doc_id, e.title)
        lines.append(f"doc_id: {e.doc_id}\ntitle: {e.title}\nexcerpt: {e.excerpt}")
    return "\n\n".join(lines)


def _get_mod_info(args: GetModInfoArgs, ctx: ToolContext) -> str:
    mod = args.mod_id.lower()
    raw = ctx.raw
    out = [f"mod_id: {mod}"]
    version = raw.mod_versions.get(mod)
    out.append(f"loaded: yes, version {version}" if version else "loaded: not in this log's mod list")
    needs = [d for d in raw.dependency_issues if d.mod_id == mod]
    if needs:
        out.append(
            "required by: " + ", ".join(sorted({d.requested_by for d in needs})) + f" (actual: {needs[0].actual})"
        )
    asks = [d for d in raw.dependency_issues if d.requested_by == mod]
    if asks:
        out.append("itself requires: " + ", ".join(f"{d.mod_id} {d.expected}" for d in asks[:5]))
    msgs = [m for m in raw.fml_errors if re.search(rf"(?<![\w-]){re.escape(mod)}(?![\w-])", m, re.IGNORECASE)]
    if msgs:
        out.append("loading errors naming it: " + " | ".join(msgs[:3]))
    if mod in raw.mixin_mods:
        out.append("a mixin of this mod failed to prepare")
    if any(mod in f.lower() for f in raw.invalid_mod_files):
        out.append("its jar was rejected as not a valid mod file")
    return "\n".join(out)


def _check_compat(args: CheckCompatArgs, ctx: ToolContext) -> str:
    mc = args.minecraft_version or ctx.raw.minecraft_version
    java = args.java_version or ctx.raw.java_version
    loader = args.neoforge_version or ctx.raw.neoforge_version
    return json.dumps({"minecraft": mc, "java": java, "neoforge": loader, **check_compat(mc, java, loader)})


_RUNNERS = {"search_docs": _search_docs, "get_mod_info": _get_mod_info, "check_compat": _check_compat}


def evidence_list(ctx: ToolContext) -> list[Evidence]:
    return [Evidence(d, ctx.titles.get(d, ""), ex) for d, ex in ctx.retrieved.items()]
