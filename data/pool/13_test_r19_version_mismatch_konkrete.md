# Judging sheet 13: `r19_version_mismatch_konkrete` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `konkrete`  |  **Acceptable:** konkrete
- **What was broken:** replaced Konkrete with the Minecraft 1.21.11 build (konkrete_neoforge_1.9.15_MC_1.21.11.jar) in a 1.21.1 pack (1.21.11 vs 1.21.1 is easy to misread)
- **Logs in this scenario:** r19_crash, r19_latest
- **Documents to judge:** 62

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 5/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_b#1@r19c, hybrid_c#1@r19c, bm25_b#3@r19c, dense_b#2@r19c, hybrid_a#6@r19l, dense_b#4@r19l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_b#2@r19c, hybrid_c#2@r19c, bm25_b#1@r19c, hybrid_a#5@r19l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 4/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_b#5@r19c, hybrid_c#5@r19c, hybrid_a#1@r19l, bm25_a#4@r19l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 4/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: bm25_b#6@r19c, hybrid_b#3@r19l, hybrid_c#3@r19l, bm25_a#9@r19l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 4/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#4@r19c, hybrid_b#3@r19c, hybrid_c#3@r19c, bm25_b#5@r19c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:Keksuccino/Konkrete#7** (github_issue, 3/6 conditions)
  - Konkrete issue #7: Using Konkrete with some mods i have used before make my game crash
  - https://github.com/Keksuccino/Konkrete/issues/7
  - retrieved by: hybrid_b#9@r19l, hybrid_c#9@r19l, bm25_b#1@r19l
  - excerpt: It's a mod conflict. [comment by NATuan123 (none)] > You basically told yourself the answer already. It's a mod conflict. What do you mean ? [comment by Keksuccino (owner)] You need to check your mods for incompatibilities. Mods can change when they get updated, especially when they get updated to a new MC version. If you can find the incompatible mod, I can try to add support for it :) [comment by NATuan123 (none)] > You need to check your mods for incompatibilities. Mods can change when they get updated, especially when they get updated to a new MC version. If you can find the incompa

- [ ] **gh-issue:Keksuccino/Konkrete#8** (github_issue, 3/6 conditions)
  - Konkrete issue #8: Konkrete causes an incompatibility conflict of the Slight Gui Modifications mod on 1.18/1.18.1 (Fabric)
  - https://github.com/Keksuccino/Konkrete/issues/8
  - retrieved by: hybrid_b#1@r19l, hybrid_c#1@r19l, bm25_b#6@r19l
  - excerpt: [issue by Disguys] Know that you already know about this problem, well, I also wanted to inform you that everything was compatible on 1.17.1, when I updated to 1.18, the Konrkete library became incompatible with Slight Gui Modifications mod. Slight Gui Modifications work without Konrkete on 1.18/1.18.1 Logs - https://pastebin.com/MszJSuEz Crash Report - https://pastebin.com/MnWGVcQ6 Additional information: System Windows 10 Fabric Loader version 0.12.11 [comment by Disguys (none)] https://github.com/Keksuccino/Konkrete/issues/7 [comment by NATuan123 (none)] You have the same probl

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#4@r19c, hybrid_c#4@r19c, dense_b#1@r19c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **neoforge-docs:user/docs/index** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: NeoForge User Guide
  - https://docs.neoforged.net/user/docs/
  - retrieved by: hybrid_b#5@r19l, hybrid_c#5@r19l, dense_b#1@r19l
  - excerpt: import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; # NeoForge User Guide Whether you are a regular player, pack developer or server administrator, this guide is intended to help you through the process of preparing your computer to run NeoForge, as well as answer some frequently asked questions. The guide mainly aims to help you install NeoForge using the official Minecraft launcher provided by Mojang. There are also a number of third-party launchers that mostly automate this process for you, some of which are mentioned in the article on [third-party launchers][launchers]

- [ ] **gh-issue:Keksuccino/Konkrete#22** (github_issue, 3/6 conditions)
  - Konkrete issue #22: Crash
  - https://github.com/Keksuccino/Konkrete/issues/22
  - retrieved by: hybrid_b#2@r19l, hybrid_c#2@r19l, dense_b#2@r19l
  - excerpt: [issue by TheWanderingTrader] Forge crashes on launch saying that concrete needs forge version 55.0.9 Forge 55.0.9 is loaded on my client. Removing Koncrete solves this issue of crashing. Potentially koncrete is not identifying the 55.0.9 jar? [comment by Keksuccino (owner)] That makes no sense. It wouldn't crash if the correct Forge version would be installed.

