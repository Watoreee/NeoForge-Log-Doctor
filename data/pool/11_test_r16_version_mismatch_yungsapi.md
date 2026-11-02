# Judging sheet 11: `r16_version_mismatch_yungsapi` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `yungsapi`  |  **Acceptable:** yungsapi, betterdungeons, betterendisland, bettermineshafts, betterstrongholds
- **What was broken:** downgraded YUNG's API to the 1.20.4 build (YungsApi-1.20.4-NeoForge-4.4.3.jar); NeoForge 21.1 skipped the jar as being for Forge or an older NeoForge, so betterstrongholds, bettermineshafts, betterdungeons and betterendisland reported yungsapi as not installed
- **Logs in this scenario:** r16_crash, r16_latest
- **Documents to judge:** 61

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 5/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#1@r16c, hybrid_b#7@r16c, hybrid_c#2@r16c, bm25_a#2@r16c, dense_b#4@r16c, hybrid_b#7@r16l, hybrid_c#5@r16l
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 5/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_a#5@r16c, hybrid_b#1@r16c, hybrid_c#1@r16c, bm25_b#4@r16c, dense_b#2@r16c, hybrid_a#2@r16l, hybrid_b#3@r16l, hybrid_c#3@r16l, dense_b#1@r16l
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 5/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: hybrid_b#2@r16c, hybrid_c#3@r16c, dense_b#1@r16c, hybrid_a#10@r16l, hybrid_b#1@r16l, hybrid_c#2@r16l, bm25_b#1@r16l, dense_b#2@r16l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#62** (github_issue, 4/6 conditions)
  - YUNGs-API issue #62: [1.20.4] fabric server won't start
  - https://github.com/YUNG-GANG/YUNGs-API/issues/62
  - retrieved by: hybrid_b#5@r16c, hybrid_b#2@r16l, hybrid_c#8@r16l, bm25_b#5@r16l, dense_b#9@r16l
  - excerpt: .transformer.MixinTransformer.transformClass(MixinTransformer.java:234) at org.spongepowered.asm.mixin.transformer.MixinTransformer.transformClassBytes(MixinTransformer.java:202) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.getPostMixinClassByteArray(KnotClassDelegate.java:422) ... 11 more Caused by: org.spongepowered.asm.mixin.throwables.MixinApplyError: Mixin [yungsapi.mixins.json:accessor.CriteriaTriggersAccessor from mod yungsapi] from phase [DEFAULT] in config [yungsapi.mixins.json] FAILED during APPLY at org.spongepowered.asm.mixin.transformer.MixinProcessor.handleM

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#8@r16c, hybrid_b#3@r16c, hybrid_c#5@r16c, bm25_b#3@r16c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#5@r16c, hybrid_a#6@r16l, bm25_a#1@r16l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 3/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_b#8@r16c, hybrid_c#6@r16c, bm25_b#1@r16c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#7@r16c, hybrid_b#9@r16c, bm25_b#2@r16c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 3/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_b#9@r16c, hybrid_a#9@r16l, bm25_a#3@r16l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 3/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#6@r16c, hybrid_b#4@r16c, hybrid_c#4@r16c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#14** (github_issue, 3/6 conditions)
  - YUNGs-API issue #14: How do I fix YUNG's API and Better Mineshafts not being able to load?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/14
  - retrieved by: dense_b#6@r16c, hybrid_a#7@r16l, hybrid_c#10@r16l, dense_b#6@r16l
  - excerpt: [issue by Sarsath] https://imgur.com/a/XvXfLCT latest: https://pastebin.com/ZEf12Kur crash report: https://pastebin.com/2Dj4fEZM What do I do? [comment by yungnickyoung (member)] You are using the 1.16 versions of my mods on Forge 1.17. Unfortunately, I do not have Forge 1.17 versions of my mods available for use.

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r16l, bm25_a#2@r16l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#2@r16c, bm25_a#4@r16c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: bm25_b#6@r16c, hybrid_b#5@r16l, bm25_b#2@r16l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#3@r16c, bm25_a#3@r16c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 2/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: hybrid_b#10@r16l, bm25_b#3@r16l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#23** (github_issue, 2/6 conditions)
  - YUNGs-API issue #23: 1.18.2 Crash on load
  - https://github.com/YUNG-GANG/YUNGs-API/issues/23
  - retrieved by: hybrid_b#10@r16c, dense_b#3@r16c, dense_b#4@r16l
  - excerpt: [issue by Merith-TK] https://mclo.gs/9Hi3Xvh < logs for my full modpack https://mclo.gs/wJJPurW < logs of just fabric API and Yungs API working on updating my vanillia modpack to 1.18.2 (mispelling intentional), and currently yungsapi is the only thing throwing errors at this time running java 17 [comment by yungnickyoung (member)] 1.18.2 is not yet supported [comment by Merith-TK (none)] Well I would reccomend pinning this issue and leaving it open for people so they can see it at the top and not blindly open and issue lol

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#35** (github_issue, 2/6 conditions)
  - YUNGs-API issue #35: Crash on Quilt 1.19.2
  - https://github.com/YUNG-GANG/YUNGs-API/issues/35
  - retrieved by: dense_b#7@r16c, hybrid_a#5@r16l, dense_b#3@r16l
  - excerpt: [issue by Gaming32] Loader is Quilt 0.18.1-beta.12. My mods folder contains only four mods: Cloth Config, QFAPI/QSL, YUNG's API, and YUNG's Better Strongholds. `com.google.gson.JsonParseException: Error loading registry data: Unknown registry key in ResourceKey[minecraft:root / minecraft:worldgen/structure_type]: yungsapi:yung_jigsaw` <details> <summary>Full traceback</summary> ``` com.google.gson.JsonParseException: Error loading registry data: Unknown registry key in ResourceKey[minecraft:root / minecraft:worldgen/structure_type]: yungsapi:yung_jigsaw at net.minecraft.class_5455

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#4@r16c, bm25_a#7@r16c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_b#8@r16l, bm25_a#4@r16l
  - excerpt: \javafmllanguage\1.19-41.0.63\javafmllanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.958] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\lowcodelanguage\1.19-41.0.63\lowcodelanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.960] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\mclanguage\1.19-41.0.63\mclanguage-1.19-41.0.63

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#34** (github_issue, 2/6 conditions)
  - YUNGs-API issue #34: Relocate Reflections (and Javassist) or depend on it with include("org.reflections:...")
  - https://github.com/YUNG-GANG/YUNGs-API/issues/34
  - retrieved by: hybrid_b#4@r16l, dense_b#8@r16l
  - excerpt: [issue by Cypher121] Causes conflict with [Light Overlay](https://modrinth.com/mod/light-overlay). In general, when including code from other libraries without use of Fabric/Quilt's `include` JiJ configuration, the package should be changed to something unique to the mod. As this API copies code from org.reflections:reflections without changing the package, it crashes alongside light overlay, which `include`s an older version of the same library lacking one of the used methods. Change the package to something like `com.yungnickyoung.minecraft.yungsapi.included.org.reflections` to fix.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#63** (github_issue, 2/6 conditions)
  - YUNGs-API issue #63: Yungs API Crashing
  - https://github.com/YUNG-GANG/YUNGs-API/issues/63
  - retrieved by: hybrid_c#7@r16c, hybrid_b#6@r16l, hybrid_c#4@r16l
  - excerpt: [issue by payphone101] I am running Arclight jar (fabric with plugins) for 1.20.4 and for some reason YungsAPI keeps crashing the server. Error log below. ---- Minecraft Crash Report ---- // But it works on my machine. Time: 2024-02-28 07:47:39 Description: Exception initializing level java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.class_3499 failed at net.minecraft.class_3781.method_27233(class_3781.java:85) at net.minecraft.class_3781.method_16627(class_3781.java:111) at com.yungnickyoung.minecraft.yungsapi.world.structure.jig

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

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#3@r16l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

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
  - retrieved by: dense_b#8@r16c, dense_b#5@r16l
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

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#6@r16c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#19** (github_issue, 1/6 conditions)
  - YUNGs-API issue #19: server crash in 1.18.2
  - https://github.com/YUNG-GANG/YUNGs-API/issues/19
  - retrieved by: hybrid_c#6@r16l
  - excerpt: ed.asm.mixin.transformer.throwables.MixinPreProcessorException: Attach error for yungsapi.mixins.json:DeepCopyStructureSettingsMixin during activity: [Transform -> Method yungsapi_deepCopyNoiseSettings(Lnet/minecraft/server/MinecraftServ [... truncated] [comment by yungnickyoung (member)] 1.18.2 is not yet supported

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#6@r16l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#6@r16l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 1/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: hybrid_b#6@r16c
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#7@r16l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 1/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: bm25_b#7@r16c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#74** (github_issue, 1/6 conditions)
  - YUNGs-API issue #74: [1.21] Mark 1.21 versions as compatible with 1.21.1
  - https://github.com/YUNG-GANG/YUNGs-API/issues/74
  - retrieved by: dense_b#7@r16l
  - excerpt: [issue by BugmanBugman] This goes for the other mods too but yeah, you cant download your 1.21 mods on a instance running 1.21.1 becasue it isnt marked as such [comment by Timolino456 (none)] Yes please, I'm using 1.21.1, downloaded a mod from another author that requires YUNG's API but had to download it manually because of this... [comment by yungnickyoung (member)] Pretty late on this, but this should be fixed now, right?

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 1/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_c#8@r16c, hybrid_c#7@r16l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#7@r16l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#8@r16c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:SuperMartijn642/TrashCans#11** (github_issue, 1/6 conditions)
  - TrashCans issue #11: [Crash] with newest version of mod
  - https://github.com/SuperMartijn642/TrashCans/issues/11
  - retrieved by: bm25_a#8@r16l
  - excerpt: [issue by Warbringer12] **Version Info** - Minecraft, 1.16.5 - Trash Cans, 1.0.10-mc1.16.5 **Steps to Reproduce** ...1. launch minecraft **Crash report (~/logs/latest.log)** ... [crash-2021-05-07_18.31.42-fml.txt](https://github.com/SuperMartijn642/TrashCans/files/6444927/crash-2021-05-07_18.31.42-fml.txt) [Uploading 2021-05-07-2.log…]() [comment by SuperMartijn642 (owner)] It says you don't have the core lib installed, it is required for the newest version. [comment by luffykick (none)] Same issue as OP... but for clarity... your latest trashcans update "trashcans-1.0.10-mc1.1

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: bm25_b#8@r16c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#2** (github_issue, 1/6 conditions)
  - YUNGs-API issue #2: Yungs API Crashing 
  - https://github.com/YUNG-GANG/YUNGs-API/issues/2
  - retrieved by: hybrid_a#8@r16l
  - excerpt: [issue by cregooo] So I'm using the Better mineshafts mod which obviously requires the Yungs Api mod to work, But when I would try to actually use the API mod it would cause my game to crash with the log saying "Process crashed with exit code 1" And I'm on forge 1.16.5 [comment by yungnickyoung (member)] Can you provide the crashlog and latest.log? [comment by RealTenzFate (none)] Also getting the same issue, here is my crash log. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 19/04/21 20:28 Description: Initializing game java.lang.VerifyError: Bad local va

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#8@r16l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#9@r16c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:Creators-of-Create/Create#9745** (github_issue, 1/6 conditions)
  - Create issue #9745: Shaders with Create
  - https://github.com/Creators-of-Create/Create/issues/9745
  - retrieved by: hybrid_a#9@r16c
  - excerpt: assets/6cdfa570-13f8-4e8f-b69a-a7c0fd408475" /> ### Game Log https://mclo.gs/nJlYbPX ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.216 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.5 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: AMD Radeon RX 7600 (radeonsi, navi33, LLVM 21.1.6, DRM 3.64, 6.18.2-3-cachyos) OpenGL Version: 4.6 (Core Profile) Mesa 25.3.2-arch1.2 Graphics Mode: fancy PojavLauncher Dete

- [ ] **gh-issue:GlodBlock/ExtendedAE#550** (github_issue, 1/6 conditions)
  - ExtendedAE issue #550: [Neoforge1.21.1]似乎PartSmartAnnihilationPlane出现了一些问题导致崩溃
  - https://github.com/GlodBlock/ExtendedAE/issues/550
  - retrieved by: hybrid_c#9@r16c
  - excerpt: jar%23429!/:?] {re:classloading} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.ConsumerEventHandler.invoke(ConsumerEventHandler.java:27) ~[bus-8.0.5.jar%23125!/:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:360) ~[bus-8.0.5.jar%23125!/:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:328) ~[bus-8.0.5.jar%23125!/:?] {} at TRANSFORMER/neoforge@21.1.216/net.neoforged.neoforge.event.EventHooks.fireLevelTickPost(EventHooks.java:1022) ~[neoforge-21.1.216-universal.jar%23417!/:1.21.1] {re:mixin,re:classloading} at

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#89** (github_issue, 1/6 conditions)
  - YUNGs-API issue #89: [Crash] Cannot invoke "it.unimi.dsi.fastutil.objects.ObjectListIterator.back(int)" because the return value of "com.yungnickyoung.minecraft.yungsapi.world.structure.terrainadaptation.beardifier.EnhancedBeardifierData.getEnhancedPieceIterator()" is null
  - https://github.com/YUNG-GANG/YUNGs-API/issues/89
  - retrieved by: hybrid_b#9@r16l
  - excerpt: logs/mc1buGr>) | [crash_assistant_app.log](<https://gnomebot.dev/paste/mclogs/TvN68Qb>) ### Mod list changes beyond the modpack: ```ansi Added mods: [2;32mmarvel-2.1.0-pre4-1.21.1-neoforge.jar[0m ``` [comment by yungnickyoung (member)] Can't say I've ever seen this before. I think this means that a mod must be preventing my [BeardifierMixin ](https://github.com/YUNG-GANG/YUNGs-API/blob/36cc2c60e7a382fe844747c854ce7ae8a2c6a27b/Common/src/main/java/com/yungnickyoung/minecraft/yungsapi/mixin/BeardifierMixin.java#L37) from injecting my custom EnhancedBeardifier logic. [comment by yungnick

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 1/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#9@r16c, dense_b#10@r16l
  - excerpt: found. So I am a bit confused. [comment by RockinOstrich (none)] When I use NeoForge 21.1.31, it's fine, but if I try updating it to Neoforge 21.1.32+, I get that crash report (the one SirTwsted got), and that's the only thing I've changed. Any suggestions? I know you mentioned above about omegaconfig, but I don't know how to read or interpret a crash report: [crash-2024-10-21_20.18.46-client.txt](https://github.com/user-attachments/files/17468161/crash-2024-10-21_20.18.46-client.txt) [comment by Redfan2 (none)] > > omegaconfig > > @Jab125 > > I don't understand. I typed omegaconfig

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 1/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: bm25_b#9@r16l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:embeddedt/ModernFix#503** (github_issue, 1/6 conditions)
  - ModernFix issue #503: MC 1.21.x [Incompatibility] Additional Placement Fabric with the Dynamic Ressouce Loading option enabled
  - https://github.com/embeddedt/ModernFix/issues/503
  - retrieved by: hybrid_c#9@r16l
  - excerpt: fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb73304 |-- fabric-rendering-v1 10.1.2+b874120c04 |-- fabric-resource-conditions-api-v1 5.0.13+203e6b2304 |-- fabric-resource-loader-v0 3.0.11+b1caf1e904 |-- fabric-screen-api-v1 2.0.38+7feeb73304 |-- fabric-screen-handler-api-v1 1.3.110+7feeb73304 |-- fabric-sound-api-v1 [... truncated] [comment by Lonseuks (none)] Same happen with the Neoforge version 1.21.x https://mclo.gs/SmqtUPw [comment by embeddedt (owner)] https://github.com/FirEmerald/AdditionalPlacement

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: bm25_a#9@r16l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#10@r16c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: hybrid_c#10@r16c
  - excerpt: $registerEventHandlers$2(BetterModsButtonNeoForgeClient.java:53) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.ConsumerEventHandler.invoke(ConsumerEventHandler.java:26) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:315) at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.gui.screens.Screen.init [... truncated] [comment by P3pp3rF1y (owner)] I don't see anything related to sophisticated in this crash log other than the fact that it's one of the mods on the list.

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 1/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: bm25_b#10@r16c
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 1/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: bm25_b#10@r16l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#11** (github_issue, 1/6 conditions)
  - YUNGs-API issue #11: crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/11
  - retrieved by: dense_b#10@r16c
  - excerpt: [issue by Giyuubutdiff] when i put yungs api forge 12 in my mods and launch tlauncher it crashes [comment by TelepathicGrunt (none)] Tlauncher is a piracy software to play minecraft without paying for it. Most mod developers will not provide support for people using tlauncher because that launcher is against Mojang's terms of service and isn't legal. You should switch to using GDLauncher, MultiMC, or CurseForge's launcher for playing with mods as those are legal and safer to use. And more mod developers will be willing to help you out. If the game still crashes using one of these other lau

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#10@r16c
  - excerpt: cpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\librari

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#10@r16l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

## Added by hand

(none)
