# Report notes (skeleton for PLAN 9)

Every number here comes from `eval/results/*.json`, rebuilt by `python scripts/report_tables.py --split test|dev`
(and printed by `run_eval.py` / `run_retrieval_eval.py`). Test numbers: `diagnosis_test_2026-11-05T083345+0000_25417e4.json`
and `retrieval_test_2026-11-05T083402+0000_25417e4.json`. Intervals are 95%, scenario-level paired bootstrap
(1,000 resamples, seed 0): logs of one scenario are resampled together.

**Provenance.** The code was built with Claude Code from a written plan (`PLAN.md`), and the author reviewed it.

**Setup in one paragraph.** Test split: 25 logs from 14 scenarios (r10 and r11 are one scenario). Dev: 7 logs from 4
scenarios. Culprit accuracy is **strict** (prediction equals `culprit_mod_id`) and **lenient** (prediction is in
`acceptable_culprits`). B0 = the LLM alone. B1 = a regex heuristic. RAG-1 = extraction, retrieval, one diagnosis call.
Agent = the same with an allow-listed tool loop (max 5 steps). All use Gemma at temperature 0.
HTTP and UI are not evaluated.

## Findings

### 1. The LLM beats the B1 heuristic
Test, strict culprit: B0 **17/25 (68%)**, B1 **7/25 (28%)**. B0 minus B1 = +0.400 of logs, CI [+0.125, +0.720], which
excludes 0. B1 typically names a mod that *reports* a missing dependency (r01: `ars_nouveau` for `curios`; r17:
`cobblefurnies` for `architectury`; r16: `betterstrongholds` for `yungsapi`) or nothing at all (`None` on r04_latest,
r14_latest and r20_latest, where gold has a culprit; it is right to say `None` on r10 and r11, the out-of-memory logs). On dev they tie at 4/7, which says nothing with 4 scenarios.

### 2. Query construction (a) vs (b) is the measured improvement
Document-level retrieval on the 18 test logs (9 scenarios) that have relevant documents, hybrid (BM25 + dense, RRF):
(a) the preprocessed log as the query, recall@5 **0.167** (6/18 hit@5); (b) a query built from the extracted fields
(exception type, suspect mod ids, category keywords), recall@5 **0.597** (13/18 hit@5). Difference **+0.431**,
CI **[+0.222, +0.681]**, excludes 0. MRR 0.208 to 0.455. BM25 on the raw log (B2) is the worst: recall@5 0.028 (1/18).
Caveat: dev alone (3 logs, 2 scenarios) gives +0.333, CI [0.000, 0.500], too small to confirm anything. The test result
is the evidence. Query (b) uses the LLM's extraction, so this is also a measure of extraction quality.

### 3. B0, RAG-1 and the agent are within noise: no claim that retrieval or the agent improves diagnosis
Test, 25 logs:

| Condition | culprit strict | culprit lenient | category |
|---|---|---|---|
| B0 | 17/25 (68%) | 19/25 (76%) | 19/25 |
| RAG-1 | 18/25 (72%) | 18/25 (72%) | 19/25 |
| Agent | 19/25 (76%) | 20/25 (80%) | 19/25 |

RAG-1 minus B0 +0.040, CI [+0.000, +0.120]; Agent minus B0 +0.080, CI [+0.000, +0.192]; Agent minus RAG-1 +0.040,
CI [+0.000, +0.120]. Every interval touches 0 at its lower end. One or two logs decide each difference. Category
accuracy is identical (19/25) in all three. Do not write "retrieval helps" or "the agent helps". The only effect
retrieval has is on **citations**: 14/25 logs carry a citation in both RAG-1 (14/14 valid) and the agent (14/15 valid;
the one invalid id was dropped by the validity check on r09_latest). The agent searched about once per log (26 tool
calls on 25 logs), and the prompt requires one search, so it behaves as a RAG-1 with an extra turn.

### 4. The oracle is not an upper bound
(c) = LLM exception type + gold `acceptable_culprits` + gold category keywords. (c2) = gold `culprit_mod_id` + gold
category + the parser's regex exception type (no LLM output). Test recall@5: (b) 0.597, (c) 0.458, (c2) 0.458.
(c) minus (b) = **-0.139**, CI [-0.292, -0.014]; (c2) minus (b) = -0.139, CI [-0.292, -0.028]. Both oracles are
significantly *worse* than the extracted query. Giving the retriever the right answer does not make its query better:
gold mod ids are not the words the relevant issues use, and a bare mod id is a weak query. Do not describe (c) or (c2)
as "perfect extraction" or as a ceiling. Also note (b) uses the LLM exception type, (c2) uses the regex one, so (c2)
differs from (b) in the exception source as well as the gold fields. On dev, (c) scored 1.000 and (c2) 0.667 on three
logs: another reason not to read dev.

