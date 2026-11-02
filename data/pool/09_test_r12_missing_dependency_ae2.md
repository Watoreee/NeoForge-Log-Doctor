# Judging sheet 09: `r12_missing_dependency_ae2` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `ae2`  |  **Acceptable:** ae2, ae2ct, ae2importexportcard, aeinfinitybooster
- **What was broken:** disabled Applied Energistics 2 (ae2) in CurseForge; aeinfinitybooster, ae2ct and ae2importexportcard still required it
- **Logs in this scenario:** r12_crash, r12_latest
- **Documents to judge:** 46

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 5/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_b#2@r12c, hybrid_c#1@r12c, bm25_b#10@r12c, dense_b#1@r12c, hybrid_a#3@r12l, hybrid_b#2@r12l, hybrid_c#1@r12l, bm25_b#10@r12l, dense_b#1@r12l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 5/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r12c, hybrid_c#4@r12c, bm25_b#1@r12c, dense_b#10@r12c, hybrid_a#9@r12l, hybrid_b#3@r12l, hybrid_c#4@r12l, bm25_b#1@r12l, dense_b#10@r12l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8961** (github_issue, 4/6 conditions)
  - Applied-Energistics-2 issue #8961: JEI Disabling the press recipes in the inscriber
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8961
  - retrieved by: hybrid_b#1@r12c, hybrid_c#2@r12c, bm25_b#6@r12c, dense_b#2@r12c, hybrid_b#1@r12l, hybrid_c#2@r12l, bm25_b#6@r12l, dense_b#2@r12l
  - excerpt: [issue by DuckTyler90] ### Describe the bug TBH I'm not sure if i should post this here or the JEI github im ligit lost for words i went throw my 205 mod list trying to fix this issue disabling all the mods and found it as a JEI issue. whats happening is JEI is just not letting the recipes register or there failing to load only for inscriber that i found so far As i said i don't know if its how you integrated JEI in to Ae2 or its jei issue i tryed on modrinth loader and curse both are not working Info { NeoForge: 1.21.1 AE2 Version: 19.2.17 JEI Version: 19.51.0.417 } ### How to reproduc

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 4/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: hybrid_b#7@r12c, hybrid_c#6@r12c, bm25_b#2@r12c, hybrid_a#4@r12l, hybrid_b#7@r12l, hybrid_c#6@r12l, bm25_b#2@r12l
  - excerpt: .0 because the newer `Placebo` (v9.9.1) conflicted with `CreativeCore` (v2.13.13). This created a secondary crash, as `Apotheosis` (v8.4.0) required `Placebo v9.9.1`. 2. **The Solution that Revealed the Bug:** We resolved the dependency hell by forcing a clean installation of the latest dependency chain (`Apotheosis v8.4.0` + `Placebo v9.9.1` + `CreativeCore v2.13.13`). 3. **The Outcome (The ModernFix Crash):** Although the dependency chain was now correct, the game still crashed instantly upon loading registry events. This proved the crash was not a dependency issue, but a **ModernFix timin

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8978** (github_issue, 4/6 conditions)
  - Applied-Energistics-2 issue #8978: AE2 causes problems to the renderer on neoforge 21.1.250, 1.21.1
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8978
  - retrieved by: hybrid_b#4@r12c, hybrid_c#5@r12c, dense_b#4@r12c, hybrid_a#10@r12l, hybrid_b#4@r12l, hybrid_c#5@r12l, dense_b#4@r12l
  - excerpt: [issue by SMGPDBGMCB] ### Describe the bug When launching AE2 version 19.2.17 on neoforge 21.1.250 1.21.1: the game gets stuck not rendering anything while the ui can still be interacted with and sounds can be heard. this tends to be stuck on the mojang loadingscreen unless i move the window in which case it becomes a black screen. ### How to reproduce the bug use neoforge 21.1.250, minecraft 1.21.1 get ae2 19.2.17 and guideme 21.1.18 launch the game ### Expected behavior the title screen should appear ### Additional details When [Remove Reloading Screen](https://modrinth.com/mod/ZP7x

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 4/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#6@r12c, hybrid_b#8@r12c, hybrid_c#8@r12c, hybrid_a#5@r12l, hybrid_b#8@r12l, hybrid_c#8@r12l, bm25_a#4@r12l
  - excerpt: 9.2, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppDat

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8692** (github_issue, 3/6 conditions)
  - Applied-Energistics-2 issue #8692: Missing Texture
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8692
  - retrieved by: hybrid_b#5@r12c, hybrid_c#3@r12c, dense_b#3@r12c, hybrid_b#5@r12l, hybrid_c#3@r12l, dense_b#3@r12l
  - excerpt: [issue by SwatPolizei] ### Describe the bug If you looking close to the ME Export Bus you can see trow it. ### How to reproduce the bug Place a ME Export Bus and look at the sides two pixels you can see are missing. ### Expected behavior Not seen trow. ### Additional details _No response_ ### Which minecraft version are you using? 1.21 ### On which mod loaders does it happen? NeoForge ### Crash log I [comment by Mithi83 (collaborator)] This is not very precise. Can you paste a screenshot of what you mean exactly? [comment by shartte (member)] I actually verified, and he's right.

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r12l, bm25_a#2@r12l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r12c, bm25_a#3@r12c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 2/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: hybrid_a#9@r12c, bm25_a#1@r12c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#2@r12l, bm25_a#1@r12l
  - excerpt: .util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:507) [?:?] at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1491) [?:?] at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:2073) [?:?] at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2035) [?:?] at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187) [?:?] [28Apr2024 18:58:29.050] [Render thread/FATAL] [net.neoforged.fml.ModLoader/LOADING]: Failed to wait for future Mod Construction, 1 errors found [28Apr2024 18:

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#5@r12c, bm25_a#2@r12c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 2/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: hybrid_c#9@r12c, hybrid_c#9@r12l, bm25_a#3@r12l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8809** (github_issue, 2/6 conditions)
  - Applied-Energistics-2 issue #8809: TheOneProbe integration doesn't work correctly on 1.21.1
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8809
  - retrieved by: hybrid_c#10@r12c, dense_b#6@r12c, hybrid_c#10@r12l, dense_b#6@r12l
  - excerpt: [issue by Lauriichan] ### Describe the bug When looking at an AE2 block which stores power the tooltip is not being generated, instead a exception is thrown and TheOneProbe shows `Error: ae2:block-entity`. ### How to reproduce the bug 1. Setup a server and client with AE2 and TheOneProbe 2. Join the server and look at any AE2 block which can store energy 3. See `Error: ae2:block-entity` in the one probe 4. Opening the debug log provides a stacktrace. ### Expected behavior That the tooltip is being shown correctly ### Additional details I also investigated where this is coming from and i

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#9021** (github_issue, 2/6 conditions)
  - Applied-Energistics-2 issue #9021: Item duplication when AE2 interface/storage bus pushes more than 8 items into Kaleidoscope Cookery's Millstone
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/9021
  - retrieved by: hybrid_a#6@r12l, bm25_a#7@r12l
  - excerpt: Server/]: Saving chunks for level 'ServerLevel[19.2.18]'/ae2:spatial_storage [0810月2026 21:32:04.174] [Render thread/INFO] [xaero.hud.minimap.MinimapLogs/]: Xaero hud session finalized. [0810月2026 21:32:04.174] [Render thread/INFO] [xaero.map.WorldMap/]: Finalizing world map session... [0810月2026 21:32:04.181] [Thread-14/INFO] [xaero.map.WorldMap/]: World map cleaned normally! [0810月2026 21:32:04.182] [Thread-14/INFO] [XaeroPlus/]: Firing world change event: EXIT_WORLD from ResourceKey[minecraft:dimension / minecraft:overworld] to null [0810月2026 21:32:04.197] [Render thread/INFO] [xaero.map.W

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 2/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_b#6@r12c, bm25_b#9@r12c, hybrid_b#6@r12l, bm25_b#9@r12l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8983** (github_issue, 2/6 conditions)
  - Applied-Energistics-2 issue #8983: Duplicate MenuType registration crash in InitMenuTypes.registerAll (AE2 19.2.17, NeoForge 1.21.1) — reproduces with all addons disabled
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8983
  - retrieved by: dense_b#9@r12c, hybrid_a#7@r12l, dense_b#9@r12l
  - excerpt: [issue by JFloresAranda] ### Describe the bug As i have grown to enjoy a lot this mod an its addons, the pack im developing wouldnt be an exception. However i disabled all of them and the game would still crash. I disabled Ae2 and the game starts. AE2 throws `java.lang.IllegalStateException: Adding duplicate value 'net.minecraft.world.inventory.MenuType@...' to registry` during its own `RegisterEvent` handling, which causes a `ModLoadingException` ("Failed to register some entries") during game startup. The crash happens consistently, in the same place, in `InitMenuTypes.registerAll` (

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#2@r12c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#3@r12c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#3@r12c, bm25_b#3@r12l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#4@r12c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#4@r12c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#4@r12c, bm25_b#4@r12l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#5@r12c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 1/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#5@r12c, dense_b#5@r12l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 1/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: bm25_a#5@r12l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#5@r12c, bm25_b#5@r12l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#6@r12l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#6@r12c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8749** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8749: AE2 AutoCrafter won't create Basic to Nitro Energy Cells
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8749
  - retrieved by: hybrid_c#7@r12c, hybrid_c#7@r12l
  - excerpt: [issue by Eevetv] ### Describe the bug Problem: When trying to autocraft any Energy Cell (Powah) above a Blazing Energy Cell it mentions missing ingredients. - When making the Blazing Energy Cell directly, shows all ingredients are available and can craft. - When trying to making a higher tier than Blazing Energy Cell, ingredient breakdown does not show ingredients for Energy Cells equal or below than Blazing tier. - Running a single AE2 network with 1 7x7x7 Quantum Computer - I noticed when crafting some Screenshots for reference: https://imgur.com/a/tUO99Sk ### How to reproduce the b

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_a#7@r12c, hybrid_a#8@r12l
  - excerpt: /issues. ========================= // Shall we play a game? Time: 2026-06-25 21:57:03 Description: Rendering overlay java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.2+mc1.21.1-mod.jar%23319!/:?] {re:mixin,re:classloading} at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigsLate(ConfigManager.java:76) ~[net.caffeinemc.sodium-neoforge-0.8

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#7@r12c
  - excerpt: [issue by cuberPidor] ### Description My cannon from Create: Big Cannons builds and shoots fine in Creative mode, but fails to assemble or work in Survival. Am I missing something like glue, stress capacity, or assembly steps? ### Game Log https://mclo.gs/wti8vMj ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Rendere

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 1/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#7@r12c, dense_b#7@r12l
  - excerpt: to dig into it a bit and sadly "Mo´ Structures" was the mod using that configfile and causing the crash. It´s a bit dissapointing not to be able to use the mod (liked it very much) but at least i can play again. Again, thank you very much for your patience and helping me out :-) [comment by SirTwsted (none)] ![Screenshot_308](https://github.com/user-attachments/assets/285348a0-af89-42a0-ad0a-6fa574b0772e) [crash-2024-07-19_08.55.05-client.txt](https://github.com/user-attachments/files/16312649/crash-2024-07-19_08.55.05-client.txt) Using MC v1.21 and on NEOForge v21.0.109 . [comme

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#7@r12c, bm25_b#7@r12l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8928** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8928: Cables Bus can't be displayed in PonderJS(Ponder for KubeJS)
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8928
  - retrieved by: bm25_b#8@r12c, bm25_b#8@r12l
  - excerpt: ableBus block, for example: - ae2:fluix_glass_cable 7. Save the scene and open/run the Ponder scene. Expected behavior: The AE2 CableBus block should be visible in the Ponder scene. Actual behavior: The CableBus block is invisible. However, the block still exists: - It can be selected/inspected. - The block information tooltip still shows the AE2 CableBus block. This indicates that the block data is present, but the rendering is missing. The above steps were generated by AI. For detailed instructions, please watch the video: https://drive.google.com/file/d/1eMgbCYqNRJmKhPuR9VIld3Dr7DddsOR5/vi

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#8@r12c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:TwelveIterations/Waystones#1126** (github_issue, 1/6 conditions)
  - Waystones issue #1126: Natural Waystone activation invalid.
  - https://github.com/TwelveIterations/Waystones/issues/1126
  - retrieved by: dense_b#8@r12c, dense_b#8@r12l
  - excerpt: ] [main/INFO]: Loading 217 mods: - achiopt 2.1.2 - amplified_nether 1.2.13 - animal_feeding_trough 1.2.0+1.21.11 - appleskin 3.0.8+mc1.21.11 - architectury 19.0.1 - awcapi 1.0.2 - balm 21.11.6 \-- kuma_api 21.11.12 - better-doors 1.0.3 \-- com_moandjiezana_toml_toml4j 0.7.2 - bettercombat 3.0.0 \-- tiny_config 3.1.0 - betterstats 5.0.0-beta.5+fabric-1.21.11 - boids 2.0.0+1.21.11 \-- blue_endless_jankson 1.2.3 - brainierbees 1.9.0 - c2me 0.3.7+alpha.0.7+1.21.11 |-- c2me-base 0.3.7+alpha.0.7+1.21.11 |-- c2me-client-uncapvd 0.3.7+alpha.0.7+1.21.11 |-- c2me

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#8@r12l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#8@r12c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#9@r12c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:TwelveIterations/Waystones#905** (github_issue, 1/6 conditions)
  - Waystones issue #905: Game not saving after activating waystone
  - https://github.com/TwelveIterations/Waystones/issues/905
  - retrieved by: hybrid_b#9@r12c, hybrid_b#9@r12l
  - excerpt: uld not parse version number component '1a'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [14:11:22] [main/WARN]: Warnings were found! - Mod 'ModMenu Badges Lib' (modmenu-badges-lib) 2023.6.1 recommends any version of modmenu, which is missing! - You should install any version of modmenu for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg) 2024.6.2 recommends any version of emi, which is missing! - You should install any version of emi for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg)

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#9@r12l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8855** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8855: AE2 26.1.7 alpha  Wireless Crafting Terminal voids items and doesn't work.
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8855
  - retrieved by: hybrid_b#10@r12c, hybrid_b#10@r12l
  - excerpt: [issue by delolione] ### Describe the bug ATM11-AE2 26.1.7 alpha The wireless crafting terminal does not craft. The whole 3x3 crafting grid doesn't work. Not through jei or manually. Anything added to the grid will be voided. ### How to reproduce the bug Open wireless crafting terminal, try putting any items in the crafting grid. ### Expected behavior Should craft items and not void things. ### Additional details _No response_ ### Which minecraft version are you using? 1.21 ### On which mod loaders does it happen? NeoForge ### Crash log There was no crash [comment by Mithi83 (col

- [ ] **gh-issue:CaffeineMC/sodium#3760** (github_issue, 1/6 conditions)
  - sodium issue #3760: minecraft crashing after collapsing window on 1.21.1 neoforge
  - https://github.com/CaffeineMC/sodium/issues/3760
  - retrieved by: bm25_a#10@r12l
  - excerpt: [issue by Kishebek] ### Bug Description minecraft crashing after collapsing window both in the menu and in the world, also after collapsing my gpu is running up to 100 percent for a second. i checked other version but nothing changed. maybe happening cuz off legacy launcher used sodium 0.6.7 on 1.21.1 neoforge GPU Intel(R) HD Graphics 4600 CPU Intel(R) Core(TM) i3-4000M CPU @ 2.40GHz ### Reproduction Steps 1. lauch sodium 0.6.7 on 1.21.1 neoforge 2. collapse window ### Log File [latest.log](https://github.com/user-attachments/files/29269020/latest.log) ### Crash Report [crash-20

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: bm25_a#10@r12c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 1/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_a#10@r12c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

## Added by hand

(none)
