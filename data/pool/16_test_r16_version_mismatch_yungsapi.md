# Judging sheet 16: `r16_version_mismatch_yungsapi` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `yungsapi`  |  **Acceptable:** yungsapi, betterdungeons, betterendisland, bettermineshafts, betterstrongholds
- **What was broken:** downgraded YUNG's API to the 1.20.4 build (YungsApi-1.20.4-NeoForge-4.4.3.jar); NeoForge 21.1 skipped the jar as being for Forge or an older NeoForge, so betterstrongholds, bettermineshafts, betterdungeons and betterendisland reported yungsapi as not installed
- **Logs in this scenario:** r16_crash, r16_latest
- **Documents to judge:** 30

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 5/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_a#5@r16c, hybrid_b#1@r16c, hybrid_c#1@r16c, bm25_b#4@r16c, dense_b#2@r16c, hybrid_a#2@r16l, hybrid_b#3@r16l, hybrid_c#3@r16l, dense_b#1@r16l
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 4/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#1@r16c, hybrid_c#2@r16c, bm25_a#2@r16c, dense_b#4@r16c, hybrid_c#5@r16l
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 4/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: hybrid_b#2@r16c, hybrid_c#3@r16c, dense_b#1@r16c, hybrid_b#1@r16l, hybrid_c#2@r16l, bm25_b#1@r16l, dense_b#2@r16l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_b#3@r16c, hybrid_c#5@r16c, bm25_b#3@r16c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r16l, bm25_a#2@r16l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#5@r16c, bm25_a#1@r16l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#2@r16c, bm25_a#4@r16c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#62** (github_issue, 2/6 conditions)
  - YUNGs-API issue #62: [1.20.4] fabric server won't start
  - https://github.com/YUNG-GANG/YUNGs-API/issues/62
  - retrieved by: hybrid_b#5@r16c, hybrid_b#2@r16l, bm25_b#5@r16l
  - excerpt: .transformer.MixinTransformer.transformClass(MixinTransformer.java:234) at org.spongepowered.asm.mixin.transformer.MixinTransformer.transformClassBytes(MixinTransformer.java:202) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.getPostMixinClassByteArray(KnotClassDelegate.java:422) ... 11 more Caused by: org.spongepowered.asm.mixin.throwables.MixinApplyError: Mixin [yungsapi.mixins.json:accessor.CriteriaTriggersAccessor from mod yungsapi] from phase [DEFAULT] in config [yungsapi.mixins.json] FAILED during APPLY at org.spongepowered.asm.mixin.transformer.MixinProcessor.handleM

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#5@r16l, bm25_b#2@r16l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#3@r16c, bm25_a#3@r16c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#35** (github_issue, 2/6 conditions)
  - YUNGs-API issue #35: Crash on Quilt 1.19.2
  - https://github.com/YUNG-GANG/YUNGs-API/issues/35
  - retrieved by: hybrid_a#5@r16l, dense_b#3@r16l
  - excerpt: [issue by Gaming32] Loader is Quilt 0.18.1-beta.12. My mods folder contains only four mods: Cloth Config, QFAPI/QSL, YUNG's API, and YUNG's Better Strongholds. `com.google.gson.JsonParseException: Error loading registry data: Unknown registry key in ResourceKey[minecraft:root / minecraft:worldgen/structure_type]: yungsapi:yung_jigsaw` <details> <summary>Full traceback</summary> ``` com.google.gson.JsonParseException: Error loading registry data: Unknown registry key in ResourceKey[minecraft:root / minecraft:worldgen/structure_type]: yungsapi:yung_jigsaw at net.minecraft.class_5455

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 2/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_b#4@r16c, hybrid_c#4@r16c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r16c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#84** (github_issue, 1/6 conditions)
  - YUNGs-API issue #84: [1.21.1] Lasted Mod version crash Game
  - https://github.com/YUNG-GANG/YUNGs-API/issues/84
  - retrieved by: hybrid_c#1@r16l
  - excerpt: [issue by Periam] After installing the latest version of the api, the game crashed when loading word. Name Version (Mod Id) Just Enough Items 19.21.0.247 (jei) Minecraft 1.21.1 (minecraft) NeoForge 21.1.128 (neoforge) Villages & Pillages 1.0.2 (villagesandpillages) YUNG's API 1.21.1-NeoForge-5.1.4 (yungsapi) [latest.log](https://github.com/user-attachments/files/19078429/latest.log) [crash-2025-03-04_19.23.48-client.txt](https://github.com/user-attachments/files/19078432/crash-2025-03-04_19.23.48-client.txt) [comment by yungnickyoung (member)] Hey, this is a known compat issue wi

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 1/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: bm25_b#1@r16c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#2@r16c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#3@r16l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#3@r16l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#23** (github_issue, 1/6 conditions)
  - YUNGs-API issue #23: 1.18.2 Crash on load
  - https://github.com/YUNG-GANG/YUNGs-API/issues/23
  - retrieved by: dense_b#3@r16c, dense_b#4@r16l
  - excerpt: [issue by Merith-TK] https://mclo.gs/9Hi3Xvh < logs for my full modpack https://mclo.gs/wJJPurW < logs of just fabric API and Yungs API working on updating my vanillia modpack to 1.18.2 (mispelling intentional), and currently yungsapi is the only thing throwing errors at this time running java 17 [comment by yungnickyoung (member)] 1.18.2 is not yet supported [comment by Merith-TK (none)] Well I would reccomend pinning this issue and leaving it open for people so they can see it at the top and not blindly open and issue lol

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#3@r16l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#4@r16c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 1/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: bm25_a#4@r16l
  - excerpt: 17 [07lip2022 18:29:10.993] [main/INFO] [cpw.mods.modlauncher.LaunchServiceHandler/MODLAUNCHER]: Launching target 'forgeclient' with arguments [--version, 1.19-forge-41.0.63, --gameDir, C:\Users\<user>\AppData\Roaming\.minecraft, --assetsDir, C:\Users\<user>\AppData\Roaming\.minecraft\assets, --uuid, <token>, --username, <player>, --assetIndex, 1.19, --accessToken, <token> truncated] [comment by BlayTheNinth (member)] Those logs are 99% OptiFine, are you sure that's the correct log? [comment by agabeluga (none)] I changed it. [comment by BlayTheNinth (member)] The Forge forum lied to you,

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#34** (github_issue, 1/6 conditions)
  - YUNGs-API issue #34: Relocate Reflections (and Javassist) or depend on it with include("org.reflections:...")
  - https://github.com/YUNG-GANG/YUNGs-API/issues/34
  - retrieved by: hybrid_b#4@r16l
  - excerpt: [issue by Cypher121] Causes conflict with [Light Overlay](https://modrinth.com/mod/light-overlay). In general, when including code from other libraries without use of Fabric/Quilt's `include` JiJ configuration, the package should be changed to something unique to the mod. As this API copies code from org.reflections:reflections without changing the package, it crashes alongside light overlay, which `include`s an older version of the same library lacking one of the used methods. Change the package to something like `com.yungnickyoung.minecraft.yungsapi.included.org.reflections` to fix.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#63** (github_issue, 1/6 conditions)
  - YUNGs-API issue #63: Yungs API Crashing
  - https://github.com/YUNG-GANG/YUNGs-API/issues/63
  - retrieved by: hybrid_c#4@r16l
  - excerpt: [issue by payphone101] I am running Arclight jar (fabric with plugins) for 1.20.4 and for some reason YungsAPI keeps crashing the server. Error log below. ---- Minecraft Crash Report ---- // But it works on my machine. Time: 2024-02-28 07:47:39 Description: Exception initializing level java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.class_3499 failed at net.minecraft.class_3781.method_27233(class_3781.java:85) at net.minecraft.class_3781.method_16627(class_3781.java:111) at com.yungnickyoung.minecraft.yungsapi.world.structure.jig

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#4@r16l
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#4@r16l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r16c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#29** (github_issue, 1/6 conditions)
  - YUNGs-API issue #29: Incompatibility with ServerCore
  - https://github.com/YUNG-GANG/YUNGs-API/issues/29
  - retrieved by: dense_b#5@r16l
  - excerpt: [issue by ioanvl] HI, There is an incompatibility with [Servercore](https://modrinth.com/mod/servercore) The game crashes with the minimum mods installed (fabric_api + cloth + yungs_api + servercore) with error: `java.lang.RuntimeException: Could not execute entrypoint stage 'main' due to errors, provided by 'fabric-api-lookup-api-v1'! Exit Code: -1` YUNG's API 2.0.7 - ServerCore 1.2.8 - Fabric Loader0.13.3/1.18.2 Both seem to try and modify similar paths [latest.log](https://github.com/yungnickyoung/YUNGs-API/files/8446588/latest.log) I've created a [mirror issue](https://g

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#46** (github_issue, 1/6 conditions)
  - YUNGs-API issue #46: Crash with 1.16.5 forge version, happens while playing a while in a world (Singleplayer)
  - https://github.com/YUNG-GANG/YUNGs-API/issues/46
  - retrieved by: dense_b#5@r16c
  - excerpt: [issue by TheOtherworldly] This is not a twilight forest and optifine issue. Ive tested everything, and ive found that the crash occurs only with your api mod installed (And of course other yungs mods). Exit code is 1 and there is no generated crash report so here is my log https://paste.gg/p/anonymous/dadacb88a0d04e41a29e0ef1571fe67f Please help, id love to use your mods, but right now they are fatal :/ [comment by SiverDX (none)] > The NVIDIA OpenGL driver has encountered an out of memory error u got any more of that ram [comment by loccocmagnotta (none)] same problem [comment by loc

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 1/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: bm25_a#5@r16l
  - excerpt: [issue by dghodgson] ### Bug Description Attempting to load Modernfix alongside VMP-Forge will cause the minecraft client to crash. Tested with following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Modernfix 5.18.0+mc1.20.1 seems to launch without any issues. All older versions tested failed with a different error than the one found in the attached log. ### Reproduction Steps Install the following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Forge: 47.4.1 ### Log File ``` MultiMC version: 0.7.0-4230 Launched instance in onlin

## Added by hand

(none)
