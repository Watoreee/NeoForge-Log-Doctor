# Judging sheet 11: `r16_version_mismatch_yungsapi` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `yungsapi`  |  **Acceptable:** yungsapi, betterdungeons, betterendisland, bettermineshafts, betterstrongholds
- **What was broken:** downgraded YUNG's API to the 1.20.4 build (YungsApi-1.20.4-NeoForge-4.4.3.jar); NeoForge 21.1 skipped the jar as being for Forge or an older NeoForge, so betterstrongholds, bettermineshafts, betterdungeons and betterendisland reported yungsapi as not installed
- **Logs in this scenario:** r16_crash, r16_latest
- **Documents to judge:** 65

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 5/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#7@r16c, hybrid_b#1@r16c, hybrid_c#2@r16c, bm25_b#3@r16c, dense_b#10@r16c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 4/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#5@r16c, hybrid_b#2@r16c, hybrid_c#1@r16c, bm25_b#6@r16c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 4/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r16c, bm25_b#5@r16c, hybrid_b#1@r16l, hybrid_c#4@r16l, bm25_b#1@r16l, dense_b#9@r16l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 4/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#4@r16c, hybrid_c#10@r16c, bm25_b#2@r16c, dense_b#5@r16l
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 3/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_b#9@r16c, hybrid_a#1@r16l, hybrid_b#8@r16l, bm25_a#2@r16l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 3/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_c#3@r16c, bm25_b#9@r16c, hybrid_c#1@r16l, bm25_a#9@r16l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#4@r16c, hybrid_a#8@r16l, bm25_a#1@r16l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 3/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r16c, hybrid_c#8@r16c, bm25_a#2@r16c, hybrid_a#9@r16l, hybrid_c#5@r16l
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 3/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_b#2@r16l, bm25_b#6@r16l, dense_b#10@r16l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 3/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#8@r16c, hybrid_c#7@r16c, bm25_b#7@r16c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r16c, bm25_a#3@r16c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 2/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: hybrid_b#10@r16c, dense_b#1@r16c, hybrid_b#10@r16l, dense_b#1@r16l
  - excerpt: found. So I am a bit confused. [comment by RockinOstrich (none)] When I use NeoForge 21.1.31, it's fine, but if I try updating it to Neoforge 21.1.32+, I get that crash report (the one SirTwsted got), and that's the only thing I've changed. Any suggestions? I know you mentioned above about omegaconfig, but I don't know how to read or interpret a crash report: [crash-2024-10-21_20.18.46-client.txt](https://github.com/user-attachments/files/17468161/crash-2024-10-21_20.18.46-client.txt) [comment by Redfan2 (none)] > > omegaconfig > > @Jab125 > > I don't understand. I typed omegaconfig

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 2/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_c#4@r16c, bm25_b#1@r16c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 2/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_a#3@r16l, dense_b#4@r16l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#3@r16c, bm25_a#6@r16c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TwelveIterations/Waystones#1118** (github_issue, 2/6 conditions)
  - Waystones issue #1118: Waystones mod looks for a missing KumaAPI and crashes when clicking on any waystone
  - https://github.com/TwelveIterations/Waystones/issues/1118
  - retrieved by: dense_b#9@r16c, hybrid_b#3@r16l, dense_b#3@r16l
  - excerpt: CurseForge. [comment by ako256 (none)] Tried reinstalling it after removing both waystones and balm, still the same issue. Here's the latest.log file: [latest.log](https://github.com/user-attachments/files/24844284/latest.log) [comment by ako256 (none)] I tried it with a new profile with no other mods, it seems to work fine with just balm, fabric API and waystones mods installed [comment by BlayTheNinth (member)] Try updating Fabric Loader to 0.18.4 (in the instance's settings), it seems to be an issue on older versions of Fabric Loader. [comment by ako256 (none)] Yep, updating the fabric

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 2/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_b#8@r16c, bm25_a#3@r16l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 2/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#4@r16c, hybrid_c#6@r16c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 2/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: hybrid_b#5@r16c, dense_b#7@r16c, hybrid_b#4@r16l
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 2/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: hybrid_b#6@r16c, hybrid_c#5@r16c
  - excerpt: BalmClientEvents$$Lambda/0x00000296fbe78800@4911b7bf 17: net.neoforged.bus.EventListenerFactory$guiPostInit/0x00000296fcde3c00@41bb9bf6 java.lang.IllegalStateException: Cannot get config value before config is loaded. at MC-BOOTSTRAP/com.google.common@32.1.2-jre/com.google.common.base.Preconditions.checkState(Preconditions.java:512) at TRANSFORMER/neoforge@21.1.90/net.neoforged.neoforge.common.ModConfigSpec$ConfigValue.getRaw(ModConfigSpec.java:1235) at TRANSFORMER/neoforge@21.1.90/net.neoforged.neoforge.common.ModConfigSpec$ConfigValue.get(ModConfigSpec.java:1222) at TRANSFORMER/b

