# Judging sheet 03: `r13_missing_dependency_extendedae` (dev)

- **Category:** `missing_dependency`  |  **Culprit:** `extendedae`  |  **Acceptable:** extendedae
- **What was broken:** ExtendedAE and MEGA Cells were left auto-disabled after the AE2 run; the pack's KubeJS startup script ExtendedAE/InfinityCells.js failed with Unknown type 'kubejs:custom_infinity_cell'
- **Logs in this scenario:** r13_latest
- **Documents to judge:** 25

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r13l, hybrid_c#3@r13l, bm25_b#1@r13l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:GlodBlock/ExtendedAE#260** (github_issue, 2/6 conditions)
  - ExtendedAE issue #260: [1.21.1] Kubejs Added Infinity Cell's Tooltips Crash the Client
  - https://github.com/GlodBlock/ExtendedAE/issues/260
  - retrieved by: hybrid_a#4@r13l, bm25_a#1@r13l
  - excerpt: [issue by Drackion] Mod Version: 2.1.0-Neoforge Lib Version: 2.0-Neoforge Pack: ATM 10 0.62 Expected Behaviour: To render the tooltips on Infinity Cells added via KJS without the client crashing. Actual Behaviour: Hovering over Infinity Cells added via KJS or searching in creative search crashes the client. Logs: https://mclo.gs/A44xcZo [comment by Drackion (none)] I have also discovered this issue also breaks Forbidden Arcanus's JEI Integration [comment by GlodBlock (owner)] this is because 'minecraft:moss' isn't a valid item id https://github.com/AllTheMods/ATM-10/blob/main/

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 2/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_b#1@r13l, bm25_b#5@r13l
  - excerpt: some sort. [comment by RubixDev (none)] I get the same error with kff 5.9.0 and Minecraft 1.20.6 with NeoForge 20.6.139, and I don't have the `atomicfu` plugin configured (at least not manually). I have not yet found a fix for this. Of note is also, that building the mod and using it in a normal Minecraft instance works fine, it's only broken in the dev environment.

- [ ] **gh-issue:TwelveIterations/Waystones#1118** (github_issue, 2/6 conditions)
  - Waystones issue #1118: Waystones mod looks for a missing KumaAPI and crashes when clicking on any waystone
  - https://github.com/TwelveIterations/Waystones/issues/1118
  - retrieved by: hybrid_b#2@r13l, bm25_b#2@r13l
  - excerpt: knot//net.minecraft.client.main.Main.main(Main.java:250) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:514) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:72) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(Unknown Source) at java.base/java.lang.reflect.Method.invoke(Unknown Source) at com.modrinth.theseus.MinecraftLaunch.relaunch(MinecraftLaunch.java:63) at com.modrinth.theseus.MinecraftLaunch.main(MinecraftLaunch.java:28) C

