# Spot-check of the relevance judgments

Seed 42; 15 ticked + 15 unticked, drawn from 21 ticked and 492 unticked eligible (sheet, document) pairs in `data/pool/` (532 judged in total); **exclusion list applied** (`spotcheck_exclude.txt`: 8 doc ids, 19 sheet entries removed, i.e. the documents already reviewed by the human). Produced by `scripts/make_spotcheck.py`. Nothing here changes a label.

For each: open the URL if the excerpt/title does not settle it. **agree** = the sheet's mark is right (ticked: it helps diagnose or fix THIS failure; unticked: it does not). **disagree** = it is wrong. Tick exactly one box. Then run `python scripts/score_spotcheck.py`.

---

### 1. sheet 01 (`r02`) `gh-issue:TheIllusiveC4/Curios#473`

- Sheet: `01_dev_r02_missing_dependency_geckolib.md`
- Title: Curios issue #473: game crashes on start up when Ars Nouveau is installed
- URL: https://github.com/TheIllusiveC4/Curios/issues/473
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): disabled geckolib in CurseForge; theurgy was auto-disabled as its dependent

Your call:  agree [ ]   disagree [ ]

---

### 2. sheet 01 (`r02`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `01_dev_r02_missing_dependency_geckolib.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): disabled geckolib in CurseForge; theurgy was auto-disabled as its dependent

Your call:  agree [ ]   disagree [ ]

---

### 3. sheet 02 (`r10`) `gh-issue:CaffeineMC/sodium#2731`

- Sheet: `02_dev_r10_out_of_memory_none.md`
- Title: sodium issue #2731: Problem with launching minecraft 1.21.1 with sodium
- URL: https://github.com/CaffeineMC/sodium/issues/2731
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): set the pack's max RAM to 3000 MB in the launcher; opening a world failed with the data pack error screen

Your call:  agree [ ]   disagree [ ]

---

### 4. sheet 03 (`r13`) `gh-issue:GlodBlock/ExtendedAE#291`

- Sheet: `03_dev_r13_missing_dependency_extendedae.md`
- Title: ExtendedAE issue #291: add kjs support for 1.20.1 (forge)
- URL: https://github.com/GlodBlock/ExtendedAE/issues/291
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): ExtendedAE and MEGA Cells were left auto-disabled after the AE2 run; the pack's KubeJS startup script ExtendedAE/InfinityCells.js failed with Unknown type 'kubejs:custom_infinity_cell'

Your call:  agree [ ]   disagree [ ]

---

### 5. sheet 03 (`r13`) `gh-issue:GlodBlock/ExtendedAE#422`

- Sheet: `03_dev_r13_missing_dependency_extendedae.md`
- Title: ExtendedAE issue #422: kubejs error with extended ae
- URL: https://github.com/GlodBlock/ExtendedAE/issues/422
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): ExtendedAE and MEGA Cells were left auto-disabled after the AE2 run; the pack's KubeJS startup script ExtendedAE/InfinityCells.js failed with Unknown type 'kubejs:custom_infinity_cell'

Your call:  agree [ ]   disagree [ ]

---

### 6. sheet 05 (`r18`) `gh-issue:TwelveIterations/Balm#228`

- Sheet: `05_dev_r18_version_mismatch_sophisticatedcore.md`
- Title: Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
- URL: https://github.com/TwelveIterations/Balm/issues/228
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): updated Sophisticated Core to the Minecraft 26.1.2 build (sophisticatedcore-26.1.2-1.5.24.2445.jar) in a 1.21.1 pack; it requires minecraft 26.1.2 and neoforge 26.1.2.44-beta+, and its 'only supports jei 29.5.0.24' line is a side effect, not a JEI problem

Your call:  agree [ ]   disagree [ ]

---

### 7. sheet 05 (`r18`) `gh-issue:bernie-g/geckolib#508`

- Sheet: `05_dev_r18_version_mismatch_sophisticatedcore.md`
- Title: geckolib issue #508: GeckoLib3 has failed to load correctly
- URL: https://github.com/bernie-g/geckolib/issues/508
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): updated Sophisticated Core to the Minecraft 26.1.2 build (sophisticatedcore-26.1.2-1.5.24.2445.jar) in a 1.21.1 pack; it requires minecraft 26.1.2 and neoforge 26.1.2.44-beta+, and its 'only supports jei 29.5.0.24' line is a side effect, not a JEI problem

Your call:  agree [ ]   disagree [ ]

---

### 8. sheet 05 (`r18`) `gh-issue:malte0811/FerriteCore#210`

- Sheet: `05_dev_r18_version_mismatch_sophisticatedcore.md`
- Title: FerriteCore issue #210: Game Crush
- URL: https://github.com/malte0811/FerriteCore/issues/210
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): updated Sophisticated Core to the Minecraft 26.1.2 build (sophisticatedcore-26.1.2-1.5.24.2445.jar) in a 1.21.1 pack; it requires minecraft 26.1.2 and neoforge 26.1.2.44-beta+, and its 'only supports jei 29.5.0.24' line is a side effect, not a JEI problem