- [ ] **gh-issue:TwelveIterations/Waystones#905** (github_issue, 2/6 conditions)
  - Waystones issue #905: Game not saving after activating waystone
  - https://github.com/TwelveIterations/Waystones/issues/905
  - retrieved by: hybrid_a#7@r16l, hybrid_b#5@r16l
  - excerpt: locked slot indices to New World.json ### Do you use any performance-enhancing mods (e.g. OptiFine) or custom server distributions (e.g. SpongeForge)? sodium,iris and Dynamic FPS by juliand665 [comment by BlayTheNinth (member)] Please provide the **full** logs. You can find the logs in the `logs` directory of the client or server. Most of the time `latest.log` is the correct file (unless the crash or issue happened during an earlier run). Logs can be uploaded here by dragging the file into the comment field, or you can post them on a site like https://gist.github.com/ or https://pa

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 2/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#6@r16l, bm25_b#10@r16l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:architectury/architectury-api#497** (github_issue, 2/6 conditions)
  - architectury-api issue #497: [1.20.5] architectury crash on neoforge
  - https://github.com/architectury/architectury-api/issues/497
  - retrieved by: hybrid_b#7@r16c, dense_b#6@r16c
  - excerpt: [issue by st0x0ef] Architectury doesn't load on neoforge since it try to use the ClientTickEvent CrashLog : ``` Caused by 0: java.lang.NoClassDefFoundError: net/neoforged/neoforge/event/TickEvent$ClientTickEvent at java.base/java.lang.Class.getDeclaredMethods0(Native Method) ~[?:?] {} at java.base/java.lang.Class.privateGetDeclaredMethods(Class.java:3578) ~[?:?] {} at java.base/java.lang.Class.getDeclaredMethods(Class.java:2676) ~[?:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.register(EventBus.java:85) ~[bus-7.2.0.jar%2394!/:?] {} at TRANSFORMER/archi

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 2/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#9@r16c, hybrid_b#6@r16l
  - excerpt: 9.2, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppDat

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 2/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: hybrid_b#7@r16l, hybrid_c#6@r16l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 2/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_b#8@r16c, bm25_a#7@r16l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 2/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: hybrid_c#9@r16l, dense_b#8@r16l
  - excerpt: ixin,re:classloading} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.handler$zib000$omegaconfig$onReturn(Minecraft.java:4020) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:APP:glitchcore.mixins.json:client.MixinMinecraft from mod glitchcore,pl:mixin:APP:resourcefulconfig.mixins.json:client.MinecraftMixin from mod resourcefulconfig,pl:mixin:APP:omega-config.mixins.json:ClientMixin from mod omegaconfig,pl:mixin:APP:architectury.mixins.json:MixinMinecraft from mod architectu

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 2/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: bm25_a#8@r16l, bm25_b#8@r16l
  - excerpt: fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20230612.114412] [19:57:10] [main/INFO]: ModLauncher 10.0.9+10.0.9+main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=M

- [ ] **gh-issue:TwelveIterations/Waystones#985** (github_issue, 2/6 conditions)
  - Waystones issue #985: Unable to rename sharestones
  - https://github.com/TwelveIterations/Waystones/issues/985
  - retrieved by: hybrid_a#10@r16l, hybrid_b#9@r16l
  - excerpt: fabric-api-0.97.2+1.20.4.jar botarium-fabric-1.20.4-3.2.2.jar shulkerboxtooltip-fabric-4.1.0+1.20.4.jar YungsBetterJungleTemples-1.20.4-Fabric-2.4.4.jar YungsBridges-1.20.4-Fabric-4.4.2.jar iris-1.7.0+mc1.20.4.jar trinkets-3.8.1.jar elytraslot-fabric-7.0.1+1.20.4.jar immersive-portals-5.1.10-mc1.20.4-fabric.jar Inventory [... truncated] [comment by BlayTheNinth (member)] Sorry, 1.20.4 is no longer supported and will not be receiving any more updates. I recommend staying on Minecraft 1.20.1 for stability as most mods have settled on that version.

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r16c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 1/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#2@r16l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:embeddedt/ModernFix#503** (github_issue, 1/6 conditions)
  - ModernFix issue #503: MC 1.21.x [Incompatibility] Additional Placement Fabric with the Dynamic Ressouce Loading option enabled
  - https://github.com/embeddedt/ModernFix/issues/503
  - retrieved by: hybrid_c#2@r16l
  - excerpt: fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb73304 |-- fabric-rendering-v1 10.1.2+b874120c04 |-- fabric-resource-conditions-api-v1 5.0.13+203e6b2304 |-- fabric-resource-loader-v0 3.0.11+b1caf1e904 |-- fabric-screen-api-v1 2.0.38+7feeb73304 |-- fabric-screen-handler-api-v1 1.3.110+7feeb73304 |-- fabric-sound-api-v1 [... truncated] [comment by Lonseuks (none)] Same happen with the Neoforge version 1.21.x https://mclo.gs/SmqtUPw [comment by embeddedt (owner)] https://github.com/FirEmerald/AdditionalPlacement

