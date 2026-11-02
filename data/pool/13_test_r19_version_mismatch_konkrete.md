# Judging sheet 13: `r19_version_mismatch_konkrete` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `konkrete`  |  **Acceptable:** konkrete
- **What was broken:** replaced Konkrete with the Minecraft 1.21.11 build (konkrete_neoforge_1.9.15_MC_1.21.11.jar) in a 1.21.1 pack (1.21.11 vs 1.21.1 is easy to misread)
- **Logs in this scenario:** r19_crash, r19_latest
- **Documents to judge:** 53

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 5/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#5@r19c, hybrid_b#1@r19c, hybrid_c#1@r19c, bm25_b#2@r19c, dense_b#2@r19c, hybrid_a#5@r19l, hybrid_b#10@r19l, hybrid_c#10@r19l, dense_b#3@r19l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 5/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#3@r19c, hybrid_b#3@r19c, hybrid_c#3@r19c, bm25_b#4@r19c, dense_b#10@r19c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#9@r19c, hybrid_b#2@r19c, hybrid_c#2@r19c, bm25_b#1@r19c, hybrid_a#3@r19l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 4/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#5@r19c, hybrid_c#5@r19c, bm25_b#5@r19c, hybrid_b#1@r19l, hybrid_c#1@r19l, bm25_a#8@r19l, bm25_b#5@r19l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 4/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_a#9@r19l, hybrid_b#2@r19l, hybrid_c#2@r19l, bm25_b#9@r19l
  - excerpt: /issues. ========================= // Shall we play a game? Time: 2026-06-25 21:57:03 Description: Rendering overlay java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.2+mc1.21.1-mod.jar%23319!/:?] {re:mixin,re:classloading} at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigsLate(ConfigManager.java:76) ~[net.caffeinemc.sodium-neoforge-0.8

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 4/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_b#7@r19c, hybrid_c#7@r19c, hybrid_a#4@r19l, bm25_a#3@r19l
  - excerpt: .fml.ModList.forEachModInOrder(ModList.java:174) ~[loader-4.0.42.jar%23107!/:4.0] {re:mixin} at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModLoader.postEvent(ModLoader.java:358) ~[loader-4.0.42.jar%23107!/:4.0] {} at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.client.ClientHooks.initClientHooks(ClientHooks.java:1028) ~[neoforge-21.1.234-universal.jar%23196!/:?] {re:mixin,re:classloading,pl:mixin:APP:sodium-neoforge.mixins.json:platform.neoforge.ClientHooksMixin from mod sodium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.<init>(Minecraft.java:60

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 4/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: dense_b#7@r19c, hybrid_b#4@r19l, hybrid_c#4@r19l, bm25_b#6@r19l, dense_b#7@r19l
  - excerpt: le.debug` | Whether Gradle is set to debug mode. Debug mode mainly means more Gradle log output. Note that this is for Gradle itself, not Minecraft. | `org.gradle.debug=false` | | `minecraft_version` | The Minecraft version you are modding on. Must match with `neo_version`. | `minecraft_version=1.20.6`

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 3/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r19l, bm25_a#2@r19l, bm25_b#8@r19l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 3/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: bm25_b#7@r19c, hybrid_b#7@r19l, hybrid_c#7@r19l, bm25_b#1@r19l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#4@r19c, hybrid_c#4@r19c, dense_b#1@r19c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **neoforge-docs:user/docs/index** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: NeoForge User Guide
  - https://docs.neoforged.net/user/docs/
  - retrieved by: hybrid_b#3@r19l, hybrid_c#3@r19l, dense_b#1@r19l
  - excerpt: import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; # NeoForge User Guide Whether you are a regular player, pack developer or server administrator, this guide is intended to help you through the process of preparing your computer to run NeoForge, as well as answer some frequently asked questions. The guide mainly aims to help you install NeoForge using the official Minecraft launcher provided by Mojang. There are also a number of third-party launchers that mostly automate this process for you, some of which are mentioned in the article on [third-party launchers][launchers]

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 3/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: hybrid_b#9@r19l, hybrid_c#9@r19l, bm25_b#2@r19l
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:malte0811/FerriteCore#210** (github_issue, 3/6 conditions)
  - FerriteCore issue #210: Game Crush
  - https://github.com/malte0811/FerriteCore/issues/210
  - retrieved by: dense_b#5@r19c, hybrid_b#8@r19l, hybrid_c#8@r19l, dense_b#2@r19l
  - excerpt: [issue by deaddiesel] 1. Forge 47.4.10 2. Minecraft 1.20.1 3. [ferritecore-6.0.1-forge.jar](https://www.curseforge.com/minecraft/mc-mods/ferritecore/files/4810975) [crash-2025-12-10_14.59.18-client.txt](https://github.com/user-attachments/files/24089186/crash-2025-12-10_14.59.18-client.txt) Your mod conflicts with Industrial Upgrade. [comment by malte0811 (owner)] This should be fixed in the latest release of Industrial Upgrade.

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_b#9@r19c, hybrid_c#9@r19c, bm25_b#3@r19c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:mrh0/createaddition#718** (github_issue, 3/6 conditions)
  - createaddition issue #718: Games crashes upon mod loading
  - https://github.com/mrh0/createaddition/issues/718
  - retrieved by: hybrid_b#8@r19c, hybrid_c#8@r19c, dense_b#3@r19c
  - excerpt: [issue by ferforious1] **Describe the bug** Game crashes with an error upon mod loading **To Reproduce** - **Additional context** - Mod version: 1.0.0b - Forge version: 47.2.20 - Create version: 0.5.1f - Minecraft version: 1.20.1 [crash-2024-01-17_09.03.21-fml.txt](https://github.com/mrh0/createaddition/files/13959323/crash-2024-01-17_09.03.21-fml.txt) [comment by mrh0 (owner)] please update to the latest version before submitting a report

- [ ] **gh-issue:mezz/JustEnoughItems#4586** (github_issue, 3/6 conditions)
  - JustEnoughItems issue #4586: [Crash]: JEI version 19.69.0.457 crashes (1.21.1 Forge) when joining the game
  - https://github.com/mezz/JustEnoughItems/issues/4586
  - retrieved by: hybrid_b#10@r19c, hybrid_c#10@r19c, dense_b#4@r19c
  - excerpt: /mc-mods/jei/files/9343790>) - [CurseForge (Fabric)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343789>) - [CurseForge (Forge)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343788>) - [Modrinth (NeoForge)](<https://modrinth.com/mod/u6dRKJwZ/version/pWGmsnGm>) - [Modrinth (Fabric)](<https://modrinth.com/mod/u6dRKJwZ/version/kFIMjB8H>) - [Modrinth (Forge)](<https://modrinth.com/mod/u6dRKJwZ/version/1rvwFzhL>)

- [ ] **neoforge-docs:user/docs/client** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Installing a NeoForge Client
  - https://docs.neoforged.net/user/docs/client/
  - retrieved by: hybrid_b#6@r19c, hybrid_c#6@r19c, bm25_b#8@r19c, hybrid_b#5@r19l, hybrid_c#5@r19l, bm25_b#10@r19l
  - excerpt: [Modrinth][modrinth]. ## Updating To update your NeoForge version, simply download and run the installer for the new NeoForge version, as described above. Then, go to the Installations tab in the launcher and change the version in your NeoForge profile to the new version. :::danger Always backup your world before updating NeoForge or mods! To backup your world, open the game directory and select the `saves` subfolder. Then, copy the folder with your world's name (e.g. `New World`) to a safe location. If anything goes wrong during updating, delete the updated world folder, downgrade NeoFor

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r19c, bm25_a#3@r19c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#10@r19l, bm25_a#1@r19l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r19c, bm25_a#2@r19c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 2/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: hybrid_a#7@r19c, dense_b#9@r19c, hybrid_a#7@r19l, dense_b#5@r19l
  - excerpt: [issue by dghodgson] ### Bug Description Attempting to load Modernfix alongside VMP-Forge will cause the minecraft client to crash. Tested with following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Modernfix 5.18.0+mc1.20.1 seems to launch without any issues. All older versions tested failed with a different error than the one found in the attached log. ### Reproduction Steps Install the following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Forge: 47.4.1 ### Log File ``` MultiMC version: 0.7.0-4230 Launched instance in onlin

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#6@r19c, bm25_a#10@r19c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#122** (github_issue, 2/6 conditions)
  - KotlinForForge issue #122: [1.21.1-Neoforge] Kotlin crashes on NeoForge 1.21.1
  - https://github.com/thedarkcolour/KotlinForForge/issues/122
  - retrieved by: hybrid_b#6@r19l, hybrid_c#6@r19l
  - excerpt: [issue by overlappingd] Mod `fzzy_config` requires Kotlin, Kotlin crashes the game when the Mod Construction stage is about to finish Crash Report: https://mclo.gs/FEz1bUZ `latest.log`: https://mclo.gs/59pOEet Using the [Just Create SMP](https://www.curseforge.com/minecraft/modpacks/just-create-smp) modpack. [comment by thedarkcolour (owner)] Not a KFF issue. Vanilla Backport bug from the looks of it

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r19c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#2@r19l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 1/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: bm25_b#3@r19l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#4@r19c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#4@r19c, hybrid_a#6@r19l
  - excerpt: 9.2, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppDat

- [ ] **gh-issue:mezz/JustEnoughItems#3709** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #3709: [Crash]: Lunar Client is incompatible with JEI mod 1.21/1.21.1
  - https://github.com/mezz/JustEnoughItems/issues/3709
  - retrieved by: bm25_b#4@r19l
  - excerpt: [issue by KR99991] ### Steps to Reproduce the Crash 1. Download lunar client. Select the 1.21.1 or 1.21 fabric version in lunar client. 3. Install jei mod to lunar client. 4. Launch game. ### Mod Pack URL (Optional) https://www.curseforge.com/minecraft/mc-mods/jei/files/5623551 ### Mod Pack Version (Optional) jei-1.21.1-fabric-19.8.4.113 ### Extra Notes (Optional) Please fix it, thanks! ### Crash Report https://gist.github.com/KR99991/7a9982edfe16b8328218399cd7687424 [comment by mezz (owner)] Thanks for the report! The crash log has this error: ``` [2024-08-25 17:02:10.802] [erro

- [ ] **gh-issue:mezz/JustEnoughItems#4255** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4255: [Bug]: Conflict with AE2 and Beyond Dimensions (Neoforge)
  - https://github.com/mezz/JustEnoughItems/issues/4255
  - retrieved by: dense_b#4@r19l
  - excerpt: :** [NeoForge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548363) | [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548362) **Modrinth:** [NeoForge](https://modrinth.com/mod/u6dRKJwZ/version/rPLXajL0) | [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/jEV5BTqf) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `15.33.0.174` for Minecraft `1.20.1`. Thanks for reporting this issue! **CurseForge:** [Fabric](https:

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 1/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: bm25_a#4@r19l
  - excerpt: fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20230612.114412] [19:57:10] [main/INFO]: ModLauncher 10.0.9+10.0.9+main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=M

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#5@r19c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#5@r19l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#6@r19c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:TheIllusiveC4/Curios#535** (github_issue, 1/6 conditions)
  - Curios issue #535: [Bug]: Curios API for 1.21.1 and 1.21 on curseforge can't load in 1.21
  - https://github.com/TheIllusiveC4/Curios/issues/535
  - retrieved by: dense_b#6@r19l
  - excerpt: [issue by Cassy-Lee] ### Minecraft Version 1.21 ### What happened? As described in the title, Curios API for 1.21(.1) depends on neoforge `[21.1.60,)` (in `neoforge.mods.toml`), but newest neoforge for 1.21 was `21.0.167`. Please change supported minecraft version for those files on curseforge to 1.21.1 only. If compatible, please use `[21.0,)` for neoforge version range and make a new release for 1.21. ### Relevant Log Outputs _No response_ [comment by Cassy-Lee (none)] All releases for 1.21(.1) have this problem. [comment by TheIllusiveC4 (owner)] Thanks for notifying me of this overs

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#6@r19l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: bm25_b#6@r19c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/versioning** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Versioning
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/versioning/
  - retrieved by: dense_b#6@r19c, dense_b#8@r19l
  - excerpt: As you probably know, NeoForge is not the only mod loader out there, and many mod developers develop on multiple platforms. As a result, a way to distinguish between two files of the same mod of the same version, but for different mod loaders is needed. Usually, this is done by including the mod loader somewhere in the name. `jei-neoforge-1.20.2-16.0.0.28`, `jei-1.20.2-neoforge-16.0.0.28` or `jei-1.20.2-16.0.0.28-neoforge` are all valid ways to do it. For other mod loaders, the `neoforge` bit would be replaced with `forge`, `fabric`, `quilt` or whatever different mod loader you might be devel

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#7@r19c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:bernie-g/geckolib#850** (github_issue, 1/6 conditions)
  - geckolib issue #850: Animation Parsing Error
  - https://github.com/bernie-g/geckolib/issues/850
  - retrieved by: bm25_a#7@r19l
  - excerpt: [issue by Filan-glitch] GeckoLib V4.8.4 NeoForge 21.1.228 MC1.21.1 Error Logs: [05May2026 11:30:01.258] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.258] [Worker-Main-5/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.261] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.290] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: attack sadly no further information in logs... [comment by Tslat (collaborator)] Provide the mod jar so I can test it I can't do anything with this [comment

