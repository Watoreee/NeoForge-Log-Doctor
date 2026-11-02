# Judging sheet 17: `r13_missing_dependency_extendedae` (dev)

- **Category:** `missing_dependency`  |  **Culprit:** `extendedae`  |  **Acceptable:** extendedae
- **What was broken:** ExtendedAE and MEGA Cells were left auto-disabled after the AE2 run; the pack's KubeJS startup script ExtendedAE/InfinityCells.js failed with Unknown type 'kubejs:custom_infinity_cell'
- **Logs in this scenario:** r13_latest
- **Documents to judge:** 41

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 4/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_b#1@r13l, hybrid_c#9@r13l, bm25_b#5@r13l, dense_b#8@r13l
  - excerpt: some sort. [comment by RubixDev (none)] I get the same error with kff 5.9.0 and Minecraft 1.20.6 with NeoForge 20.6.139, and I don't have the `atomicfu` plugin configured (at least not manually). I have not yet found a fix for this. Of note is also, that building the mod and using it in a normal Minecraft instance works fine, it's only broken in the dev environment.

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 3/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: hybrid_a#7@r13l, hybrid_b#8@r13l, dense_b#1@r13l
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r13l, hybrid_c#3@r13l, bm25_b#1@r13l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 3/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: hybrid_b#10@r13l, hybrid_c#7@r13l, bm25_b#3@r13l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:GlodBlock/ExtendedAE#260** (github_issue, 2/6 conditions)
  - ExtendedAE issue #260: [1.21.1] Kubejs Added Infinity Cell's Tooltips Crash the Client
  - https://github.com/GlodBlock/ExtendedAE/issues/260
  - retrieved by: hybrid_a#4@r13l, bm25_a#1@r13l
  - excerpt: [issue by Drackion] Mod Version: 2.1.0-Neoforge Lib Version: 2.0-Neoforge Pack: ATM 10 0.62 Expected Behaviour: To render the tooltips on Infinity Cells added via KJS without the client crashing. Actual Behaviour: Hovering over Infinity Cells added via KJS or searching in creative search crashes the client. Logs: https://mclo.gs/A44xcZo [comment by Drackion (none)] I have also discovered this issue also breaks Forbidden Arcanus's JEI Integration [comment by GlodBlock (owner)] this is because 'minecraft:moss' isn't a valid item id https://github.com/AllTheMods/ATM-10/blob/main/

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 2/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_b#9@r13l, dense_b#2@r13l
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:TwelveIterations/Waystones#1118** (github_issue, 2/6 conditions)
  - Waystones issue #1118: Waystones mod looks for a missing KumaAPI and crashes when clicking on any waystone
  - https://github.com/TwelveIterations/Waystones/issues/1118
  - retrieved by: hybrid_b#2@r13l, bm25_b#2@r13l
  - excerpt: knot//net.minecraft.client.main.Main.main(Main.java:250) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:514) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:72) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(Unknown Source) at java.base/java.lang.reflect.Method.invoke(Unknown Source) at com.modrinth.theseus.MinecraftLaunch.relaunch(MinecraftLaunch.java:63) at com.modrinth.theseus.MinecraftLaunch.main(MinecraftLaunch.java:28) C

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 2/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: hybrid_a#6@r13l, bm25_a#2@r13l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **gh-issue:GlodBlock/ExtendedAE#638** (github_issue, 2/6 conditions)
  - ExtendedAE issue #638: [Bug] Error During Mod Loading
  - https://github.com/GlodBlock/ExtendedAE/issues/638
  - retrieved by: hybrid_a#3@r13l, hybrid_c#6@r13l
  - excerpt: [issue by Marioluigi7896] Trying to include ExtendedAE in a modpack with a bunch of other mods, however when including the mod AE2 fails to load, disabling the mod fixes the issue. The reported issue in the crashlog seems to be a duplicate resource key, unsure if this will end up being an AE2 issue but since it only appeared with this mod enabled I figured I'd report here first. ``java.lang.IllegalStateException: Adding duplicate key 'ResourceKey[minecraft:menu / extendedae:ex_emc_import_bus]' to registry`` Mincraft Version: 1.21.1 Java Version: 21.0.3, Eclipse Adoptium Mod Version: 1.21-2.2.

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 2/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#8@r13l, bm25_a#3@r13l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#516** (github_issue, 2/6 conditions)
  - Aquaculture issue #516: Missing Registry Crash
  - https://github.com/TeamMetallurgy/Aquaculture/issues/516
  - retrieved by: hybrid_b#4@r13l, dense_b#7@r13l
  - excerpt: [issue by XUrielX-Chosen] The game crashed: unexpected error Error: java.lang.NullPointerException: Registry Object not present: aquaculturedelight:roasted_tambaqui I keep getting this error when I crash. [comment by GirafiStudios (collaborator)] Wrong mod. The crash is from Aquaculture Delight

