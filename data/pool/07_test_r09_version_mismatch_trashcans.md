# Judging sheet 07: `r09_version_mismatch_trashcans` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `trashcans`  |  **Acceptable:** trashcans
- **What was broken:** updated Trash Cans to the latest build (trashcans-1.1.2a-neoforge-mc26.3.jar), which targets Minecraft 26.x
- **Logs in this scenario:** r09_crash, r09_latest
- **Documents to judge:** 61

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 5/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r09l, hybrid_b#1@r09l, hybrid_c#7@r09l, bm25_a#2@r09l, dense_b#3@r09l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 5/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#8@r09c, hybrid_b#1@r09c, hybrid_c#1@r09c, bm25_b#1@r09c, dense_b#2@r09c, hybrid_a#3@r09l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 5/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_b#8@r09c, dense_b#3@r09c, hybrid_a#10@r09l, hybrid_b#9@r09l, hybrid_c#5@r09l, bm25_b#10@r09l, dense_b#2@r09l
  - excerpt: :B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:A,pl:connector_pre_launch:A,pl:runtimedistcleaner:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.buildInitialScreens(Minecraft.java:675) ~[client-1.21.1-20240808.144430-srg.jar%23317!/:?] {re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mi

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 5/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#4@r09c, hybrid_b#2@r09c, hybrid_c#3@r09c, bm25_b#4@r09c, dense_b#5@r09c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 5/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_b#6@r09c, hybrid_c#7@r09c, dense_b#10@r09c, hybrid_a#2@r09l, bm25_a#10@r09l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 4/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_b#3@r09c, hybrid_c#2@r09c, bm25_b#2@r09c, dense_b#8@r09c, hybrid_c#8@r09l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 4/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#7@r09c, hybrid_b#9@r09c, hybrid_c#8@r09c, bm25_b#3@r09c, hybrid_b#3@r09l, hybrid_c#4@r09l
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 4/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#5@r09c, hybrid_c#5@r09c, bm25_b#5@r09c, hybrid_c#3@r09l, bm25_a#3@r09l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 3/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: hybrid_b#4@r09l, hybrid_c#1@r09l, bm25_b#1@r09l
  - excerpt: .0 because the newer `Placebo` (v9.9.1) conflicted with `CreativeCore` (v2.13.13). This created a secondary crash, as `Apotheosis` (v8.4.0) required `Placebo v9.9.1`. 2. **The Solution that Revealed the Bug:** We resolved the dependency hell by forcing a clean installation of the latest dependency chain (`Apotheosis v8.4.0` + `Placebo v9.9.1` + `CreativeCore v2.13.13`). 3. **The Outcome (The ModernFix Crash):** Although the dependency chain was now correct, the game still crashed instantly upon loading registry events. This proved the crash was not a dependency issue, but a **ModernFix timin

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#4@r09c, hybrid_c#4@r09c, dense_b#1@r09c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 3/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#5@r09c, hybrid_a#4@r09l, hybrid_b#2@r09l, dense_b#4@r09l
  - excerpt: 9.2, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppDat

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_c#6@r09c, hybrid_b#10@r09l, bm25_b#2@r09l
  - excerpt: of the mod shown on the mod list screen. | `displayURL="https://neoforged.net/"` | | `enumExtensions` | string | _nothing_ | The file path of a JSON file used for [enum extension][enumextension]

- [ ] **gh-issue:malte0811/FerriteCore#210** (github_issue, 3/6 conditions)
  - FerriteCore issue #210: Game Crush
  - https://github.com/malte0811/FerriteCore/issues/210
  - retrieved by: hybrid_b#10@r09c, hybrid_c#9@r09c, dense_b#4@r09c
  - excerpt: [issue by deaddiesel] 1. Forge 47.4.10 2. Minecraft 1.20.1 3. [ferritecore-6.0.1-forge.jar](https://www.curseforge.com/minecraft/mc-mods/ferritecore/files/4810975) [crash-2025-12-10_14.59.18-client.txt](https://github.com/user-attachments/files/24089186/crash-2025-12-10_14.59.18-client.txt) Your mod conflicts with Industrial Upgrade. [comment by malte0811 (owner)] This should be fixed in the latest release of Industrial Upgrade.

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 3/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#6@r09c, hybrid_c#10@r09c, bm25_b#6@r09c, hybrid_a#7@r09l
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r09c, bm25_a#3@r09c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 2/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_b#8@r09l, dense_b#1@r09l
  - excerpt: 0.4/cpw.mods.modlauncher.Launcher.main(Launcher.java:74) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.run(BootstrapLauncher.java:210) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:69) at java.base/jdk.internal.reflect.DirectMethodHan

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r09c, bm25_a#2@r09c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:bernie-g/geckolib#804** (github_issue, 2/6 conditions)
  - geckolib issue #804: NullPointerException in GeoArmorRenderer when checking entity glow status
  - https://github.com/bernie-g/geckolib/issues/804
  - retrieved by: hybrid_c#10@r09l, bm25_b#5@r09l
  - excerpt: [issue by Henrique200005] ## Bug Report: NullPointerException in GeoArmorRenderer when checking entity glow status ### Description Game crashes when rendering armor on entities due to a null entity being passed to `shouldEntityAppearGlowing()` method in `GeoArmorRenderer.java` line 333. ### Minecraft Version - **Minecraft**: 1.21.1 - **NeoForge**: 21.1.216 - **GeckoLib**: 4.8.2 (geckolib-neoforge-1.21.1-4.8.2.jar) ### Crash Location ``` at software.bernie.geckolib.renderer.GeoArmorRenderer.renderToBuffer(GeoArmorRenderer.java:333) at net.minecraft.client.Minecraft.shouldEntityAppearGlowing(

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 2/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: hybrid_b#5@r09l, dense_b#5@r09l
  - excerpt: comment by caionodaryluz-ctrl (none)] Minecraft Crash Report ---- // Hey, that tickles! Hehehe! Time: 2026-09-25 22:02:55 Description: mouseClicked event handler java.lang.NullPointerException: Cannot invoke "com.cobblemon.mod.relocations.graalvm.polyglot.Value.execute(Object[])" because "receiveMoveDataFn" is null at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.lambda$movesLoad$0(Moves.java:48) at knot//com.cobblemon.mod.common.battles.ShowdownThread.queue(ShowdownThread.java:32) at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.movesLo

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 2/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: hybrid_a#5@r09l, bm25_a#6@r09l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 2/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: hybrid_b#6@r09l, bm25_b#7@r09l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 2/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: bm25_b#7@r09c, hybrid_c#9@r09l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 2/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: hybrid_a#9@r09l, hybrid_b#7@r09l
  - excerpt: fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20230612.114412] [19:57:10] [main/INFO]: ModLauncher 10.0.9+10.0.9+main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=M

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

