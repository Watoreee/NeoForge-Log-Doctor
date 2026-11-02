"""Truncation, extraction (+ repair, hallucination check, fallback), retrieval + floor, queries, metrics, B1, B0."""

from __future__ import annotations

import json
from dataclasses import dataclass

import numpy as np
import pytest

from crashdoc.baselines import b0_predict, b1_predict
from crashdoc.config import LOG_TOKEN_BUDGET, REPO_ROOT
from crashdoc.extraction import (
    LogFacts,
    extract_facts,
    is_whole_token_in,
    parse_json_object,
    regex_facts,
)
from crashdoc.preprocess import parse_log, preprocess_log
from crashdoc.retrieval.index import Hit, Index, top_docs
from crashdoc.retrieval.query import build_query, embedding_input, oracle_facts
from crashdoc.schemas import Category, GoldLabel
from eval.metrics import score, summarize

GOLD = REPO_ROOT / "data" / "gold"


def gold_text(name: str) -> str:
    return next(p for p in GOLD.rglob(f"{name}.*") if p.suffix != ".json").read_text(encoding="utf-8")


def label(**kw) -> GoldLabel:
    base = dict(
        log_id="x",
        scenario_id="s",
        source_file_type="latest_log",
        culprit_mod_id="curios",
        acceptable_culprits=["curios", "ars_nouveau"],
        category="missing_dependency",
    )
    return GoldLabel(**{**base, **kw})


# --- truncation ----------------------------------------------------------------------------------


def test_short_log_is_sent_whole():
    text = "[17:37:04] [main/INFO]: a\n[17:37:05] [main/WARN]: b\n[17:37:06] [main/ERROR]: c\n"
    pre = preprocess_log(text)
    assert pre.text == text and not pre.truncated


@pytest.mark.parametrize("name", ["r01_latest", "r04_latest", "r06_latest", "r10_latest", "r17_crash", "r14_latest"])
def test_long_real_logs_fit_the_budget_and_keep_the_culprit(name):
    text = gold_text(name)
    label_path = next(p for p in GOLD.rglob(f"{name}.json"))
    culprit = json.loads(label_path.read_text(encoding="utf-8"))["culprit_mod_id"]
    pre = preprocess_log(text)
    assert pre.tokens <= LOG_TOKEN_BUDGET + 50  # header is not counted against line selection
    if culprit:
        assert culprit in pre.text.lower()


def test_truncation_drops_the_mod_list_and_keeps_exception_with_frames():
    pre = preprocess_log(gold_text("r14_latest"))
    assert "Cobblemon Raid Dens 0.10.0" not in pre.text  # mod list row
    assert "NullPointerException" in pre.text and "isModAndNewerThan" in pre.text


# --- JSON + whole-token helpers ---------------------------------------------------------------------


def test_parse_json_object_strips_a_markdown_fence():
    assert parse_json_object('```json\n{"a": 1}\n```') == {"a": 1}
    assert parse_json_object('Sure! {"a": 1} hope that helps') == {"a": 1}
    for bad in ("", "no json here", "[1, 2]"):
        with pytest.raises(ValueError):
            parse_json_object(bad)


def test_whole_token_check_does_not_match_inside_other_words():
    assert is_whole_token_in("ae2", "Mod ID: 'ae2', Requested by")
    assert not is_whole_token_in("ae2", "the tae2x thing")
    assert not is_whole_token_in("jei", "C:\\mods\\jeiextras-1.0.jar")
    assert is_whole_token_in("create", "mods/Create/x")  # case-insensitive


# --- extraction ------------------------------------------------------------------------------------


@dataclass
class FakeReply:
    content: str


class FakeLLM:
    """Replays canned replies; records the messages it was sent."""

    def __init__(self, *replies: str):
        self.replies, self.calls = list(replies), []

    def chat(self, messages, **kw):
        self.calls.append(messages)
        return FakeReply(self.replies.pop(0))


LOG = (
    "[17:37:04] [main/INFO]: a\n[17:37:05] [main/ERROR]: Mod ID: 'curios', Requested by: 'ars_nouveau', "
    "Expected range: '[1,)', Actual version: '[MISSING]'\n[17:37:06] [main/INFO]: c\n"
)


def test_extraction_valid_reply_and_hallucinated_ids_are_dropped():
    reply = json.dumps(
        {
            "exception_type": None,
            "error_category": "missing_dependency",
            "suspect_mod_ids": ["Curios", "madeupmod"],
            "mc_version": "1.21.1",
        }
    )
    out = extract_facts(FakeLLM("```json\n" + reply + "\n```"), preprocess_log(LOG), LOG)
    assert out.source == "llm" and out.facts.suspect_mod_ids == ["curios"] and out.dropped_ids == ["madeupmod"]
    assert out.facts.error_category == Category.MISSING_DEPENDENCY


