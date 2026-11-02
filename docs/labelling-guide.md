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

**(d) Acceptable culprits = the culprit + every mod listed as `Requested by` for the culprit in the log.**
Read `Mod ID: '<culprit>', Requested by: '<mod>'` lines. When the culprit is itself the requester (a jar that
needs a newer Minecraft/NeoForge), the list is just the culprit. Cascades are **not** added: a mod that was missing
only because it was auto-disabled as a dependant of the culprit is not acceptable (r02 `theurgy`, r03 `rctapi`;
r18's "only supports jei" line is a side effect, not a JEI problem).

**(d2) No `Requested by` line (confirmed).** When the log has no such line, use the mod(s) the
equivalent message names: r04 (`NoClassDefFoundError` in `allthemons` for a `simpletms` class) and r05 ("Mod File
… needs language provider kotlinforforge" for `cobbleworkers` and `torchmastercobblemoncompat`).

## Precedence (from PLAN 6.1)
- A mixin conflict caused by a version mismatch is `version_mismatch`.
- Registry errors are `version_mismatch` unless clearly something else.
- Out of memory: `culprit_mod_id = null`, `acceptable_culprits = []`.

## Relevance judging (PLAN 6.7)
Judge the **document**, not the one chunk shown. If the shown chunk doesn't settle it, open the URL.
`relevant_doc_ids` stays `null` until judged.

## Metrics that use these labels
Culprit accuracy is reported two ways, for every condition including B1: **strict** (prediction equals
`culprit_mod_id`) and **lenient** (prediction is in `acceptable_culprits`). See `decisions.md`.
