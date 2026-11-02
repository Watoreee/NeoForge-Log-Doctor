# Judging sheet 12: `r17_version_mismatch_architectury` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `architectury`  |  **Acceptable:** architectury, accelerateddecay, chisel, cobblefurnies, cobblemon_battle_tower, factory_blocks, fightorflight, ftbchunks, ftbfiltersystem, ftblibrary, ftbranks, ftbteams, ftbultimine, ftbxmodcompat, mega_showdown, more_cobblemon_tweaks, observable, octolib, oracle_index, oritech, polylib, rctapi, shrink, simpletms, wild_battle_api, zamega
- **What was broken:** replaced Architectury API with the Fabric build (architectury-fabric-22.0.5.jar); NeoForge skipped it as a Fabric mod, so 25 mods reported architectury as not installed
- **Logs in this scenario:** r17_crash, r17_latest
- **Documents to judge:** 58

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 6/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#4@r17c, hybrid_c#2@r17c, bm25_b#7@r17c, dense_b#9@r17c, hybrid_a#3@r17l, hybrid_c#1@r17l, bm25_a#6@r17l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:architectury/architectury-api#497** (github_issue, 5/6 conditions)
  - architectury-api issue #497: [1.20.5] architectury crash on neoforge
  - https://github.com/architectury/architectury-api/issues/497
  - retrieved by: hybrid_b#1@r17c, hybrid_c#3@r17c, bm25_b#10@r17c, dense_b#3@r17c, hybrid_a#9@r17l, hybrid_c#2@r17l
  - excerpt: [issue by st0x0ef] Architectury doesn't load on neoforge since it try to use the ClientTickEvent CrashLog : ``` Caused by 0: java.lang.NoClassDefFoundError: net/neoforged/neoforge/event/TickEvent$ClientTickEvent at java.base/java.lang.Class.getDeclaredMethods0(Native Method) ~[?:?] {} at java.base/java.lang.Class.privateGetDeclaredMethods(Class.java:3578) ~[?:?] {} at java.base/java.lang.Class.getDeclaredMethods(Class.java:2676) ~[?:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.register(EventBus.java:85) ~[bus-7.2.0.jar%2394!/:?] {} at TRANSFORMER/archi

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 5/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: hybrid_b#5@r17c, hybrid_c#5@r17c, dense_b#6@r17c, hybrid_a#2@r17l, bm25_a#9@r17l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 4/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: hybrid_b#8@r17c, hybrid_c#7@r17c, dense_b#8@r17c, hybrid_a#7@r17l, hybrid_b#1@r17l, hybrid_c#3@r17l, dense_b#3@r17l
  - excerpt: er:A} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.<init>(Minecraft.java:636) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:A [... truncated] [comment by Jab125 (member)] this looks similar to #527, so i'm going to close this issue [comment by jelly612 (none)] But how do i fix this? [comment by Jab125 (member)] do you have a mod installed called `omegaconfig`?, if so, remove it and see if the issue persists [comment by jelly612 (none)] I don´t have that mod hopefull

