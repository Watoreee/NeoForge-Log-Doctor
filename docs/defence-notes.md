# Defence notes

Numbers are from `eval/results/` (test split, 25 logs from 14 scenarios, unless stated). Rebuild every table with
`python scripts/report_tables.py --split test`. Answers marked **[unsure]** are things I could not confirm from the repo.

## Start the app and run the two examples

```bash
# once: venv + install (README); with a key in .env for live calls, or no key with replay
source .venv/bin/activate                        # Windows PowerShell: .venv\Scripts\Activate.ps1
uvicorn crashdoc.api:app --port 8000
# PowerShell, no key, cached answers only:  $env:CRASHDOC_REPLAY=1; uvicorn crashdoc.api:app --port 8000
```

Open <http://127.0.0.1:8000/> and press **Success example** (a Create dependency failure; expect `missing_dependency`,
culprit `create`) then **Known failure** (a Fabric build of Cobblemon; expect culprit `cobblemon` but category
`missing_dependency`, where the truth is `version_mismatch`). Progress lines (`facts`, `tool_call`, `tool_result`,
`final`) appear as they arrive. Both examples are cached, so in replay they finish in under a second; on an uncached
log the first progress line came about 4.5 s after the click (headless Chrome check). Health: `GET /health`.
Without the page: `python -c "import httpx;..."` snippet in the README.

For a cache-cold demo use a log from `data/demo/` (d1, d2, d3, d6 were never in dev or test); they need the live proxy.
The request cap is 10 MB; longer-than-budget logs are trimmed for the model and the page says so.

## The one design choice: how the retrieval query is built

The query is built from extracted fields (exception type, suspect mod ids, category keywords) instead of the raw log.

| Query | recall@5 | hit@5 | MRR |
|---|---|---|---|
| (a) preprocessed log text | 0.167 | 6/18 | 0.208 |
| (b) extracted fields | **0.597** | 13/18 | 0.455 |

Difference **+0.431**, 95% CI **[+0.222, +0.681]** (scenario-level paired bootstrap, 1,000 resamples, seed 0),
over 18 test logs from 9 scenarios that have relevant documents. Reproduce:

```bash
CRASHDOC_REPLAY=1 python scripts/run_retrieval_eval.py --split test --allow-test --min-score 0.45
```

Say plainly: this is a retrieval improvement; it did not produce a significant diagnosis improvement (below).

## Five likely questions

**1. Why `min_score = 0.45`?**
PLAN 7.3 says to choose the floor on dev; I took the middle of the dev plateau (0.30 to 0.60) where specificity stayed
perfect. It does not work as an abstention rule, and I say so: on dev the `none_found` logs have a higher max cosine
(0.675 to 0.747) than logs with relevant documents (0.617 to 0.698); on test abstention recall is 0/7 at 0.45
(`decisions.md`, "Cosine floor"). The value is a mechanical choice, not a good one.

**2. Why is there no abstention?**
The only mechanism built is that floor, and it failed: similarity of a log to the corpus does not tell you whether the
corpus holds the answer: the `none_found` logs scored a max cosine of 0.535 to 0.647 on test, inside the range of
the logs that do have relevant documents (0.618 to 0.787). The agent cited nothing on those 7 logs, but it still diagnosed them with `high` confidence, so I do not
claim abstention. A rule-based citation gate was planned and cut. Confidence is not calibrated (high on all 6 of the
agent's strict-culprit misses). **[unsure]** whether a learned abstainer would fix it; not tried.

**3. Why a text-protocol agent instead of native tool calling?**
Measured on this proxy: with the real prompt the model made 0 native tool calls on 7 of 7 dev logs, and
`tool_choice="required"` returned an empty tool call (`decisions.md`, "Agent: JSON text protocol"). A minimal prompt did
call a tool, so it fails with the long prompt. The text protocol keeps the same safeguards: allow-list, pydantic args
with `extra=forbid`, errors for unknown tools or bad args, untrusted-data delimiters, max 5 steps then a forced final
answer. **[unsure]** whether native calling would work with a shorter prompt or another proxy setting; I did not tune it
further.

**4. Why these 15 + 7 repos?**
The first 15 repos are the mods of the author's test pack plus the NeoForge docs; 7 more were added after the logs were
collected so that the repository of each *broken* mod is present (PLAN 6.4: corpus mods are chosen from the mods
broken). That was done before any judgment or test result (`decisions.md`, Day 3 and "culprits broken during
collection"). Total: 22 GitHub repos + docs = 689 documents, 2,160 chunks. Five culprits still have no usable tracker
(simpletms, cobblemonraiddens, sophisticatedcore, ftbquests, cobblemon; Cobblemon's tracker is on GitLab, not fetched).
**[unsure]** why each of the original 15 was chosen beyond "mods in the pack"; I did not see a written criterion beyond that.

**5. What do the baselines show?**
Test, strict culprit: B1 (regex) **7/25 (28%)**, B0 (LLM alone) **17/25 (68%)**, RAG-1 **18/25 (72%)**, agent **19/25 (76%)**.
B0 beats B1: +0.400, CI [+0.125, +0.720], excludes 0. RAG-1 minus B0 +0.040 [0.000, +0.120] and agent minus B0
+0.080 [0.000, +0.192]: both touch 0, so **retrieval and the agent are not shown to improve diagnosis**; one or two
logs decide the difference. Category accuracy is 19/25 for B0, RAG-1 and the agent. What retrieval adds is citations
(14 of 25 logs; 14/14 valid for RAG-1, 14/15 for the agent), and whether those citations support the explanations
is the hand-judged groundedness number (**not yet available**). Errors are systematic: the wrong-version jar is
reported as `missing_dependency` (r16, r17), and the mod that *reports* a failure is blamed (r03, r05, r09_latest).

## Other questions to expect (short)

- **Is the oracle query an upper bound?** No. (c) and (c2) score 0.458 recall@5, significantly below (b) at 0.597 (-0.139, CIs exclude 0): the gold mod id is not what the relevant issues say, so a bare id is a weak query.
- **Did you tune on test?** The agent prompt was tuned on dev only; the RAG-1 prompt was not tuned. Two labels (r04, r14) were corrected after test results had been seen, documented with before/after numbers (r04: no change; r14: category 20/25 to 19/25 for B0, RAG-1, agent).
- **Who judged relevance?** An LLM first pass, reviewed by the author; the spot-check count is still to be filled in (`report-notes.md`, finding 10). Pooling bias applies.
- **Does it generalise?** Unknown: one modpack, 18 scenarios, 7 dev logs. A fresh demo log is a new example, not evidence of generalisation.
- **What if a log is big?** Up to 10 MB is accepted (HTTP 413 above that; the 200 KB limit was a mistake, `decisions.md`). The pipeline trims it to about 6,000 Gemma tokens of the most informative lines, and the `facts` event reports `truncated` and `original_bytes`. **[unsure]** how much accuracy is lost by trimming: not measured separately (gold logs up to 1.8 MB were evaluated through the same trimming).
- **Is user data safe?** The server redacts the log (player name, UUID, tokens, IPs, user folders) before any LLM call; model text is inserted into the page with `textContent` only. Player-name redaction covers captured and listed names only.
