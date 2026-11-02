# Judging sheet 07: `r09_version_mismatch_trashcans` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `trashcans`  |  **Acceptable:** trashcans
- **What was broken:** updated Trash Cans to the latest build (trashcans-1.1.2a-neoforge-mc26.3.jar), which targets Minecraft 26.x
- **Logs in this scenario:** r09_crash, r09_latest
- **Documents to judge:** 58

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 5/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#9@r09c, hybrid_b#1@r09c, hybrid_c#1@r09c, bm25_b#1@r09c, dense_b#7@r09c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:SuperMartijn642/TrashCans#38** (github_issue, 5/6 conditions)
  - TrashCans issue #38: [Crash] Failing to find corelib dependency
  - https://github.com/SuperMartijn642/TrashCans/issues/38
  - retrieved by: hybrid_c#9@r09c, dense_b#2@r09c, hybrid_a#10@r09l, hybrid_b#1@r09l, hybrid_c#8@r09l, bm25_b#1@r09l, dense_b#2@r09l
  - excerpt: [issue by jackhexed] Minecraft 1.18.2 Trashcans 1.0.18-forge-mc1.18 Corelib 1.1.15-forge-mc1.18 **Steps to Reproduce** Install the trashcans mod (through curseforge client, which automatically installs dependencies) and launch the game. **Crash report (~/logs/latest.log)** [latest.log](https://github.com/SuperMartijn642/TrashCans/files/13370809/latest.log) [comment by SuperMartijn642 (owner)] The CurseForge launcher sometimes doesn't download dependency files correctly. Please delete the core lib file from your mods folder and download it manually from the website [comment by jackh

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 5/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#5@r09c, hybrid_b#3@r09c, hybrid_c#3@r09c, bm25_b#6@r09c, dense_b#10@r09c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:SuperMartijn642/TrashCans#11** (github_issue, 4/6 conditions)
  - TrashCans issue #11: [Crash] with newest version of mod
  - https://github.com/SuperMartijn642/TrashCans/issues/11
  - retrieved by: hybrid_c#8@r09c, dense_b#1@r09c, hybrid_a#3@r09l, hybrid_b#4@r09l, hybrid_c#3@r09l, dense_b#1@r09l
  - excerpt: [issue by Warbringer12] **Version Info** - Minecraft, 1.16.5 - Trash Cans, 1.0.10-mc1.16.5 **Steps to Reproduce** ...1. launch minecraft **Crash report (~/logs/latest.log)** ... [crash-2021-05-07_18.31.42-fml.txt](https://github.com/SuperMartijn642/TrashCans/files/6444927/crash-2021-05-07_18.31.42-fml.txt) [Uploading 2021-05-07-2.log…]() [comment by SuperMartijn642 (owner)] It says you don't have the core lib installed, it is required for the newest version. [comment by luffykick (none)] Same issue as OP... but for clarity... your latest trashcans update "trashcans-1.0.10-mc1.1

- [ ] **gh-issue:SuperMartijn642/TrashCans#61** (github_issue, 4/6 conditions)
  - TrashCans issue #61: [1.1.1 NeoForge 26.1.2] Crash (NullPointerException) when an Item Trash Can writes its deleted items
  - https://github.com/SuperMartijn642/TrashCans/issues/61
  - retrieved by: hybrid_b#9@r09c, hybrid_c#4@r09c, hybrid_b#3@r09l, hybrid_c#1@r09l, bm25_b#2@r09l, dense_b#3@r09l
  - excerpt: [issue by alexhcferreira] ### Minecraft version 26.1.2 ### Mod Loader NeoForge ### Trash Cans version trashcans-1.1.1-neoforge-mc26.1 ### Game environment Client ### Steps to reproduce Put an item in a chest, transfer to an Item Trash Can with a Pipez or smth Claude Opus 5.5 Max ANALYSIS: **Versions** - Trash Cans 1.1.1-neoforge-mc26.1 - SuperMartijn642's Core Lib 1.1.24b - NeoForge 26.1.2.109, Minecraft 26.1.2 **What happens** Once an item enters an Item Trash Can through its item handler (hopper, pipe, another mod exporting into it), the server crashes the next time the trash

- [ ] **gh-issue:SuperMartijn642/TrashCans#37** (github_issue, 4/6 conditions)
  - TrashCans issue #37: [Crash] Game crash when searching JEI while trash can UI is showing
  - https://github.com/SuperMartijn642/TrashCans/issues/37
  - retrieved by: hybrid_b#2@r09c, bm25_b#5@r09c, dense_b#6@r09c, hybrid_b#2@r09l, hybrid_c#7@r09l, bm25_b#6@r09l, dense_b#5@r09l
  - excerpt: martijn642.core.gui.WidgetContainerScreen.m_88315_(WidgetContainerScreen.java:136) ~[supermartijn642corelib-1.1.12a-forge-mc1.20.jar%23721!/:?] {re:classloading} at net.minecraft.client.gui.screens.Screen.m_280264_(Screen.java:109) ~[client-1.20.1-20230612.114412-srg.jar%23748!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistclean [... truncated] [comment by SuperMartijn642 (owner)] Makes you wonder how no one has reported this until now... Anyways, it's fixed now in Trash Cans version 1.0.18b for Forge 1.20. Thank you for reporting the issue!

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 4/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#8@r09c, hybrid_c#7@r09c, bm25_b#7@r09c, hybrid_c#6@r09l, bm25_a#3@r09l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_c#10@r09c, bm25_b#2@r09c, hybrid_b#6@r09l
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 3/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_b#4@r09c, hybrid_c#2@r09c, bm25_b#3@r09c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:SuperMartijn642/TrashCans#59** (github_issue, 3/6 conditions)
  - TrashCans issue #59: [Crash] Your title here
  - https://github.com/SuperMartijn642/TrashCans/issues/59
  - retrieved by: dense_b#3@r09c, hybrid_a#9@r09l, hybrid_b#10@r09l, dense_b#4@r09l
  - excerpt: [issue by Trko0045] ### Minecraft version 1.20.1 ### Mod Loader Fabric ### Trash Cans version 1.1.0a-fabr ic-mc1.20.4 ### Game environment Client ### Steps to reproduce update the corelib of supermartin join server, open trash and game crashes [crash-2026-09-25_13.56.10-client.txt](https://github.com/user-attachments/files/32651450/crash-2026-09-25_13.56.10-client.txt) ### Crash report (~/logs/latest.log) Crashlog uploaded above [comment by SuperMartijn642 (owner)] It should be fixed not in Trash Cans version 1.1.1. Thank you for reporting the issue!

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#6@r09c, hybrid_c#5@r09c, dense_b#5@r09c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 3/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_b#7@r09c, hybrid_c#6@r09c, dense_b#9@r09l
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r09l, bm25_a#2@r09l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r09c, bm25_a#4@r09c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#8@r09l, bm25_a#1@r09l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#2@r09c, bm25_a#2@r09c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 2/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: hybrid_c#2@r09l, bm25_b#4@r09l
  - excerpt: [issue by ivannf-oviedo] ### Bug Description Hello, I am reporting a critical incompatibility/race condition found in a complex NeoForge 1.21.1 modpack (160+ mods, heavily optimized with Lithium/Sodium). The issue causes a **cascading mod loading failure (FATAL CRASH)** due to multiple major mods failing to access their own registered items during the loading process. ### Bug Description When loading a large pack, the game crashes during the `net.neoforged.neoforge.registries.RegisterEvent`. The error indicates that the item registration has been accelerated too aggressively, causing ke

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#3@r09c, bm25_a#3@r09c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#9@r09l, bm25_b#3@r09l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 2/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: hybrid_b#5@r09c, bm25_b#4@r09c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 2/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_b#10@r09c, hybrid_a#4@r09l
  - excerpt: .fml.ModList.forEachModInOrder(ModList.java:174) ~[loader-4.0.42.jar%23107!/:4.0] {re:mixin} at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModLoader.postEvent(ModLoader.java:358) ~[loader-4.0.42.jar%23107!/:4.0] {} at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.client.ClientHooks.initClientHooks(ClientHooks.java:1028) ~[neoforge-21.1.234-universal.jar%23196!/:?] {re:mixin,re:classloading,pl:mixin:APP:sodium-neoforge.mixins.json:platform.neoforge.ClientHooksMixin from mod sodium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.<init>(Minecraft.java:60

- [ ] **gh-issue:SuperMartijn642/TrashCans#27** (github_issue, 2/6 conditions)
  - TrashCans issue #27: [Crash] Right-click on trash kicks client out of server
  - https://github.com/SuperMartijn642/TrashCans/issues/27
  - retrieved by: hybrid_a#5@r09l, bm25_b#10@r09l
  - excerpt: [issue by spiral6] **Version Info** - Minecraft 1.12.2, Forge 14.23.5.2859 - Trash Cans, 1.0.17 - Core lib, 1.1.1a for 1.12.2 **Steps to Reproduce** Right click on trash can, get kicked out of server. **Crash report (~/logs/latest.log)** ``` [00:19:46] [Client thread/INFO] [net.minecraft.client.multiplayer.GuiConnecting]: Connecting to <ip>, 25565 [00:19:51] [Netty Client IO #2/INFO] [FML]: Server protocol version 2 [00:19:51] [Netty Client IO #2/INFO] [FML]: Attempting connection with missing mods [essential, betteroofing, betteradvancements, bettertitlescreen, controlling, craf

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#516** (github_issue, 2/6 conditions)
  - Aquaculture issue #516: Missing Registry Crash
  - https://github.com/TeamMetallurgy/Aquaculture/issues/516
  - retrieved by: hybrid_b#5@r09l, bm25_b#5@r09l
  - excerpt: [issue by XUrielX-Chosen] The game crashed: unexpected error Error: java.lang.NullPointerException: Registry Object not present: aquaculturedelight:roasted_tambaqui I keep getting this error when I crash. [comment by GirafiStudios (collaborator)] Wrong mod. The crash is from Aquaculture Delight

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 2/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#6@r09c, bm25_b#8@r09c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 2/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#7@r09c, dense_b#6@r09l
  - excerpt: cpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\librari

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_b#7@r09l, dense_b#7@r09l
  - excerpt: \javafmllanguage\1.19-41.0.63\javafmllanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.958] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\lowcodelanguage\1.19-41.0.63\lowcodelanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.960] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\mclanguage\1.19-41.0.63\mclanguage-1.19-41.0.63

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 2/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#7@r09l, dense_b#8@r09l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 2/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: bm25_b#10@r09c, hybrid_a#7@r09l
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:SuperMartijn642/TrashCans#19** (github_issue, 2/6 conditions)
  - TrashCans issue #19: [Crash] 1.19.2 Crash When Placing Fluid/Ultimate Trash Cans
  - https://github.com/SuperMartijn642/TrashCans/issues/19
  - retrieved by: hybrid_c#9@r09l, bm25_b#8@r09l
  - excerpt: [issue by enigmaquip] **Version Info** - Minecraft, 1.19.2 - Trash Cans, 1.0.15a - Core lib, 1.0.19a **Steps to Reproduce** With Mekanism installed, place down a trash can that handles Gasses (Fluid or Ultimate) **Crash report (~/logs/latest.log)** https://mclo.gs/y9yMjzQ ``` java.lang.NoSuchFieldError: GAS_HANDLER_CAPABILITY at com.supermartijn642.trashcans.compat.mekanism.MekanismCompatOn.getGasHandlerCapability(MekanismCompatOn.java:33) ~[trashcans-1.0.15a-forge-mc1.19.jar%23264!/:?] {re:classloading} ``` Looks like the capability was renamed to just `GAS_HANDLER` <https

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r09c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#2@r09l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#4@r09c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:SuperMartijn642/TrashCans#52** (github_issue, 1/6 conditions)
  - TrashCans issue #52: [Crash] ... please see picture to understand
  - https://github.com/SuperMartijn642/TrashCans/issues/52
  - retrieved by: dense_b#4@r09c
  - excerpt: [issue by superblast1] **Version Info** - Minecraft, ... - Trash Cans, ... - Core lib, ... **Steps to Reproduce** ... **Crash report (~/logs/latest.log)** ... im not sure what to do as theres no logs but i installed a crash detector mod just thought you should know ![Image](https://github.com/user-attachments/assets/973fb7b4-d8a5-4434-b727-34225ef42db8) [comment by SuperMartijn642 (owner)] Nuclear Trash Can copies the code from Trash Cans without changing the package or class names. Since Nuclear Trash Can now contains classes at the same locations as Trash Cans, it conflicts. Nothing I ca

- [ ] **gh-issue:TwelveIterations/Waystones#1190** (github_issue, 1/6 conditions)
  - Waystones issue #1190: Crash due to Confluence on newest update [Solution: Remove Confluence or downgrade Waystones]
  - https://github.com/TwelveIterations/Waystones/issues/1190
  - retrieved by: hybrid_c#4@r09l
  - excerpt: [issue by VaporeonScripts] ### Minecraft Version 1.21.1 ### Mod Loader NeoForge ### Describe the Issue crash after updating to the newest balm (required for waystone's anniversary update) ### Logs https://mclo.gs/pmbfo56 [comment by BlayTheNinth (member)] The crash is happening in Prefab and does not seem to be related to Balm. > java.lang.NullPointerException: Cannot invoke "net.minecraft.world.level.ItemLike.asItem()" because "itemlike" is null at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.color.item.ItemColors.register(ItemColors.java:122) ~[client-1.21.1-20240808.144430-sr

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#4@r09l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r09c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:SuperMartijn642/TrashCans#12** (github_issue, 1/6 conditions)
  - TrashCans issue #12: [Crash] ...
  - https://github.com/SuperMartijn642/TrashCans/issues/12
  - retrieved by: hybrid_c#5@r09l
  - excerpt: [issue by TheTechPny] Sorry forgot to edit the title **Version Info** - Minecraft, 1.16.5 - Trash Cans, trashcans-1.0.10-mc1.16.5.jar **Steps to Reproduce** A player mined a trash can with an Ars Nouveau spell "ars nouveau, so it was a custom spell touch+break+pickup" **Crash report (~/logs/latest.log)** https://pastebin.com/raw/Lwu3ge5E [comment by SuperMartijn642 (owner)] I fixed it now in [Core Lib version 1.0.10](https://www.curseforge.com/minecraft/mc-mods/supermartijn642s-core-lib/files/all). Thank you for the reporting the issue!

- [ ] **gh-issue:embeddedt/ModernFix#641** (github_issue, 1/6 conditions)
  - ModernFix issue #641: 1.21.1 WorldEdit 7.3.8 + ModernFix 5.27.x Crash
  - https://github.com/embeddedt/ModernFix/issues/641
  - retrieved by: bm25_a#5@r09l
  - excerpt: [issue by magictruffle] ### Bug Description See logs. Issue does not occur with modernfix-neoforge-5.26.1+mc1.21.1.jar. ### Reproduction Steps Generate a new single player world and attempt to enter with mods enabled. ### Log File [crash-2026-04-12_10.11.35-server.txt](https://github.com/user-attachments/files/26659843/crash-2026-04-12_10.11.35-server.txt) [crash-2026-04-12_10.16.00-server.txt](https://github.com/user-attachments/files/26659844/crash-2026-04-12_10.16.00-server.txt) [comment by embeddedt (owner)] Thanks for the report, this should be fixed in the latest builds for all ver

- [ ] **gh-issue:CaffeineMC/sodium#3760** (github_issue, 1/6 conditions)
  - sodium issue #3760: minecraft crashing after collapsing window on 1.21.1 neoforge
  - https://github.com/CaffeineMC/sodium/issues/3760
  - retrieved by: bm25_a#6@r09l
  - excerpt: [issue by Kishebek] ### Bug Description minecraft crashing after collapsing window both in the menu and in the world, also after collapsing my gpu is running up to 100 percent for a second. i checked other version but nothing changed. maybe happening cuz off legacy launcher used sodium 0.6.7 on 1.21.1 neoforge GPU Intel(R) HD Graphics 4600 CPU Intel(R) Core(TM) i3-4000M CPU @ 2.40GHz ### Reproduction Steps 1. lauch sodium 0.6.7 on 1.21.1 neoforge 2. collapse window ### Log File [latest.log](https://github.com/user-attachments/files/29269020/latest.log) ### Crash Report [crash-20

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#6@r09c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#6@r09l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#7@r09c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:mezz/JustEnoughItems#4451** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4451: [Crash]: loading issue JEI
  - https://github.com/mezz/JustEnoughItems/issues/4451
  - retrieved by: bm25_a#7@r09l
  - excerpt: [issue by flybywiremod-boop] ### Steps to Reproduce the Crash The culprit is that: [27srp2026 16:55:48.717] [Render thread/INFO] [mezz.jei.common.util.LoggedTimer/]: Starting JEI... [27srp2026 16:55:48.721] [Render thread/INFO] [mezz.jei.library.load.PluginCaller/]: Configuring JEI... [27srp2026 16:55:48.723] [Render thread/INFO] [mezz.jei.library.load.PluginCaller/]: Configuring JEI took 2.027 milliseconds [27srp2026 16:55:48.735] [Render thread/INFO] [mezz.jei.library.load.PluginCaller/]: Registering item subtypes... [27srp2026 16:55:48.748] [Render thread/INFO] [mezz.jei.library.load.Plugi

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#8@r09l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: dense_b#8@r09c
  - excerpt: :B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:A,pl:connector_pre_launch:A,pl:runtimedistcleaner:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.buildInitialScreens(Minecraft.java:675) ~[client-1.21.1-20240808.144430-srg.jar%23317!/:?] {re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mi

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#8@r09c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:TwelveIterations/Balm#85** (github_issue, 1/6 conditions)
  - Balm issue #85: Server crashes on startup
  - https://github.com/TwelveIterations/Balm/issues/85
  - retrieved by: hybrid_a#8@r09c
  - excerpt: [issue by ashton727] ### Minecraft Version 1.21 ### Mod Loader NeoForge ### Mod Loader Version 21.0.46 ### Mod Version 21.0.11 ### Balm Version 21.0.11 ### Describe the Issue 1. Start neoforge 21.0.46 server with balm 2. Observe crash ### Logs https://pastebin.com/4asPjjkH ### Do you use any performance-enhancing mods (e.g. OptiFine) or custom server distributions (e.g. SpongeForge)? no [comment by BlayTheNinth (member)] Try Java 21 [comment by ashton727 (none)] This version of Neoforge requires Java 22 I believe. [comment by BlayTheNinth (member)] Minecraft 1.21 uses Java 2

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: hybrid_b#8@r09l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#9@r09c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 1/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: bm25_b#9@r09c
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **gh-issue:malte0811/FerriteCore#210** (github_issue, 1/6 conditions)
  - FerriteCore issue #210: Game Crush
  - https://github.com/malte0811/FerriteCore/issues/210
  - retrieved by: dense_b#9@r09c
  - excerpt: [issue by deaddiesel] 1. Forge 47.4.10 2. Minecraft 1.20.1 3. [ferritecore-6.0.1-forge.jar](https://www.curseforge.com/minecraft/mc-mods/ferritecore/files/4810975) [crash-2025-12-10_14.59.18-client.txt](https://github.com/user-attachments/files/24089186/crash-2025-12-10_14.59.18-client.txt) Your mod conflicts with Industrial Upgrade. [comment by malte0811 (owner)] This should be fixed in the latest release of Industrial Upgrade.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#9@r09l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#9@r09l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#10@r09c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:GlodBlock/ExtendedAE#341** (github_issue, 1/6 conditions)
  - ExtendedAE issue #341: [Render thread/ERROR] appeng/client/guidebook/color/ColorValue
  - https://github.com/GlodBlock/ExtendedAE/issues/341
  - retrieved by: bm25_a#10@r09l
  - excerpt: [issue by YoSiJo] ``` [21:54:01] [Render thread/ERROR] [ne.ne.fm.ModContainer/LOADING]: Caught exception during event net.neoforged.neoforge.client.event.RegisterMenuScreensEvent@2ba7828b dispatch for modid extendedae java.lang.NoClassDefFoundError: appeng/client/guidebook/color/ColorValue at TRANSFORMER/extendedae@1.21-2.0.1-neoforge/com.glodblock.github.extendedae.client.ClientRegistryHandler.registerGui(ClientRegistryHandler.java:108) ~[ExtendedAE-1.21-2.0.1-neoforge.jar%23219!/:?] {re:classloading} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) ~[bus

- [ ] **gh-issue:SuperMartijn642/TrashCans#13** (github_issue, 1/6 conditions)
  - TrashCans issue #13: [Crash] ...
  - https://github.com/SuperMartijn642/TrashCans/issues/13
  - retrieved by: hybrid_c#10@r09l
  - excerpt: [issue by PessimisticBastard] **Version Info** 1.16.5 trashcans-1.0.10-mc1.16.5.jar Forge 36.2.2 **Steps to Reproduce** Right click on trashcan, crashes. Might be issue with newer versions of Forge. **Crash report (~/logs/latest.log)** See https://pastebin.com/VamGaLcV [comment by SuperMartijn642 (owner)] It seems this issue was introduced in Core lib version 1.0.11. It *should* be fixed now in Core lib version 1.0.11a for 1.16.5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 1/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: dense_b#10@r09l
  - excerpt: 0.4/cpw.mods.modlauncher.Launcher.main(Launcher.java:74) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.run(BootstrapLauncher.java:210) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:69) at java.base/jdk.internal.reflect.DirectMethodHan

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#10@r09c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

## Added by hand

(none)