Your call:  agree [ ]   disagree [ ]

---

### 9. sheet 05 (`r18`) `gh-issue:thedarkcolour/KotlinForForge#98`

- Sheet: `05_dev_r18_version_mismatch_sophisticatedcore.md`
- Title: KotlinForForge issue #98: Not working on Neoforge 20.6.14+
- URL: https://github.com/thedarkcolour/KotlinForForge/issues/98
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): updated Sophisticated Core to the Minecraft 26.1.2 build (sophisticatedcore-26.1.2-1.5.24.2445.jar) in a 1.21.1 pack; it requires minecraft 26.1.2 and neoforge 26.1.2.44-beta+, and its 'only supports jei 29.5.0.24' line is a side effect, not a JEI problem

Your call:  agree [ ]   disagree [ ]

---

### 10. sheet 06 (`r01`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `06_test_r01_missing_dependency_curios.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): disabled curios in CurseForge

Your call:  agree [ ]   disagree [ ]

---

### 11. sheet 07 (`r03`) `gh-issue:architectury/architectury-api#542`

- Sheet: `07_test_r03_missing_dependency_architectury.md`
- Title: architectury-api issue #542: "Architectury is not available" with the latest mod version
- URL: https://github.com/architectury/architectury-api/issues/542
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): disabled Architectury API in CurseForge; rctapi was auto-disabled as its dependent

Your call:  agree [ ]   disagree [ ]

---

### 12. sheet 07 (`r03`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `07_test_r03_missing_dependency_architectury.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): disabled Architectury API in CurseForge; rctapi was auto-disabled as its dependent

Your call:  agree [ ]   disagree [ ]

---

### 13. sheet 08 (`r04`) `gh-issue:thedarkcolour/KotlinForForge#75`

- Sheet: `08_test_r04_missing_dependency_simpletms.md`
- Title: KotlinForForge issue #75: 1.19.2 crashes after installing KFF
- URL: https://github.com/thedarkcolour/KotlinForForge/issues/75
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): disabled cloth-config in CurseForge; cloth_config stayed loaded via fightorflight but simpletms was missing too

Your call:  agree [ ]   disagree [ ]

---

### 14. sheet 09 (`r05`) `gh-issue:TwelveIterations/Balm#27`

- Sheet: `09_test_r05_missing_dependency_kotlinforforge.md`
- Title: Balm issue #27: Forge Crash
- URL: https://github.com/TwelveIterations/Balm/issues/27
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): disabled KotlinForForge in CurseForge; Cobblemon and its dependents then failed to load

Your call:  agree [ ]   disagree [ ]

---

### 15. sheet 09 (`r05`) `gh-issue:thedarkcolour/KotlinForForge#160`

- Sheet: `09_test_r05_missing_dependency_kotlinforforge.md`
- Title: KotlinForForge issue #160: new update causing mod not to load
- URL: https://github.com/thedarkcolour/KotlinForForge/issues/160
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): disabled KotlinForForge in CurseForge; Cobblemon and its dependents then failed to load

Your call:  agree [ ]   disagree [ ]

---

### 16. sheet 10 (`r06`) `gh-issue:bernie-g/geckolib#804`

- Sheet: `10_test_r06_version_mismatch_ironfurnaces.md`
- Title: geckolib issue #804: NullPointerException in GeoArmorRenderer when checking entity glow status
- URL: https://github.com/bernie-g/geckolib/issues/804
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): updated Iron Furnaces to the 26.1 build (ironfurnaces-neoforge-26.1.2-4.4.2.jar) in a 1.21.1 pack

Your call:  agree [ ]   disagree [ ]

---

### 17. sheet 11 (`r08`) `gh-issue:CaffeineMC/sodium#3606`

- Sheet: `11_test_r08_version_mismatch_create.md`
- Title: sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
- URL: https://github.com/CaffeineMC/sodium/issues/3606
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): downgraded Create to 6.0.0 (create-1.21.1-6.0.0.jar); 11 mods require a newer Create

Your call:  agree [ ]   disagree [ ]

---

### 18. sheet 11 (`r08`) `gh-issue:TwelveIterations/Balm#27`

- Sheet: `11_test_r08_version_mismatch_create.md`
- Title: Balm issue #27: Forge Crash
- URL: https://github.com/TwelveIterations/Balm/issues/27
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): downgraded Create to 6.0.0 (create-1.21.1-6.0.0.jar); 11 mods require a newer Create

Your call:  agree [ ]   disagree [ ]

---

### 19. sheet 11 (`r08`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `11_test_r08_version_mismatch_create.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): downgraded Create to 6.0.0 (create-1.21.1-6.0.0.jar); 11 mods require a newer Create

Your call:  agree [ ]   disagree [ ]

---

### 20. sheet 12 (`r09`) `gh-issue:SuperMartijn642/TrashCans#38`

- Sheet: `12_test_r09_version_mismatch_trashcans.md`
- Title: TrashCans issue #38: [Crash] Failing to find corelib dependency
- URL: https://github.com/SuperMartijn642/TrashCans/issues/38
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): updated Trash Cans to the latest build (trashcans-1.1.2a-neoforge-mc26.3.jar), which targets Minecraft 26.x

