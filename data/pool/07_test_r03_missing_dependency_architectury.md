# Judging sheet 07: `r03_missing_dependency_architectury` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `architectury`  |  **Acceptable:** architectury, cobblemon_battle_tower, fightorflight, wild_battle_api
- **What was broken:** disabled Architectury API in CurseForge; rctapi was auto-disabled as its dependent
- **Logs in this scenario:** r03_crash, r03_latest
- **Documents to judge:** 30

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 4/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: hybrid_b#5@r03c, hybrid_c#4@r03c, hybrid_a#1@r03l, bm25_a#2@r03l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:architectury/architectury-api#497** (github_issue, 3/6 conditions)
  - architectury-api issue #497: [1.20.5] architectury crash on neoforge
  - https://github.com/architectury/architectury-api/issues/497
  - retrieved by: hybrid_b#1@r03c, hybrid_c#2@r03c, dense_b#4@r03c
  - excerpt: [issue by st0x0ef] Architectury doesn't load on neoforge since it try to use the ClientTickEvent CrashLog : ``` Caused by 0: java.lang.NoClassDefFoundError: net/neoforged/neoforge/event/TickEvent$ClientTickEvent at java.base/java.lang.Class.getDeclaredMethods0(Native Method) ~[?:?] {} at java.base/java.lang.Class.privateGetDeclaredMethods(Class.java:3578) ~[?:?] {} at java.base/java.lang.Class.getDeclaredMethods(Class.java:2676) ~[?:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.register(EventBus.java:85) ~[bus-7.2.0.jar%2394!/:?] {} at TRANSFORMER/archi