def test_extraction_repairs_once_and_feeds_back_the_error():
    llm = FakeLLM(
        '{"error_category": "not_a_category"}', '{"error_category": "version_mismatch", "suspect_mod_ids": []}'
    )
    out = extract_facts(llm, preprocess_log(LOG), LOG)
    assert out.source == "llm_repaired" and out.facts.error_category == Category.VERSION_MISMATCH
    assert "invalid" in llm.calls[1][-1]["content"] and len(llm.calls) == 2


def test_extraction_falls_back_to_regex_facts_after_a_failed_repair():
    out = extract_facts(FakeLLM("nonsense", "still nonsense"), preprocess_log(LOG), LOG)
    assert out.source == "regex_fallback" and len(out.errors) == 2
    assert out.facts.error_category == Category.MISSING_DEPENDENCY and out.facts.suspect_mod_ids == ["curios"]


def test_regex_facts_on_real_logs():
    assert regex_facts(parse_log(gold_text("r10_latest"))).error_category == Category.OUT_OF_MEMORY
    f = regex_facts(parse_log(gold_text("r14_latest")))
    assert f.error_category == Category.MIXIN_CONFLICT and f.suspect_mod_ids == ["cobblemonraiddens"]
    f = regex_facts(parse_log(gold_text("r15_latest")))
    assert f.error_category == Category.VERSION_MISMATCH and f.suspect_mod_ids == ["aquaculture"]
    assert regex_facts(parse_log(gold_text("r06_latest"))).suspect_mod_ids == ["ironfurnaces"]


def test_logfacts_tolerates_nulls_and_missing_fields():
    f = LogFacts.model_validate({"suspect_mod_ids": None, "exception_type": None})
    assert f.suspect_mod_ids == [] and f.error_category is None


# --- retrieval ----------------------------------------------------------------------------------------


def tiny_index() -> Index:
    chunks = [
        {"chunk_id": "d1#0", "doc_id": "d1", "title": "missing mod", "text": "curios is not installed"},
        {"chunk_id": "d1#1", "doc_id": "d1", "title": "missing mod", "text": "install the api"},
        {"chunk_id": "d2#0", "doc_id": "d2", "title": "heap", "text": "OutOfMemoryError java heap space xmx"},
        {"chunk_id": "d3#0", "doc_id": "d3", "title": "mixin", "text": "mixin apply failed"},
    ]
    emb = np.eye(4, dtype=np.float32)  # chunk i is exactly axis i, so cosines are easy to predict
    return Index(chunks, emb)


def test_dense_search_ranks_by_cosine_and_floor_drops_below_threshold():
    ix = tiny_index()
    q = np.array([0.9, 0.1, 0, 0], dtype=np.float32)
    hits = ix.search("dense", query_vec=q, k=4).hits
    assert [h.chunk_id for h in hits][:2] == ["d1#0", "d1#1"]
    floored = ix.search("dense", query_vec=q, k=4, min_score=0.5)
    assert [h.chunk_id for h in floored.hits] == ["d1#0"] and not floored.abstained


def test_floor_that_removes_everything_abstains():
    ix = tiny_index()
    flat = np.array([1, 1, 1, 1], dtype=np.float32)  # cosine 0.5 to every chunk
    r = ix.search("hybrid", query_text="curios", query_vec=flat, k=4, min_score=0.9)
    assert r.abstained and r.hits == []


def test_no_floor_never_abstains_and_bm25_only_candidates_dropped_by_floor_are_reported():
    ix = tiny_index()
    q = np.array([0, 0, 1, 0], dtype=np.float32)  # dense points at the heap doc
    assert not ix.search("hybrid", query_text="curios", query_vec=q, k=1).abstained
    r = ix.search("hybrid", query_text="curios", query_vec=q, k=1, min_score=0.5)
    assert [h.chunk_id for h in r.hits] == ["d2#0"]  # d1#0 was found by BM25 only, cosine 0 < floor
    assert [h.chunk_id for h in r.dropped_bm25_only] == ["d1#0"]


def test_hybrid_fuses_both_rankings_and_bm25_requires_a_term_match():
    ix = tiny_index()
    q = np.array([0, 0, 1, 0], dtype=np.float32)
    ids = [h.chunk_id for h in ix.search("hybrid", query_text="curios", query_vec=q, k=3).hits]
    assert set(ids) >= {"d1#0", "d2#0"}
    assert ix.search("bm25", query_text="zzzz nothing", k=3).hits == []  # BM25 score 0 -> no candidates


