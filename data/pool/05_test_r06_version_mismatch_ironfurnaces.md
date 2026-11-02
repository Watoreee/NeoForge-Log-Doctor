# Judging sheet 05: `r06_version_mismatch_ironfurnaces` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `ironfurnaces`  |  **Acceptable:** ironfurnaces
- **What was broken:** updated Iron Furnaces to the 26.1 build (ironfurnaces-neoforge-26.1.2-4.4.2.jar) in a 1.21.1 pack
- **Logs in this scenario:** r06_latest
- **Documents to judge:** 29

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 5/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_a#3@r06l, hybrid_b#3@r06l, hybrid_c#3@r06l, bm25_a#8@r06l, dense_b#5@r06l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:Qelifern/IronFurnacesNeoForge#56** (github_issue, 4/6 conditions)
  - IronFurnacesNeoForge issue #56: [Crash] Game Crashes when auto output is turned on
  - https://github.com/Qelifern/IronFurnacesNeoForge/issues/56
  - retrieved by: hybrid_b#1@r06l, hybrid_c#1@r06l, bm25_b#1@r06l, dense_b#1@r06l
  - excerpt: [issue by anderspike] IronFurnaces Version: 26.1-1.0.0 NeoForge Version: 26.1.36 Every time auto output is enabled, the game instantly crashes when the furnace tries to output something. Doesn't matter the slot used to output, or what type of container it is outputting into (tested both barrel and chest). I was able to replicate the bug consistently on a brand new world with ONLY iron furnaces and Neoforge installed. Every other feature of Iron Furnaces (including auto input) seems to work fine. I didn't test every type of furnace, but at the very least, iron, emerald, and obsidian all caused

