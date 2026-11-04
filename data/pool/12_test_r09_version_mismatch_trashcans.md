# Judging sheet 12: `r09_version_mismatch_trashcans` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `trashcans`  |  **Acceptable:** trashcans
- **What was broken:** updated Trash Cans to the latest build (trashcans-1.1.2a-neoforge-mc26.3.jar), which targets Minecraft 26.x
- **Logs in this scenario:** r09_crash, r09_latest
- **Documents to judge:** 31

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:SuperMartijn642/TrashCans#11** (github_issue, 4/6 conditions)
  - TrashCans issue #11: [Crash] with newest version of mod
  - https://github.com/SuperMartijn642/TrashCans/issues/11
  - retrieved by: dense_b#1@r09c, hybrid_a#3@r09l, hybrid_b#4@r09l, hybrid_c#3@r09l, dense_b#1@r09l
  - excerpt: [issue by Warbringer12] **Version Info** - Minecraft, 1.16.5 - Trash Cans, 1.0.10-mc1.16.5 **Steps to Reproduce** ...1. launch minecraft **Crash report (~/logs/latest.log)** ... [crash-2021-05-07_18.31.42-fml.txt](https://github.com/SuperMartijn642/TrashCans/files/6444927/crash-2021-05-07_18.31.42-fml.txt) [Uploading 2021-05-07-2.log…]() [comment by SuperMartijn642 (owner)] It says you don't have the core lib installed, it is required for the newest version. [comment by luffykick (none)] Same issue as OP... but for clarity... your latest trashcans update "trashcans-1.0.10-mc1.1

- [ ] **gh-issue:SuperMartijn642/TrashCans#61** (github_issue, 4/6 conditions)
  - TrashCans issue #61: [1.1.1 NeoForge 26.1.2] Crash (NullPointerException) when an Item Trash Can writes its deleted items
  - https://github.com/SuperMartijn642/TrashCans/issues/61
  - retrieved by: hybrid_c#4@r09c, hybrid_b#3@r09l, hybrid_c#1@r09l, bm25_b#2@r09l, dense_b#3@r09l
  - excerpt: [issue by alexhcferreira] ### Minecraft version 26.1.2 ### Mod Loader NeoForge ### Trash Cans version trashcans-1.1.1-neoforge-mc26.1 ### Game environment Client ### Steps to reproduce Put an item in a chest, transfer to an Item Trash Can with a Pipez or smth Claude Opus 5.5 Max ANALYSIS: **Versions** - Trash Cans 1.1.1-neoforge-mc26.1 - SuperMartijn642's Core Lib 1.1.24b - NeoForge 26.1.2.109, Minecraft 26.1.2 **What happens** Once an item enters an Item Trash Can through its item handler (hopper, pipe, another mod exporting into it), the server crashes the next time the trash

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_b#1@r09c, hybrid_c#1@r09c, bm25_b#1@r09c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [x] **gh-issue:SuperMartijn642/TrashCans#38** (github_issue, 3/6 conditions)
  - TrashCans issue #38: [Crash] Failing to find corelib dependency
  - https://github.com/SuperMartijn642/TrashCans/issues/38
  - retrieved by: dense_b#2@r09c, hybrid_b#1@r09l, bm25_b#1@r09l, dense_b#2@r09l
  - excerpt: [issue by jackhexed] Minecraft 1.18.2 Trashcans 1.0.18-forge-mc1.18 Corelib 1.1.15-forge-mc1.18 **Steps to Reproduce** Install the trashcans mod (through curseforge client, which automatically installs dependencies) and launch the game. **Crash report (~/logs/latest.log)** [latest.log](https://github.com/SuperMartijn642/TrashCans/files/13370809/latest.log) [comment by SuperMartijn642 (owner)] The CurseForge launcher sometimes doesn't download dependency files correctly. Please delete the core lib file from your mods folder and download it manually from the website [comment by jackh

- [ ] **gh-issue:SuperMartijn642/TrashCans#37** (github_issue, 3/6 conditions)
  - TrashCans issue #37: [Crash] Game crash when searching JEI while trash can UI is showing
  - https://github.com/SuperMartijn642/TrashCans/issues/37
  - retrieved by: hybrid_b#2@r09c, bm25_b#5@r09c, hybrid_b#2@r09l, dense_b#5@r09l
  - excerpt: martijn642.core.gui.WidgetContainerScreen.m_88315_(WidgetContainerScreen.java:136) ~[supermartijn642corelib-1.1.12a-forge-mc1.20.jar%23721!/:?] {re:classloading} at net.minecraft.client.gui.screens.Screen.m_280264_(Screen.java:109) ~[client-1.20.1-20230612.114412-srg.jar%23748!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistclean [... truncated] [comment by SuperMartijn642 (owner)] Makes you wonder how no one has reported this until now... Anyways, it's fixed now in Trash Cans version 1.0.18b for Forge 1.20. Thank you for reporting the issue!

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 3/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_b#4@r09c, hybrid_c#2@r09c, bm25_b#3@r09c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 3/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#5@r09c, hybrid_b#3@r09c, hybrid_c#3@r09c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

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

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 2/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: hybrid_b#5@r09c, bm25_b#4@r09c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#516** (github_issue, 2/6 conditions)
  - Aquaculture issue #516: Missing Registry Crash
  - https://github.com/TeamMetallurgy/Aquaculture/issues/516
  - retrieved by: hybrid_b#5@r09l, bm25_b#5@r09l
  - excerpt: [issue by XUrielX-Chosen] The game crashed: unexpected error Error: java.lang.NullPointerException: Registry Object not present: aquaculturedelight:roasted_tambaqui I keep getting this error when I crash. [comment by GirafiStudios (collaborator)] Wrong mod. The crash is from Aquaculture Delight

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 2/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_c#5@r09c, dense_b#5@r09c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r09c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 1/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_a#1@r09l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#2@r09l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#2@r09c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:SuperMartijn642/TrashCans#59** (github_issue, 1/6 conditions)
  - TrashCans issue #59: [Crash] Your title here
  - https://github.com/SuperMartijn642/TrashCans/issues/59
  - retrieved by: dense_b#3@r09c, dense_b#4@r09l
  - excerpt: [issue by Trko0045] ### Minecraft version 1.20.1 ### Mod Loader Fabric ### Trash Cans version 1.1.0a-fabr ic-mc1.20.4 ### Game environment Client ### Steps to reproduce update the corelib of supermartin join server, open trash and game crashes [crash-2026-09-25_13.56.10-client.txt](https://github.com/user-attachments/files/32651450/crash-2026-09-25_13.56.10-client.txt) ### Crash report (~/logs/latest.log) Crashlog uploaded above [comment by SuperMartijn642 (owner)] It should be fixed not in Trash Cans version 1.1.1. Thank you for reporting the issue!

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 1/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: bm25_a#3@r09l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [x] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: bm25_b#3@r09l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

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

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#4@r09l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

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

- [ ] **gh-issue:SuperMartijn642/TrashCans#27** (github_issue, 1/6 conditions)
  - TrashCans issue #27: [Crash] Right-click on trash kicks client out of server
  - https://github.com/SuperMartijn642/TrashCans/issues/27
  - retrieved by: hybrid_a#5@r09l
  - excerpt: [issue by spiral6] **Version Info** - Minecraft 1.12.2, Forge 14.23.5.2859 - Trash Cans, 1.0.17 - Core lib, 1.1.1a for 1.12.2 **Steps to Reproduce** Right click on trash can, get kicked out of server. **Crash report (~/logs/latest.log)** ``` [00:19:46] [Client thread/INFO] [net.minecraft.client.multiplayer.GuiConnecting]: Connecting to <ip>, 25565 [00:19:51] [Netty Client IO #2/INFO] [FML]: Server protocol version 2 [00:19:51] [Netty Client IO #2/INFO] [FML]: Attempting connection with missing mods [essential, betteroofing, betteradvancements, bettertitlescreen, controlling, craf

- [ ] **gh-issue:embeddedt/ModernFix#641** (github_issue, 1/6 conditions)
  - ModernFix issue #641: 1.21.1 WorldEdit 7.3.8 + ModernFix 5.27.x Crash
  - https://github.com/embeddedt/ModernFix/issues/641
  - retrieved by: bm25_a#5@r09l
  - excerpt: [issue by magictruffle] ### Bug Description See logs. Issue does not occur with modernfix-neoforge-5.26.1+mc1.21.1.jar. ### Reproduction Steps Generate a new single player world and attempt to enter with mods enabled. ### Log File [crash-2026-04-12_10.11.35-server.txt](https://github.com/user-attachments/files/26659843/crash-2026-04-12_10.11.35-server.txt) [crash-2026-04-12_10.16.00-server.txt](https://github.com/user-attachments/files/26659844/crash-2026-04-12_10.16.00-server.txt) [comment by embeddedt (owner)] Thanks for the report, this should be fixed in the latest builds for all ver

## Added by hand

(none)
