# Judging sheet 14: `r12_missing_dependency_ae2` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `ae2`  |  **Acceptable:** ae2, ae2ct, ae2importexportcard, aeinfinitybooster
- **What was broken:** disabled Applied Energistics 2 (ae2) in CurseForge; aeinfinitybooster, ae2ct and ae2importexportcard still required it
- **Logs in this scenario:** r12_crash, r12_latest
- **Documents to judge:** 24

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 4/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_b#2@r12c, hybrid_c#1@r12c, dense_b#2@r12c, hybrid_a#4@r12l, hybrid_b#2@r12l, hybrid_c#1@r12l, dense_b#2@r12l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8961** (github_issue, 3/6 conditions)
  - Applied-Energistics-2 issue #8961: JEI Disabling the press recipes in the inscriber
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8961
  - retrieved by: hybrid_b#1@r12c, hybrid_c#2@r12c, dense_b#3@r12c, hybrid_b#1@r12l, hybrid_c#2@r12l, dense_b#3@r12l
  - excerpt: [issue by DuckTyler90] ### Describe the bug TBH I'm not sure if i should post this here or the JEI github im ligit lost for words i went throw my 205 mod list trying to fix this issue disabling all the mods and found it as a JEI issue. whats happening is JEI is just not letting the recipes register or there failing to load only for inscriber that i found so far As i said i don't know if its how you integrated JEI in to Ae2 or its jei issue i tryed on modrinth loader and curse both are not working Info { NeoForge: 1.21.1 AE2 Version: 19.2.17 JEI Version: 19.51.0.417 } ### How to reproduc

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r12c, hybrid_c#5@r12c, bm25_b#1@r12c, hybrid_b#3@r12l, hybrid_c#5@r12l, bm25_b#1@r12l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8692** (github_issue, 3/6 conditions)
  - Applied-Energistics-2 issue #8692: Missing Texture
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8692
  - retrieved by: hybrid_b#5@r12c, hybrid_c#3@r12c, dense_b#4@r12c, hybrid_b#5@r12l, hybrid_c#3@r12l, dense_b#4@r12l
  - excerpt: [issue by SwatPolizei] ### Describe the bug If you looking close to the ME Export Bus you can see trow it. ### How to reproduce the bug Place a ME Export Bus and look at the sides two pixels you can see are missing. ### Expected behavior Not seen trow. ### Additional details _No response_ ### Which minecraft version are you using? 1.21 ### On which mod loaders does it happen? NeoForge ### Crash log I [comment by Mithi83 (collaborator)] This is not very precise. Can you paste a screenshot of what you mean exactly? [comment by shartte (member)] I actually verified, and he's right.

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8978** (github_issue, 3/6 conditions)
  - Applied-Energistics-2 issue #8978: AE2 causes problems to the renderer on neoforge 21.1.250, 1.21.1
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8978
  - retrieved by: hybrid_b#4@r12c, hybrid_c#4@r12c, dense_b#5@r12c, hybrid_b#4@r12l, hybrid_c#4@r12l, dense_b#5@r12l
  - excerpt: [issue by SMGPDBGMCB] ### Describe the bug When launching AE2 version 19.2.17 on neoforge 21.1.250 1.21.1: the game gets stuck not rendering anything while the ui can still be interacted with and sounds can be heard. this tends to be stuck on the mojang loadingscreen unless i move the window in which case it becomes a black screen. ### How to reproduce the bug use neoforge 21.1.250, minecraft 1.21.1 get ae2 19.2.17 and guideme 21.1.18 launch the game ### Expected behavior the title screen should appear ### Additional details When [Remove Reloading Screen](https://modrinth.com/mod/ZP7x

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r12l, bm25_a#2@r12l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r12c, bm25_a#4@r12c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#2@r12l, bm25_a#1@r12l
  - excerpt: .util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:507) [?:?] at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1491) [?:?] at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:2073) [?:?] at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2035) [?:?] at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187) [?:?] [28Apr2024 18:58:29.050] [Render thread/FATAL] [net.neoforged.fml.ModLoader/LOADING]: Failed to wait for future Mod Construction, 1 errors found [28Apr2024 18:

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#2@r12c, bm25_a#2@r12c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_a#5@r12l, bm25_a#4@r12l
  - excerpt: mods.modlauncher.Launcher/MODLAUNCHER]: ModLauncher 10.0.1+10.0.1+main.e9521dc3 starting: java version 17.0.3 by Microsoft; OS Windows 10 arch amd64 version 10.0 [07lip2022 18:29:06.835] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.minecraft/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2390!/ Service=ModLauncher Env=CLIENT [07lip2022 18:29:07.952] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\fmlcore

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r12c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:GlodBlock/ExtendedAE#638** (github_issue, 1/6 conditions)
  - ExtendedAE issue #638: [Bug] Error During Mod Loading
  - https://github.com/GlodBlock/ExtendedAE/issues/638
  - retrieved by: dense_b#1@r12c, dense_b#1@r12l
  - excerpt: [issue by Marioluigi7896] Trying to include ExtendedAE in a modpack with a bunch of other mods, however when including the mod AE2 fails to load, disabling the mod fixes the issue. The reported issue in the crashlog seems to be a duplicate resource key, unsure if this will end up being an AE2 issue but since it only appeared with this mod enabled I figured I'd report here first. ``java.lang.IllegalStateException: Adding duplicate key 'ResourceKey[minecraft:menu / extendedae:ex_emc_import_bus]' to registry`` Mincraft Version: 1.21.1 Java Version: 21.0.3, Eclipse Adoptium Mod Version: 1.21-2.2.

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 1/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: bm25_b#2@r12c, bm25_b#2@r12l
  - excerpt: .0 because the newer `Placebo` (v9.9.1) conflicted with `CreativeCore` (v2.13.13). This created a secondary crash, as `Apotheosis` (v8.4.0) required `Placebo v9.9.1`. 2. **The Solution that Revealed the Bug:** We resolved the dependency hell by forcing a clean installation of the latest dependency chain (`Apotheosis v8.4.0` + `Placebo v9.9.1` + `CreativeCore v2.13.13`). 3. **The Outcome (The ModernFix Crash):** Although the dependency chain was now correct, the game still crashed instantly upon loading registry events. This proved the crash was not a dependency issue, but a **ModernFix timin

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 1/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: bm25_a#3@r12c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#3@r12l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#3@r12c, bm25_b#3@r12l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#3@r12c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#3@r12l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#4@r12c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#4@r12c, bm25_b#4@r12l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r12c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 1/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#5@r12c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#5@r12c, bm25_b#5@r12l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: bm25_a#5@r12l
  - excerpt: [issue by julionoir] been trying to run my 25 mod modpack, and it crashes with ferrite core, i know its the ferrite core crashing because once i took it out my game ran normally, just incredibly laggy bcs my pc is a potato crash log: Picked up _JAVA_OPTIONS: 2025-03-04 11:31:52,692 main WARN Advanced terminal features are not available in this environment [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher running: args [--username, <player>, --version, Forge 1.19.2, --gameDir, C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.19.2, --assetsDir, C:

## Added by hand

(none)