- [ ] **gh-issue:Keksuccino/Konkrete#4** (github_issue, 3/6 conditions)
  - Konkrete issue #4: Crash with multiple mods installed
  - https://github.com/Keksuccino/Konkrete/issues/4
  - retrieved by: hybrid_b#10@r19l, hybrid_c#10@r19l, bm25_b#2@r19l
  - excerpt: [issue by Suatae] I tried loading it in my modpack so I can have the latest FancyMenu but for some reason Konkrete is not working well with these mods specifically: [crash-2021-07-17_14.48.01-client.txt](https://github.com/Keksuccino/Konkrete/files/6835357/crash-2021-07-17_14.48.01-client.txt) [comment by Keksuccino (owner)] Hi! This is not a direct issue with Konkrete, it's more like an issue with FancyMenu being incompatible with one of your core mods.

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_b#8@r19c, hybrid_c#8@r19c, bm25_b#2@r19c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:mrh0/createaddition#718** (github_issue, 3/6 conditions)
  - createaddition issue #718: Games crashes upon mod loading
  - https://github.com/mrh0/createaddition/issues/718
  - retrieved by: hybrid_b#9@r19c, hybrid_c#9@r19c, dense_b#3@r19c
  - excerpt: [issue by ferforious1] **Describe the bug** Game crashes with an error upon mod loading **To Reproduce** - **Additional context** - Mod version: 1.0.0b - Forge version: 47.2.20 - Create version: 0.5.1f - Minecraft version: 1.20.1 [crash-2024-01-17_09.03.21-fml.txt](https://github.com/mrh0/createaddition/files/13959323/crash-2024-01-17_09.03.21-fml.txt) [comment by mrh0 (owner)] please update to the latest version before submitting a report

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 3/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_a#10@r19l, hybrid_b#4@r19l, hybrid_c#4@r19l
  - excerpt: /issues. ========================= // Shall we play a game? Time: 2026-06-25 21:57:03 Description: Rendering overlay java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.2+mc1.21.1-mod.jar%23319!/:?] {re:mixin,re:classloading} at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigsLate(ConfigManager.java:76) ~[net.caffeinemc.sodium-neoforge-0.8

- [ ] **gh-issue:mezz/JustEnoughItems#4586** (github_issue, 3/6 conditions)
  - JustEnoughItems issue #4586: [Crash]: JEI version 19.69.0.457 crashes (1.21.1 Forge) when joining the game
  - https://github.com/mezz/JustEnoughItems/issues/4586
  - retrieved by: hybrid_b#10@r19c, hybrid_c#10@r19c, dense_b#4@r19c
  - excerpt: /mc-mods/jei/files/9343790>) - [CurseForge (Fabric)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343789>) - [CurseForge (Forge)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343788>) - [Modrinth (NeoForge)](<https://modrinth.com/mod/u6dRKJwZ/version/pWGmsnGm>) - [Modrinth (Fabric)](<https://modrinth.com/mod/u6dRKJwZ/version/kFIMjB8H>) - [Modrinth (Forge)](<https://modrinth.com/mod/u6dRKJwZ/version/1rvwFzhL>)

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: dense_b#7@r19c, hybrid_b#7@r19l, hybrid_c#7@r19l, dense_b#8@r19l
  - excerpt: le.debug` | Whether Gradle is set to debug mode. Debug mode mainly means more Gradle log output. Note that this is for Gradle itself, not Minecraft. | `org.gradle.debug=false` | | `minecraft_version` | The Minecraft version you are modding on. Must match with `neo_version`. | `minecraft_version=1.20.6`

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r19c, bm25_a#4@r19c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#9@r19l, bm25_a#1@r19l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#2@r19l, bm25_a#2@r19l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#2@r19c, bm25_a#2@r19c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#3@r19c, bm25_a#3@r19c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 2/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: hybrid_a#9@r19c, dense_b#9@r19c, dense_b#6@r19l
  - excerpt: [issue by dghodgson] ### Bug Description Attempting to load Modernfix alongside VMP-Forge will cause the minecraft client to crash. Tested with following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Modernfix 5.18.0+mc1.20.1 seems to launch without any issues. All older versions tested failed with a different error than the one found in the attached log. ### Reproduction Steps Install the following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Forge: 47.4.1 ### Log File ``` MultiMC version: 0.7.0-4230 Launched instance in onlin

- [ ] **neoforge-docs:user/docs/client** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Installing a NeoForge Client
  - https://docs.neoforged.net/user/docs/client/
  - retrieved by: hybrid_b#6@r19c, hybrid_c#6@r19c, hybrid_b#6@r19l, hybrid_c#6@r19l
  - excerpt: [Modrinth][modrinth]. ## Updating To update your NeoForge version, simply download and run the installer for the new NeoForge version, as described above. Then, go to the Installations tab in the launcher and change the version in your NeoForge profile to the new version. :::danger Always backup your world before updating NeoForge or mods! To backup your world, open the game directory and select the `saves` subfolder. Then, copy the folder with your world's name (e.g. `New World`) to a safe location. If anything goes wrong during updating, delete the updated world folder, downgrade NeoFor

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 2/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#7@r19c, bm25_b#7@r19c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 2/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_b#7@r19c, hybrid_c#7@r19c
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_a#8@r19l, bm25_a#10@r19l
  - excerpt: mods.modlauncher.Launcher/MODLAUNCHER]: ModLauncher 10.0.1+10.0.1+main.e9521dc3 starting: java version 17.0.3 by Microsoft; OS Windows 10 arch amd64 version 10.0 [07lip2022 18:29:06.835] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.minecraft/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2390!/ Service=ModLauncher Env=CLIENT [07lip2022 18:29:07.952] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\fmlcore

- [ ] **gh-issue:thedarkcolour/KotlinForForge#122** (github_issue, 2/6 conditions)
  - KotlinForForge issue #122: [1.21.1-Neoforge] Kotlin crashes on NeoForge 1.21.1
  - https://github.com/thedarkcolour/KotlinForForge/issues/122
  - retrieved by: hybrid_b#8@r19l, hybrid_c#8@r19l
  - excerpt: [issue by overlappingd] Mod `fzzy_config` requires Kotlin, Kotlin crashes the game when the Mod Construction stage is about to finish Crash Report: https://mclo.gs/FEz1bUZ `latest.log`: https://mclo.gs/59pOEet Using the [Just Create SMP](https://www.curseforge.com/minecraft/modpacks/just-create-smp) modpack. [comment by thedarkcolour (owner)] Not a KFF issue. Vanilla Backport bug from the looks of it

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r19c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#3@r19l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:malte0811/FerriteCore#210** (github_issue, 1/6 conditions)
  - FerriteCore issue #210: Game Crush
  - https://github.com/malte0811/FerriteCore/issues/210
  - retrieved by: dense_b#5@r19c, dense_b#3@r19l
  - excerpt: [issue by deaddiesel] 1. Forge 47.4.10 2. Minecraft 1.20.1 3. [ferritecore-6.0.1-forge.jar](https://www.curseforge.com/minecraft/mc-mods/ferritecore/files/4810975) [crash-2025-12-10_14.59.18-client.txt](https://github.com/user-attachments/files/24089186/crash-2025-12-10_14.59.18-client.txt) Your mod conflicts with Industrial Upgrade. [comment by malte0811 (owner)] This should be fixed in the latest release of Industrial Upgrade.

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 1/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: bm25_b#10@r19c, bm25_b#3@r19l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: bm25_a#3@r19l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:Keksuccino/Konkrete#24** (github_issue, 1/6 conditions)
  - Konkrete issue #24: Game keep crashing after installing konkrete
  - https://github.com/Keksuccino/Konkrete/issues/24
  - retrieved by: bm25_b#4@r19l
  - excerpt: [issue by NR-5tudio] Hey! i wanted to use `fancy menu` mod for `1.24.4 forge` i installed all the used mods such as `melody` and `konkrete`. but the game crashed i thought that the mod is the broken one so i removed it (i kept the `melody` and `konkrete`, but i deleted fancy mod for testing) and still crashing so i removed `melody` and still crashing but when i deleted `konkrete` it stops crashing im not sure what is the issue exactly but i do know that there is an issue, WHO KNOWS maybe im dum :D Thank you :). [comment by Keksuccino (owner)] I can't do anything without the log. Please send y

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: bm25_b#4@r19c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#4@r19l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r19c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 1/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: bm25_b#5@r19l
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#5@r19l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#5@r19c, hybrid_a#7@r19l
  - excerpt: cpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\librari

- [ ] **gh-issue:mezz/JustEnoughItems#4255** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4255: [Bug]: Conflict with AE2 and Beyond Dimensions (Neoforge)
  - https://github.com/mezz/JustEnoughItems/issues/4255
  - retrieved by: dense_b#5@r19l
  - excerpt: :** [NeoForge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548363) | [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548362) **Modrinth:** [NeoForge](https://modrinth.com/mod/u6dRKJwZ/version/rPLXajL0) | [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/jEV5BTqf) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `15.33.0.174` for Minecraft `1.20.1`. Thanks for reporting this issue! **CurseForge:** [Fabric](https:

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#6@r19c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:TwelveIterations/Balm#85** (github_issue, 1/6 conditions)
  - Balm issue #85: Server crashes on startup
  - https://github.com/TwelveIterations/Balm/issues/85
  - retrieved by: hybrid_a#6@r19c
  - excerpt: [issue by ashton727] ### Minecraft Version 1.21 ### Mod Loader NeoForge ### Mod Loader Version 21.0.46 ### Mod Version 21.0.11 ### Balm Version 21.0.11 ### Describe the Issue 1. Start neoforge 21.0.46 server with balm 2. Observe crash ### Logs https://pastebin.com/4asPjjkH ### Do you use any performance-enhancing mods (e.g. OptiFine) or custom server distributions (e.g. SpongeForge)? no [comment by BlayTheNinth (member)] Try Java 21 [comment by ashton727 (none)] This version of Neoforge requires Java 22 I believe. [comment by BlayTheNinth (member)] Minecraft 1.21 uses Java 2

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/versioning** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Versioning
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/versioning/
  - retrieved by: dense_b#6@r19c, dense_b#9@r19l
  - excerpt: As you probably know, NeoForge is not the only mod loader out there, and many mod developers develop on multiple platforms. As a result, a way to distinguish between two files of the same mod of the same version, but for different mod loaders is needed. Usually, this is done by including the mod loader somewhere in the name. `jei-neoforge-1.20.2-16.0.0.28`, `jei-1.20.2-neoforge-16.0.0.28` or `jei-1.20.2-16.0.0.28-neoforge` are all valid ways to do it. For other mod loaders, the `neoforge` bit would be replaced with `forge`, `fabric`, `quilt` or whatever different mod loader you might be devel

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#6@r19l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#7@r19c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:Keksuccino/Konkrete#20** (github_issue, 1/6 conditions)
  - Konkrete issue #20: crash due to unchecked fabric api internal implementation mixin
  - https://github.com/Keksuccino/Konkrete/issues/20
  - retrieved by: bm25_b#7@r19l
  - excerpt: [issue by Linguardium] https://github.com/Keksuccino/Konkrete/blob/309c477fec7f9d58dafdb9a63e22b16b93cb804a/src/main/java/de/keksuccino/konkrete/mixin/mixins/client/MixinScreenEvents.java#L20 https://mclo.gs/vQNMvfY Should mark the mixin as not required and null check. Should also mark tested fabric api versions in fabric.mod.json to prevent issues on versions where implementation may change since you call internal methods that may change even in minor patch releases of fapi [comment by Keksuccino (owner)] - You are using an **old version** of FancyMenu and Konkrete that had problems

- [ ] **gh-issue:TheIllusiveC4/Curios#535** (github_issue, 1/6 conditions)
  - Curios issue #535: [Bug]: Curios API for 1.21.1 and 1.21 on curseforge can't load in 1.21
  - https://github.com/TheIllusiveC4/Curios/issues/535
  - retrieved by: dense_b#7@r19l
  - excerpt: [issue by Cassy-Lee] ### Minecraft Version 1.21 ### What happened? As described in the title, Curios API for 1.21(.1) depends on neoforge `[21.1.60,)` (in `neoforge.mods.toml`), but newest neoforge for 1.21 was `21.0.167`. Please change supported minecraft version for those files on curseforge to 1.21.1 only. If compatible, please use `[21.0,)` for neoforge version range and make a new release for 1.21. ### Relevant Log Outputs _No response_ [comment by Cassy-Lee (none)] All releases for 1.21(.1) have this problem. [comment by TheIllusiveC4 (owner)] Thanks for notifying me of this overs

- [ ] **gh-issue:bernie-g/geckolib#850** (github_issue, 1/6 conditions)
  - geckolib issue #850: Animation Parsing Error
  - https://github.com/bernie-g/geckolib/issues/850
  - retrieved by: bm25_a#7@r19l
  - excerpt: [issue by Filan-glitch] GeckoLib V4.8.4 NeoForge 21.1.228 MC1.21.1 Error Logs: [05May2026 11:30:01.258] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.258] [Worker-Main-5/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.261] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.290] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: attack sadly no further information in logs... [comment by Tslat (collaborator)] Provide the mod jar so I can test it I can't do anything with this [comment

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#8@r19c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#8@r19c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 1/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: bm25_b#8@r19c
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#8@r19l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:embeddedt/ModernFix#641** (github_issue, 1/6 conditions)
  - ModernFix issue #641: 1.21.1 WorldEdit 7.3.8 + ModernFix 5.27.x Crash
  - https://github.com/embeddedt/ModernFix/issues/641
  - retrieved by: dense_b#8@r19c
  - excerpt: [issue by magictruffle] ### Bug Description See logs. Issue does not occur with modernfix-neoforge-5.26.1+mc1.21.1.jar. ### Reproduction Steps Generate a new single player world and attempt to enter with mods enabled. ### Log File [crash-2026-04-12_10.11.35-server.txt](https://github.com/user-attachments/files/26659843/crash-2026-04-12_10.11.35-server.txt) [crash-2026-04-12_10.16.00-server.txt](https://github.com/user-attachments/files/26659844/crash-2026-04-12_10.16.00-server.txt) [comment by embeddedt (owner)] Thanks for the report, this should be fixed in the latest builds for all ver

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 1/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: bm25_b#8@r19l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#9@r19c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:Keksuccino/Konkrete#31** (github_issue, 1/6 conditions)
  - Konkrete issue #31: Enchantment Table crashes game
  - https://github.com/Keksuccino/Konkrete/issues/31
  - retrieved by: bm25_b#9@r19l
  - excerpt: [issue by Spiderman31807] I didn't have this crash (i dont use this mod), but i looked at a crash report of somebody else on my server since im a modder, and from what i could tell the cause was your mod using a mixin that tried to access a field that was private in the class. Not sure why it does that when you could just @shadow the field but either way, should be a simple fix for you- heres the crash report they sent me! [message (1).txt](https://github.com/user-attachments/files/28417492/message.1.txt) [comment by Keksuccino (owner)] - The user is using MC 1.21.8, which I do not support a

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: bm25_b#9@r19c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#10@r19c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:SuperMartijn642/TrashCans#11** (github_issue, 1/6 conditions)
  - TrashCans issue #11: [Crash] with newest version of mod
  - https://github.com/SuperMartijn642/TrashCans/issues/11
  - retrieved by: dense_b#10@r19c
  - excerpt: [issue by Warbringer12] **Version Info** - Minecraft, 1.16.5 - Trash Cans, 1.0.10-mc1.16.5 **Steps to Reproduce** ...1. launch minecraft **Crash report (~/logs/latest.log)** ... [crash-2021-05-07_18.31.42-fml.txt](https://github.com/SuperMartijn642/TrashCans/files/6444927/crash-2021-05-07_18.31.42-fml.txt) [Uploading 2021-05-07-2.log…]() [comment by SuperMartijn642 (owner)] It says you don't have the core lib installed, it is required for the newest version. [comment by luffykick (none)] Same issue as OP... but for clarity... your latest trashcans update "trashcans-1.0.10-mc1.1

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 1/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: dense_b#10@r19l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: bm25_b#10@r19l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#10@r19c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

## Added by hand

(none)
