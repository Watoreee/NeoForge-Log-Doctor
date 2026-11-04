# Report notes

Running notes for the report (PLAN 9). Numbers go here only if produced by `run_eval.py` / `bootstrap.py`.

## Limitations (collected as we go)

- **Cobblemon is not in the corpus.** The ATMons pack is built around Cobblemon, but Cobblemon's issue tracker
  is on GitLab, not GitHub, and the fetcher only covers GitHub. Crashes whose fix is documented only in
  Cobblemon's tracker can't be supported by a citation, so expect `support_search = none_found` and abstention there.
- **Changelog coverage is partial.** Only some of the 15 repos publish GitHub releases; the others keep changelogs
  on CurseForge/Modrinth, which are not fetched.
- **The corpus is limited to the 15 chosen mods + NeoForge docs.**
- **Issue threads are truncated** (3,000 characters per post, 12 comments, 6 chunks), so a fix stated late in a
  long thread can be missing.
- **`mixin_conflict` was never tuned on.** It has one scenario (r14), so by the stratification rule it sits in **test only**: no prompt, threshold or retrieval setting could be tuned on it. Its test result is an honest out-of-sample number, but from a single `latest.log`, which is too little to generalise. Say so wherever per-category results appear.
- **A crash report may not name the culprit.** r06's crash report only shows a downstream `Registry is already frozen` error; the culprit appears only in `latest.log`. User guidance: if a crash report doesn't name a mod, paste `latest.log` instead. (r06_crash was dropped from gold for this reason.)
- **Relevance labels came from an LLM, not full human reading.** An LLM (Claude) judged each pooled document from its title + the one excerpt shown; the human reviewed the unsure ones and did not open every URL. Documents spot-checked by the human: **TODO (human to fill in)**. Retrieval metrics inherit any error in these labels, and the pool only holds the top-5 of six conditions (pooling bias).
- **The corpus was extended after the logs were collected** (7 repos for the broken mods, before any judgment or test result), so recall is measured with the right repo present. Culprits with no tracker in the corpus (simpletms, cobblemonraiddens, sophisticatedcore, ftbquests, cobblemon) have `none_found` scenarios: they test abstention, not retrieval.
- **`duplicate_mod` was dropped:** NeoForge 21.1 tolerates identical duplicate jars, so no duplicate-mod failure could be produced. `config_error` was also dropped (no usable log).
- **Dev is thin:** only 2 dev scenarios (r02, r13) have relevant documents, so any choice made on dev (min_score, query design) is weakly supported.
- **The first oracle query (c) is not an upper bound.** (c) = extracted `exception_type` (from the LLM) + the gold `acceptable_culprits` + gold category keywords. On test it scored *below* the extracted-fields query (b) (first run: recall@5 0.458 vs 0.597), because gold mod ids are not always the words the relevant issues use, and the exception type is still extraction output. Do not describe (c) as "perfect extraction". (c2) = gold `culprit_mod_id` + gold category + the parser's regex exception type, with no LLM output at all; both are reported, and neither is a ceiling on retrieval quality.
- **Known B1 bug (left in on purpose).** B1 returns `file` for r05: its rule reads the first FML loading error with `Mod (\w+) `, and r05's messages start "Mod File mods\...jar needs language provider ...", so it takes the word "File" as a mod id. It was noticed after the first test run, so it was not fixed (a fix after seeing test results would be tuning on test). It does not change any score (`file` is not acceptable for r05 either), but B1's behaviour on that log is a parsing accident, not a diagnosis.
- **Labels were corrected after the first test run.** r04's acceptable list dropped `cloth_config` (the log shows it loaded). Numbers before and after are in `docs/decisions.md`.

## Failure cases (log during development)

(none yet)
