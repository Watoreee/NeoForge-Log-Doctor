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

## Failure cases (log during development)

(none yet)