- [x] **gh-issue:architectury/architectury-api#528** (github_issue, 3/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#1@r03c, hybrid_b#1@r03l, hybrid_c#4@r03l, dense_b#2@r03l
  - excerpt: to dig into it a bit and sadly "Mo´ Structures" was the mod using that configfile and causing the crash. It´s a bit dissapointing not to be able to use the mod (liked it very much) but at least i can play again. Again, thank you very much for your patience and helping me out :-) [comment by SirTwsted (none)] ![Screenshot_308](https://github.com/user-attachments/assets/285348a0-af89-42a0-ad0a-6fa574b0772e) [crash-2024-07-19_08.55.05-client.txt](https://github.com/user-attachments/files/16312649/crash-2024-07-19_08.55.05-client.txt) Using MC v1.21 and on NEOForge v21.0.109 . [comme

- [x] **gh-issue:architectury/architectury-api#664** (github_issue, 3/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#3@r03c, hybrid_a#3@r03l, hybrid_b#3@r03l, dense_b#1@r03l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 3/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: hybrid_b#4@r03c, hybrid_b#2@r03l, hybrid_c#3@r03l, dense_b#4@r03l
  - excerpt: er:A} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.<init>(Minecraft.java:636) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:A [... truncated] [comment by Jab125 (member)] this looks similar to #527, so i'm going to close this issue [comment by jelly612 (none)] But how do i fix this? [comment by Jab125 (member)] do you have a mod installed called `omegaconfig`?, if so, remove it and see if the issue persists [comment by jelly612 (none)] I don´t have that mod hopefull

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 3/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#3@r03c, hybrid_c#5@r03c, hybrid_a#2@r03l
  - excerpt: ArchitecturyTransformer > Task :common:processIncludeJars UP-TO-DATE > Task :common:jar UP-TO-DATE > Task :neoforge:compileJava UP-TO-DATE > Task :neoforge:classes UP-TO-DATE > Task :neoforge:configureLaunch > Task :neoforge:downloadAssets UP-TO-DATE > Task :neoforge:configureClientLaunch > Task :neoforge:runClient [Architectury Transformer] Architectury Runtime 5.2.91 [Architectury Transformer] Read classpath in 1.061 s [Architectury Transformer] Listening at C:\Users\<user>\Documents\01Developpement\Projets\DopedHorses\common\build\libs\dopedhorses-common-1.2.4-26.1-dev.jar [23:03:14] [main

- [ ] **gh-issue:thedarkcolour/KotlinForForge#103** (github_issue, 3/6 conditions)
  - KotlinForForge issue #103: [1.21 NeoForge] Architectury - Module fml_loader reads another module named fml_loader
  - https://github.com/thedarkcolour/KotlinForForge/issues/103
  - retrieved by: hybrid_b#2@r03c, hybrid_c#3@r03c, bm25_b#4@r03c, hybrid_c#2@r03l, bm25_b#5@r03l
  - excerpt: t figure out whether the issue is with KFF or Architectury so making [an issue for Architectury too](https://github.com/architectury/architectury-api/issues/543). Architectury Enabled Platforms: Fabric, NeoForge Minecraft Version: 1.21 Architectury API Version: 13.0.4 NeoForge Version: 21.0.86-beta KotlinForForge Version: 5.4.0 [comment by thedarkcolour (owner)] This is a bug in Loom. It doesn't happen in plain ModDevGradle/NeoGradle. That being said, have you tried excluding KFF's transitive dependency on FancyModLoader? Has group: `net.neoforged.fancymodloader` and name: `loader`.

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r03c, bm25_a#4@r03c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 2/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: hybrid_c#1@r03c, hybrid_c#1@r03l, bm25_b#1@r03l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#5@r03c, bm25_a#1@r03l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 2/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r03c, bm25_b#1@r03c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r03c, bm25_a#3@r03c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#3@r03c, bm25_a#2@r03c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#4@r03l, bm25_a#3@r03l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [x] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#5@r03l, bm25_b#3@r03l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:architectury/architectury-api#748** (github_issue, 2/6 conditions)
  - architectury-api issue #748: NeoForge fails to launch with architectury-api (except 26.2)
  - https://github.com/architectury/architectury-api/issues/748
  - retrieved by: hybrid_b#4@r03l, hybrid_c#5@r03l
  - excerpt: this is my 26.1 instance running with only architectury-api installed https://pastebin.com/uG2GesT5 [comment by st0x0ef (collaborator)] You have architectury 20.0.4 installed, the latest is 20.1.16. [comment by Lilyy2565 (none)] 20.1.16 does not appear to be released on modrinth, where can I obtain this version? <img width="948" height="439" alt="Image" src="https://github.com/user-attachments/assets/6d803926-854d-4352-a0d2-b9723316fb43" /> [comment by st0x0ef (collaborator)] <img width="894" height="124" alt="Image" src="https://github.com/user-attachments/assets/a78fd6b0-6b4c-4607-b1ec-1

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r03c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#2@r03c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [x] **gh-issue:architectury/architectury-api#542** (github_issue, 1/6 conditions)
  - architectury-api issue #542: "Architectury is not available" with the latest mod version
  - https://github.com/architectury/architectury-api/issues/542
  - retrieved by: dense_b#2@r03c
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

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 1/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: dense_b#3@r03l
  - excerpt: jar:?] {} at cpw.mods.modlauncher.Launcher.main(Launcher.java:66) [modlauncher-8.0.9.jar:?] {} at io.github.zekerzhayard.forgewrapper.installer.Main.main(Main.java:50) [ForgeWrapper-1.4.2.jar:?] {} at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[?:1.8.0_271] {} at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at [... truncated] [comment by khorvo77 (none)] Sorry, Modlist: Mods: [✔️] [1.16.5]+SecurityCraft+v1.8.21.1 [✔️] abnormals_core-1.16

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#4@r03l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#4@r03l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#5@r03c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#5@r03l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 1/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: bm25_a#5@r03l
  - excerpt: 17 [07lip2022 18:29:10.993] [main/INFO] [cpw.mods.modlauncher.LaunchServiceHandler/MODLAUNCHER]: Launching target 'forgeclient' with arguments [--version, 1.19-forge-41.0.63, --gameDir, C:\Users\<user>\AppData\Roaming\.minecraft, --assetsDir, C:\Users\<user>\AppData\Roaming\.minecraft\assets, --uuid, <token>, --username, <player>, --assetIndex, 1.19, --accessToken, <token> truncated] [comment by BlayTheNinth (member)] Those logs are 99% OptiFine, are you sure that's the correct log? [comment by agabeluga (none)] I changed it. [comment by BlayTheNinth (member)] The Forge forum lied to you,

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: dense_b#5@r03l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:architectury/architectury-api#504** (github_issue, 1/6 conditions)
  - architectury-api issue #504: Architectury fails to load on neoforge 20.6.61-beta
  - https://github.com/architectury/architectury-api/issues/504
  - retrieved by: dense_b#5@r03c
  - excerpt: [issue by Manos654764] the mod fails to load. provided is the crash log: https://mclo.gs/bjdLIWS please fix. [comment by Jab125 (member)] See #494 [comment by Jab125 (member)] Closed with the merge of #494

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#5@r03c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

## Added by hand

(none)