- [ ] **gh-issue:architectury/architectury-api#748** (github_issue, 4/6 conditions)
  - architectury-api issue #748: NeoForge fails to launch with architectury-api (except 26.2)
  - https://github.com/architectury/architectury-api/issues/748
  - retrieved by: hybrid_b#5@r17l, hybrid_c#9@r17l, bm25_b#6@r17l, dense_b#8@r17l
  - excerpt: this is my 26.1 instance running with only architectury-api installed https://pastebin.com/uG2GesT5 [comment by st0x0ef (collaborator)] You have architectury 20.0.4 installed, the latest is 20.1.16. [comment by Lilyy2565 (none)] 20.1.16 does not appear to be released on modrinth, where can I obtain this version? <img width="948" height="439" alt="Image" src="https://github.com/user-attachments/assets/6d803926-854d-4352-a0d2-b9723316fb43" /> [comment by st0x0ef (collaborator)] <img width="894" height="124" alt="Image" src="https://github.com/user-attachments/assets/a78fd6b0-6b4c-4607-b1ec-1

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 3/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#5@r17c, hybrid_a#1@r17l, hybrid_b#6@r17l, dense_b#1@r17l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#5@r17c, hybrid_a#6@r17l, bm25_a#1@r17l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 3/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r17c, hybrid_c#1@r17c, bm25_b#1@r17c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 3/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#2@r17c, bm25_a#6@r17c, hybrid_c#6@r17l
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#3@r17c, bm25_a#2@r17c, bm25_b#2@r17c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 3/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: hybrid_c#9@r17c, hybrid_a#8@r17l, hybrid_c#10@r17l, bm25_a#2@r17l
  - excerpt: comment by caionodaryluz-ctrl (none)] Minecraft Crash Report ---- // Hey, that tickles! Hehehe! Time: 2026-09-25 22:02:55 Description: mouseClicked event handler java.lang.NullPointerException: Cannot invoke "com.cobblemon.mod.relocations.graalvm.polyglot.Value.execute(Object[])" because "receiveMoveDataFn" is null at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.lambda$movesLoad$0(Moves.java:48) at knot//com.cobblemon.mod.common.battles.ShowdownThread.queue(ShowdownThread.java:32) at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.movesLo

