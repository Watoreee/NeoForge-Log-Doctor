# Judging sheet 19: `r18_version_mismatch_sophisticatedcore` (dev)

- **Category:** `version_mismatch`  |  **Culprit:** `sophisticatedcore`  |  **Acceptable:** sophisticatedcore
- **What was broken:** updated Sophisticated Core to the Minecraft 26.1.2 build (sophisticatedcore-26.1.2-1.5.24.2445.jar) in a 1.21.1 pack; its 'only supports jei 29.5.0.24' line is a side effect, not a JEI problem
- **Logs in this scenario:** r18_crash, r18_latest
- **Documents to judge:** 55

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 5/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#6@r18c, hybrid_b#1@r18c, hybrid_c#1@r18c, bm25_b#1@r18c, dense_b#2@r18c, hybrid_a#4@r18l, dense_b#5@r18l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 5/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#2@r18l, hybrid_b#5@r18l, hybrid_c#5@r18l, bm25_a#2@r18l, bm25_b#10@r18l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 5/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r18c, hybrid_b#2@r18c, hybrid_c#2@r18c, bm25_b#3@r18c, dense_b#10@r18c, dense_b#10@r18l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 5/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#5@r18c, hybrid_c#5@r18c, bm25_b#9@r18c, hybrid_a#3@r18l, hybrid_b#3@r18l, hybrid_c#3@r18l, bm25_a#9@r18l, bm25_b#7@r18l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#825** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #825: [Neoforge 1.21.11] ticking entity crash
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/825
  - retrieved by: dense_b#8@r18c, hybrid_b#1@r18l, hybrid_c#1@r18l, bm25_b#9@r18l, dense_b#2@r18l
  - excerpt: [issue by Baggytrousers27] SophisticatedCore is named in the crashlog but there isn't a repo for it so posting it here instead. Seemed to occur after cursor moved over an item in Backpack Description: Ticking entity com.google.common.util.concurrent.UncheckedExecutionException: java.lang.IllegalArgumentException: Failed to hash minecraft:max_damage=>0: Value must be positive: 0 [Crashlog](https://pastebin.com/RcQVcg5K) (Will post a Full log when Gists decide to work again) sophisticatedbackpacks-1.21.11-3.25.34.1565 sophisticatedcore-1.21.11-1.4.7.1513 sophisticateditemactions-1.21.11-0.3.

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#725** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #725: Server side crash when inserting Compression upgrade into limited barrel Neoforge 1.21.8
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/725
  - retrieved by: hybrid_b#10@r18c, hybrid_c#7@r18c, hybrid_b#2@r18l, hybrid_c#2@r18l, bm25_b#8@r18l, dense_b#7@r18l
  - excerpt: [issue by Neposis] Mod: Sophisticated Storage Version: 1.4.50 (NeoForge 1.21.8) Core: Sophisticated Core 1.3.65 Environment: Minecraft 1.21.8 NeoForge 21.8.35 Dedicated server (Linux, Java 21) Good afternoon, I am having an issue where my server insta crashes as soon as I right click the compression upgrade onto a limited barrel 3 (only tested black) or trying to insert it in via the interface. Maybe caused by a client side call on server? java.lang.NoClassDefFoundError: net/minecraft/client/renderer/texture/TextureAtlas at net.p3pp3rf1y.sophisticatedstorage.upgrades.compression.Compre

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 4/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#7@r18c, hybrid_b#3@r18c, hybrid_c#6@r18c, bm25_b#7@r18c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 4/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: hybrid_a#10@r18c, hybrid_b#9@r18l, hybrid_c#9@r18l, dense_b#3@r18l
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

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: hybrid_b#8@r18c, hybrid_c#3@r18c, dense_b#9@r18l
  - excerpt: $registerEventHandlers$2(BetterModsButtonNeoForgeClient.java:53) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.ConsumerEventHandler.invoke(ConsumerEventHandler.java:26) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:315) at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.gui.screens.Screen.init [... truncated] [comment by P3pp3rF1y (owner)] I don't see anything related to sophisticated in this crash log other than the fact that it's one of the mods on the list.

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 3/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: hybrid_b#10@r18l, hybrid_c#10@r18l, bm25_b#3@r18l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 3/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_a#10@r18l, hybrid_b#4@r18l, hybrid_c#4@r18l
  - excerpt: /issues. ========================= // Shall we play a game? Time: 2026-06-25 21:57:03 Description: Rendering overlay java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.2+mc1.21.1-mod.jar%23319!/:?] {re:mixin,re:classloading} at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigsLate(ConfigManager.java:76) ~[net.caffeinemc.sodium-neoforge-0.8

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#6@r18c, hybrid_c#4@r18c, dense_b#5@r18c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r18c, bm25_a#4@r18c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 2/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#1@r18l, bm25_a#6@r18l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#8@r18l, bm25_a#1@r18l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r18c, bm25_a#3@r18c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 2/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_c#10@r18c, bm25_b#2@r18c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#3@r18c, bm25_a#2@r18c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_a#8@r18c, hybrid_a#6@r18l, bm25_a#4@r18l
  - excerpt: mods.modlauncher.Launcher/MODLAUNCHER]: ModLauncher 10.0.1+10.0.1+main.e9521dc3 starting: java version 17.0.3 by Microsoft; OS Windows 10 arch amd64 version 10.0 [07lip2022 18:29:06.835] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.minecraft/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2390!/ Service=ModLauncher Env=CLIENT [07lip2022 18:29:07.952] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\fmlcore