- [ ] **gh-issue:mezz/JustEnoughItems#4003** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4003: [Crash]: 1.21.5 latest neoforge update crash
  - https://github.com/mezz/JustEnoughItems/issues/4003
  - retrieved by: dense_b#2@r16c
  - excerpt: } at TRANSFORMER/jei@21.3.0.17/mezz.jei.library.plugins.vanilla.anvil.AnvilRecipeMaker$EnchantmentData.getEnchantedBooks(AnvilRecipeMaker.java:73) ~[jei-1.21.5-neoforge-21.3.0.17.jar%23219!/:21.3.0.17] {re:classloading} at TRANSFORMER/jei@21.3.0.17/mezz.jei.library.plugins.vanilla.anvil.AnvilRecipeMaker.lambda$getBookEnchantmentRecipes$2(AnvilRecipeMaker.java:123) ~[jei-1.21.5-neoforge-21.3.0.17.jar%23219!/:21.3.0.17] {re:classloading}` ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) _No response_ ### Crash Report .

- [ ] **gh-issue:shedaniel/cloth-config#162** (github_issue, 1/6 conditions)
  - cloth-config issue #162: Duplicate Cloth Class
  - https://github.com/shedaniel/cloth-config/issues/162
  - retrieved by: hybrid_a#2@r16l
  - excerpt: [issue by Chaosyr] [17:57:44] [main/INFO]: Loading Minecraft 1.19 with Fabric Loader 0.14.8 [17:57:44] [ForkJoinPool-1-worker-4/WARN]: Mod journeymap uses the version 5.8.5rc2 which isn't compatible with Loader's extended semantic version format (Could not parse version number component '5rc2'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [17:57:45] [ForkJoinPool-1-worker-3/WARN]: Mod saplanting uses the version fabric-1.19-1.1.2+fix-1 which isn't compatible with Loader's extended semantic version format (Could not parse version number component

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#2@r16l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#3@r16l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: dense_b#3@r16c
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **neoforge-docs:user/docs/client** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Installing a NeoForge Client
  - https://docs.neoforged.net/user/docs/client/
  - retrieved by: hybrid_c#3@r16l
  - excerpt: [Modrinth][modrinth]. ## Updating To update your NeoForge version, simply download and run the installer for the new NeoForge version, as described above. Then, go to the Installations tab in the launcher and change the version in your NeoForge profile to the new version. :::danger Always backup your world before updating NeoForge or mods! To backup your world, open the game directory and select the `saves` subfolder. Then, copy the folder with your world's name (e.g. `New World`) to a safe location. If anything goes wrong during updating, delete the updated world folder, downgrade NeoFor

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#4@r16c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#4@r16l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:bernie-g/geckolib#684** (github_issue, 1/6 conditions)
  - geckolib issue #684: I crashed while running the rundata command while developing the 1.20.1forge module
  - https://github.com/bernie-g/geckolib/issues/684
  - retrieved by: dense_b#4@r16c, dense_b#6@r16l
  - excerpt: [issue by Zhixi-mc] The code I wrote should be fine, at least Idea did not report any errors, and there were no errors before adding this dependency. From the error message, the main error is java. lang. NoSuchMethodError: net.minecraft.client.Minecraft net.minecraft.client.Minecraft.m_91087_()'， Below, I will provide you with the complete error message, configuration file, and main class `content: build.gradle:`plugins { id 'eclipse' id 'idea' id 'maven-publish' id 'net.minecraftforge.gradle' version '[6.0,6.2)' } version = mod_version group = mod_group_id base { arc

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#4@r16l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#4@r16l
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:CaffeineMC/sodium#3792** (github_issue, 1/6 conditions)
  - sodium issue #3792: crash 1.21.1 neoforge
  - https://github.com/CaffeineMC/sodium/issues/3792
  - retrieved by: dense_b#5@r16c
  - excerpt: [issue by bryaN171Z] ### Bug Description The error happens sometimes; sometimes it loads without crashing, and at other times, a crash occurs. ### Reproduction Steps Sodium works fine when it's the only mod in the folder; the error starts when you add the Ender Cataclysm mod to the folder. ### Log File sodium-neoforge-0.8.12-beta.2+mc1.21.1.jar ### Crash Report https://mclo.gs/XMzlhH4 [comment by jellysquid3 (member)] This is almost guaranteed to not be a bug with Sodium (cascading mod load error), but your crash report is useless and you did not provide any of the information we aske

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#5@r16c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 1/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: bm25_a#5@r16l
  - excerpt: [issue by dghodgson] ### Bug Description Attempting to load Modernfix alongside VMP-Forge will cause the minecraft client to crash. Tested with following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Modernfix 5.18.0+mc1.20.1 seems to launch without any issues. All older versions tested failed with a different error than the one found in the attached log. ### Reproduction Steps Install the following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Forge: 47.4.1 ### Log File ``` MultiMC version: 0.7.0-4230 Launched instance in onlin

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#5@r16l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#5@r16l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:Creators-of-Create/Create#9745** (github_issue, 1/6 conditions)
  - Create issue #9745: Shaders with Create
  - https://github.com/Creators-of-Create/Create/issues/9745
  - retrieved by: hybrid_a#6@r16c
  - excerpt: assets/6cdfa570-13f8-4e8f-b69a-a7c0fd408475" /> ### Game Log https://mclo.gs/nJlYbPX ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.216 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.5 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: AMD Radeon RX 7600 (radeonsi, navi33, LLVM 21.1.6, DRM 3.64, 6.18.2-3-cachyos) OpenGL Version: 4.6 (Core Profile) Mesa 25.3.2-arch1.2 Graphics Mode: fancy PojavLauncher Dete

