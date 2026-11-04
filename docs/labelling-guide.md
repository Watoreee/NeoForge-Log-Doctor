# Labelling guide (PLAN 6.1)

Written before the labels were drafted. A label is valid only if **the log file it is attached to** supports it.

## Categories in use
`missing_dependency`, `version_mismatch`, `out_of_memory`, `mixin_conflict`. (`duplicate_mod` and `config_error` were
dropped, see `decisions.md`. `java_version`, `gpu_native` and `other` have 0 logs and are not used.)

## Label fields
- `culprit_mod_id`: the mod whose fault caused the failure. For a missing dependency it is the **missing** mod.
  `null` when no mod is at fault (out of memory).
- `acceptable_culprits`: always contains `culprit_mod_id` (the validator enforces it); `[]` when the culprit is `null`.
  Scoring checks only this list.
- One label file per log file: the crash report and the `latest.log` of one run are two gold logs sharing a
  `scenario_id`. `debug.log` is never a gold log.

## Rules
**(a) Label by cause, not symptom.** A jar that NeoForge skipped because it is for the wrong version or loader
(a Fabric build, a 1.20.x or 26.x build) is `version_mismatch`, even though dependants report it as "not installed".

**(b) A mixin crash triggered by a missing mod is `mixin_conflict`.** The culprit is the mod whose mixin crashed.
The missing mod that triggered it is also acceptable. (r14: culprit `cobblemonraiddens`, also accepts `owo`.)

**(c) A KubeJS script that fails because a mod it uses is not loaded is `missing_dependency`.** The culprit is the
missing mod, not KubeJS or the script's mod.

**(d) Strict acceptable_culprits rule (supersedes the earlier "Requested by" rule).**
`acceptable_culprits` = `culprit_mod_id` + **only mods that were actually disabled, removed, swapped or changed by the
human**, according to the run's `notes.txt`. and that the log itself shows **absent or faulty** (a mod the notes say was disabled but the log shows loaded, e.g. r04's `cloth_config`, is not listed). **Never** mods that merely *report* the failure (requirers, "victims":
the mods in `Requested by:` lines, the better* mods that say yungsapi is missing, ...). `culprit_mod_id` is always in
the list. No-culprit runs (out_of_memory): culprit `null`, list `[]`.

**(e) Cascade rule.** Mods the launcher auto-disabled as a side effect of the human's fault may be listed **if
`notes.txt` says so** (r02 `theurgy`, r03 `rctapi`, r13 `megacells`, r14 `mega_showdown`). A mod that only "failed to
load" or "reported" is not a cascade (r05's Cobblemon dependents).

**(f) Category follows the log, not the intention.** The category is what the log supports, whatever the human meant
to test. (r13 was intended as `other` in its notes but the log shows a KubeJS script failing because a mod is not
loaded, so by rule (c) it is `missing_dependency`.)

**(g) One scenario group per fault.** The two out_of_memory runs (r10: 3000 MB, r11: 1000 MB) are one scenario
group, `r10_r11_out_of_memory_none`, so they stay on the same side of the split (test).

## Precedence (from PLAN 6.1)
- A mixin conflict caused by a version mismatch is `version_mismatch`.
- Registry errors are `version_mismatch` unless clearly something else.
- Out of memory: `culprit_mod_id = null`, `acceptable_culprits = []`.

## Relevance judging (PLAN 6.7)
Judge the **document**, not the one chunk shown. If the shown chunk doesn't settle it, open the URL.

**A document is relevant if someone with this exact crash would use it to diagnose or fix it: an issue about the same mod
with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely
on-topic don't count.** This is the rule the judging sheets used (same mod + same kind of error, or a docs page
explaining that exact error message).

`relevant_doc_ids` stays `null` until judged.

## Metrics that use these labels
Culprit accuracy is reported two ways, for every condition including B1: **strict** (prediction equals
`culprit_mod_id`) and **lenient** (prediction is in `acceptable_culprits`). See `decisions.md`.