### 5. Abstention failed
The cosine floor (`min_score = 0.45`, chosen on dev) never fired where it should have: abstention recall **0/7** on
the `none_found` test logs, specificity 18/18 (it never wrongly abstained, because it never abstained). Max cosine of
`none_found` logs 0.535 to 0.647; for logs with relevant documents 0.618 to 0.787. The ranges overlap, and the dev
`none_found` logs scored *higher* than the dev logs with relevant documents. A similarity floor does not detect
"nothing in the corpus is relevant". On those 7 logs the agent cited nothing in all 7 and RAG-1 cited something in 1
(`r04_latest`), but the agent still diagnosed all 7 with `high` confidence, so this is not abstention. **Confidence is
useless**: the agent said `high` on all 7, and on all 6 of its strict-culprit misses.

### 6. Tuning
The **RAG-1 prompt (`rag1-v1`) was not tuned**. The **agent prompt (`agent-v4`) was tuned on dev only**
(v1 to v3 were attempts at native tool calling, abandoned: 0 tool calls on 7/7 dev logs, see `decisions.md`). The
agent had more tuning than RAG-1, and on a dev set of 7 logs, which makes its small edge over RAG-1 weaker, not
stronger.

### 7. Dev is thin
7 logs, 4 scenarios; only 2 scenarios (r02, r13) have relevant documents (3 logs); the other two (r15, r18) are
`none_found`. Choices made on dev (`min_score`, query design, the agent prompt) are weakly supported, and dev
bootstrap intervals collapse to a point (0.000 to 0.000 on every diagnosis comparison).

### 8. Labels were corrected after the first test run
Twice, both after test results had been seen, both documented in `decisions.md` with before and after numbers:
(i) **r04**: the acceptable list dropped `cloth_config` (the log shows it loaded). No number changed.
(ii) **r14**: `mixin_conflict` changed to `other` (the log shows one plugin crashing on a missing mod, not two mixins
conflicting). B0, RAG-1 and the agent each lost one on category accuracy on test (20/25 to 19/25) because they said
`mixin_conflict`; culprit and retrieval numbers did not change. Side effect: **no log has the category
`mixin_conflict` any more**, so it is never evaluated. Test runs per condition: retrieval, B0 and B1 ran three times on the test split
(initial, after the r04 fix, after the r14 fix); RAG-1 and the agent ran twice (their first test run was the second pass). The numbers reported are from the last run and are label-corrected, not tuned.

### 9. Single pack; corpus extended after the logs were collected
All logs come from one modpack (ATMons) with injected faults, collected by one person. The corpus was extended with 7
repositories after the logs existed (before any judgment or test result) so that recall is measured with the right
repository present. Culprits with no tracker in the corpus (simpletms, cobblemonraiddens, sophisticatedcore,
ftbquests, cobblemon) are `none_found` scenarios: they test abstention, not retrieval. Cobblemon's own issue tracker
(GitLab) is not in the corpus.