- [ ] **gh-issue:embeddedt/ModernFix#536** (github_issue, 1/6 conditions)
  - ModernFix issue #536: [1.21.4+] dynamic_entity_renderers is broken
  - https://github.com/embeddedt/ModernFix/issues/536
  - retrieved by: hybrid_a#6@r16l
  - excerpt: [issue by Poopooracoocoo] ### Bug Description Hangs on Mojang splash screen ### Reproduction Steps 1. Launch game with ModernFix and [Entity View Distance](https://modrinth.com/mod/entity-view-distance) and with ModernFix's dynamic_entity_renderers set to true ### Log File [latest.log](https://github.com/user-attachments/files/19275619/latest.log) <details><summary>Details</summary> ``` [08:56:54] [main/INFO]: Loading Minecraft 1.21.4 with Fabric Loader 0.16.10 [08:56:54] [main/WARN]: Skipping missing system property provided mod path C:\Users\<user>\AppData\Roaming\Pris

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#7@r16c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:embeddedt/ModernFix#660** (github_issue, 1/6 conditions)
  - ModernFix issue #660: mixin.perf.faster_ingredients breaks many recipes from Prefab mod (especially conditional recipes)
  - https://github.com/embeddedt/ModernFix/issues/660
  - retrieved by: bm25_b#7@r16l
  - excerpt: (Brian Wuest) confirmed this is a **ModernFix-side issue**, not a Prefab bug. Quote from Prefab developer: > "Found issue, turn off the setting: mixin.perf.faster_ingredients. This for some reason is what is causing ALL of Prefab's recipes to be broken! Not just the ones you pointed out. ... This needs to be reported to the Modern Fix mod team as this is not something I can fix within Prefab." Workaround: Setting `mixin.perf.faster_ingredients = false` immediately restores all affected recipes. ### Minimal Mod List **Minimal reproduction list:** - ModernFix 5.27.5+mc1.21.1 (NeoForge) - P

- [ ] **gh-issue:mezz/JustEnoughItems#3709** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #3709: [Crash]: Lunar Client is incompatible with JEI mod 1.21/1.21.1
  - https://github.com/mezz/JustEnoughItems/issues/3709
  - retrieved by: dense_b#7@r16l
  - excerpt: [issue by KR99991] ### Steps to Reproduce the Crash 1. Download lunar client. Select the 1.21.1 or 1.21 fabric version in lunar client. 3. Install jei mod to lunar client. 4. Launch game. ### Mod Pack URL (Optional) https://www.curseforge.com/minecraft/mc-mods/jei/files/5623551 ### Mod Pack Version (Optional) jei-1.21.1-fabric-19.8.4.113 ### Extra Notes (Optional) Please fix it, thanks! ### Crash Report https://gist.github.com/KR99991/7a9982edfe16b8328218399cd7687424 [comment by mezz (owner)] Thanks for the report! The crash log has this error: ``` [2024-08-25 17:02:10.802] [erro