- [ ] **gh-issue:TwelveIterations/Balm#123** (github_issue, 2/6 conditions)
  - Balm issue #123: [Crash] ticking hopper below Cooking for blockheads' Oven tries to take item from slot 4 (only 3 slots)
  - https://github.com/TwelveIterations/Balm/issues/123
  - retrieved by: hybrid_a#10@r13l, bm25_a#4@r13l
  - excerpt: [issue by MindStudioOfficial] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader Fabric ### Describe the Issue placing a hopper below a cooking for blockheads oven which has 3 input slots and 3 output slots crashes the server whenever the block is loaded and ticked because it tries to take items from slot 4 of 3 (IndexOutOfBounds) ``` java.lang.IndexOutOfBoundsException: Index 4 out of bounds for length 3 at java.base/jdk.internal.util.Preconditions.outOfBounds(Unknown Source) at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Unknown Source) at java.base/jdk.internal.u

- [ ] **gh-issue:GlodBlock/ExtendedAE#399** (github_issue, 2/6 conditions)
  - ExtendedAE issue #399: I get this error when using ExtendedAE with KubeJS
  - https://github.com/GlodBlock/ExtendedAE/issues/399
  - retrieved by: hybrid_c#10@r13l, bm25_a#6@r13l
  - excerpt: [issue by Samu2004G] ![Image](https://github.com/user-attachments/assets/7ec997eb-9777-4a45-a738-301faba485fa) I already asked on the KubeJS Discord server, and they said the error was caused by ExtendedAE. The error was related to com.glodblock.github.extendedae.xmod.kjs.KJSPlugin. The mods I had installed were: Using NeoForge version 21.1.146 for Minecraft 1.21.1 Mod list: • AE2WTLib API 19.2.0 • Applied Energistics 2 19.2.8 • ExtendedAE 1.21-2.2.8-neoforge • Glodium 1.21-2.2-neoforge • GuideME 21.1.7 • KubeJS 2101.7.2-build.231 • Rhino 2101.2.7-build.74 [crash-2025-04-12_21

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 2/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_a#9@r13l, dense_b#6@r13l
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:GlodBlock/ExtendedAE#422** (github_issue, 1/6 conditions)
  - ExtendedAE issue #422: kubejs error with extended ae
  - https://github.com/GlodBlock/ExtendedAE/issues/422
  - retrieved by: hybrid_c#1@r13l
  - excerpt: [issue by baka4n] etails: Mod file: /C:/Users/<user>/.gradle/caches/modules-2/files-2.1/dev.latvian.mods/kubejs-neoforge/2101.7.2-build.233/7c5dbc2e152f819c929b51fcf1247747770af4c9/kubejs-neoforge-2101.7.2-build.233.jar Failure message: KubeJS (kubejs) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.NoSuchMethodError: 'void dev.latvian.mods.kubejs.registry.BuilderTypeRegistry$Callback.add(java.lang.String, java.lang.Class, dev.latvian.mods.kubejs.registry.BuilderFactory)' Mod version: 2101.7.2-build.233 Mod issues URL: https://ku

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#1@r13l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:GlodBlock/ExtendedAE#271** (github_issue, 1/6 conditions)
  - ExtendedAE issue #271: EMI Error
  - https://github.com/GlodBlock/ExtendedAE/issues/271
  - retrieved by: hybrid_c#2@r13l
  - excerpt: ClassInitialized(java.lang.Class)' at TRANSFORMER/glodium@1.21-2.1-neoforge/com.glodblock.github.glodium.reflect.moon.Moon.getField(Moon.java:61) at TRANSFORMER/glodium@1.21-2.1-neoforge/com.glodblock.github.glodium.reflect.ReflectKit.readField(ReflectKit.java:54) at TRANSFORMER/extendedae@1.21-2.1.1-neoforge/com.glodblock.github.extendedae.util.Ae2ReflectClient.getInscribeRecipe(Ae2ReflectClient.java:70) at TRANSFORMER/extendedae@1.21-2.1.1-neoforge/com.glodblock.github.extendedae.xmod.emi.EMIPlugin.register(EMIPlugin.java:34) at TRANSFORMER/emi@1.1.16+1.21.1+neoforge/dev.emi.emi.ru

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#2@r13l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#350** (github_issue, 1/6 conditions)
  - Aquaculture issue #350: Crash on Startup
  - https://github.com/TeamMetallurgy/Aquaculture/issues/350
  - retrieved by: dense_b#3@r13l
  - excerpt: [issue by StarrSage] Trying to load this mod gives an error that says "Failed to load correctly java.lang.InvocationTargetException: null" [comment by GirafiStudios (collaborator)] Please provide a crash report, otherwise there is nowhere for me to even start attempting to look into the issue. [comment by StarrSage (none)] I’ve dealt with this issue on a few of my mods and have learned it has something to do with the mod needing to be updated for Forge. I am currently using the recommended 1.19 version. [comment by GirafiStudios (collaborator)] What version of Aquaculture 2 are you using?

- [ ] **gh-issue:GlodBlock/ExtendedAE#341** (github_issue, 1/6 conditions)
  - ExtendedAE issue #341: [Render thread/ERROR] appeng/client/guidebook/color/ColorValue
  - https://github.com/GlodBlock/ExtendedAE/issues/341
  - retrieved by: hybrid_c#4@r13l
  - excerpt: [issue by YoSiJo] ``` [21:54:01] [Render thread/ERROR] [ne.ne.fm.ModContainer/LOADING]: Caught exception during event net.neoforged.neoforge.client.event.RegisterMenuScreensEvent@2ba7828b dispatch for modid extendedae java.lang.NoClassDefFoundError: appeng/client/guidebook/color/ColorValue at TRANSFORMER/extendedae@1.21-2.0.1-neoforge/com.glodblock.github.extendedae.client.ClientRegistryHandler.registerGui(ClientRegistryHandler.java:108) ~[ExtendedAE-1.21-2.0.1-neoforge.jar%23219!/:?] {re:classloading} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) ~[bus

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#347** (github_issue, 1/6 conditions)
  - Aquaculture issue #347: This mod is incompatible with 1.19 advent of ascension. 
  - https://github.com/TeamMetallurgy/Aquaculture/issues/347
  - retrieved by: dense_b#4@r13l
  - excerpt: ] The bottom one. The one that does not say api :) [comment by Thisguyneedshelp (none)] i tried that first luckily and it worked thanks!!! [comment by GirafiStudios (collaborator)] Perfect! :)

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#4@r13l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 1/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_b#5@r13l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 1/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: bm25_a#5@r13l
  - excerpt: [issue by jrn907-lab] ### Description they are invisible once turned into a physics object ### Game Log USERNAME}\AppData\Roaming\ModrinthApp\profiles\Create_ Plane and Simple\dynamic-resource-pack-cache\amendments-generated_pack in 13.41 ms [17:56:09] [Worker-ResourceReload-0/INFO] [Moonlight/]: Regenerating Dynamic CLIENT_RESOURCES Resources Provider [moonlight:dynamic_resources], requested by strategy REGEN_ON_EVERY_RELOAD [17:56:09] [Worker-ResourceReload-0/INFO] [Moonlight/]: Generated runtime CLIENT_RESOURCES for pack moonlight:dynamic_resources in 629.7 ?s [17:56:09] [Worker-Resource

- [ ] **gh-issue:GlodBlock/ExtendedAE#291** (github_issue, 1/6 conditions)
  - ExtendedAE issue #291: add kjs support for 1.20.1 (forge)
  - https://github.com/GlodBlock/ExtendedAE/issues/291
  - retrieved by: hybrid_c#5@r13l
  - excerpt: [issue by hyperclocked333] tried using the example code from [the example code](https://github.com/GlodBlock/ExtendedAE/wiki/Custom-Infinity-Cell), kept getting this error from the looks of it seems to work fine and dandy for 1.21 players so i dont know what the issue could be yes i have all the modeling stuff installed yes nobody else in the issue tracker seems to have this error ![image](https://github.com/user-attachments/assets/b45d1fef-da88-4763-99cb-19d65315acd0) [comment by hyperclocked333 (none)] update: i have found out there is no kjs integration for 1.20.1 that would be co

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: dense_b#5@r13l
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#62** (github_issue, 1/6 conditions)
  - YUNGs-API issue #62: [1.20.4] fabric server won't start
  - https://github.com/YUNG-GANG/YUNGs-API/issues/62
  - retrieved by: hybrid_a#5@r13l
  - excerpt: fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:470) ... 3 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.class_174 failed at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.getPostMixinClassByteArray(KnotClassDelegate.java:427) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.tryLoadClass(KnotClassDelegate.java:323) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.loadClass(KnotClassDelegate.java:218) at net.fabricmc.loader.impl.launch.knot.KnotClassLoader.loadClass(KnotClassLoad

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: hybrid_b#6@r13l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#6@r13l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#9021** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #9021: Item duplication when AE2 interface/storage bus pushes more than 8 items into Kaleidoscope Cookery's Millstone
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/9021
  - retrieved by: bm25_a#7@r13l
  - excerpt: [issue by Arc149] ### Describe the bug AE2 version is 19.2.18,Kaleidoscope Cookery is 1.6.0,Minecraft is 1.21.1 neoforge 21.1.250.When I want let the ore in the ME Interface use ME Storage Bus to the millstone sometime will make a bug,if I take in ME Interface is more 8(8 is millstone's max capacity),so the bug will come,in the ME Interface ore will keep a same number,if I take number is at 8 lower the bug will not have. ### How to reproduce the bug When I want let the ore in the ME Interface use ME Storage Bus to the millstone sometime will make a bug,if I take in ME Interface is more 8

- [ ] **gh-issue:TwelveIterations/Balm#227** (github_issue, 1/6 conditions)
  - Balm issue #227: ClassNotFoundException: FabricPermissionsAPIIntegration when fabric-permissions-api is present on 26.1
  - https://github.com/TwelveIterations/Balm/issues/227
  - retrieved by: hybrid_b#7@r13l
  - excerpt: [issue by LegitMeme] ### Minecraft Version 26.1 (LTS) ### Mod Loader Fabric ### Describe the Issue When fabric-permissions-api is present on MC 26.1 (in this case bundled by Fzzy Config), Balm attempts to load FabricPermissionsAPIIntegration but the class doesn't exist in Balm's own jar, causing a ClassNotFoundException and crashing on startup. Steps to reproduce: 1. Install Balm 26.1.0.2 and Fzzy Config 0.7.6+26.1 together. 2. Launch the game. ### Logs Latest: https://mclo.gs/HVJabRm Crash report: https://mclo.gs/Jqx9OUD [comment by BlayTheNinth (member)] Fixed in Balm 26.1.0.3 [com

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#7@r13l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_c#8@r13l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: bm25_b#8@r13l
  - excerpt: [issue by gamebastian-creator] ### Bug Description Hello, I am experiencing a crash when launching Minecraft 1.21.1 on NeoForge with my modpack. I use Sable for Aeronautics, and Sable requires a newer version of Sodium. However, after installing the required Sodium version, the game crashes during startup. Environment: * Minecraft 1.21.1 * NeoForge 21.1.233 * Sable 2.0.3 * Aeronautics * Sodium 0.8.12-alpha.2+ (required by Sable) Because Sable requires this version of Sodium, removing Sodium is not a viable workaround for my setup. Could you please help determine whether this is a known

- [ ] **gh-issue:wisp-forest/owo-lib#504** (github_issue, 1/6 conditions)
  - owo-lib issue #504: EdmOps throws a NullPointerException on null input instead of returning a DataResult error
  - https://github.com/wisp-forest/owo-lib/issues/504
  - retrieved by: bm25_a#8@r13l
  - excerpt: [issue by neonishere] ### Versions - Minecraft 1.21.1, NeoForge 21.1.248 - owo-lib 0.12.15.5-beta.1+1.21 - Accessories 1.1.0-beta.53+1.21.1 - Cold Sweat 2.4.3.1 ### What happens Putting armor that was insulated at Cold Sweat's sewing table into an Accessories cosmetic armor slot disconnects the player. The item stays in the slot, so the same packet is sent on every login and the player cannot rejoin until the save is edited. reports of the same crash: - wisp-forest/accessories#418 - Momo-Softworks/Cold-Sweat#605 - Momo-Softworks/Cold-Sweat#683 - Momo-Softworks/Cold-Sweat#699 ``` Interna

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#9@r13l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 1/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#9@r13l
  - excerpt: to dig into it a bit and sadly "Mo´ Structures" was the mod using that configfile and causing the crash. It´s a bit dissapointing not to be able to use the mod (liked it very much) but at least i can play again. Again, thank you very much for your patience and helping me out :-) [comment by SirTwsted (none)] ![Screenshot_308](https://github.com/user-attachments/assets/285348a0-af89-42a0-ad0a-6fa574b0772e) [crash-2024-07-19_08.55.05-client.txt](https://github.com/user-attachments/files/16312649/crash-2024-07-19_08.55.05-client.txt) Using MC v1.21 and on NEOForge v21.0.109 . [comme

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#9@r13l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: bm25_a#10@r13l
  - excerpt: -beta/net.neoforged.neoforge.server.loading.ServerModLoader.load(ServerModLoader.java:31) ~[neoforge-26.1.0.3-beta-universal.jar:?] {} at TRANSFORMER/minecraft@26.1/net.minecraft.server.Main.main(Main.java:114) [minecraft-server-patched-26.1.0.3-beta.jar:?] {} at net.neoforged.fml.startup.Server.main(Server.java:19) [loader-11.0.4.jar:11.0] {} [12:24:46] [main/INFO] [ne.ne.fm.lo.FMLLoader/]: Closing FML Loader 136d26a8 [12:24:46] [main/INFO] [ne.ne.fm.ModLoader/]: Clearing ModLoader net.neoforged.fml.startup.FatalStartupException: Couldn't find Minecraft server thread. Startup likely failed. a

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 1/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#10@r13l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 1/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: bm25_b#10@r13l
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

## Added by hand

(none)