def test_search_argument_errors():
    ix = tiny_index()
    with pytest.raises(ValueError):
        ix.search("dense")
    with pytest.raises(ValueError):
        ix.search("bm25", query_text="curios", min_score=0.3)


def test_top_docs_deduplicates_by_doc_and_keeps_best_chunk():
    hits = [
        Hit("d1#1", "d1", 0.9, 0.9, True, False),
        Hit("d1#0", "d1", 0.8, 0.8, True, False),
        Hit("d2#0", "d2", 0.7, 0.7, True, False),
    ]
    docs = top_docs(hits, 5)
    assert [d.doc_id for d in docs] == ["d1", "d2"] and docs[0].best_chunk_id == "d1#1"
    assert len(top_docs(hits, 1)) == 1


def test_real_index_loads_and_a_self_query_finds_itself():
    ix = Index.load()
    manifest = json.loads((REPO_ROOT / "data" / "processed" / "manifest.json").read_text(encoding="utf-8"))
    assert len(ix.chunks) == len(ix.emb) == sum(d["n_chunks"] for d in manifest)
    top = ix.search("dense", query_vec=ix.emb[7], k=3).hits[0]
    assert top.chunk_id == ix.chunks[7]["chunk_id"] and top.cos > 0.99


# --- queries ---------------------------------------------------------------------------------------------


def test_query_templates_a_b_c():
    extracted = LogFacts(
        exception_type="java.lang.NullPointerException", error_category=Category.OTHER, suspect_mod_ids=["wrongmod"]
    )
    assert build_query(extracted) == "java.lang.NullPointerException wrongmod"
    gold = label()
    oracle = oracle_facts(extracted, gold)
    assert oracle.suspect_mod_ids == ["curios", "ars_nouveau"] and oracle.error_category == Category.MISSING_DEPENDENCY
    assert oracle.exception_type == "java.lang.NullPointerException"  # kept from extraction
    assert "missing dependency" in build_query(oracle)
    assert (
        oracle_facts(
            extracted, label(culprit_mod_id=None, acceptable_culprits=[], category="out_of_memory")
        ).suspect_mod_ids
        == []
    )
    assert len(embedding_input("x" * 10_000)) == 6_000


# --- metrics + baselines -------------------------------------------------------------------------------------


def test_strict_and_lenient_culprit_metrics_differ_on_victims():
    gold = label()
    assert score("l", "curios", "missing_dependency", gold).strict
    victim = score("l", "ars_nouveau", "missing_dependency", gold)
    assert victim.lenient and not victim.strict  # the case lenient alone would hide
    assert not score("l", "other", None, gold).lenient and not score("l", None, None, gold).lenient


def test_null_culprit_logs_need_a_null_prediction_under_both_metrics():
    oom = label(culprit_mod_id=None, acceptable_culprits=[], category="out_of_memory")
    assert score("l", None, "out_of_memory", oom).strict and score("l", "", "out_of_memory", oom).lenient
    assert not score("l", "create", "out_of_memory", oom).strict


def test_summary_reports_counts_with_logs_and_scenarios():
    rows = [
        score("a", "curios", "missing_dependency", label(scenario_id="s1")),
        score("b", "ars_nouveau", "missing_dependency", label(scenario_id="s1")),
        score("c", "x", "other", label(scenario_id="s2")),
    ]
    s = summarize(rows)
    assert (s["n_logs"], s["n_scenarios"], s["culprit_strict"], s["culprit_lenient"], s["category"]) == (
        3,
        2,
        "1/3",
        "2/3",
        "2/3",
    )


def test_b1_rule_on_real_logs_names_the_requester_not_the_missing_mod():
    assert b1_predict(parse_log(gold_text("r01_latest"))) == "ars_nouveau"  # the victim; gold culprit is curios
    assert b1_predict(parse_log(gold_text("r01_crash"))) == "ars_nouveau"
    assert b1_predict(parse_log(gold_text("r06_latest"))) == "ironfurnaces"
    assert b1_predict(parse_log(gold_text("r10_latest"))) is None


def test_b0_validates_and_drops_a_culprit_that_is_not_in_the_log():
    ok = b0_predict(
        FakeLLM('{"culprit_mod_id": "curios", "category": "missing_dependency", "explanation": "x"}'),
        preprocess_log(LOG),
        LOG,
    )
    assert ok.culprit == "curios" and ok.valid
    fake = b0_predict(FakeLLM('{"culprit_mod_id": "ghost", "category": "other"}'), preprocess_log(LOG), LOG)
    assert fake.culprit is None
    bad = b0_predict(FakeLLM("x", "y"), preprocess_log(LOG), LOG)
    assert not bad.valid