- [ ] **gh-issue:mezz/JustEnoughItems#4255** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4255: [Bug]: Conflict with AE2 and Beyond Dimensions (Neoforge)
  - https://github.com/mezz/JustEnoughItems/issues/4255
  - retrieved by: hybrid_c#7@r16l
  - excerpt: :** [NeoForge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548363) | [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548362) **Modrinth:** [NeoForge](https://modrinth.com/mod/u6dRKJwZ/version/rPLXajL0) | [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/jEV5BTqf) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `15.33.0.174` for Minecraft `1.20.1`. Thanks for reporting this issue! **CurseForge:** [Fabric](https:

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#8@r16c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 1/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: hybrid_c#8@r16l
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:architectury/architectury-api#535** (github_issue, 1/6 conditions)
  - architectury-api issue #535: Architectury api always crashing
  - https://github.com/architectury/architectury-api/issues/535
  - retrieved by: dense_b#8@r16c
  - excerpt: ne)] the same here: Neoforge: 21.0.87 Architectury: i try it with 4 versions available log: [log crash.txt](https://github.com/user-attachments/files/16202574/log.crash.txt) [comment by ascenstohe4vn (none)] i also have this issue [comment by Jab125 (member)] > the same here: > > Neoforge: 21.0.87 Architectury: i try it with 4 versions available > > log: [log crash.txt](https://github.com/user-attachments/files/16202574/log.crash.txt) Your crash is not related. You need to install [YACL](https://modrinth.com/mod/yacl).

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r16c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:TwelveIterations/Waystones#1126** (github_issue, 1/6 conditions)
  - Waystones issue #1126: Natural Waystone activation invalid.
  - https://github.com/TwelveIterations/Waystones/issues/1126
  - retrieved by: bm25_b#9@r16l
  - excerpt: [issue by von-get] ### Minecraft Version 1.21.11 ### Mod Loader Fabric ### Describe the Issue When activating a new waystone found in a village (haven't found wild ones yet), it will 'successfully' activate it with the name 'invalid'. Right-clicking it again does not bring up the teleport menu, but instead just 'successfully' activates again. I didn't have this issue before upgrading to 21.11.5, and downgrading it to 21.11.4 seems to have resolved it. Additionally, picking up the waystone and putting it back down does seem to allow normal interaction. ### Logs ``` [00:27:08] [main/INF

- [ ] **gh-issue:mezz/JustEnoughItems#4586** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4586: [Crash]: JEI version 19.69.0.457 crashes (1.21.1 Forge) when joining the game
  - https://github.com/mezz/JustEnoughItems/issues/4586
  - retrieved by: hybrid_c#9@r16c
  - excerpt: /mc-mods/jei/files/9343790>) - [CurseForge (Fabric)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343789>) - [CurseForge (Forge)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343788>) - [Modrinth (NeoForge)](<https://modrinth.com/mod/u6dRKJwZ/version/pWGmsnGm>) - [Modrinth (Fabric)](<https://modrinth.com/mod/u6dRKJwZ/version/kFIMjB8H>) - [Modrinth (Forge)](<https://modrinth.com/mod/u6dRKJwZ/version/1rvwFzhL>)

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#10@r16c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 1/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: hybrid_a#10@r16c
  - excerpt: ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.234 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:instancing OpenGL Renderer: Intel(R) UHD Graphics OpenGL Version: 4.6.0 - Build 31.0.101.2127 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecr

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 1/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: hybrid_c#10@r16l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#10@r16l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **neoforge-docs:user/docs/server** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Installing a NeoForge Server
  - https://docs.neoforged.net/user/docs/server/
  - retrieved by: bm25_b#10@r16c
  - excerpt: import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; # Installing a NeoForge Server _This article assumes that you [have the correct version of Java installed][java]._ ## Installing <Tabs defaultValue="unix"> <TabItem value="unix" label="UNIX-like (Linux, macOS, FreeBSD, etc.)"> Running a NeoForge server on Linux, macOS, BSD, or any UNIX-like OS assumes your ability to use basic terminal commands. - Navigate to the folder you'd like to install the server into. - Download the installer `.jar` from the Maven using the following command (swap out version numbers and `-bet

## Added by hand

(none)