### 10. Relevance labels were made by an LLM; 8 checked by the author, 30 by a second LLM pass
An LLM (Claude) judged each pooled document from its title and one excerpt; the human reviewed the unsure ones and
did not open every URL. **8 documents were checked by the author; 30 more were checked by a second LLM pass, which
agreed with 26/30** (15 ticked, 15 unticked, seed 42, `data/spotcheck.md`, `python scripts/score_spotcheck.py`). All 4
disagreements are ticked documents whose title matches the failure but whose cause differs (ExtendedAE #422 for r13;
architectury-api #542 for r03; #528 and #664 for r17). The author kept the labels, so the reported retrieval numbers
use them as they are. A second LLM pass is not a human check. The pool holds only the top 5 of six conditions, so
retrieval metrics have pooling bias and inherit any labelling error.

## Groundedness (hand-judged)
Not yet judged. `data/groundedness/test_FULL.md`: 25 logs, 14 with a citation. Rule (human's decision): the denominator
is the logs that have a citation; coverage is reported separately.

| | value |
|---|---|
| Citation coverage (Agent, test) | 14/25 logs |
| Grounded, among logs with a citation | **TODO** /14 (`python scripts/export_groundedness_sheet.py --score data/groundedness/test_FULL.md`) |

## Failure cases (real log ids; test split, Agent unless stated)

**Right mod, wrong category (version mismatch reported as missing dependency).** r16 (`yungsapi` swapped to a 1.20.4
build) and r17 (`architectury` swapped to the Fabric build), both `_crash` and `_latest`: B0, RAG-1 and the agent all
name the right culprit but say `missing_dependency`, because the dependants report the mod as "not installed" and NeoForge
skips the wrong jar quietly. This is the page's "Known failure" example in spirit (d3, Cobblemon Fabric build, a demo
log). Four of the six test category misses of the agent are these.

**Victim instead of culprit.** r09_latest (`trashcans` swapped to the mc26.3 build): all three LLM conditions name
`supermartijn642corelib` and say `missing_dependency`; gold is `trashcans`, `version_mismatch`. The agent's only invalid
citation (1 of 15, dropped) is on this log. r05 (`kotlinforforge`): the agent and RAG-1 name `cobblemon` (both logs); B0
names `wild_battle_api` (crash report) or `cobblemon` (latest.log). r03 (`architectury`): B0 says `rctapi` on both
logs, RAG-1 says nothing (`None`) on both, the agent says `rctapi` on the crash report and `None` on latest.log. In
these the named mod is one that appears in the loading errors, not the root cause: this is "blames the mod that
reports", the pattern B1 shows too.

**No-corpus scenarios answered with confidence.** r04 (`simpletms`, a `ClassNotFoundException`): on latest.log the
agent says `dragomordor` with `high` confidence and no citation; RAG-1 says `allthemons` (crash report) and
`dragomordor` (latest.log); B0 says `allthemons` on both. simpletms has no tracker in the corpus, and nothing in the
system says so.

**r14 (`other`).** All three say `mixin_conflict`, correctly naming `cobblemonraiddens`. After the relabel this is a
category miss that reflects a label choice as much as a model error.

**B1 parsing accident (left in on purpose).** r05: B1 returns `file`, because its rule reads `Mod (\w+) ` and r05's
messages begin "Mod File mods\...jar needs language provider ...". Noticed after the first test run, so not fixed (a
fix after seeing the test set would be tuning on it). It scores the same either way, but it is not a diagnosis.

**Unrelated or weak citations (to be settled by the human groundedness judgment).** For example r03_crash cites
`gh-issue:thedarkcolour/KotlinForForge#75` while its diagnosis is about `rctapi` and `architectury`. Whether this
counts as ungrounded is the human's call; it is listed here only as a candidate.

**Retrieval misses (hybrid (b), recall@5 = 0 on 5 of the 18 logs).** r03_crash, r08_crash, r09_crash, r17_crash and
r19_crash: all five are crash reports, and their `latest.log` twins score higher (r03_latest 0.75, r08_latest 1.00,
r09_latest 0.50, r17_latest 0.50, r19_latest 1.00). Why is not investigated. The per-log table is printed by
`python scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.45`.

## Limitations (collected as we go)

- **Cobblemon is not in the corpus.** Its issue tracker is on GitLab and the fetcher only covers GitHub. Crashes whose
  fix is documented only there can't be supported by a citation, so expect `none_found` and abstention there.
- **Changelog coverage is partial.** Only some of the 22 repos publish GitHub releases; the others keep changelogs on
  CurseForge/Modrinth, which are not fetched.
- **The corpus is limited to 22 GitHub repos (15 chosen from the pack + 7 added after the logs were collected) and the NeoForge docs
  (689 documents).**
- **Issue threads are truncated** (3,000 characters per post, 12 comments, 6 chunks), so a fix stated late in a long
  thread can be missing.
- **`mixin_conflict` is not evaluated.** Its only scenario (r14) was relabelled `other` (finding 8), so the category
  has no test log and no dev log. The system can still output it, and does (r14).
- **A crash report may not name the culprit.** r06's crash report only shows a downstream `Registry is already frozen`
  error; the culprit appears only in `latest.log`. User guidance: if a crash report doesn't name a mod, paste
  `latest.log` instead. (r06_crash was dropped from gold for this reason.)
- **`duplicate_mod` was dropped:** NeoForge 21.1 tolerates identical duplicate jars, so no duplicate-mod failure
  could be produced. `config_error` was also dropped (no usable log). `java_version`, `gpu_native` and `hs_err` files
  are not covered.
- **Known B1 bug (left in on purpose)**: see Failure cases.
- **Truncation:** only about 6,000 Gemma tokens of the most informative lines of a log are sent to the model.
- **Not done (cut list):** the rule-based citation gate (human: skip), the chunking experiment, `sweep.py`, the
  tool-call panel, a replay-mode test of `run_eval.py`.