- [ ] **gh-issue:wisp-forest/owo-lib#384** (github_issue, 1/6 conditions)
  - owo-lib issue #384: Network error spam with particle systems on 1.21.1 Neoforge
  - https://github.com/wisp-forest/owo-lib/issues/384
  - retrieved by: bm25_b#7@r19l
  - excerpt: [issue by Rearth] Hi, I'm using the owo lib ParticleSystemController / ParticleSystem feature a lot in Oritech (both on fabric and neoforge). I recently was made aware that the neoforge version of owo lib logs an error every time a particle is spawned on the server side. The particles still spawn just fine, but with multiple machines potentially creating particles every tick, it quickly adds up to the logs being unusable. I hope it's okay for me to create issues about the Neoforge version of owo lib here, I wasn't able to create issues in the NF branch. Original issue with logs: https://githu

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#8@r19c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 1/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: hybrid_a#8@r19l
  - excerpt: [issue by ivannf-oviedo] ### Bug Description Hello, I am reporting a critical incompatibility/race condition found in a complex NeoForge 1.21.1 modpack (160+ mods, heavily optimized with Lithium/Sodium). The issue causes a **cascading mod loading failure (FATAL CRASH)** due to multiple major mods failing to access their own registered items during the loading process. ### Bug Description When loading a large pack, the game crashes during the `net.neoforged.neoforge.registries.RegisterEvent`. The error indicates that the item registration has been accelerated too aggressively, causing ke