- [ ] **gh-issue:malte0811/FerriteCore#211** (github_issue, 4/6 conditions)
  - FerriteCore issue #211: [Neoforge1.21.1]Conflict with industrialupgrade mod causing crash
  - https://github.com/malte0811/FerriteCore/issues/211
  - retrieved by: hybrid_b#2@r06l, hybrid_c#2@r06l, bm25_b#3@r06l, dense_b#2@r06l
  - excerpt: [issue by FortyTwoCn] ``` -- Head -- Thread: main Stacktrace: at MC-BOOTSTRAP/com.google.common@32.1.2-jre/com.google.common.collect.ImmutableMap.conflictException(ImmutableMap.java:378) ~[guava-32.1.2-jre.jar%23179!/:?] {} -- Mod loading issue for: industrialupgrade -- Details: Mod file: /D:/1.21.1Youer/40000-TEST/mods/[I][1.21.1][工业升级]IndustrialUpgrade-1.21.1-3.3.2.26.jar Failure message: Industrial Upgrade (industrialupgrade) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.IllegalArgumentException: Multiple entries with same ke

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#2@r06l, bm25_a#1@r06l, bm25_b#8@r06l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:thedarkcolour/KotlinForForge#105** (github_issue, 3/6 conditions)
  - KotlinForForge issue #105: Wrong fml translation key used, leading to crash when displaying loading errors
  - https://github.com/thedarkcolour/KotlinForForge/issues/105
  - retrieved by: hybrid_b#8@r06l, hybrid_c#8@r06l, bm25_b#2@r06l
  - excerpt: [issue by Erdragh] ``` java.lang.IllegalArgumentException: When using FML translation keys, only use fml.modloadingissue. keys for mod loading issues: fml.modloading.javafml.dangling_entrypoint at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:30) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:24) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.error(ModLoadingIssue.java:35) ~[loader-4.0.24.jar%23132!/:

- [ ] **gh-issue:malte0811/FerriteCore#210** (github_issue, 3/6 conditions)
  - FerriteCore issue #210: Game Crush
  - https://github.com/malte0811/FerriteCore/issues/210
  - retrieved by: hybrid_b#7@r06l, hybrid_c#7@r06l, dense_b#3@r06l
  - excerpt: [issue by deaddiesel] 1. Forge 47.4.10 2. Minecraft 1.20.1 3. [ferritecore-6.0.1-forge.jar](https://www.curseforge.com/minecraft/mc-mods/ferritecore/files/4810975) [crash-2025-12-10_14.59.18-client.txt](https://github.com/user-attachments/files/24089186/crash-2025-12-10_14.59.18-client.txt) Your mod conflicts with Industrial Upgrade. [comment by malte0811 (owner)] This should be fixed in the latest release of Industrial Upgrade.

- [ ] **gh-issue:Qelifern/IronFurnacesNeoForge#12** (github_issue, 3/6 conditions)
  - IronFurnacesNeoForge issue #12: Out of Memory Issue with Large Maximum Stack Sizes
  - https://github.com/Qelifern/IronFurnacesNeoForge/issues/12
  - retrieved by: hybrid_b#4@r06l, hybrid_c#4@r06l, bm25_b#9@r06l
  - excerpt: [issue by IACTU] https://github.com/Qelifern/IronFurnacesNeoForge/blob/dc6b6d96dd766acf90698a87032e8078b21b80e8/src/main/java/ironfurnaces/tileentity/TileEntityInventory.java#L68 I have another mod which greatly increases maximum stack sizes. However, with Iron Furnaces this line causes a massive list to be created which quickly crashes the game. What is the reasoning behind this implementation? [comment by Qelifern (owner)] That line of code is wrong, will push an update soon. [comment by Jonathan404 (none)] I'm having the same problem on 1.20.1, everytime i place down a netherite furnac

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 3/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: hybrid_b#9@r06l, hybrid_c#9@r06l, bm25_b#4@r06l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 3/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_b#5@r06l, hybrid_c#5@r06l, bm25_b#10@r06l
  - excerpt: [issue by gamebastian-creator] ### Bug Description Hello, I am experiencing a crash when launching Minecraft 1.21.1 on NeoForge with my modpack. I use Sable for Aeronautics, and Sable requires a newer version of Sodium. However, after installing the required Sodium version, the game crashes during startup. Environment: * Minecraft 1.21.1 * NeoForge 21.1.233 * Sable 2.0.3 * Aeronautics * Sodium 0.8.12-alpha.2+ (required by Sable) Because Sable requires this version of Sodium, removing Sodium is not a viable workaround for my setup. Could you please help determine whether this is a known

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 3/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: hybrid_b#10@r06l, hybrid_c#10@r06l, bm25_b#5@r06l
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:mezz/JustEnoughItems#4227** (github_issue, 3/6 conditions)
  - JustEnoughItems issue #4227: [Crash]: IllegalArgumentException when tabbing out while in inventory
  - https://github.com/mezz/JustEnoughItems/issues/4227
  - retrieved by: hybrid_b#6@r06l, hybrid_c#6@r06l, dense_b#10@r06l
  - excerpt: ing this issue! **CurseForge:** [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8575785) | [Forge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8575786) **Modrinth:** [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/E8jJJK1I) | [Forge](https://modrinth.com/mod/u6dRKJwZ/version/b3rXIQsb) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `10.81.0.1029` for Minecraft `1.18.2` (Fabric, Forge). Thanks for reporting this

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 2/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#1@r06l, bm25_a#2@r06l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#8@r06l, bm25_a#3@r06l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 2/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#4@r06l, bm25_a#6@r06l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 2/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#5@r06l, dense_b#8@r06l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 2/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#7@r06l, dense_b#6@r06l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:CaffeineMC/sodium#3013** (github_issue, 1/6 conditions)
  - sodium issue #3013: Texture Bleeding with Custom Models using half pixel translations
  - https://github.com/CaffeineMC/sodium/issues/3013
  - retrieved by: bm25_a#4@r06l
  - excerpt: the texture of weeping vines to plain orange and the texture bleeding is visible like seen in the image above. ### Log File [20:01:14] [main/INFO]: Loading Minecraft 1.21.4 with Fabric Loader 0.16.9 [20:01:14] [main/INFO]: Loading 11 mods: - fabricloader 0.16.9 \-- mixinextras 0.4.1 - java 21 - minecraft 1.21.4 - sodium 0.6.6+mc1.21.4 |-- fabric-api-base 0.4.54+b47eab6b04 |-- fabric-block-view-api-v2 1.0.19+7feeb73304 |-- fabric-renderer-api-v1 5.0.2+84404cdd04 |-- fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb733

- [ ] **gh-issue:mezz/JustEnoughItems#4255** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4255: [Bug]: Conflict with AE2 and Beyond Dimensions (Neoforge)
  - https://github.com/mezz/JustEnoughItems/issues/4255
  - retrieved by: dense_b#4@r06l
  - excerpt: :** [NeoForge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548363) | [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548362) **Modrinth:** [NeoForge](https://modrinth.com/mod/u6dRKJwZ/version/rPLXajL0) | [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/jEV5BTqf) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `15.33.0.174` for Minecraft `1.20.1`. Thanks for reporting this issue! **CurseForge:** [Fabric](https:

- [ ] **gh-issue:bernie-g/geckolib#804** (github_issue, 1/6 conditions)
  - geckolib issue #804: NullPointerException in GeoArmorRenderer when checking entity glow status
  - https://github.com/bernie-g/geckolib/issues/804
  - retrieved by: bm25_a#5@r06l
  - excerpt: [issue by Henrique200005] ## Bug Report: NullPointerException in GeoArmorRenderer when checking entity glow status ### Description Game crashes when rendering armor on entities due to a null entity being passed to `shouldEntityAppearGlowing()` method in `GeoArmorRenderer.java` line 333. ### Minecraft Version - **Minecraft**: 1.21.1 - **NeoForge**: 21.1.216 - **GeckoLib**: 4.8.2 (geckolib-neoforge-1.21.1-4.8.2.jar) ### Crash Location ``` at software.bernie.geckolib.renderer.GeoArmorRenderer.renderToBuffer(GeoArmorRenderer.java:333) at net.minecraft.client.Minecraft.shouldEntityAppearGlowing(

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#6@r06l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 1/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: bm25_b#6@r06l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 1/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: dense_b#7@r06l
  - excerpt: ixin,re:classloading} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.handler$zib000$omegaconfig$onReturn(Minecraft.java:4020) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:APP:glitchcore.mixins.json:client.MixinMinecraft from mod glitchcore,pl:mixin:APP:resourcefulconfig.mixins.json:client.MinecraftMixin from mod resourcefulconfig,pl:mixin:APP:omega-config.mixins.json:ClientMixin from mod omegaconfig,pl:mixin:APP:architectury.mixins.json:MixinMinecraft from mod architectu

- [ ] **gh-issue:embeddedt/ModernFix#651** (github_issue, 1/6 conditions)
  - ModernFix issue #651: Crash on startup with `mixin.perf.dynamic_resources=true` — incompatibility with Create: Teleporters
  - https://github.com/embeddedt/ModernFix/issues/651
  - retrieved by: bm25_a#7@r06l
  - excerpt: [issue by Kur-Dev] ## Crash on startup with `mixin.perf.dynamic_resources=true` — incompatibility with Create: Teleporters **ModernFix version:** `modernfix-neoforge-5.26.1+mc1.21.1` **Minecraft version:** 1.21.1 **NeoForge version:** 21.1.224 **Create: Teleporters version:** `createteleporters-remastered-2.0.1d-neoforge-1.21.1.jar` (latest) [Create: Teleporters 2.0.2a](https://modrinth.com/mod/create-teleporters/version/2.0.2a) ### Description When `mixin.perf.dynamic_resources=true` is manually enabled in `config/modernfix-mixins.properties`, the game crashes at startup during the title s

- [ ] **gh-issue:mezz/JustEnoughItems#4498** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4498: [Crash]: Create 6.0.10 Causes JEI 19.56.0.441 Crash
  - https://github.com/mezz/JustEnoughItems/issues/4498
  - retrieved by: bm25_b#7@r06l
  - excerpt: [issue by Bopkasen] ### Steps to Reproduce the Crash Based on the log file you provided, the problem with JEI is a hard code conflict with the Create mod (create-1.21.1-6.0.10.jar). The critical crash error preventing JEI from indexing ingredients on world join is: `java.lang.IllegalArgumentException: An interpreter is already registered for this: create:potion` Why this is happening: Both Create and another active mod are trying to register a sub-type interpreter for fluid potions (`create:potion`) inside the JEI registry map simultaneously. Java does not allow double-registrations on th

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: hybrid_a#9@r06l
  - excerpt: [issue by ModernGamingWorld] [23Dec2024 13:03:50.769] [Render thread/ERROR] [net.neoforged.bus.EventBus/EVENTBUS]: Exception caught during firing event: Cannot get config value before config is loaded. Index: 3 Listeners: 0: net.neoforged.bus.EventListenerFactory$addAttribComponent/0x00000296fa13c000@1783c60c 1: net.neoforged.bus.EventListenerFactory$eventInitScreenEvent/0x00000296fb9fc000@7dcadb11 2: net.neoforged.bus.EventListenerFactory$onInitTitleScreen/0x00000296f93dcc00@1172dc2c 3: fuzs.bettermodsbutton.neoforge.client.BetterModsButtonNeoForgeClient$$Lambda/0x00000296f975

- [ ] **gh-issue:wisp-forest/owo-lib#504** (github_issue, 1/6 conditions)
  - owo-lib issue #504: EdmOps throws a NullPointerException on null input instead of returning a DataResult error
  - https://github.com/wisp-forest/owo-lib/issues/504
  - retrieved by: bm25_a#9@r06l
  - excerpt: [issue by neonishere] ### Versions - Minecraft 1.21.1, NeoForge 21.1.248 - owo-lib 0.12.15.5-beta.1+1.21 - Accessories 1.1.0-beta.53+1.21.1 - Cold Sweat 2.4.3.1 ### What happens Putting armor that was insulated at Cold Sweat's sewing table into an Accessories cosmetic armor slot disconnects the player. The item stays in the slot, so the same packet is sent on every login and the player cannot rejoin until the save is edited. reports of the same crash: - wisp-forest/accessories#418 - Momo-Softworks/Cold-Sweat#605 - Momo-Softworks/Cold-Sweat#683 - Momo-Softworks/Cold-Sweat#699 ``` Interna

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/versioning** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Versioning
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/versioning/
  - retrieved by: dense_b#9@r06l
  - excerpt: w/Java_Edition_20w14∞ [jei]: https://www.curseforge.com/minecraft/mc-mods/jei [mekanism]: https://www.curseforge.com/minecraft/mc-mods/mekanism [minecolonies]: https://www.curseforge.com/minecraft/mc-mods/minecolonies [minecraft]: #minecraft [neoforgemodstoml]: modfiles.md#neoforgemodstoml [mvr]: https://maven.apache.org/enforcer/enforcer-rules/versionRanges.html [mvr]: https://maven.apache.org/ref/3.5.2/maven-artifact/apidocs/org/apache/maven/artifact/versioning/ComparableVersion.html [neoforge]: #neoforge [pre]: #pre-releases [rc]: #release-candidates [semver]: https://semver.org/ [supplemen

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#10@r06l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: bm25_a#10@r06l
  - excerpt: [issue by ToxinZangoose] Hello, I have recently been trying to diagnose an issue with my modpack and the log files point to this mod when I try launching. When launching, owo lib tries to load shaders for Spectrum which is not supported for NeoForge. Below is the log file for the crash I've been experiencing since I've tried removing 19 mods from this pack. https://mclo.gs/wDKVGtH Thank you for your time! [comment by Dragon-Seeker (member)] ``` [02Nov2024 11:04:06.859] [modloading-worker-0/ERROR] [io.github.lightman314.lightmanscurrency.LightmansCurrency/]: Error setting up C

## Added by hand

(none)