- [ ] **gh-issue:TwelveIterations/Waystones#1190** (github_issue, 1/6 conditions)
  - Waystones issue #1190: Crash due to Confluence on newest update [Solution: Remove Confluence or downgrade Waystones]
  - https://github.com/TwelveIterations/Waystones/issues/1190
  - retrieved by: hybrid_c#2@r09l
  - excerpt: [issue by VaporeonScripts] ### Minecraft Version 1.21.1 ### Mod Loader NeoForge ### Describe the Issue crash after updating to the newest balm (required for waystone's anniversary update) ### Logs https://mclo.gs/pmbfo56 [comment by BlayTheNinth (member)] The crash is happening in Prefab and does not seem to be related to Balm. > java.lang.NullPointerException: Cannot invoke "net.minecraft.world.level.ItemLike.asItem()" because "itemlike" is null at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.color.item.ItemColors.register(ItemColors.java:122) ~[client-1.21.1-20240808.144430-sr

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#3@r09c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#3@r09l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:CaffeineMC/sodium#3760** (github_issue, 1/6 conditions)
  - sodium issue #3760: minecraft crashing after collapsing window on 1.21.1 neoforge
  - https://github.com/CaffeineMC/sodium/issues/3760
  - retrieved by: bm25_a#4@r09l
  - excerpt: [issue by Kishebek] ### Bug Description minecraft crashing after collapsing window both in the menu and in the world, also after collapsing my gpu is running up to 100 percent for a second. i checked other version but nothing changed. maybe happening cuz off legacy launcher used sodium 0.6.7 on 1.21.1 neoforge GPU Intel(R) HD Graphics 4600 CPU Intel(R) Core(TM) i3-4000M CPU @ 2.40GHz ### Reproduction Steps 1. lauch sodium 0.6.7 on 1.21.1 neoforge 2. collapse window ### Log File [latest.log](https://github.com/user-attachments/files/29269020/latest.log) ### Crash Report [crash-20

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#4@r09c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:architectury/architectury-api#551** (github_issue, 1/6 conditions)
  - architectury-api issue #551: IClientFluidTypeExtension for Neo
  - https://github.com/architectury/architectury-api/issues/551
  - retrieved by: bm25_b#4@r09l
  - excerpt: that break due to the texture being null incorrectly. If it is up to the modder to register these extensions, you may want to put in some safe guards to inform a dev that they are missing at the very least to try to mitigate the number that slip through. Example of a mod that has recently come by my issue tracker: https://github.com/st0x0ef/stellaris/issues/17 [comment by MaxNeedsSnacks (member)] I haven't worked on Architectury in a hot minute, but from a cursory glance I found out that the mod doesn't seem to actually register fluid types? This should probably additionally be looked at f

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#5@r09c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:embeddedt/ModernFix#641** (github_issue, 1/6 conditions)
  - ModernFix issue #641: 1.21.1 WorldEdit 7.3.8 + ModernFix 5.27.x Crash
  - https://github.com/embeddedt/ModernFix/issues/641
  - retrieved by: bm25_a#5@r09l
  - excerpt: [issue by magictruffle] ### Bug Description See logs. Issue does not occur with modernfix-neoforge-5.26.1+mc1.21.1.jar. ### Reproduction Steps Generate a new single player world and attempt to enter with mods enabled. ### Log File [crash-2026-04-12_10.11.35-server.txt](https://github.com/user-attachments/files/26659843/crash-2026-04-12_10.11.35-server.txt) [crash-2026-04-12_10.16.00-server.txt](https://github.com/user-attachments/files/26659844/crash-2026-04-12_10.16.00-server.txt) [comment by embeddedt (owner)] Thanks for the report, this should be fixed in the latest builds for all ver

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#6@r09c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:Creators-of-Create/Create#10802** (github_issue, 1/6 conditions)
  - Create issue #10802: java lang exeption null in gradle
  - https://github.com/Creators-of-Create/Create/issues/10802
  - retrieved by: hybrid_c#6@r09l
  - excerpt: [issue by Sebz102030] ### Context sometimes when i start client cia gradle for 1.21.1 neoforge game gives java lang exeption null error crash only happends sometimes my system windows 11 java 21 ModDevGradle minecraft_version = 1.21.1 create_version = 6.0.10-280 ponder_version = 1.0.82 flywheel_version = 1.0.6 sableCompanionVersion = 1.6.0 registrate_version = MC1.21-1.3.0+67 I know there was closed issiue about it but it happends to me [debug.log](https://github.com/user-attachments/files/33029191/debug.log) ### Crash Report https://mclo.gs/Tp2lhA5 [comment by IThundxr (member)] This

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#6@r09l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#6@r09l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:mezz/JustEnoughItems#4255** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4255: [Bug]: Conflict with AE2 and Beyond Dimensions (Neoforge)
  - https://github.com/mezz/JustEnoughItems/issues/4255
  - retrieved by: dense_b#6@r09c
  - excerpt: :** [NeoForge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548363) | [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548362) **Modrinth:** [NeoForge](https://modrinth.com/mod/u6dRKJwZ/version/rPLXajL0) | [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/jEV5BTqf) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `15.33.0.174` for Minecraft `1.20.1`. Thanks for reporting this issue! **CurseForge:** [Fabric](https:

- [ ] **gh-issue:wisp-forest/owo-lib#99** (github_issue, 1/6 conditions)
  - owo-lib issue #99: Player crashed and cant log back in
  - https://github.com/wisp-forest/owo-lib/issues/99
  - retrieved by: dense_b#6@r09l
  - excerpt: [issue by gamerpotion] Hi, a player of my modpack - https://www.curseforge.com/minecraft/modpacks/darkrpg has reported that they keep getting constant error as per below and cant login any more, whenever they load the game it shows the following ![image](https://user-images.githubusercontent.com/88756564/220700106-222917ee-6a15-4355-989f-92f551f3cab3.png) ```---- Minecraft Crash Report ---- // Shall we play a game? Time: 2023-02-22 15:21:43 Description: Unexpected error java.lang.NullPointerException: Cannot invoke "net.minecraft.class_5944.method_34583(String, Object)" because

- [ ] **gh-issue:CaffeineMC/sodium#3299** (github_issue, 1/6 conditions)
  - sodium issue #3299: im really tired, can anyone please decipher this crash report and tell me what mod is the problem.
  - https://github.com/CaffeineMC/sodium/issues/3299
  - retrieved by: dense_b#7@r09l
  - excerpt: /java.lang.reflect.Method.invoke(Unknown Source) at com.modrinth.theseus.MinecraftLaunch.relaunch(MinecraftLaunch.java:63) at com.modrinth.theseus.MinecraftLaunch.main(MinecraftLaunch.java:28) A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- Head -- Thread: Render thread Stacktrace: at knot//net.caffeinemc.mods.sodium.client.render.chunk.RenderSectionManager.sectionVisible(RenderSectionManager.java:386) at knot//net.caffeinemc.mods.sodium.client.render.chunk.

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#7@r09c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#865** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #865: Crashes server when upgrading vanilla chest
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/865
  - retrieved by: dense_b#7@r09c
  - excerpt: thium,pl:mixin:APP:lithium.mixins.json:util.chunk_status_tracking.ChunkHolderMixin from mod lithium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.server.level.ServerChunkCache.lambda$tickChunks$4(ServerChunkCache.java:423) ~[server-1.21.1-20240808.144430-srg.ja [... truncated] [comment by P3pp3rF1y (owner)] Looks like some mod that you have there is causing new blockentity that is created as part of the upgrade to not get level properly set on it as it should and as it does based on code I can see in neoforge / vanilla. If you can figure out what mods addition causes this to happ

- [ ] **gh-issue:mezz/JustEnoughItems#4451** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4451: [Crash]: loading issue JEI
  - https://github.com/mezz/JustEnoughItems/issues/4451
  - retrieved by: bm25_a#7@r09l
  - excerpt: [issue by flybywiremod-boop] ### Steps to Reproduce the Crash The culprit is that: [27srp2026 16:55:48.717] [Render thread/INFO] [mezz.jei.common.util.LoggedTimer/]: Starting JEI... [27srp2026 16:55:48.721] [Render thread/INFO] [mezz.jei.library.load.PluginCaller/]: Configuring JEI... [27srp2026 16:55:48.723] [Render thread/INFO] [mezz.jei.library.load.PluginCaller/]: Configuring JEI took 2.027 milliseconds [27srp2026 16:55:48.735] [Render thread/INFO] [mezz.jei.library.load.PluginCaller/]: Registering item subtypes... [27srp2026 16:55:48.748] [Render thread/INFO] [mezz.jei.library.load.Plugi

- [ ] **gh-issue:thedarkcolour/KotlinForForge#35** (github_issue, 1/6 conditions)
  - KotlinForForge issue #35: Kotlin crash on loading when using Magnesium
  - https://github.com/thedarkcolour/KotlinForForge/issues/35
  - retrieved by: hybrid_b#7@r09c
  - excerpt: [issue by IamKayrox] Crash log: ``` ---- Minecraft Crash Report ---- // Hey, that tickles! Hehehe! Time: 07/03/22 01:47 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) [?:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) [?:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null$1(Minecraft.java:508) [?:?] {re:classloading,pl:accesstransform

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 1/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#8@r09l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#8@r09c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 1/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#8@r09l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:bernie-g/geckolib#669** (github_issue, 1/6 conditions)
  - geckolib issue #669: Marvel Mod crashes with latest Geckolib version! Geckolib v. 4.7.2 works fine!
  - https://github.com/bernie-g/geckolib/issues/669
  - retrieved by: hybrid_a#8@r09l
  - excerpt: [issue by Tomatoe1] The error will show that Geckolib latest version 4.7.3 causes the Marvel mod to crash because of a missing model of the vibranium shield! I hope I did it right by including the error log, and I hope it's not too long either... ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 2025-01-02 13:46:53 Description: Rendering overlay java.lang.IllegalArgumentException: No model for layer marvel:vibranium_shield#main at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.model.geom.EntityModelSet.bakeLayer(EntityModelSet.java:17) ~[client-1.21.1-20240808.144430-sr

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 1/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: bm25_b#8@r09l
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **neoforge-docs:user/docs/client** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Installing a NeoForge Client
  - https://docs.neoforged.net/user/docs/client/
  - retrieved by: bm25_b#8@r09c
  - excerpt: [Modrinth][modrinth]. ## Updating To update your NeoForge version, simply download and run the installer for the new NeoForge version, as described above. Then, go to the Installations tab in the launcher and change the version in your NeoForge profile to the new version. :::danger Always backup your world before updating NeoForge or mods! To backup your world, open the game directory and select the `saves` subfolder. Then, copy the folder with your world's name (e.g. `New World`) to a safe location. If anything goes wrong during updating, delete the updated world folder, downgrade NeoFor

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#9@r09c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#9@r09l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:bernie-g/geckolib#684** (github_issue, 1/6 conditions)
  - geckolib issue #684: I crashed while running the rundata command while developing the 1.20.1forge module
  - https://github.com/bernie-g/geckolib/issues/684
  - retrieved by: dense_b#9@r09l
  - excerpt: [issue by Zhixi-mc] The code I wrote should be fine, at least Idea did not report any errors, and there were no errors before adding this dependency. From the error message, the main error is java. lang. NoSuchMethodError: net.minecraft.client.Minecraft net.minecraft.client.Minecraft.m_91087_()'， Below, I will provide you with the complete error message, configuration file, and main class `content: build.gradle:`plugins { id 'eclipse' id 'idea' id 'maven-publish' id 'net.minecraftforge.gradle' version '[6.0,6.2)' } version = mod_version group = mod_group_id base { arc

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: hybrid_a#9@r09c
  - excerpt: .76, 108.156.211.10] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instances/1.19/.minecraft Java path is: /usr/lib/jvm/java-17-openjdk-amd64/bin/java Checking Java version... Java is version 17.0.4, using 64-bit architecture, from Private Build. Intel(R) Pentium(R) Silver N5000 CPU @ 1.10GHz Intel Corporation UHD Graphics 605 (rev 03) DeviceName: Onboard - Video Subsystem: Dell UHD Graphics 605 OpenGL version string: 4.6 (Compatibility Profile) Mesa 21

- [ ] **gh-issue:thedarkcolour/KotlinForForge#105** (github_issue, 1/6 conditions)
  - KotlinForForge issue #105: Wrong fml translation key used, leading to crash when displaying loading errors
  - https://github.com/thedarkcolour/KotlinForForge/issues/105
  - retrieved by: bm25_b#9@r09c
  - excerpt: [issue by Erdragh] ``` java.lang.IllegalArgumentException: When using FML translation keys, only use fml.modloadingissue. keys for mod loading issues: fml.modloading.javafml.dangling_entrypoint at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:30) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:24) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.error(ModLoadingIssue.java:35) ~[loader-4.0.24.jar%23132!/:

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: dense_b#9@r09c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#9@r09l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: dense_b#10@r09l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#10@r09c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:Creators-of-Create/Create#9745** (github_issue, 1/6 conditions)
  - Create issue #9745: Shaders with Create
  - https://github.com/Creators-of-Create/Create/issues/9745
  - retrieved by: hybrid_a#10@r09c
  - excerpt: assets/6cdfa570-13f8-4e8f-b69a-a7c0fd408475" /> ### Game Log https://mclo.gs/nJlYbPX ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.216 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.5 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: AMD Radeon RX 7600 (radeonsi, navi33, LLVM 21.1.6, DRM 3.64, 6.18.2-3-cachyos) OpenGL Version: 4.6 (Core Profile) Mesa 25.3.2-arch1.2 Graphics Mode: fancy PojavLauncher Dete

- [ ] **neoforge-docs:user/docs/server** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Installing a NeoForge Server
  - https://docs.neoforged.net/user/docs/server/
  - retrieved by: bm25_b#10@r09c
  - excerpt: import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; # Installing a NeoForge Server _This article assumes that you [have the correct version of Java installed][java]._ ## Installing <Tabs defaultValue="unix"> <TabItem value="unix" label="UNIX-like (Linux, macOS, FreeBSD, etc.)"> Running a NeoForge server on Linux, macOS, BSD, or any UNIX-like OS assumes your ability to use basic terminal commands. - Navigate to the folder you'd like to install the server into. - Download the installer `.jar` from the Maven using the following command (swap out version numbers and `-bet

## Added by hand

(none)