- [ ] **gh-issue:thedarkcolour/KotlinForForge#103** (github_issue, 3/6 conditions)
  - KotlinForForge issue #103: [1.21 NeoForge] Architectury - Module fml_loader reads another module named fml_loader
  - https://github.com/thedarkcolour/KotlinForForge/issues/103
  - retrieved by: hybrid_b#2@r17c, hybrid_c#4@r17c, bm25_b#4@r17c, hybrid_b#3@r17l, hybrid_c#7@r17l, bm25_b#5@r17l
  - excerpt: t figure out whether the issue is with KFF or Architectury so making [an issue for Architectury too](https://github.com/architectury/architectury-api/issues/543). Architectury Enabled Platforms: Fabric, NeoForge Minecraft Version: 1.21 Architectury API Version: 13.0.4 NeoForge Version: 21.0.86-beta KotlinForForge Version: 5.4.0 [comment by thedarkcolour (owner)] This is a bug in Loom. It doesn't happen in plain ModDevGradle/NeoGradle. That being said, have you tried excluding KFF's transitive dependency on FancyModLoader? Has group: `net.neoforged.fancymodloader` and name: `loader`.

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#5@r17c, hybrid_b#3@r17c, bm25_b#3@r17c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 3/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: hybrid_b#6@r17c, hybrid_c#10@r17c, bm25_b#9@r17c
  - excerpt: lementation("dev.isxander:yet-another-config-lib:${rootProject.yacl_version}-neoforge") { exclude(group: "net.neoforged.fancymodloader", module: "loader") } ``` I get _almost_ the same error as before, except it says `fml_loader` found multiple copies of `fml_loader`, instead of KFF finding them: ``` Exception in thread "main" java.lang.module.ResolutionException: Module fml_loader reads another module named fml_loader ``` I can't really tell if this is progress or just a shifting goalpost. Edit: If it's better for me to create a new ticket and/or move the conversation to Discord, I am

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 2/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: hybrid_a#9@r17c, bm25_a#1@r17c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 2/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#1@r17c, hybrid_b#4@r17l, dense_b#2@r17l
  - excerpt: found. So I am a bit confused. [comment by RockinOstrich (none)] When I use NeoForge 21.1.31, it's fine, but if I try updating it to Neoforge 21.1.32+, I get that crash report (the one SirTwsted got), and that's the only thing I've changed. Any suggestions? I know you mentioned above about omegaconfig, but I don't know how to read or interpret a crash report: [crash-2024-10-21_20.18.46-client.txt](https://github.com/user-attachments/files/17468161/crash-2024-10-21_20.18.46-client.txt) [comment by Redfan2 (none)] > > omegaconfig > > @Jab125 > > I don't understand. I typed omegaconfig

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 2/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: hybrid_c#6@r17c, bm25_b#1@r17l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#7@r17c, hybrid_b#2@r17l, bm25_b#3@r17l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#10@r17l, bm25_a#3@r17l
  - excerpt: loading phase: Mod sodium_extra requires sodium 0.8.12-alpha.3+mc1.21.1 or above Currently, sodium is 0.6.13+mc1.21.1 Error during pre-loading phase: Mod reeses_sodium_options requires sodium 0.8.12-alpha.3 or above Currently, sodium is 0.6.13+mc1.21.1 ``` [comment by Official-V-Zer0 (none)] It may be due to the crashlog only formed after getting through the load screen hence Sodium being 0.6.13, but using 0.8.12-beta.1 is the issue [comment by jellysquid3 (member)] Your log files and crash logs do not relate to each other. The log file contains the actual error, not the crash report. Pleas

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 2/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: hybrid_a#6@r17c, hybrid_a#4@r17l, hybrid_c#4@r17l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 2/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: hybrid_a#5@r17l, hybrid_c#8@r17l
  - excerpt: [issue by KP2048] ``` [Architectury Transformer] Architectury Runtime 5.2.61 [Architectury Transformer] Read classpath in 1.251 s [Architectury Transformer] Listening at C:\Users\<user>\Documents\MCDEV\Minitect\common\build\devlibs\minitect-1.0.0-dev.jar [09:56:15] [main/INFO] (Launcher) ModLauncher running: args [--launchTarget, forgeclientuserdev, --version, MOD_DEV, --assetIndex, 1.18.1-1.18, --assetsDir, C:\Users\<user>\.gradle\caches\fabric-loom\assets, --gameDir, ., --fml.forgeVersion, 39.0.64, --fml.mcVersion, 1.18.1, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20211210.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 2/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_b#9@r17c, dense_b#7@r17l
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 2/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#8@r17c, bm25_b#8@r17c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#1@r17c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:architectury/architectury-api#542** (github_issue, 1/6 conditions)
  - architectury-api issue #542: "Architectury is not available" with the latest mod version
  - https://github.com/architectury/architectury-api/issues/542
  - retrieved by: dense_b#2@r17c, dense_b#4@r17l
  - excerpt: [issue by Shadowglitchjpg] NeoForge version: 21.0.86 Mod version: 13.0.4 When I try to launch the game with the latest version of the mod, it crashes. ![AAAAAAAAAA](https://github.com/user-attachments/assets/4c1988aa-cdb9-4dd8-a22b-5012d1a5c9d8) [comment by Jab125 (member)] We need logs to provide support, open a new issue with the logs attached. [comment by Jab125 (member)] You could see if it is related to #528

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#2@r17l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#3@r17c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#4@r17c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#4@r17l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:architectury/architectury-api#504** (github_issue, 1/6 conditions)
  - architectury-api issue #504: Architectury fails to load on neoforge 20.6.61-beta
  - https://github.com/architectury/architectury-api/issues/504
  - retrieved by: dense_b#4@r17c, dense_b#9@r17l
  - excerpt: [issue by Manos654764] the mod fails to load. provided is the crash log: https://mclo.gs/bjdLIWS please fix. [comment by Jab125 (member)] See #494 [comment by Jab125 (member)] Closed with the merge of #494

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#4@r17l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#5@r17c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 1/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: bm25_a#5@r17l
  - excerpt: 17 [07lip2022 18:29:10.993] [main/INFO] [cpw.mods.modlauncher.LaunchServiceHandler/MODLAUNCHER]: Launching target 'forgeclient' with arguments [--version, 1.19-forge-41.0.63, --gameDir, C:\Users\<user>\AppData\Roaming\.minecraft, --assetsDir, C:\Users\<user>\AppData\Roaming\.minecraft\assets, --uuid, <token>, --username, <player>, --assetIndex, 1.19, --accessToken, <token> truncated] [comment by BlayTheNinth (member)] Those logs are 99% OptiFine, are you sure that's the correct log? [comment by agabeluga (none)] I changed it. [comment by BlayTheNinth (member)] The Forge forum lied to you,

- [ ] **gh-issue:architectury/architectury-api#557** (github_issue, 1/6 conditions)
  - architectury-api issue #557: mod compiled in java 22 (i can be wrong)
  - https://github.com/architectury/architectury-api/issues/557
  - retrieved by: dense_b#5@r17l
  - excerpt: [issue by IINovaIl] so I've been trying to get my 1.21 profile to run and after a bunch of skull crushing and having to ask chatGPT. I've come to the conclusion that architectury's latest version for 1.21 has been compiled in java 22 which minecraft doesn't use on 1.21/.1 a log and some info below mod loader: fabric mod loader V: 0.16.3 mc V: 1.21 crash report: https://mclo.gs/afNRkSH NOTICE: if this is not related to architectury then i apologize for wasting time. [comment by Jab125 (member)] Perhaps check out if puzzleslib is causing a problem

- [ ] **gh-issue:embeddedt/ModernFix#503** (github_issue, 1/6 conditions)
  - ModernFix issue #503: MC 1.21.x [Incompatibility] Additional Placement Fabric with the Dynamic Ressouce Loading option enabled
  - https://github.com/embeddedt/ModernFix/issues/503
  - retrieved by: hybrid_c#5@r17l
  - excerpt: fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb73304 |-- fabric-rendering-v1 10.1.2+b874120c04 |-- fabric-resource-conditions-api-v1 5.0.13+203e6b2304 |-- fabric-resource-loader-v0 3.0.11+b1caf1e904 |-- fabric-screen-api-v1 2.0.38+7feeb73304 |-- fabric-screen-handler-api-v1 1.3.110+7feeb73304 |-- fabric-sound-api-v1 [... truncated] [comment by Lonseuks (none)] Same happen with the Neoforge version 1.21.x https://mclo.gs/SmqtUPw [comment by embeddedt (owner)] https://github.com/FirEmerald/AdditionalPlacement

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: bm25_b#6@r17c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:architectury/architectury-api#535** (github_issue, 1/6 conditions)
  - architectury-api issue #535: Architectury api always crashing
  - https://github.com/architectury/architectury-api/issues/535
  - retrieved by: dense_b#7@r17c, dense_b#6@r17l
  - excerpt: ne)] the same here: Neoforge: 21.0.87 Architectury: i try it with 4 versions available log: [log crash.txt](https://github.com/user-attachments/files/16202574/log.crash.txt) [comment by ascenstohe4vn (none)] i also have this issue [comment by Jab125 (member)] > the same here: > > Neoforge: 21.0.87 Architectury: i try it with 4 versions available > > log: [log crash.txt](https://github.com/user-attachments/files/16202574/log.crash.txt) Your crash is not related. You need to install [YACL](https://modrinth.com/mod/yacl).

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#7@r17l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#7@r17c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:TwelveIterations/Waystones#1202** (github_issue, 1/6 conditions)
  - Waystones issue #1202: Crash with FTB XMod Compat [Solution: Update FTB XMod Compat]
  - https://github.com/TwelveIterations/Waystones/issues/1202
  - retrieved by: hybrid_a#7@r17c
  - excerpt: [issue by lerai77] ### Minecraft Version 1.21.1 ### Mod Loader NeoForge ### Describe the Issue I usually play modpacks that allow for file editing; I'm currently playing AllTheMons. I updated Waystones to the latest version (1.21.1.36) and it crashed, so I had to revert to a previous version (1.21.1.35)—where the scroll button doesn't work. ### Logs [crash-2026-07-11_09.57.07-server.txt](https://github.com/user-attachments/files/29927302/crash-2026-07-11_09.57.07-server.txt) [comment by BlayTheNinth (member)] This is originating from FTB XMod Compat and is already being fixed (https://

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#7@r17l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 1/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_b#7@r17l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: bm25_a#8@r17c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 1/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: hybrid_b#8@r17l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:TwelveIterations/Waystones#1126** (github_issue, 1/6 conditions)
  - Waystones issue #1126: Natural Waystone activation invalid.
  - https://github.com/TwelveIterations/Waystones/issues/1126
  - retrieved by: bm25_a#8@r17l
  - excerpt: [issue by von-get] ### Minecraft Version 1.21.11 ### Mod Loader Fabric ### Describe the Issue When activating a new waystone found in a village (haven't found wild ones yet), it will 'successfully' activate it with the name 'invalid'. Right-clicking it again does not bring up the teleport menu, but instead just 'successfully' activates again. I didn't have this issue before upgrading to 21.11.5, and downgrading it to 21.11.4 seems to have resolved it. Additionally, picking up the waystone and putting it back down does seem to allow normal interaction. ### Logs ``` [00:27:08] [main/INF

- [ ] **gh-issue:architectury/architectury-api#541** (github_issue, 1/6 conditions)
  - architectury-api issue #541: Minecraft launcher crash - new crash file - Version 21.0.86
  - https://github.com/architectury/architectury-api/issues/541
  - retrieved by: hybrid_c#8@r17c
  - excerpt: [issue by Fidulus] https://pastebin.com/BtwY5fbk After updating everything to newest version game won´t start anymore. I hope my crash log helps locating any problems. It seems to me this is still an architectury issue. If that is not the case please tell me whats wrong instead, i´m not very good in reading the crash logs. Thank you [comment by TheeMrCheeky (none)] Ya I am having this issue with neoforge [crash-2024-07-12_07.10.01-client.txt](https://github.com/user-attachments/files/16192836/crash-2024-07-12_07.10.01-client.txt) [comment by Jab125 (member)] Duplicate of #527

- [ ] **gh-issue:thedarkcolour/KotlinForForge#65** (github_issue, 1/6 conditions)
  - KotlinForForge issue #65: 1.19.4 file crashes game
  - https://github.com/thedarkcolour/KotlinForForge/issues/65
  - retrieved by: bm25_b#8@r17l
  - excerpt: [issue by Droolphobia] Hello I'm currently in the process of installing the Cobblemon mod, it requires Kotlin, and I've made sure it was this specific file that is causing the issue. I need version 1.19.4 for the mod, but whenever I launch the game with the file installed, the game crashes before launch and I get a crash exit code:1. I'm not familiar at all with programming, and I'm not the brightest with tech in general, so perhaps I'm doing something wrong here. I should say that I'm putting this file in my mods folder. I appreciate any help I can get, thank you! [comment by davidromrell (n

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#9@r17c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:TwelveIterations/Waystones#905** (github_issue, 1/6 conditions)
  - Waystones issue #905: Game not saving after activating waystone
  - https://github.com/TwelveIterations/Waystones/issues/905
  - retrieved by: bm25_b#9@r17l
  - excerpt: uld not parse version number component '1a'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [14:11:22] [main/WARN]: Warnings were found! - Mod 'ModMenu Badges Lib' (modmenu-badges-lib) 2023.6.1 recommends any version of modmenu, which is missing! - You should install any version of modmenu for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg) 2024.6.2 recommends any version of emi, which is missing! - You should install any version of emi for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg)

- [ ] **gh-issue:architectury/architectury-api#551** (github_issue, 1/6 conditions)
  - architectury-api issue #551: IClientFluidTypeExtension for Neo
  - https://github.com/architectury/architectury-api/issues/551
  - retrieved by: hybrid_b#9@r17l
  - excerpt: that break due to the texture being null incorrectly. If it is up to the modder to register these extensions, you may want to put in some safe guards to inform a dev that they are missing at the very least to try to mitigate the number that slip through. Example of a mod that has recently come by my issue tracker: https://github.com/st0x0ef/stellaris/issues/17 [comment by MaxNeedsSnacks (member)] I haven't worked on Architectury in a hot minute, but from a cursory glance I found out that the mod doesn't seem to actually register fluid types? This should probably additionally be looked at f

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#10@r17c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: hybrid_b#10@r17l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:architectury/architectury-api#538** (github_issue, 1/6 conditions)
  - architectury-api issue #538: architectury-13.0.3-neoforge.jar causing game to crash when trying to open the crative inventory
  - https://github.com/architectury/architectury-api/issues/538
  - retrieved by: hybrid_b#10@r17c
  - excerpt: [issue by CsillaAria] I'm on NeoForge 21.0.78, but the issue started before that. Everything works fine in survival but trying to open the inventory in creative mode causes the game to crash. Exit Code: -1 message: The game crashed whilst unexpected error Error: net.neoforged.fml.ModLoadingException: Loading errors encountered: Crash Report: https://bytebin.lucko.me/ULsHK3DSvJ [comment by Kevin-Marsh (none)] I also have this issue. Neoforge had a breaking change that effect Architectury. I do not know if that is related though. SpawnPlacementRegisterEvent renamed to RegisterSpawnPla

- [ ] **gh-issue:architectury/architectury-api#575** (github_issue, 1/6 conditions)
  - architectury-api issue #575: [1.21] Architectury 13.0.8 is labelled as incompatible with 1.21.1 on Modrinth
  - https://github.com/architectury/architectury-api/issues/575
  - retrieved by: dense_b#10@r17l
  - excerpt: [issue by cassiancc] Architectury 13.0.8 is not labelled as compatible with 1.21.1, unlike 13.0.6. This causes some mods like Right Click Harvest that depend on 13.0.8 to crash when loaded with 13.0.6, despite that currently being the latest version that supports 1.21.1. [comment by shedaniel (member)] Thanks for reporting, this is now resolved

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#10@r17l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:wisp-forest/owo-lib#304** (github_issue, 1/6 conditions)
  - owo-lib issue #304: Game crashes 1.21.1
  - https://github.com/wisp-forest/owo-lib/issues/304
  - retrieved by: hybrid_a#10@r17c
  - excerpt: [issue by asanaik] **### When ever I try to launch the game it crashes after taking out owo libraries it doesn't crash. Here's my log file from the crash.** [17:23:21] [main/INFO]: Loading Minecraft 1.21.1 with Fabric Loader 0.16.3 [17:23:21] [main/WARN]: Warnings were found! - Mod 'Dynamic Lights' (dynamiclights) 1.8.3+mod recommends any version of modmenu, which is missing! - You should install any version of modmenu for the optimal experience. - Mod 'Dynamic Lights' (dynamiclights) 1.8.3+mod recommends any version of modmenu-badges-lib, which is missing! - You should install a

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: dense_b#10@r17c
  - excerpt: t.Constructor.newInstance(Constructor.java:486) ~[?:?] at MC-BOOTSTRAP/fml_loader@4.0.31/net.neoforged.fml.javafmlmod.FMLModContainer.constructMod(FMLModContainer.java:115) ~[loader-4.0.31.jar#175!/:4.0] at MC-BOOTSTRAP/fml_loader@4.0.31/net.neoforged.fml.ModLoader.lambda$constructMods$3(ModLoader.java:153) ~[loader-4.0.31.jar#175!/:4.0] at MC-BOOTSTRAP/fml_loader@4.0.31/net.neoforged.fml.ModLoader.lambda$dispatchParallelTask$7(ModLoader.java:231) ~[loader-4.0.31.jar#175!/:4.0] at java.base/java.util.concurrent.CompletableFuture.uniHandle(CompletableFuture.java:934) [?:?] at java.bas

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#10@r17l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

## Added by hand

(none)
