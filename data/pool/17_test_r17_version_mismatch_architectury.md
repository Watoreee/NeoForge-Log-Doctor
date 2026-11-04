# Judging sheet 17: `r17_version_mismatch_architectury` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `architectury`  |  **Acceptable:** architectury, accelerateddecay, chisel, cobblefurnies, cobblemon_battle_tower, factory_blocks, fightorflight, ftbchunks, ftbfiltersystem, ftblibrary, ftbranks, ftbteams, ftbultimine, ftbxmodcompat, mega_showdown, more_cobblemon_tweaks, observable, octolib, oracle_index, oritech, polylib, rctapi, shrink, simpletms, wild_battle_api, zamega
- **What was broken:** replaced Architectury API with the Fabric build (architectury-fabric-22.0.5.jar); NeoForge skipped it as a Fabric mod, so 25 mods reported architectury as not installed
- **Logs in this scenario:** r17_crash, r17_latest
- **Documents to judge:** 32

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:architectury/architectury-api#497** (github_issue, 3/6 conditions)
  - architectury-api issue #497: [1.20.5] architectury crash on neoforge
  - https://github.com/architectury/architectury-api/issues/497
  - retrieved by: hybrid_b#1@r17c, hybrid_c#3@r17c, dense_b#3@r17c, hybrid_c#2@r17l
  - excerpt: [issue by st0x0ef] Architectury doesn't load on neoforge since it try to use the ClientTickEvent CrashLog : ``` Caused by 0: java.lang.NoClassDefFoundError: net/neoforged/neoforge/event/TickEvent$ClientTickEvent at java.base/java.lang.Class.getDeclaredMethods0(Native Method) ~[?:?] {} at java.base/java.lang.Class.privateGetDeclaredMethods(Class.java:3578) ~[?:?] {} at java.base/java.lang.Class.getDeclaredMethods(Class.java:2676) ~[?:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.register(EventBus.java:85) ~[bus-7.2.0.jar%2394!/:?] {} at TRANSFORMER/archi

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 3/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: hybrid_b#1@r17l, hybrid_c#3@r17l, dense_b#3@r17l
  - excerpt: ishllama (none)] I am having this same issue. The mod list in the crash report mentions omegaconfig-neoforge-1.5.1.jar |Omega Config Architectury |omegaconfig |1.5.1 |Manifest: NOSIGNATURE, however, this is nowhere to be found in the mod folder. I have also looked for a download of it, but the 1.5.1 release doesn't seem to exist. Aside from removing any mods that rely on Architectury, are there any other solutions? [comment by ThexXTURBOXx (none)] It is part of various mods - you need to look inside the mod jars. Some of them contain other jars which are subsequently added to the classpath. S

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 3/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#4@r17c, hybrid_c#2@r17c, hybrid_a#3@r17l, hybrid_c#1@r17l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 3/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r17c, hybrid_c#1@r17c, bm25_b#1@r17c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#3@r17c, bm25_a#2@r17c, bm25_b#2@r17c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 3/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: hybrid_b#5@r17c, hybrid_c#5@r17c, hybrid_a#2@r17l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:thedarkcolour/KotlinForForge#103** (github_issue, 3/6 conditions)
  - KotlinForForge issue #103: [1.21 NeoForge] Architectury - Module fml_loader reads another module named fml_loader
  - https://github.com/thedarkcolour/KotlinForForge/issues/103
  - retrieved by: hybrid_b#2@r17c, hybrid_c#4@r17c, bm25_b#4@r17c, hybrid_b#3@r17l, bm25_b#5@r17l
  - excerpt: t figure out whether the issue is with KFF or Architectury so making [an issue for Architectury too](https://github.com/architectury/architectury-api/issues/543). Architectury Enabled Platforms: Fabric, NeoForge Minecraft Version: 1.21 Architectury API Version: 13.0.4 NeoForge Version: 21.0.86-beta KotlinForForge Version: 5.4.0 [comment by thedarkcolour (owner)] This is a bug in Loom. It doesn't happen in plain ModDevGradle/NeoGradle. That being said, have you tried excluding KFF's transitive dependency on FancyModLoader? Has group: `net.neoforged.fancymodloader` and name: `loader`.

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#5@r17c, hybrid_b#3@r17c, bm25_b#3@r17c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [x] **gh-issue:architectury/architectury-api#528** (github_issue, 2/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#1@r17c, hybrid_b#4@r17l, dense_b#2@r17l
  - excerpt: found. So I am a bit confused. [comment by RockinOstrich (none)] When I use NeoForge 21.1.31, it's fine, but if I try updating it to Neoforge 21.1.32+, I get that crash report (the one SirTwsted got), and that's the only thing I've changed. Any suggestions? I know you mentioned above about omegaconfig, but I don't know how to read or interpret a crash report: [crash-2024-10-21_20.18.46-client.txt](https://github.com/user-attachments/files/17468161/crash-2024-10-21_20.18.46-client.txt) [comment by Redfan2 (none)] > > omegaconfig > > @Jab125 > > I don't understand. I typed omegaconfig

- [x] **gh-issue:architectury/architectury-api#664** (github_issue, 2/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#5@r17c, hybrid_a#1@r17l, dense_b#1@r17l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#5@r17c, bm25_a#1@r17l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [x] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#2@r17l, bm25_b#3@r17l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 2/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: hybrid_a#4@r17l, hybrid_c#4@r17l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r17c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#1@r17c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#1@r17l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 1/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#2@r17c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [x] **gh-issue:architectury/architectury-api#542** (github_issue, 1/6 conditions)
  - architectury-api issue #542: "Architectury is not available" with the latest mod version
  - https://github.com/architectury/architectury-api/issues/542
  - retrieved by: dense_b#2@r17c, dense_b#4@r17l
  - excerpt: [issue by Shadowglitchjpg] NeoForge version: 21.0.86 Mod version: 13.0.4 When I try to launch the game with the latest version of the mod, it crashes. ![AAAAAAAAAA](https://github.com/user-attachments/assets/4c1988aa-cdb9-4dd8-a22b-5012d1a5c9d8) [comment by Jab125 (member)] We need logs to provide support, open a new issue with the logs attached. [comment by Jab125 (member)] You could see if it is related to #528

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 1/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: bm25_a#2@r17l
  - excerpt: comment by caionodaryluz-ctrl (none)] Minecraft Crash Report ---- // Hey, that tickles! Hehehe! Time: 2026-09-25 22:02:55 Description: mouseClicked event handler java.lang.NullPointerException: Cannot invoke "com.cobblemon.mod.relocations.graalvm.polyglot.Value.execute(Object[])" because "receiveMoveDataFn" is null at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.lambda$movesLoad$0(Moves.java:48) at knot//com.cobblemon.mod.common.battles.ShowdownThread.queue(ShowdownThread.java:32) at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.movesLo

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#2@r17l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 1/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: bm25_a#3@r17l
  - excerpt: loading phase: Mod sodium_extra requires sodium 0.8.12-alpha.3+mc1.21.1 or above Currently, sodium is 0.6.13+mc1.21.1 Error during pre-loading phase: Mod reeses_sodium_options requires sodium 0.8.12-alpha.3 or above Currently, sodium is 0.6.13+mc1.21.1 ``` [comment by Official-V-Zer0 (none)] It may be due to the crashlog only formed after getting through the load screen hence Sodium being 0.6.13, but using 0.8.12-beta.1 is the issue [comment by jellysquid3 (member)] Your log files and crash logs do not relate to each other. The log file contains the actual error, not the crash report. Pleas

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
  - retrieved by: dense_b#4@r17c
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

- [ ] **gh-issue:architectury/architectury-api#748** (github_issue, 1/6 conditions)
  - architectury-api issue #748: NeoForge fails to launch with architectury-api (except 26.2)
  - https://github.com/architectury/architectury-api/issues/748
  - retrieved by: hybrid_b#5@r17l
  - excerpt: this is my 26.1 instance running with only architectury-api installed https://pastebin.com/uG2GesT5 [comment by st0x0ef (collaborator)] You have architectury 20.0.4 installed, the latest is 20.1.16. [comment by Lilyy2565 (none)] 20.1.16 does not appear to be released on modrinth, where can I obtain this version? <img width="948" height="439" alt="Image" src="https://github.com/user-attachments/assets/6d803926-854d-4352-a0d2-b9723316fb43" /> [comment by st0x0ef (collaborator)] <img width="894" height="124" alt="Image" src="https://github.com/user-attachments/assets/a78fd6b0-6b4c-4607-b1ec-1

- [ ] **gh-issue:embeddedt/ModernFix#503** (github_issue, 1/6 conditions)
  - ModernFix issue #503: MC 1.21.x [Incompatibility] Additional Placement Fabric with the Dynamic Ressouce Loading option enabled
  - https://github.com/embeddedt/ModernFix/issues/503
  - retrieved by: hybrid_c#5@r17l
  - excerpt: fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb73304 |-- fabric-rendering-v1 10.1.2+b874120c04 |-- fabric-resource-conditions-api-v1 5.0.13+203e6b2304 |-- fabric-resource-loader-v0 3.0.11+b1caf1e904 |-- fabric-screen-api-v1 2.0.38+7feeb73304 |-- fabric-screen-handler-api-v1 1.3.110+7feeb73304 |-- fabric-sound-api-v1 [... truncated] [comment by Lonseuks (none)] Same happen with the Neoforge version 1.21.x https://mclo.gs/SmqtUPw [comment by embeddedt (owner)] https://github.com/FirEmerald/AdditionalPlacement

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 1/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: hybrid_a#5@r17l
  - excerpt: [issue by KP2048] ``` [Architectury Transformer] Architectury Runtime 5.2.61 [Architectury Transformer] Read classpath in 1.251 s [Architectury Transformer] Listening at C:\Users\<user>\Documents\MCDEV\Minitect\common\build\devlibs\minitect-1.0.0-dev.jar [09:56:15] [main/INFO] (Launcher) ModLauncher running: args [--launchTarget, forgeclientuserdev, --version, MOD_DEV, --assetIndex, 1.18.1-1.18, --assetsDir, C:\Users\<user>\.gradle\caches\fabric-loom\assets, --gameDir, ., --fml.forgeVersion, 39.0.64, --fml.mcVersion, 1.18.1, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20211210.

## Added by hand

(none)
