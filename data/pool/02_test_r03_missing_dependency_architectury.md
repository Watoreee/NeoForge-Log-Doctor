# Judging sheet 02: `r03_missing_dependency_architectury` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `architectury`  |  **Acceptable:** architectury, cobblemon_battle_tower, fightorflight, wild_battle_api
- **What was broken:** disabled Architectury API in CurseForge; rctapi was auto-disabled as its dependent
- **Logs in this scenario:** r03_crash, r03_latest
- **Documents to judge:** 55

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 6/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#3@r03c, hybrid_c#5@r03c, bm25_b#7@r03c, dense_b#9@r03c, hybrid_a#2@r03l, hybrid_b#9@r03l, hybrid_c#9@r03l, bm25_a#5@r03l
  - excerpt: ArchitecturyTransformer > Task :common:processIncludeJars UP-TO-DATE > Task :common:jar UP-TO-DATE > Task :neoforge:compileJava UP-TO-DATE > Task :neoforge:classes UP-TO-DATE > Task :neoforge:configureLaunch > Task :neoforge:downloadAssets UP-TO-DATE > Task :neoforge:configureClientLaunch > Task :neoforge:runClient [Architectury Transformer] Architectury Runtime 5.2.91 [Architectury Transformer] Read classpath in 1.061 s [Architectury Transformer] Listening at C:\Users\<user>\Documents\01Developpement\Projets\DopedHorses\common\build\libs\dopedhorses-common-1.2.4-26.1-dev.jar [23:03:14] [main

- [ ] **gh-issue:architectury/architectury-api#497** (github_issue, 5/6 conditions)
  - architectury-api issue #497: [1.20.5] architectury crash on neoforge
  - https://github.com/architectury/architectury-api/issues/497
  - retrieved by: hybrid_b#1@r03c, hybrid_c#2@r03c, bm25_b#10@r03c, dense_b#4@r03c, hybrid_a#9@r03l
  - excerpt: [issue by st0x0ef] Architectury doesn't load on neoforge since it try to use the ClientTickEvent CrashLog : ``` Caused by 0: java.lang.NoClassDefFoundError: net/neoforged/neoforge/event/TickEvent$ClientTickEvent at java.base/java.lang.Class.getDeclaredMethods0(Native Method) ~[?:?] {} at java.base/java.lang.Class.privateGetDeclaredMethods(Class.java:3578) ~[?:?] {} at java.base/java.lang.Class.getDeclaredMethods(Class.java:2676) ~[?:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.register(EventBus.java:85) ~[bus-7.2.0.jar%2394!/:?] {} at TRANSFORMER/archi

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 5/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: hybrid_b#5@r03c, hybrid_c#3@r03c, dense_b#8@r03c, hybrid_a#1@r03l, bm25_a#2@r03l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 5/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: hybrid_b#6@r03c, hybrid_c#7@r03c, bm25_b#8@r03c, dense_b#10@r03c, hybrid_a#10@r03l
  - excerpt: .java:220) > Task :neoforge:dev.architectury.transformer.TransformerRuntime.main() FAILED ``` https://github.com/thedarkcolour/KotlinForForghttps://github.com/thedarkcolour/KotlinForForge/issues/103e/issues/103 ``` modImplementation("thedarkcolour:kotlinforforge-neoforge:5.5.0") { exclude group: "net.neoforged.fancymodloader", module: "loader" } ``` ``` Exception in thread "main" java.lang.RuntimeException: java.lang.reflect.InvocationTargetException at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.LaunchServiceHandlerDecorator.launch(LaunchServiceHan

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 4/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: hybrid_b#10@r03c, dense_b#1@r03c, hybrid_a#6@r03l, hybrid_b#1@r03l, hybrid_c#4@r03l, dense_b#2@r03l
  - excerpt: to dig into it a bit and sadly "Mo´ Structures" was the mod using that configfile and causing the crash. It´s a bit dissapointing not to be able to use the mod (liked it very much) but at least i can play again. Again, thank you very much for your patience and helping me out :-) [comment by SirTwsted (none)] ![Screenshot_308](https://github.com/user-attachments/assets/285348a0-af89-42a0-ad0a-6fa574b0772e) [crash-2024-07-19_08.55.05-client.txt](https://github.com/user-attachments/files/16312649/crash-2024-07-19_08.55.05-client.txt) Using MC v1.21 and on NEOForge v21.0.109 . [comme

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 4/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#3@r03c, hybrid_a#3@r03l, hybrid_b#4@r03l, hybrid_c#7@r03l, dense_b#1@r03l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 4/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: hybrid_b#4@r03c, hybrid_c#6@r03c, dense_b#7@r03c, hybrid_a#7@r03l, hybrid_b#2@r03l, hybrid_c#3@r03l, dense_b#3@r03l
  - excerpt: er:A} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.<init>(Minecraft.java:636) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:A [... truncated] [comment by Jab125 (member)] this looks similar to #527, so i'm going to close this issue [comment by jelly612 (none)] But how do i fix this? [comment by Jab125 (member)] do you have a mod installed called `omegaconfig`?, if so, remove it and see if the issue persists [comment by jelly612 (none)] I don´t have that mod hopefull