- [ ] **gh-issue:mezz/JustEnoughItems#4003** (github_issue, 2/6 conditions)
  - JustEnoughItems issue #4003: [Crash]: 1.21.5 latest neoforge update crash
  - https://github.com/mezz/JustEnoughItems/issues/4003
  - retrieved by: hybrid_b#4@r18c, dense_b#7@r18c
  - excerpt: } at TRANSFORMER/jei@21.3.0.17/mezz.jei.library.plugins.vanilla.anvil.AnvilRecipeMaker$EnchantmentData.getEnchantedBooks(AnvilRecipeMaker.java:73) ~[jei-1.21.5-neoforge-21.3.0.17.jar%23219!/:21.3.0.17] {re:classloading} at TRANSFORMER/jei@21.3.0.17/mezz.jei.library.plugins.vanilla.anvil.AnvilRecipeMaker.lambda$getBookEnchantmentRecipes$2(AnvilRecipeMaker.java:123) ~[jei-1.21.5-neoforge-21.3.0.17.jar%23219!/:21.3.0.17] {re:classloading}` ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) _No response_ ### Crash Report .

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 2/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_c#8@r18c, bm25_a#5@r18l
  - excerpt: .fml.ModList.forEachModInOrder(ModList.java:174) ~[loader-4.0.42.jar%23107!/:4.0] {re:mixin} at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModLoader.postEvent(ModLoader.java:358) ~[loader-4.0.42.jar%23107!/:4.0] {} at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.client.ClientHooks.initClientHooks(ClientHooks.java:1028) ~[neoforge-21.1.234-universal.jar%23196!/:?] {re:mixin,re:classloading,pl:mixin:APP:sodium-neoforge.mixins.json:platform.neoforge.ClientHooksMixin from mod sodium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.<init>(Minecraft.java:60

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r18c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:mezz/JustEnoughItems#4586** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4586: [Crash]: JEI version 19.69.0.457 crashes (1.21.1 Forge) when joining the game
  - https://github.com/mezz/JustEnoughItems/issues/4586
  - retrieved by: dense_b#1@r18c
  - excerpt: /mc-mods/jei/files/9343790>) - [CurseForge (Fabric)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343789>) - [CurseForge (Forge)](<https://www.curseforge.com/minecraft/mc-mods/jei/files/9343788>) - [Modrinth (NeoForge)](<https://modrinth.com/mod/u6dRKJwZ/version/pWGmsnGm>) - [Modrinth (Fabric)](<https://modrinth.com/mod/u6dRKJwZ/version/kFIMjB8H>) - [Modrinth (Forge)](<https://modrinth.com/mod/u6dRKJwZ/version/1rvwFzhL>)

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#3@r18l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10344** (github_issue, 1/6 conditions)
  - Create issue #10344: Cannot read field "x" because "mf.axis" is null
  - https://github.com/Creators-of-Create/Create/issues/10344
  - retrieved by: bm25_b#4@r18c, bm25_b#6@r18l
  - excerpt: NeoForge$$Lambda/0x0000000076f81078@ccb2269 2: net.p3pp3rf1y.sophisticatedcore.common.CommonEventHandler$$Lambda/0x0000000076fa9000@5d251949 3: net.neoforged.neoforge.common.NeoForgeMod$$Lambda/0x0000000077057018@21a04589 4: net.p3pp3rf1y.sophisticatedbackpacks.common.CommonEventHandler$$Lambda/0x000000007731a270@1dd00c23 5: net.neoforged.bus.EventListenerFactory$onServerTick/0x00000000774b1800@4735f276 6: net.fabricmc.fabric.impl.event.lifecycle.LifecycleEventsImpl$$Lambda/0x00000000774e4990@16109588 7: com.hlysine.create_connected.CreateConnected$$Lambda/0x0000000077559298@330888

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#677** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #677: Mod incompatibility on dedicated servers
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/677
  - retrieved by: dense_b#4@r18l
  - excerpt: ted Storage (latest version tested was 1.4.39.1174 for MC NeoForge 1.21.1) and Chisels & Bits (latest version tested was 21.1.25) 2. Set up a server with the same mods 3. Place a Limited Barrel and try to left click it. ## Mods used NeoForge 21.1.176 Chisels & Bits 21.1.25 Jade 15.10.1 JEI 19.21.0.247 Sophisticated Storage 1.4.39.1174 Sophisticated Core 1.5.50.1004 [comment by P3pp3rF1y (owner)] That is a bug in Scena where they try to parse forge event result values of `TRUE/DEFAULT/FALSE` into enumeration that has constants of ` DENY/DEFAULT/ALLOW` and yup that is only going to work for th

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: bm25_b#4@r18l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:mezz/JustEnoughItems#4369** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4369: [Crash]: Crashes on world load with modpack
  - https://github.com/mezz/JustEnoughItems/issues/4369
  - retrieved by: dense_b#4@r18c
  - excerpt: [issue by FrostBiteA426] ### Steps to Reproduce the Crash (Neoforge 1.21.1) Attempting to load every beta version of JEI starting from Beta 19.32.0.358 causes the game to crash when attempting to join a world. Tested from Beta 19.32.0.358 to latest beta 19.39.0.368. All seem to cause a crash while using modpack. Cannot replicate crashes using JEI on its own. Cannot replicate crashes without JEI enabled in modpack. [A-426 (1.21.1 NF).zip](https://github.com/user-attachments/files/30062078/A-426.1.21.1.NF.zip) ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) Neofor

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r18c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: bm25_b#5@r18c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#5@r18l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#5@r18c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:mezz/JustEnoughItems#3709** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #3709: [Crash]: Lunar Client is incompatible with JEI mod 1.21/1.21.1
  - https://github.com/mezz/JustEnoughItems/issues/3709
  - retrieved by: bm25_b#8@r18c, bm25_b#5@r18l
  - excerpt: [issue by KR99991] ### Steps to Reproduce the Crash 1. Download lunar client. Select the 1.21.1 or 1.21 fabric version in lunar client. 3. Install jei mod to lunar client. 4. Launch game. ### Mod Pack URL (Optional) https://www.curseforge.com/minecraft/mc-mods/jei/files/5623551 ### Mod Pack Version (Optional) jei-1.21.1-fabric-19.8.4.113 ### Extra Notes (Optional) Please fix it, thanks! ### Crash Report https://gist.github.com/KR99991/7a9982edfe16b8328218399cd7687424 [comment by mezz (owner)] Thanks for the report! The crash log has this error: ``` [2024-08-25 17:02:10.802] [erro

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#6@r18c
  - excerpt: tes (4572 MiB) / 8589934592 bytes (8192 MiB) up to 8589934592 bytes (8192 MiB) Total Memory: 3890826992 bytes (3710 MiB) / 8589934592 bytes (8192 MiB) CPU: AMD Ryzen 9 5900HS with Radeon Graphics @ 3.29 GHz; 8 cores / 16 threads on 1 socket(s) Graphics card #0: AMD Radeon(TM) Graphics (Advanced Micro Devices, Inc. (0x1002)); 512.00 MB of VRAM Graphics card #1: NVIDIA GeForce RTX 3050 Ti Laptop GPU (NVIDIA (0x10de)); 4095.00 MB of VRAM Other Mods: KubeJS: 2001.6.5-build.16 Horseman: 1.3.15 Simple Magnets: 1.1.12 KubeJSCurios: 1.0.4 Fabric Rendering Fluids (v1): 3.0.29+4ac5e37a77 Fabr

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

- [ ] **gh-issue:mezz/JustEnoughItems#4450** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4450: [Bug]: Create: Aeronautics mixin mismatch causing client crash
  - https://github.com/mezz/JustEnoughItems/issues/4450
  - retrieved by: bm25_b#6@r18c
  - excerpt: [issue by viralhysteria] ### Steps to Reproduce the Bug The recent 19.44.0.406 update causes a client crash on world load when running the game with only Create, Create: Aeronautics and Sable enabled. All aforementioned mods are on the latest release channel. <details> <summary>Error 1</summary> [Render thread/ERROR] [net.neoforged.bus.EventBus/EVENTBUS]: Exception caught during firing event: An unexpected critical error was encountered Index: 1 Listeners: 0: mezz.jei.neoforge.JustEnoughItemsClient$$Lambda/0x0000025398eba5c8@7a90d6de 1: mezz.jei.neoforge.startup.StartEventObserver$$Lam

- [ ] **gh-issue:CaffeineMC/sodium#3703** (github_issue, 1/6 conditions)
  - sodium issue #3703: [Crash] Crash with Create Big Cannons smoke particle render type on Sodium 0.8 1.21.1 backport
  - https://github.com/CaffeineMC/sodium/issues/3703
  - retrieved by: bm25_a#7@r18l
  - excerpt: [issue by rbasamoyai] ### Bug Description When firing a big cannon produced with Create Big Cannons, the game crashes due to apparently not satisfying a vertex data format introduced by the Sodium 0.8 1.21.1 backport. (See also https://github.com/Cannoneers-of-Create/CreateBigCannons/issues/938). ### Reproduction Steps 1. Create a NeoForge 1.21.1 mod instance with Create Big Cannons v5.11.5 (including dependencies) and Sodium 0.8.12-alpha.4. 2. Launch Minecraft, create a new world. 4. Build a big cannon and fill it with propellant (such as powder charges). (See the Create Big Cannons ponder

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#7@r18c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:GlodBlock/ExtendedAE#550** (github_issue, 1/6 conditions)
  - ExtendedAE issue #550: [Neoforge1.21.1]似乎PartSmartAnnihilationPlane出现了一些问题导致崩溃
  - https://github.com/GlodBlock/ExtendedAE/issues/550
  - retrieved by: hybrid_b#7@r18c
  - excerpt: jar%23429!/:?] {re:classloading} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.ConsumerEventHandler.invoke(ConsumerEventHandler.java:27) ~[bus-8.0.5.jar%23125!/:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:360) ~[bus-8.0.5.jar%23125!/:?] {} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:328) ~[bus-8.0.5.jar%23125!/:?] {} at TRANSFORMER/neoforge@21.1.216/net.neoforged.neoforge.event.EventHooks.fireLevelTickPost(EventHooks.java:1022) ~[neoforge-21.1.216-universal.jar%23417!/:1.21.1] {re:mixin,re:classloading} at

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#7@r18l
  - excerpt: legacy\Minecraft\game\libraries\net\minecraftforge\javafmllanguage\1.19.2-43.4.20\javafmllanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\lowcodelanguage\1.19.2-43.4.20\lowcodelanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\mclanguage\1.19.2-43.4.20\mclangu

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#8@r18c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:SuperMartijn642/TrashCans#11** (github_issue, 1/6 conditions)
  - TrashCans issue #11: [Crash] with newest version of mod
  - https://github.com/SuperMartijn642/TrashCans/issues/11
  - retrieved by: dense_b#8@r18l
  - excerpt: [issue by Warbringer12] **Version Info** - Minecraft, 1.16.5 - Trash Cans, 1.0.10-mc1.16.5 **Steps to Reproduce** ...1. launch minecraft **Crash report (~/logs/latest.log)** ... [crash-2021-05-07_18.31.42-fml.txt](https://github.com/SuperMartijn642/TrashCans/files/6444927/crash-2021-05-07_18.31.42-fml.txt) [Uploading 2021-05-07-2.log…]() [comment by SuperMartijn642 (owner)] It says you don't have the core lib installed, it is required for the newest version. [comment by luffykick (none)] Same issue as OP... but for clarity... your latest trashcans update "trashcans-1.0.10-mc1.1

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#8@r18l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r18c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:GlodBlock/ExtendedAE#638** (github_issue, 1/6 conditions)
  - ExtendedAE issue #638: [Bug] Error During Mod Loading
  - https://github.com/GlodBlock/ExtendedAE/issues/638
  - retrieved by: hybrid_a#9@r18l
  - excerpt: [issue by Marioluigi7896] Trying to include ExtendedAE in a modpack with a bunch of other mods, however when including the mod AE2 fails to load, disabling the mod fixes the issue. The reported issue in the crashlog seems to be a duplicate resource key, unsure if this will end up being an AE2 issue but since it only appeared with this mod enabled I figured I'd report here first. ``java.lang.IllegalStateException: Adding duplicate key 'ResourceKey[minecraft:menu / extendedae:ex_emc_import_bus]' to registry`` Mincraft Version: 1.21.1 Java Version: 21.0.3, Eclipse Adoptium Mod Version: 1.21-2.2.

- [ ] **gh-issue:TwelveIterations/Balm#85** (github_issue, 1/6 conditions)
  - Balm issue #85: Server crashes on startup
  - https://github.com/TwelveIterations/Balm/issues/85
  - retrieved by: hybrid_a#9@r18c
  - excerpt: [issue by ashton727] ### Minecraft Version 1.21 ### Mod Loader NeoForge ### Mod Loader Version 21.0.46 ### Mod Version 21.0.11 ### Balm Version 21.0.11 ### Describe the Issue 1. Start neoforge 21.0.46 server with balm 2. Observe crash ### Logs https://pastebin.com/4asPjjkH ### Do you use any performance-enhancing mods (e.g. OptiFine) or custom server distributions (e.g. SpongeForge)? no [comment by BlayTheNinth (member)] Try Java 21 [comment by ashton727 (none)] This version of Neoforge requires Java 22 I believe. [comment by BlayTheNinth (member)] Minecraft 1.21 uses Java 2

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 1/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_b#9@r18c
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:embeddedt/ModernFix#428** (github_issue, 1/6 conditions)
  - ModernFix issue #428: [Bug] Crash on Initialization Due to 'modernfix' in Conjunction with 'Just Enough Items (JEI)
  - https://github.com/embeddedt/ModernFix/issues/428
  - retrieved by: dense_b#9@r18c
  - excerpt: [issue by Stanelbrow] ### Bug Description **Minecraft Version: 1.21 fabric** **Mod Versions:** - Just Enough Items (JEI): [jei-1.21-fabric-19.0.0.16] - Modernfix: [modernfix-fabric-5.18.4+mc1.21] Minecraft crashes during the initialization phase when using the mods 'Just Enough Items (JEI)' and 'modernfix' together. The error seems related to a missing class provided by 'modernfix' that is required by 'JEI'. ### Reproduction Steps 1. Install the mods 'Just Enough Items (JEI)' and 'modernfix'. 2. Launch Minecraft with these mods enabled. ### Log File [crash-2024-07-03_09.21.13-cli

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#10@r18c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 1/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: bm25_b#10@r18c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:architectury/architectury-api#736** (github_issue, 1/6 conditions)
  - architectury-api issue #736: crash when create new world
  - https://github.com/architectury/architectury-api/issues/736
  - retrieved by: bm25_a#10@r18l
  - excerpt: shut down the game with console... and there is no crash report generated. and in the latest.log: ``` [297��2026 22:48:12.871] [Render thread/INFO] [KubeJS Tweaks/]: Testing [297��2026 22:48:12.881] [Render thread/WARN] [KubeJS Server/]: Due to the way Minecraft resource loading works, KubeJS' server.log may not contain everything that happened in your server scripts on initial world creation. [297��2026 22:48:12.882] [Render thread/WARN] [KubeJS Server/]: You can still see the full log (including past reloads) in your latest.log file. [297��2026 22:48:12.888] [Render thread/INFO] [FluxNetwor

## Added by hand

(none)