- [ ] **gh-issue:GlodBlock/ExtendedAE#422** (github_issue, 1/6 conditions)
  - ExtendedAE issue #422: kubejs error with extended ae
  - https://github.com/GlodBlock/ExtendedAE/issues/422
  - retrieved by: hybrid_c#1@r13l
  - excerpt: [issue by baka4n] etails: Mod file: /C:/Users/<user>/.gradle/caches/modules-2/files-2.1/dev.latvian.mods/kubejs-neoforge/2101.7.2-build.233/7c5dbc2e152f819c929b51fcf1247747770af4c9/kubejs-neoforge-2101.7.2-build.233.jar Failure message: KubeJS (kubejs) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.NoSuchMethodError: 'void dev.latvian.mods.kubejs.registry.BuilderTypeRegistry$Callback.add(java.lang.String, java.lang.Class, dev.latvian.mods.kubejs.registry.BuilderFactory)' Mod version: 2101.7.2-build.233 Mod issues URL: https://ku

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 1/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: dense_b#1@r13l
  - excerpt: /:?] {} at cpw.mods.modlauncher.LaunchServiceHandlerDecorator.launch(LaunchServiceHandlerDecorator.java:30) [modlauncher-10.0.8.jar%2381!/:?] {} at cpw.mods.modlauncher.LaunchServiceHandler.launch(LaunchServiceHandler.java:53) [modlauncher-10.0.8.jar%2381!/:?] {} at cpw.mods.modlauncher.LaunchServiceHandler.launch(LaunchServiceHandler.java:71) [modlauncher-10.0.8.jar%2381!/:?] {} at cpw.mods.modlauncher.Launcher.run(Launcher.java:106) [modlauncher [... truncated] [comment by GirafiStudios (collaborator)] Please update Aquaculture, should be fixed in newer versions.

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

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 1/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: dense_b#2@r13l
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#2@r13l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: bm25_a#2@r13l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **gh-issue:GlodBlock/ExtendedAE#638** (github_issue, 1/6 conditions)
  - ExtendedAE issue #638: [Bug] Error During Mod Loading
  - https://github.com/GlodBlock/ExtendedAE/issues/638
  - retrieved by: hybrid_a#3@r13l
  - excerpt: [issue by Marioluigi7896] Trying to include ExtendedAE in a modpack with a bunch of other mods, however when including the mod AE2 fails to load, disabling the mod fixes the issue. The reported issue in the crashlog seems to be a duplicate resource key, unsure if this will end up being an AE2 issue but since it only appeared with this mod enabled I figured I'd report here first. ``java.lang.IllegalStateException: Adding duplicate key 'ResourceKey[minecraft:menu / extendedae:ex_emc_import_bus]' to registry`` Mincraft Version: 1.21.1 Java Version: 21.0.3, Eclipse Adoptium Mod Version: 1.21-2.2.

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#350** (github_issue, 1/6 conditions)
  - Aquaculture issue #350: Crash on Startup
  - https://github.com/TeamMetallurgy/Aquaculture/issues/350
  - retrieved by: dense_b#3@r13l
  - excerpt: [issue by StarrSage] Trying to load this mod gives an error that says "Failed to load correctly java.lang.InvocationTargetException: null" [comment by GirafiStudios (collaborator)] Please provide a crash report, otherwise there is nowhere for me to even start attempting to look into the issue. [comment by StarrSage (none)] I’ve dealt with this issue on a few of my mods and have learned it has something to do with the mod needing to be updated for Forge. I am currently using the recommended 1.19 version. [comment by GirafiStudios (collaborator)] What version of Aquaculture 2 are you using?

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: bm25_a#3@r13l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#3@r13l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

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

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#516** (github_issue, 1/6 conditions)
  - Aquaculture issue #516: Missing Registry Crash
  - https://github.com/TeamMetallurgy/Aquaculture/issues/516
  - retrieved by: hybrid_b#4@r13l
  - excerpt: [issue by XUrielX-Chosen] The game crashed: unexpected error Error: java.lang.NullPointerException: Registry Object not present: aquaculturedelight:roasted_tambaqui I keep getting this error when I crash. [comment by GirafiStudios (collaborator)] Wrong mod. The crash is from Aquaculture Delight

- [ ] **gh-issue:TwelveIterations/Balm#123** (github_issue, 1/6 conditions)
  - Balm issue #123: [Crash] ticking hopper below Cooking for blockheads' Oven tries to take item from slot 4 (only 3 slots)
  - https://github.com/TwelveIterations/Balm/issues/123
  - retrieved by: bm25_a#4@r13l
  - excerpt: [issue by MindStudioOfficial] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader Fabric ### Describe the Issue placing a hopper below a cooking for blockheads oven which has 3 input slots and 3 output slots crashes the server whenever the block is loaded and ticked because it tries to take items from slot 4 of 3 (IndexOutOfBounds) ``` java.lang.IndexOutOfBoundsException: Index 4 out of bounds for length 3 at java.base/jdk.internal.util.Preconditions.outOfBounds(Unknown Source) at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Unknown Source) at java.base/jdk.internal.u

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

## Added by hand

(none)