- [ ] **gh-issue:architectury/architectury-api#748** (github_issue, 4/6 conditions)
  - architectury-api issue #748: NeoForge fails to launch with architectury-api (except 26.2)
  - https://github.com/architectury/architectury-api/issues/748
  - retrieved by: hybrid_b#8@r03c, hybrid_b#3@r03l, hybrid_c#5@r03l, bm25_b#6@r03l, dense_b#8@r03l
  - excerpt: this is my 26.1 instance running with only architectury-api installed https://pastebin.com/uG2GesT5 [comment by st0x0ef (collaborator)] You have architectury 20.0.4 installed, the latest is 20.1.16. [comment by Lilyy2565 (none)] 20.1.16 does not appear to be released on modrinth, where can I obtain this version? <img width="948" height="439" alt="Image" src="https://github.com/user-attachments/assets/6d803926-854d-4352-a0d2-b9723316fb43" /> [comment by st0x0ef (collaborator)] <img width="894" height="124" alt="Image" src="https://github.com/user-attachments/assets/a78fd6b0-6b4c-4607-b1ec-1

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#5@r03c, hybrid_a#8@r03l, bm25_a#1@r03l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:thedarkcolour/KotlinForForge#103** (github_issue, 3/6 conditions)
  - KotlinForForge issue #103: [1.21 NeoForge] Architectury - Module fml_loader reads another module named fml_loader
  - https://github.com/thedarkcolour/KotlinForForge/issues/103
  - retrieved by: hybrid_b#2@r03c, hybrid_c#4@r03c, bm25_b#4@r03c, hybrid_b#6@r03l, hybrid_c#2@r03l, bm25_b#4@r03l
  - excerpt: t figure out whether the issue is with KFF or Architectury so making [an issue for Architectury too](https://github.com/architectury/architectury-api/issues/543). Architectury Enabled Platforms: Fabric, NeoForge Minecraft Version: 1.21 Architectury API Version: 13.0.4 NeoForge Version: 21.0.86-beta KotlinForForge Version: 5.4.0 [comment by thedarkcolour (owner)] This is a bug in Loom. It doesn't happen in plain ModDevGradle/NeoGradle. That being said, have you tried excluding KFF's transitive dependency on FancyModLoader? Has group: `net.neoforged.fancymodloader` and name: `loader`.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 3/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: hybrid_c#10@r03l, bm25_a#9@r03l, bm25_b#5@r03l
  - excerpt: mods} [19:57:12] [main/INFO]: Found mod file architectury-9.1.12-forge.jar of type MOD with provider {mods folder locator at C:\Users\<user>\Twitch\Minecraft\Instances\Tome of Ahsenna\mods} [19:57:12] [main/INFO]: Found mod file athena-forge-1.20.1-3.1.1.jar of type MOD with provider {mods folder locator at C:\Users\<user>\Twitch\Minecraft\Instances\Tome of Ahsenna\mods} [19:57:12] [main/INFO]: Found mod file balm-forge-1.20.1-7.1.4.jar of type MOD with provider {mods folder locator at C:\Users\<user>\Twitch\Minecraft\Instances\Tome of Ahsenna\mods} [19:57:12] [main/INFO]: Found mod file b

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r03c, bm25_a#3@r03c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 2/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: hybrid_c#1@r03c, hybrid_c#1@r03l, bm25_b#1@r03l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 2/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r03c, bm25_b#1@r03c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r03c, bm25_a#2@r03c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 2/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#9@r03c, bm25_b#2@r03c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#4@r03l, bm25_a#3@r03l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: bm25_b#9@r03c, hybrid_b#5@r03l, bm25_b#3@r03l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 2/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: hybrid_a#6@r03c, bm25_a#4@r03c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 2/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#8@r03c, bm25_b#6@r03c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:thedarkcolour/KotlinForForge#65** (github_issue, 2/6 conditions)
  - KotlinForForge issue #65: 1.19.4 file crashes game
  - https://github.com/thedarkcolour/KotlinForForge/issues/65
  - retrieved by: hybrid_c#6@r03l, bm25_b#8@r03l
  - excerpt: [issue by Droolphobia] Hello I'm currently in the process of installing the Cobblemon mod, it requires Kotlin, and I've made sure it was this specific file that is causing the issue. I need version 1.19.4 for the mod, but whenever I launch the game with the file installed, the game crashes before launch and I get a crash exit code:1. I'm not familiar at all with programming, and I'm not the brightest with tech in general, so perhaps I'm doing something wrong here. I should say that I'm putting this file in my mods folder. I appreciate any help I can get, thank you! [comment by davidromrell (n

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#7@r03c, bm25_a#7@r03c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TwelveIterations/Waystones#905** (github_issue, 2/6 conditions)
  - Waystones issue #905: Game not saving after activating waystone
  - https://github.com/TwelveIterations/Waystones/issues/905
  - retrieved by: hybrid_c#8@r03l, bm25_b#9@r03l
  - excerpt: uld not parse version number component '1a'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [14:11:22] [main/WARN]: Warnings were found! - Mod 'ModMenu Badges Lib' (modmenu-badges-lib) 2023.6.1 recommends any version of modmenu, which is missing! - You should install any version of modmenu for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg) 2024.6.2 recommends any version of emi, which is missing! - You should install any version of emi for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg)

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 2/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#10@r03c, hybrid_c#9@r03c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 2/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: hybrid_b#9@r03c, hybrid_c#10@r03c
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r03c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:architectury/architectury-api#542** (github_issue, 1/6 conditions)
  - architectury-api issue #542: "Architectury is not available" with the latest mod version
  - https://github.com/architectury/architectury-api/issues/542
  - retrieved by: dense_b#2@r03c, dense_b#6@r03l
  - excerpt: [issue by Shadowglitchjpg] NeoForge version: 21.0.86 Mod version: 13.0.4 When I try to launch the game with the latest version of the mod, it crashes. ![AAAAAAAAAA](https://github.com/user-attachments/assets/4c1988aa-cdb9-4dd8-a22b-5012d1a5c9d8) [comment by Jab125 (member)] We need logs to provide support, open a new issue with the logs attached. [comment by Jab125 (member)] You could see if it is related to #528

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#2@r03l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: bm25_b#3@r03c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#3@r03c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:architectury/architectury-api#557** (github_issue, 1/6 conditions)
  - architectury-api issue #557: mod compiled in java 22 (i can be wrong)
  - https://github.com/architectury/architectury-api/issues/557
  - retrieved by: dense_b#4@r03l
  - excerpt: [issue by IINovaIl] so I've been trying to get my 1.21 profile to run and after a bunch of skull crushing and having to ask chatGPT. I've come to the conclusion that architectury's latest version for 1.21 has been compiled in java 22 which minecraft doesn't use on 1.21/.1 a log and some info below mod loader: fabric mod loader V: 0.16.3 mc V: 1.21 crash report: https://mclo.gs/afNRkSH NOTICE: if this is not related to architectury then i apologize for wasting time. [comment by Jab125 (member)] Perhaps check out if puzzleslib is causing a problem

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#4@r03l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r03c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 1/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: hybrid_a#5@r03c
  - excerpt: ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.234 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:instancing OpenGL Renderer: Intel(R) UHD Graphics OpenGL Version: 4.6.0 - Build 31.0.101.2127 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecr

- [ ] **gh-issue:architectury/architectury-api#504** (github_issue, 1/6 conditions)
  - architectury-api issue #504: Architectury fails to load on neoforge 20.6.61-beta
  - https://github.com/architectury/architectury-api/issues/504
  - retrieved by: dense_b#5@r03c
  - excerpt: [issue by Manos654764] the mod fails to load. provided is the crash log: https://mclo.gs/bjdLIWS please fix. [comment by Jab125 (member)] See #494 [comment by Jab125 (member)] Closed with the merge of #494

- [ ] **gh-issue:architectury/architectury-api#535** (github_issue, 1/6 conditions)
  - architectury-api issue #535: Architectury api always crashing
  - https://github.com/architectury/architectury-api/issues/535
  - retrieved by: dense_b#6@r03c, dense_b#5@r03l
  - excerpt: [issue by AdithyaGithubRepos] What the hell is this mod's problem? Like what, does this mod expect us to have mods that ONLY support architectury api? I'm tired of these crash logs and half of my mods had to be removed in 1.16.5. DO SOMETHING! MANY MODS DEPEND ON YOUR API! [comment by Jab125 (member)] What is the crash report/logs?, we can't help without log files [comment by AdithyaGithubRepos (none)] Will send. On Sun, 7 Jul 2024, 13:56 Jab125, ***@***.***> wrote: > What is the crash report/logs?, we can't help without log files > > — > Reply to this email directly, view it on Git

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#5@r03l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#6@r03c
  - excerpt: tes (4572 MiB) / 8589934592 bytes (8192 MiB) up to 8589934592 bytes (8192 MiB) Total Memory: 3890826992 bytes (3710 MiB) / 8589934592 bytes (8192 MiB) CPU: AMD Ryzen 9 5900HS with Radeon Graphics @ 3.29 GHz; 8 cores / 16 threads on 1 socket(s) Graphics card #0: AMD Radeon(TM) Graphics (Advanced Micro Devices, Inc. (0x1002)); 512.00 MB of VRAM Graphics card #1: NVIDIA GeForce RTX 3050 Ti Laptop GPU (NVIDIA (0x10de)); 4095.00 MB of VRAM Other Mods: KubeJS: 2001.6.5-build.16 Horseman: 1.3.15 Simple Magnets: 1.1.12 KubeJSCurios: 1.0.4 Fabric Rendering Fluids (v1): 3.0.29+4ac5e37a77 Fabr

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#6@r03l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:TwelveIterations/Waystones#1207** (github_issue, 1/6 conditions)
  - Waystones issue #1207: Compatibility Issue with Riding in Cobblemon
  - https://github.com/TwelveIterations/Waystones/issues/1207
  - retrieved by: bm25_a#7@r03l
  - excerpt: [issue by OutOfOrderCandy] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Version that is casing an issue : waystones-fabric-1.21.1-21.1.37.jar Balm version : balm-fabric-1.21.1-21.0.63 Fabric API : 0.116.14 Cobblemon : 1.7.3 If you try to use waystones while riding a pokemon, this leaves traces of the pokemon and sometimes causing crashes to server. https://imgur.com/a/mR9y5hl It works fine on version before 21.1.37 ### Logs [crash-2026-07-18_17.40.27-server.txt](https://github.com/user-attachments/files/30160941/crash-2026-07-18_17.40.27-server.txt) [c

- [ ] **gh-issue:architectury/architectury-api#727** (github_issue, 1/6 conditions)
  - architectury-api issue #727: Crash with allowCharType on Architectury 20.0.8/21.0.3
  - https://github.com/architectury/architectury-api/issues/727
  - retrieved by: dense_b#7@r03l
  - excerpt: [issue by Madis0] The users of my modpack report crashes with Architectury 20.0.8 and Minecraft 26.1.2/21.0.3 and 26.2, that did not happen on Architectury 20.0.7. Since Architectury is not currently a part of the modpack, each user has a different set of mods they got the crash with. Crash logs / latest logs: https://mclo.gs/q748ONJ / https://mclo.gs/DQaW8fg https://mclo.gs/1CyspDv / https://mclo.gs/nWjC1W9 https://mclo.gs/bMNzPui / https://mclo.gs/Lhu6APv Related to https://github.com/architectury/architectury-api/issues/726 [comment by st0x0ef (collaborator)] You need to update fabric a

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#7@r03l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 1/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_b#7@r03l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 1/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#7@r03c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#8@r03c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:architectury/architectury-api#538** (github_issue, 1/6 conditions)
  - architectury-api issue #538: architectury-13.0.3-neoforge.jar causing game to crash when trying to open the crative inventory
  - https://github.com/architectury/architectury-api/issues/538
  - retrieved by: hybrid_c#8@r03c
  - excerpt: [issue by CsillaAria] I'm on NeoForge 21.0.78, but the issue started before that. Everything works fine in survival but trying to open the inventory in creative mode causes the game to crash. Exit Code: -1 message: The game crashed whilst unexpected error Error: net.neoforged.fml.ModLoadingException: Loading errors encountered: Crash Report: https://bytebin.lucko.me/ULsHK3DSvJ [comment by Kevin-Marsh (none)] I also have this issue. Neoforge had a breaking change that effect Architectury. I do not know if that is related though. SpawnPlacementRegisterEvent renamed to RegisterSpawnPla

- [ ] **gh-issue:architectury/architectury-api#551** (github_issue, 1/6 conditions)
  - architectury-api issue #551: IClientFluidTypeExtension for Neo
  - https://github.com/architectury/architectury-api/issues/551
  - retrieved by: hybrid_b#8@r03l
  - excerpt: that break due to the texture being null incorrectly. If it is up to the modder to register these extensions, you may want to put in some safe guards to inform a dev that they are missing at the very least to try to mitigate the number that slip through. Example of a mod that has recently come by my issue tracker: https://github.com/st0x0ef/stellaris/issues/17 [comment by MaxNeedsSnacks (member)] I haven't worked on Architectury in a hot minute, but from a cursory glance I found out that the mod doesn't seem to actually register fluid types? This should probably additionally be looked at f

- [ ] **gh-issue:architectury/architectury-api#736** (github_issue, 1/6 conditions)
  - architectury-api issue #736: crash when create new world
  - https://github.com/architectury/architectury-api/issues/736
  - retrieved by: bm25_a#8@r03l
  - excerpt: shut down the game with console... and there is no crash report generated. and in the latest.log: ``` [297��2026 22:48:12.871] [Render thread/INFO] [KubeJS Tweaks/]: Testing [297��2026 22:48:12.881] [Render thread/WARN] [KubeJS Server/]: Due to the way Minecraft resource loading works, KubeJS' server.log may not contain everything that happened in your server scripts on initial world creation. [297��2026 22:48:12.882] [Render thread/WARN] [KubeJS Server/]: You can still see the full log (including past reloads) in your latest.log file. [297��2026 22:48:12.888] [Render thread/INFO] [FluxNetwor

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: dense_b#9@r03l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r03c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#10@r03l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#10@r03c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:TwelveIterations/Waystones#1126** (github_issue, 1/6 conditions)
  - Waystones issue #1126: Natural Waystone activation invalid.
  - https://github.com/TwelveIterations/Waystones/issues/1126
  - retrieved by: dense_b#10@r03l
  - excerpt: ] [main/INFO]: Loading 217 mods: - achiopt 2.1.2 - amplified_nether 1.2.13 - animal_feeding_trough 1.2.0+1.21.11 - appleskin 3.0.8+mc1.21.11 - architectury 19.0.1 - awcapi 1.0.2 - balm 21.11.6 \-- kuma_api 21.11.12 - better-doors 1.0.3 \-- com_moandjiezana_toml_toml4j 0.7.2 - bettercombat 3.0.0 \-- tiny_config 3.1.0 - betterstats 5.0.0-beta.5+fabric-1.21.11 - boids 2.0.0+1.21.11 \-- blue_endless_jankson 1.2.3 - brainierbees 1.9.0 - c2me 0.3.7+alpha.0.7+1.21.11 |-- c2me-base 0.3.7+alpha.0.7+1.21.11 |-- c2me-client-uncapvd 0.3.7+alpha.0.7+1.21.11 |-- c2me

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#10@r03l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_b#10@r03l
  - excerpt: :\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\javafmllanguage\1.19.2-43.4.20\javafmllanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\lowcodelanguage\1.19.2-43.4.20\lowcodelanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecr

## Added by hand

(none)
