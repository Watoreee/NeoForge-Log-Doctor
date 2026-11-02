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

## Failure cases (log during development)

(none yet)
