# Judging sheet 19: `r18_version_mismatch_sophisticatedcore` (dev)

- **Category:** `version_mismatch`  |  **Culprit:** `sophisticatedcore`  |  **Acceptable:** sophisticatedcore
- **What was broken:** updated Sophisticated Core to the Minecraft 26.1.2 build (sophisticatedcore-26.1.2-1.5.24.2445.jar) in a 1.21.1 pack; its 'only supports jei 29.5.0.24' line is a side effect, not a JEI problem
- **Logs in this scenario:** r18_crash, r18_latest
- **Documents to judge:** 52

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 5/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#5@r18c, hybrid_b#1@r18c, hybrid_c#1@r18c, bm25_b#1@r18c, dense_b#2@r18c, hybrid_a#4@r18l, dense_b#5@r18l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#725** (github_issue, 5/6 conditions)
  - SophisticatedStorage issue #725: Server side crash when inserting Compression upgrade into limited barrel Neoforge 1.21.8
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/725
  - retrieved by: hybrid_b#9@r18c, hybrid_c#5@r18c, hybrid_a#6@r18l, hybrid_b#2@r18l, hybrid_c#2@r18l, bm25_b#7@r18l, dense_b#7@r18l
  - excerpt: [issue by Neposis] Mod: Sophisticated Storage Version: 1.4.50 (NeoForge 1.21.8) Core: Sophisticated Core 1.3.65 Environment: Minecraft 1.21.8 NeoForge 21.8.35 Dedicated server (Linux, Java 21) Good afternoon, I am having an issue where my server insta crashes as soon as I right click the compression upgrade onto a limited barrel 3 (only tested black) or trying to insert it in via the interface. Maybe caused by a client side call on server? java.lang.NoClassDefFoundError: net/minecraft/client/renderer/texture/TextureAtlas at net.p3pp3rf1y.sophisticatedstorage.upgrades.compression.Compre

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 5/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#5@r18c, hybrid_c#6@r18c, bm25_b#8@r18c, hybrid_a#2@r18l, hybrid_b#3@r18l, hybrid_c#3@r18l, bm25_a#7@r18l, bm25_b#6@r18l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 5/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r18c, hybrid_b#2@r18c, hybrid_c#2@r18c, bm25_b#2@r18c, dense_b#10@r18c, dense_b#10@r18l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 4/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#1@r18l, hybrid_b#5@r18l, hybrid_c#5@r18l, bm25_a#2@r18l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#825** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #825: [Neoforge 1.21.11] ticking entity crash
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/825
  - retrieved by: dense_b#8@r18c, hybrid_b#1@r18l, hybrid_c#1@r18l, bm25_b#8@r18l, dense_b#2@r18l
  - excerpt: [issue by Baggytrousers27] SophisticatedCore is named in the crashlog but there isn't a repo for it so posting it here instead. Seemed to occur after cursor moved over an item in Backpack Description: Ticking entity com.google.common.util.concurrent.UncheckedExecutionException: java.lang.IllegalArgumentException: Failed to hash minecraft:max_damage=>0: Value must be positive: 0 [Crashlog](https://pastebin.com/RcQVcg5K) (Will post a Full log when Gists decide to work again) sophisticatedbackpacks-1.21.11-3.25.34.1565 sophisticatedcore-1.21.11-1.4.7.1513 sophisticateditemactions-1.21.11-0.3.

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 4/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#7@r18c, hybrid_b#3@r18c, hybrid_c#7@r18c, bm25_b#6@r18c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 4/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: hybrid_a#9@r18c, hybrid_b#9@r18l, hybrid_c#9@r18l, dense_b#3@r18l
  - excerpt: [issue by dghodgson] ### Bug Description Attempting to load Modernfix alongside VMP-Forge will cause the minecraft client to crash. Tested with following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Modernfix 5.18.0+mc1.20.1 seems to launch without any issues. All older versions tested failed with a different error than the one found in the attached log. ### Reproduction Steps Install the following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Forge: 47.4.1 ### Log File ``` MultiMC version: 0.7.0-4230 Launched instance in onlin