Your call:  agree [ ]   disagree [ ]

---

### 21. sheet 12 (`r09`) `gh-issue:YUNG-GANG/YUNGs-API#12`

- Sheet: `12_test_r09_version_mismatch_trashcans.md`
- Title: YUNGs-API issue #12: server crash
- URL: https://github.com/YUNG-GANG/YUNGs-API/issues/12
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): updated Trash Cans to the latest build (trashcans-1.1.2a-neoforge-mc26.3.jar), which targets Minecraft 26.x

Your call:  agree [ ]   disagree [ ]

---

### 22. sheet 12 (`r09`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `12_test_r09_version_mismatch_trashcans.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): updated Trash Cans to the latest build (trashcans-1.1.2a-neoforge-mc26.3.jar), which targets Minecraft 26.x

Your call:  agree [ ]   disagree [ ]

---

### 23. sheet 13 (`r11`) `gh-issue:Creators-of-Create/Create#10533`

- Sheet: `13_test_r11_out_of_memory_none.md`
- Title: Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
- URL: https://github.com/Creators-of-Create/Create/issues/10533
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): set the pack's max RAM to 1000 MB; ran out of memory during mod loading

Your call:  agree [ ]   disagree [ ]

---

### 24. sheet 14 (`r12`) `gh-issue:Creators-of-Create/Create#10596`

- Sheet: `14_test_r12_missing_dependency_ae2.md`
- Title: Create issue #10596: Jetpack enchantment Above The Clouds not working
- URL: https://github.com/Creators-of-Create/Create/issues/10596
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): disabled Applied Energistics 2 (ae2) in CurseForge; aeinfinitybooster, ae2ct and ae2importexportcard still required it

Your call:  agree [ ]   disagree [ ]

---

### 25. sheet 14 (`r12`) `gh-issue:TwelveIterations/Waystones#1007`

- Sheet: `14_test_r12_missing_dependency_ae2.md`
- Title: Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
- URL: https://github.com/TwelveIterations/Waystones/issues/1007
- **Sheet's current mark: UNTICKED (not relevant)**
- What was broken (notes.txt): disabled Applied Energistics 2 (ae2) in CurseForge; aeinfinitybooster, ae2ct and ae2importexportcard still required it

Your call:  agree [ ]   disagree [ ]

---

### 26. sheet 16 (`r16`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `16_test_r16_version_mismatch_yungsapi.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): downgraded YUNG's API to the 1.20.4 build (YungsApi-1.20.4-NeoForge-4.4.3.jar); NeoForge 21.1 skipped the jar as being for Forge or an older NeoForge, so betterstrongholds, bettermineshafts, betterdungeons and betterendisland reported yungsapi as not installed

Your call:  agree [ ]   disagree [ ]

---

### 27. sheet 17 (`r17`) `gh-issue:architectury/architectury-api#528`

- Sheet: `17_test_r17_version_mismatch_architectury.md`
- Title: architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
- URL: https://github.com/architectury/architectury-api/issues/528
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): replaced Architectury API with the Fabric build (architectury-fabric-22.0.5.jar); NeoForge skipped it as a Fabric mod, so 25 mods reported architectury as not installed

Your call:  agree [ ]   disagree [ ]

---

### 28. sheet 17 (`r17`) `gh-issue:architectury/architectury-api#664`

- Sheet: `17_test_r17_version_mismatch_architectury.md`
- Title: architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
- URL: https://github.com/architectury/architectury-api/issues/664
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): replaced Architectury API with the Fabric build (architectury-fabric-22.0.5.jar); NeoForge skipped it as a Fabric mod, so 25 mods reported architectury as not installed

Your call:  agree [ ]   disagree [ ]

---

### 29. sheet 17 (`r17`) `neoforge-docs:docs/1.21.1/gettingstarted/modfiles`

- Sheet: `17_test_r17_version_mismatch_architectury.md`
- Title: NeoForge docs: Mod Files
- URL: https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): replaced Architectury API with the Fabric build (architectury-fabric-22.0.5.jar); NeoForge skipped it as a Fabric mod, so 25 mods reported architectury as not installed

Your call:  agree [ ]   disagree [ ]

---

### 30. sheet 18 (`r19`) `gh-issue:Keksuccino/Konkrete#22`

- Sheet: `18_test_r19_version_mismatch_konkrete.md`
- Title: Konkrete issue #22: Crash
- URL: https://github.com/Keksuccino/Konkrete/issues/22
- **Sheet's current mark: TICKED (relevant)**
- What was broken (notes.txt): replaced Konkrete with the Minecraft 1.21.11 build (konkrete_neoforge_1.9.15_MC_1.21.11.jar) in a 1.21.1 pack; it requires minecraft 1.21.11+ and neoforge 21.11.13-beta+ (1.21.11 vs 1.21.1 is easy to misread)

Your call:  agree [ ]   disagree [ ]