- [ ] **gh-issue:embeddedt/ModernFix#641** (github_issue, 1/6 conditions)
  - ModernFix issue #641: 1.21.1 WorldEdit 7.3.8 + ModernFix 5.27.x Crash
  - https://github.com/embeddedt/ModernFix/issues/641
  - retrieved by: dense_b#8@r19c
  - excerpt: [issue by magictruffle] ### Bug Description See logs. Issue does not occur with modernfix-neoforge-5.26.1+mc1.21.1.jar. ### Reproduction Steps Generate a new single player world and attempt to enter with mods enabled. ### Log File [crash-2026-04-12_10.11.35-server.txt](https://github.com/user-attachments/files/26659843/crash-2026-04-12_10.11.35-server.txt) [crash-2026-04-12_10.16.00-server.txt](https://github.com/user-attachments/files/26659844/crash-2026-04-12_10.16.00-server.txt) [comment by embeddedt (owner)] Thanks for the report, this should be fixed in the latest builds for all ver

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#8@r19c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r19c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 1/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: dense_b#9@r19l
  - excerpt: ixin,re:classloading} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.handler$zib000$omegaconfig$onReturn(Minecraft.java:4020) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:APP:glitchcore.mixins.json:client.MixinMinecraft from mod glitchcore,pl:mixin:APP:resourcefulconfig.mixins.json:client.MinecraftMixin from mod resourcefulconfig,pl:mixin:APP:omega-config.mixins.json:ClientMixin from mod omegaconfig,pl:mixin:APP:architectury.mixins.json:MixinMinecraft from mod architectu