- [ ] **gh-issue:malte0811/FerriteCore#210** (github_issue, 3/6 conditions)
  - FerriteCore issue #210: Game Crush
  - https://github.com/malte0811/FerriteCore/issues/210
  - retrieved by: hybrid_c#9@r18c, dense_b#3@r18c, hybrid_b#6@r18l, hybrid_c#6@r18l, dense_b#1@r18l
  - excerpt: [issue by deaddiesel] 1. Forge 47.4.10 2. Minecraft 1.20.1 3. [ferritecore-6.0.1-forge.jar](https://www.curseforge.com/minecraft/mc-mods/ferritecore/files/4810975) [crash-2025-12-10_14.59.18-client.txt](https://github.com/user-attachments/files/24089186/crash-2025-12-10_14.59.18-client.txt) Your mod conflicts with Industrial Upgrade. [comment by malte0811 (owner)] This should be fixed in the latest release of Industrial Upgrade.

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 3/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: hybrid_b#7@r18l, hybrid_c#7@r18l, bm25_b#1@r18l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 3/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: hybrid_b#8@r18l, hybrid_c#8@r18l, bm25_b#2@r18l
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 3/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_c#10@r18c, bm25_a#8@r18c, bm25_b#3@r18c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#7@r18c, hybrid_c#3@r18c, dense_b#5@r18c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 3/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: hybrid_b#10@r18l, hybrid_c#10@r18l, bm25_b#3@r18l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 3/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_a#8@r18l, hybrid_b#4@r18l, hybrid_c#4@r18l
  - excerpt: /issues. ========================= // Shall we play a game? Time: 2026-06-25 21:57:03 Description: Rendering overlay java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.2+mc1.21.1-mod.jar%23319!/:?] {re:mixin,re:classloading} at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigsLate(ConfigManager.java:76) ~[net.caffeinemc.sodium-neoforge-0.8

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: hybrid_b#8@r18c, hybrid_c#4@r18c, dense_b#8@r18l
  - excerpt: $registerEventHandlers$2(BetterModsButtonNeoForgeClient.java:53) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.ConsumerEventHandler.invoke(ConsumerEventHandler.java:26) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:315) at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.gui.screens.Screen.init [... truncated] [comment by P3pp3rF1y (owner)] I don't see anything related to sophisticated in this crash log other than the fact that it's one of the mods on the list.

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r18c, bm25_a#3@r18c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:mezz/JustEnoughItems#4586** (github_issue, 2/6 conditions)
  - JustEnoughItems issue #4586: [Crash]: JEI version 19.69.0.457 crashes (1.21.1 Forge) when joining the game
  - https://github.com/mezz/JustEnoughItems/issues/4586
  - retrieved by: hybrid_b#6@r18c, dense_b#1@r18c
  - excerpt: /mc-mods/jei/files/9343790>) - [CurseForge (Fabric)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343789>) - [CurseForge (Forge)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343788>) - [Modrinth (NeoForge)](<https://modrinth.com/mod/u6dRKJwZ/version/pWGmsnGm>) - [Modrinth (Fabric)](<https://modrinth.com/mod/u6dRKJwZ/version/kFIMjB8H>) - [Modrinth (Forge)](<https://modrinth.com/mod/u6dRKJwZ/version/1rvwFzhL>)

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#9@r18l, bm25_a#1@r18l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r18c, bm25_a#2@r18c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 2/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#3@r18c, bm25_b#10@r18c, hybrid_a#7@r18l
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 2/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#6@r18c, hybrid_a#3@r18l, dense_b#9@r18l
  - excerpt: 9.2, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppDat

- [ ] **gh-issue:mezz/JustEnoughItems#4003** (github_issue, 2/6 conditions)
  - JustEnoughItems issue #4003: [Crash]: 1.21.5 latest neoforge update crash
  - https://github.com/mezz/JustEnoughItems/issues/4003
  - retrieved by: hybrid_b#4@r18c, dense_b#7@r18c
  - excerpt: } at TRANSFORMER/jei@21.3.0.17/mezz.jei.library.plugins.vanilla.anvil.AnvilRecipeMaker$EnchantmentData.getEnchantedBooks(AnvilRecipeMaker.java:73) ~[jei-1.21.5-neoforge-21.3.0.17.jar%23219!/:21.3.0.17] {re:classloading} at TRANSFORMER/jei@21.3.0.17/mezz.jei.library.plugins.vanilla.anvil.AnvilRecipeMaker.lambda$getBookEnchantmentRecipes$2(AnvilRecipeMaker.java:123) ~[jei-1.21.5-neoforge-21.3.0.17.jar%23219!/:21.3.0.17] {re:classloading}` ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) _No response_ ### Crash Report .

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 2/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_c#8@r18c, bm25_a#4@r18l
  - excerpt: .fml.ModList.forEachModInOrder(ModList.java:174) ~[loader-4.0.42.jar%23107!/:4.0] {re:mixin} at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModLoader.postEvent(ModLoader.java:358) ~[loader-4.0.42.jar%23107!/:4.0] {} at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.client.ClientHooks.initClientHooks(ClientHooks.java:1028) ~[neoforge-21.1.234-universal.jar%23196!/:?] {re:mixin,re:classloading,pl:mixin:APP:sodium-neoforge.mixins.json:platform.neoforge.ClientHooksMixin from mod sodium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.<init>(Minecraft.java:60

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_a#10@r18l, bm25_b#9@r18l
  - excerpt: of the mod shown on the mod list screen. | `displayURL="https://neoforged.net/"` | | `enumExtensions` | string | _nothing_ | The file path of a JSON file used for [enum extension][enumextension]

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r18c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#3@r18l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10344** (github_issue, 1/6 conditions)
  - Create issue #10344: Cannot read field "x" because "mf.axis" is null
  - https://github.com/Creators-of-Create/Create/issues/10344
  - retrieved by: bm25_b#4@r18c, bm25_b#5@r18l
  - excerpt: NeoForge$$Lambda/0x0000000076f81078@ccb2269 2: net.p3pp3rf1y.sophisticatedcore.common.CommonEventHandler$$Lambda/0x0000000076fa9000@5d251949 3: net.neoforged.neoforge.common.NeoForgeMod$$Lambda/0x0000000077057018@21a04589 4: net.p3pp3rf1y.sophisticatedbackpacks.common.CommonEventHandler$$Lambda/0x000000007731a270@1dd00c23 5: net.neoforged.bus.EventListenerFactory$onServerTick/0x00000000774b1800@4735f276 6: net.fabricmc.fabric.impl.event.lifecycle.LifecycleEventsImpl$$Lambda/0x00000000774e4990@16109588 7: com.hlysine.create_connected.CreateConnected$$Lambda/0x0000000077559298@330888

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#4@r18c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#677** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #677: Mod incompatibility on dedicated servers
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/677
  - retrieved by: dense_b#4@r18l
  - excerpt: ted Storage (latest version tested was 1.4.39.1174 for MC NeoForge 1.21.1) and Chisels & Bits (latest version tested was 21.1.25) 2. Set up a server with the same mods 3. Place a Limited Barrel and try to left click it. ## Mods used NeoForge 21.1.176 Chisels & Bits 21.1.25 Jade 15.10.1 JEI 19.21.0.247 Sophisticated Storage 1.4.39.1174 Sophisticated Core 1.5.50.1004 [comment by P3pp3rF1y (owner)] That is a bug in Scena where they try to parse forge event result values of `TRUE/DEFAULT/FALSE` into enumeration that has constants of ` DENY/DEFAULT/ALLOW` and yup that is only going to work for th

- [ ] **gh-issue:mezz/JustEnoughItems#3709** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #3709: [Crash]: Lunar Client is incompatible with JEI mod 1.21/1.21.1
  - https://github.com/mezz/JustEnoughItems/issues/3709
  - retrieved by: bm25_b#7@r18c, bm25_b#4@r18l
  - excerpt: [issue by KR99991] ### Steps to Reproduce the Crash 1. Download lunar client. Select the 1.21.1 or 1.21 fabric version in lunar client. 3. Install jei mod to lunar client. 4. Launch game. ### Mod Pack URL (Optional) https://www.curseforge.com/minecraft/mc-mods/jei/files/5623551 ### Mod Pack Version (Optional) jei-1.21.1-fabric-19.8.4.113 ### Extra Notes (Optional) Please fix it, thanks! ### Crash Report https://gist.github.com/KR99991/7a9982edfe16b8328218399cd7687424 [comment by mezz (owner)] Thanks for the report! The crash log has this error: ``` [2024-08-25 17:02:10.802] [erro

- [ ] **gh-issue:mezz/JustEnoughItems#4369** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4369: [Crash]: Crashes on world load with modpack
  - https://github.com/mezz/JustEnoughItems/issues/4369
  - retrieved by: dense_b#4@r18c
  - excerpt: [issue by FrostBiteA426] ### Steps to Reproduce the Crash (Neoforge 1.21.1) Attempting to load every beta version of JEI starting from Beta 19.32.0.358 causes the game to crash when attempting to join a world. Tested from Beta 19.32.0.358 to latest beta 19.39.0.368. All seem to cause a crash while using modpack. Cannot replicate crashes using JEI on its own. Cannot replicate crashes without JEI enabled in modpack. [A-426 (1.21.1 NF).zip](https://github.com/user-attachments/files/30062078/A-426.1.21.1.NF.zip) ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) Neofor

- [ ] **gh-issue:CaffeineMC/sodium#3703** (github_issue, 1/6 conditions)
  - sodium issue #3703: [Crash] Crash with Create Big Cannons smoke particle render type on Sodium 0.8 1.21.1 backport
  - https://github.com/CaffeineMC/sodium/issues/3703
  - retrieved by: bm25_a#5@r18l
  - excerpt: [issue by rbasamoyai] ### Bug Description When firing a big cannon produced with Create Big Cannons, the game crashes due to apparently not satisfying a vertex data format introduced by the Sodium 0.8 1.21.1 backport. (See also https://github.com/Cannoneers-of-Create/CreateBigCannons/issues/938). ### Reproduction Steps 1. Create a NeoForge 1.21.1 mod instance with Create Big Cannons v5.11.5 (including dependencies) and Sodium 0.8.12-alpha.4. 2. Launch Minecraft, create a new world. 4. Build a big cannon and fill it with propellant (such as powder charges). (See the Create Big Cannons ponder

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#5@r18c
  - excerpt: tes (4572 MiB) / 8589934592 bytes (8192 MiB) up to 8589934592 bytes (8192 MiB) Total Memory: 3890826992 bytes (3710 MiB) / 8589934592 bytes (8192 MiB) CPU: AMD Ryzen 9 5900HS with Radeon Graphics @ 3.29 GHz; 8 cores / 16 threads on 1 socket(s) Graphics card #0: AMD Radeon(TM) Graphics (Advanced Micro Devices, Inc. (0x1002)); 512.00 MB of VRAM Graphics card #1: NVIDIA GeForce RTX 3050 Ti Laptop GPU (NVIDIA (0x10de)); 4095.00 MB of VRAM Other Mods: KubeJS: 2001.6.5-build.16 Horseman: 1.3.15 Simple Magnets: 1.1.12 KubeJSCurios: 1.0.4 Fabric Rendering Fluids (v1): 3.0.29+4ac5e37a77 Fabr

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#5@r18l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:mezz/JustEnoughItems#4450** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4450: [Bug]: Create: Aeronautics mixin mismatch causing client crash
  - https://github.com/mezz/JustEnoughItems/issues/4450
  - retrieved by: bm25_b#5@r18c
  - excerpt: [issue by viralhysteria] ### Steps to Reproduce the Bug The recent 19.44.0.406 update causes a client crash on world load when running the game with only Create, Create: Aeronautics and Sable enabled. All aforementioned mods are on the latest release channel. <details> <summary>Error 1</summary> [Render thread/ERROR] [net.neoforged.bus.EventBus/EVENTBUS]: Exception caught during firing event: An unexpected critical error was encountered Index: 1 Listeners: 0: mezz.jei.neoforge.JustEnoughItemsClient$$Lambda/0x0000025398eba5c8@7a90d6de 1: mezz.jei.neoforge.startup.StartEventObserver$$Lam

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#6@r18c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#932** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #932: Sodium `ConcurrentModificationException` thrown from `BarrelBakedModelBase.getDisplayRotation`
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/932
  - retrieved by: dense_b#6@r18l
  - excerpt: [issue by dkarvik] | Component | Version | |---|---| | Minecraft | 1.21.1 | | Loader | NeoForge 21.1.248 (FML 4.0.43) | | Sophisticated Storage | 1.5.91.2127 (`sophisticatedstorage-1.21.1-1.5.91.2127.jar`) | | Sophisticated Core | 1.5.0 | | Sophisticated Backpacks | 3.26.1 | | Sodium | 0.8.13+mc1.21.1 (`sodium-neoforge-0.8.13+mc1.21.1-mod.jar`) | ## Stacktrace ``` ---- Minecraft Crash Report ---- // Ouch. That hurt :( Time: 2026-09-22 07:30:47 Description: Encountered exception while building chunk meshes java.util.ConcurrentModificationException: null at java.base/java.util.HashMap.compu

- [ ] **gh-issue:malte0811/FerriteCore#211** (github_issue, 1/6 conditions)
  - FerriteCore issue #211: [Neoforge1.21.1]Conflict with industrialupgrade mod causing crash
  - https://github.com/malte0811/FerriteCore/issues/211
  - retrieved by: dense_b#6@r18c
  - excerpt: jre.jar%23179!/:?] {} at MC-BOOTSTRAP/com.google.common@32.1.2-jre/com.google.common.collect.ImmutableMap$Builder.build(ImmutableMap.java:572) ~[guava-32.1.2-jre.jar%23179!/:?] {} at MC-BOOTSTRAP/com.google.common@32.1.2-jre/com.google.common.collect.ImmutableMap$Builder.buildOrThrow(ImmutableMap.java:600) ~[guava-32.1.2-jre.jar%23179!/:?] {} at MC-BOOTSTRAP/com.google.common@32.1.2-jre/com.google.common.collect.ImmutableMap$Builder.build(ImmutableMap.java:587) ~[guava-32.1.2-jre.jar%23179!/:?] {} at TRANSFORMER/ferritecore@7.0.2/malte0811.ferritecore.fastmap.PropertyIndexer$GenericIndexer

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 1/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: bm25_a#6@r18l
  - excerpt: fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20230612.114412] [19:57:10] [main/INFO]: ModLauncher 10.0.9+10.0.9+main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=M

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#7@r18c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:architectury/architectury-api#736** (github_issue, 1/6 conditions)
  - architectury-api issue #736: crash when create new world
  - https://github.com/architectury/architectury-api/issues/736
  - retrieved by: bm25_a#8@r18l
  - excerpt: shut down the game with console... and there is no crash report generated. and in the latest.log: ``` [297��2026 22:48:12.871] [Render thread/INFO] [KubeJS Tweaks/]: Testing [297��2026 22:48:12.881] [Render thread/WARN] [KubeJS Server/]: Due to the way Minecraft resource loading works, KubeJS' server.log may not contain everything that happened in your server scripts on initial world creation. [297��2026 22:48:12.882] [Render thread/WARN] [KubeJS Server/]: You can still see the full log (including past reloads) in your latest.log file. [297��2026 22:48:12.888] [Render thread/INFO] [FluxNetwor

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: hybrid_a#8@r18c
  - excerpt: .76, 108.156.211.10] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instances/1.19/.minecraft Java path is: /usr/lib/jvm/java-17-openjdk-amd64/bin/java Checking Java version... Java is version 17.0.4, using 64-bit architecture, from Private Build. Intel(R) Pentium(R) Silver N5000 CPU @ 1.10GHz Intel Corporation UHD Graphics 605 (rev 03) DeviceName: Onboard - Video Subsystem: Dell UHD Graphics 605 OpenGL version string: 4.6 (Compatibility Profile) Mesa 21

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#9@r18c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#9@r18l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:embeddedt/ModernFix#428** (github_issue, 1/6 conditions)
  - ModernFix issue #428: [Bug] Crash on Initialization Due to 'modernfix' in Conjunction with 'Just Enough Items (JEI)
  - https://github.com/embeddedt/ModernFix/issues/428
  - retrieved by: dense_b#9@r18c
  - excerpt: [issue by Stanelbrow] ### Bug Description **Minecraft Version: 1.21 fabric** **Mod Versions:** - Just Enough Items (JEI): [jei-1.21-fabric-19.0.0.16] - Modernfix: [modernfix-fabric-5.18.4+mc1.21] Minecraft crashes during the initialization phase when using the mods 'Just Enough Items (JEI)' and 'modernfix' together. The error seems related to a missing class provided by 'modernfix' that is required by 'JEI'. ### Reproduction Steps 1. Install the mods 'Just Enough Items (JEI)' and 'modernfix'. 2. Launch Minecraft with these mods enabled. ### Log File [crash-2024-07-03_09.21.13-cli

- [ ] **gh-issue:mezz/JustEnoughItems#4000** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4000: [Crash]: open the backpack then crashed | 'boolean net.minecraft.world.item.Item.isBookEnchantable(net.minecraft.world.item.ItemStack, net.minecraft.world.item.ItemStack)'
  - https://github.com/mezz/JustEnoughItems/issues/4000
  - retrieved by: bm25_b#9@r18c
  - excerpt: .github.com/DeliciousBread481/88f69f8ba2786b28c811dd6b0c8e5001 [comment by BugmanBugman (none)] Getting this too [comment by bitberlin (none)] I get this too every time i open an inventory. **Versions:** Neoforge **21.5.73 and above** (21.5.72 and lower works fine) JEI 21.3.0.17 for NeoForge 1.21.5 **Crash Report:** [<script src="https://gist.github.com/bitberlin/aa99a355faadff02613cd6e4d9216833.js"></script>](url) [comment by weppnesp (none)] Same results, same crash report as bitberlin. Neoforge 21.5.73 [comment by bl1te (none)] Supposedly happens because of https://github.com/neoforg

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#10@r18c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:malte0811/FerriteCore#160** (github_issue, 1/6 conditions)
  - FerriteCore issue #160: UnsupportedOperationException with SimpleStorageNetwork 1.7.0 (1.18.2 Forge)
  - https://github.com/malte0811/FerriteCore/issues/160
  - retrieved by: hybrid_b#10@r18c
  - excerpt: [issue by LordDarthDan] When running my pack with that version of SSN, I get a crash with UnsupportedOperationException: "A mod tried to access the state neighbor table directly." Reporting here as that's what the log suggested. MC version: 1.18.2 Forge Forge version: 40.2.18 FerriteCore version: 4.2.2 Simple Storage Network version: 1.7.0 Log: https://mclo.gs/YQs06Rd (Note: the issue does not appear with Simple Storage Network version 1.6.2) [comment by malte0811 (owner)] You need to update JEI. The problem is this: Simple Storage Network wants a newer JEI version than you hav

- [ ] **gh-issue:mezz/JustEnoughItems#4344** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4344: [Bug]: Flashback replays of servers can't be opened if JEI is installed
  - https://github.com/mezz/JustEnoughItems/issues/4344
  - retrieved by: bm25_a#10@r18l
  - excerpt: [issue by Syntrait] ### Steps to Reproduce the Bug 1. Join a Minecraft server 2. Start recording a Flashback replay 3. Return to the main menu 4. Try opening the replay file 5. Error when world is loading ### Expected Behavior I expected JEI to not error out the replay file ### Actual Behavior Replay file ends up not opening due to the error ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) Disabling JEI allows me to open the replay file in Flashback. Launching a singleplayer session's replay file does work even with

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#10@r18c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:wisp-forest/owo-lib#384** (github_issue, 1/6 conditions)
  - owo-lib issue #384: Network error spam with particle systems on 1.21.1 Neoforge
  - https://github.com/wisp-forest/owo-lib/issues/384
  - retrieved by: bm25_b#10@r18l
  - excerpt: [issue by Rearth] Hi, I'm using the owo lib ParticleSystemController / ParticleSystem feature a lot in Oritech (both on fabric and neoforge). I recently was made aware that the neoforge version of owo lib logs an error every time a particle is spawned on the server side. The particles still spawn just fine, but with multiple machines potentially creating particles every tick, it quickly adds up to the logs being unusable. I hope it's okay for me to create issues about the Neoforge version of owo lib here, I wasn't able to create issues in the NF branch. Original issue with logs: https://githu

## Added by hand

(none)
