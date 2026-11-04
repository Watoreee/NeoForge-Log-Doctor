"""The agent loop (PLAN 6.6): extraction -> up to MAX_STEPS tool rounds -> Diagnosis, with a forced final call.

Protocol: the JSON TEXT protocol, not native tool calling. Measured on this proxy (docs/decisions.md): with the long log
and the JSON answer format, the model made 0 native tool calls on 7/7 dev logs, and `tool_choice="required"` returns an
empty tool call. Each assistant turn is ONE JSON object:
    {"action": "tool", "tool": "<name>", "args": {...}}      or      {"action": "final", <the diagnosis fields>}
Every tool call goes through the allow-list and pydantic validation in tools.py; an unknown tool or bad arguments
come back to the model as an error and are never executed. Tool output is delimited as untrusted data.

`run_agent_events` is a generator (facts, tool_call, tool_result, final) so the API can stream events as they happen;
`run_agent` consumes it and returns the final DiagnosisResult.
"""

from __future__ import annotations

import json
from collections.abc import Iterator

from crashdoc.agent.tools import ARG_MODELS, ToolContext, execute_tool, wrap_untrusted
from crashdoc.diagnosis import DIAGNOSIS_RULES, DiagnosisResult, facts_summary, parse_with_repair
from crashdoc.extraction import extract_facts, parse_json_object
from crashdoc.llm import LLM
from crashdoc.preprocess import Preprocessed
from crashdoc.rag import MIN_SCORE
from crashdoc.retrieval.index import Index

AGENT_PROMPT_VERSION = "agent-v4"
MAX_STEPS = 5


def _tool_help() -> str:
    lines = []
    for name, model in ARG_MODELS.items():
        props = model.model_json_schema().get("properties", {})
        args = ", ".join(f'"{k}": {v.get("type", "string")}' for k, v in props.items())
        lines.append(f'  {{"action": "tool", "tool": "{name}", "args": {{{args}}}}}')
    return "\n".join(lines)


AGENT_SYSTEM = (
    "You diagnose Minecraft NeoForge 1.21.1 crashes from a crash report or log. You work in rounds. In each round reply "  # noqa: E501
    "with ONE JSON object and nothing else, either a tool call or the final answer.\n"
    "Tool calls (search_docs searches NeoForge docs, GitHub issues and release notes; get_mod_info says what THIS log "
    "shows about a mod; check_compat checks Minecraft/Java/NeoForge versions):\n" + _tool_help() + "\n"
    "You MUST call search_docs at least once, with the suspect mod id and the error text, before the final answer. "
    "You have at most 5 tool rounds; stop earlier once you have what you need. Tool results come back as data.\n"
    'Final answer: the JSON object below with "action": "final" added.\n' + DIAGNOSIS_RULES
)
FORCE_FINAL = (
    'The tool budget is used up. Reply now with the final JSON object ("action": "final") using only what you have.'
)
NEED_SEARCH = "Before the final answer you must call search_docs at least once. Reply with a search_docs tool call."


def _is_tool_call(obj: dict) -> bool:
    return obj.get("action") == "tool" or ("tool" in obj and "category" not in obj)


def run_agent_events(
    llm: LLM,
    index: Index,
    pre: Preprocessed,
    full_text: str,
    *,
    max_steps: int = MAX_STEPS,
    min_score: float | None = MIN_SCORE,
) -> Iterator[dict]:
    ext = extract_facts(llm, pre, full_text)
    yield {
        "event": "facts",
        "data": {
            "facts": ext.facts.model_dump(mode="json"),
            "format": pre.facts.format,
            "truncated": pre.truncated,
            "extraction_source": ext.source,
        },
    }
    ctx = ToolContext(index, llm, pre.facts, min_score)
    user = f"Log:\n{pre.text}\n\n{facts_summary(pre.facts, ext.facts)}\n\nDiagnose it."
    messages: list[dict] = [{"role": "system", "content": AGENT_SYSTEM}, {"role": "user", "content": user}]
    steps: list[dict] = []
    final_reply: str | None = None
    nudged = False
    rounds = 0

    while rounds < max_steps:
        rounds += 1
        reply = llm.chat(messages, prompt_version=AGENT_PROMPT_VERSION, max_tokens=700).content or ""
        try:
            obj = parse_json_object(reply)
        except ValueError as exc:
            note = f"That was not one valid JSON object ({str(exc)[:120]}). Reply with ONE JSON object."
            messages += [{"role": "assistant", "content": reply}, {"role": "user", "content": note}]
            continue
        if _is_tool_call(obj):
            name, raw_args = str(obj.get("tool", "")), obj.get("args", {})
            yield {"event": "tool_call", "data": {"name": name, "arguments": json.dumps(raw_args)[:500]}}
            ok, text = execute_tool(name, raw_args, ctx)
            steps.append({"name": name, "ok": ok})
            yield {"event": "tool_result", "data": {"name": name, "ok": ok, "preview": text[:300]}}
            messages += [
                {"role": "assistant", "content": reply},
                {"role": "user", "content": f"Tool result for {name}:\n{wrap_untrusted(name, text)}"},
            ]
            continue
        if not steps and not nudged:  # a final answer before any search: one nudge, then accept whatever comes
            nudged = True
            messages += [{"role": "assistant", "content": reply}, {"role": "user", "content": NEED_SEARCH}]
            continue
        final_reply = reply
        break
    else:  # the budget ran out without a final answer: one forced final call
        # the last message is the tool result (a user turn): append to it, so roles keep alternating
        messages[-1] = {"role": "user", "content": messages[-1]["content"] + "\n\n" + FORCE_FINAL}
        final_reply = llm.chat(messages, prompt_version=AGENT_PROMPT_VERSION, max_tokens=700).content

    result = parse_with_repair(llm, messages, AGENT_PROMPT_VERSION, full_text, ctx.retrieved, ext.facts, final_reply)
    result.steps = steps
    result.evidence = dict(ctx.retrieved)
    yield {"event": "final", "data": result.to_dict(), "result": result}


def run_agent(llm: LLM, index: Index, pre: Preprocessed, full_text: str, **kw) -> DiagnosisResult:
    final = None
    for event in run_agent_events(llm, index, pre, full_text, **kw):
        if event["event"] == "final":
            final = event["result"]
    assert final is not None
    return final