- [ ] **gh-issue:thedarkcolour/KotlinForForge#105** (github_issue, 1/6 conditions)
  - KotlinForForge issue #105: Wrong fml translation key used, leading to crash when displaying loading errors
  - https://github.com/thedarkcolour/KotlinForForge/issues/105
  - retrieved by: bm25_b#9@r19c
  - excerpt: [issue by Erdragh] ``` java.lang.IllegalArgumentException: When using FML translation keys, only use fml.modloadingissue. keys for mod loading issues: fml.modloading.javafml.dangling_entrypoint at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:30) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:24) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.error(ModLoadingIssue.java:35) ~[loader-4.0.24.jar%23132!/:

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#9@r19l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#10@r19l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: hybrid_a#10@r19c
  - excerpt: .76, 108.156.211.10] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instances/1.19/.minecraft Java path is: /usr/lib/jvm/java-17-openjdk-amd64/bin/java Checking Java version... Java is version 17.0.4, using 64-bit architecture, from Private Build. Intel(R) Pentium(R) Silver N5000 CPU @ 1.10GHz Intel Corporation UHD Graphics 605 (rev 03) DeviceName: Onboard - Video Subsystem: Dell UHD Graphics 605 OpenGL version string: 4.6 (Compatibility Profile) Mesa 21

- [ ] **gh-issue:wisp-forest/owo-lib#336** (github_issue, 1/6 conditions)
  - owo-lib issue #336: Minecraft crashing error code 2
  - https://github.com/wisp-forest/owo-lib/issues/336
  - retrieved by: dense_b#10@r19l
  - excerpt: [issue by NikitaDarkstar] The latest update causes Minecraft 1.21.1 (Neoforge) to crash, giving error code 2. Rolling back to the previous version fixes the problem. [comment by uhloin (none)] Yes log is here: [stdout.txt](https://github.com/user-attachments/files/17958531/stdout.txt) [comment by Dragon-Seeker (member)] Ah my bad, I believe the latest was mis labeled for 1.21.1 instead of 1.21.3 [comment by Dragon-Seeker (member)] Sorry about this as the script is currently set to 1.21.1 and forgot when uploading yesterday to adjust the version to 1.21.2 for latest release but it has bee

- [ ] **neoforge-docs:user/docs/server** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Installing a NeoForge Server
  - https://docs.neoforged.net/user/docs/server/
  - retrieved by: bm25_b#10@r19c
  - excerpt: import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; # Installing a NeoForge Server _This article assumes that you [have the correct version of Java installed][java]._ ## Installing <Tabs defaultValue="unix"> <TabItem value="unix" label="UNIX-like (Linux, macOS, FreeBSD, etc.)"> Running a NeoForge server on Linux, macOS, BSD, or any UNIX-like OS assumes your ability to use basic terminal commands. - Navigate to the folder you'd like to install the server into. - Download the installer `.jar` from the Maven using the following command (swap out version numbers and `-bet

## Added by hand

(none)
