# Judging sheet 03: `r04_missing_dependency_simpletms` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `simpletms`  |  **Acceptable:** simpletms, allthemons
- **What was broken:** disabled cloth-config in CurseForge; cloth_config stayed loaded via fightorflight but simpletms was missing too
- **Logs in this scenario:** r04_crash, r04_latest
- **Documents to judge:** 56

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:embeddedt/ModernFix#535** (github_issue, 4/6 conditions)
  - ModernFix issue #535: Caught exception in thread: java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab (net.minecraft.client.gui.tab.Tab)
  - https://github.com/embeddedt/ModernFix/issues/535
  - retrieved by: hybrid_b#1@r04c, hybrid_c#1@r04c, bm25_b#7@r04c, dense_b#1@r04c, dense_b#6@r04l
  - excerpt: [issue by meyverick] ### Bug Description ``` [08:01:30] [Worker-ResourceReload-0/ERROR]: Caught exception in thread Thread[#178,Worker-ResourceReload-0,8,main] java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab at java.base/java.lang.ClassLoader.defineClass1(Native Method) ~[?:?] at java.base/java.lang.ClassLoader.defineClass(ClassLoader.java:1026) ~[?:?] at java.base/java.security.SecureClassLoader.defineClass(SecureClassLoader.java:150) ~[?:?] at net.fabricmc.loader.impl.launch.knot.KnotClassLoader.defineClassFwd(KnotClassLoader.java:160) ~[fabr

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 4/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#5@r04c, hybrid_c#10@r04c, bm25_b#1@r04c, dense_b#5@r04c, hybrid_b#3@r04l, hybrid_c#9@r04l, bm25_b#1@r04l, dense_b#9@r04l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 4/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#9@r04c, hybrid_c#8@r04c, hybrid_a#8@r04l, bm25_a#3@r04l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 4/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: dense_b#6@r04c, hybrid_b#6@r04l, hybrid_c#3@r04l, bm25_b#5@r04l
  - excerpt: 0.4/cpw.mods.modlauncher.Launcher.main(Launcher.java:74) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.run(BootstrapLauncher.java:210) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:69) at java.base/jdk.internal.reflect.DirectMethodHan

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 3/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_b#3@r04c, hybrid_c#2@r04c, dense_b#2@r04c, hybrid_b#2@r04l, hybrid_c#2@r04l, dense_b#1@r04l
  - excerpt: \javafmllanguage\1.19-41.0.63\javafmllanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.958] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\lowcodelanguage\1.19-41.0.63\lowcodelanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.960] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\mclanguage\1.19-41.0.63\mclanguage-1.19-41.0.63

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 3/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: hybrid_b#2@r04c, hybrid_c#5@r04c, bm25_b#3@r04c, hybrid_b#1@r04l, hybrid_c#5@r04l, bm25_b#3@r04l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:TwelveIterations/Waystones#1118** (github_issue, 3/6 conditions)
  - Waystones issue #1118: Waystones mod looks for a missing KumaAPI and crashes when clicking on any waystone
  - https://github.com/TwelveIterations/Waystones/issues/1118
  - retrieved by: hybrid_b#10@r04c, hybrid_c#9@r04c, hybrid_b#4@r04l, hybrid_c#1@r04l, bm25_b#2@r04l
  - excerpt: knot//net.minecraft.client.main.Main.main(Main.java:250) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:514) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:72) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(Unknown Source) at java.base/java.lang.reflect.Method.invoke(Unknown Source) at com.modrinth.theseus.MinecraftLaunch.relaunch(MinecraftLaunch.java:63) at com.modrinth.theseus.MinecraftLaunch.main(MinecraftLaunch.java:28) C

- [ ] **gh-issue:TheIllusiveC4/Curios#619** (github_issue, 3/6 conditions)
  - Curios issue #619: [Bug]: Failure message: An uncaught parallel processing error has occurred. java.lang.NoClassDefFoundError: net/hazen/hazentouvelib/Items/Curios/WingCurioRenderer
  - https://github.com/TheIllusiveC4/Curios/issues/619
  - retrieved by: hybrid_b#6@r04c, hybrid_c#3@r04c, bm25_b#10@r04c
  - excerpt: 01.07.02-fml.txt) [comment by TheIllusiveC4 (owner)] It looks like this was an issue with Hazen 'N Stuff and should be resolved as of their `1.4.0.14` update for that mod.

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 3/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_b#4@r04c, hybrid_c#4@r04c, dense_b#3@r04c, hybrid_b#8@r04l, hybrid_c#4@r04l
  - excerpt: legacy\Minecraft\game\libraries\net\minecraftforge\javafmllanguage\1.19.2-43.4.20\javafmllanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\lowcodelanguage\1.19.2-43.4.20\lowcodelanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\mclanguage\1.19.2-43.4.20\mclangu

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 3/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: hybrid_a#10@r04l, bm25_a#4@r04l, dense_b#10@r04l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r04c, bm25_a#6@r04c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:GlodBlock/ExtendedAE#422** (github_issue, 2/6 conditions)
  - ExtendedAE issue #422: kubejs error with extended ae
  - https://github.com/GlodBlock/ExtendedAE/issues/422
  - retrieved by: hybrid_a#5@r04l, bm25_a#1@r04l
  - excerpt: [issue by baka4n] etails: Mod file: /C:/Users/<user>/.gradle/caches/modules-2/files-2.1/dev.latvian.mods/kubejs-neoforge/2101.7.2-build.233/7c5dbc2e152f819c929b51fcf1247747770af4c9/kubejs-neoforge-2101.7.2-build.233.jar Failure message: KubeJS (kubejs) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.NoSuchMethodError: 'void dev.latvian.mods.kubejs.registry.BuilderTypeRegistry$Callback.add(java.lang.String, java.lang.Class, dev.latvian.mods.kubejs.registry.BuilderFactory)' Mod version: 2101.7.2-build.233 Mod issues URL: https://ku

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 2/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#3@r04c, hybrid_a#1@r04l, bm25_a#9@r04l
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 2/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_a#1@r04c, dense_b#10@r04c, bm25_a#7@r04l
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 2/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#7@r04l, bm25_a#2@r04l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 2/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: hybrid_b#10@r04l, dense_b#2@r04l
  - excerpt: ge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod file B2e20f83d9414-B2e20f83d9414.jar of type MOD with locator net.minecraftforge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod fi [... truncated] [comment by thedarkcolour (owner)] Do you have a GitHub repo for this? [comment by KP2048 (none)] Yes but I haven’t committed the switch to kotlin yet [comment by KP2048 (none)] I can zip it up and post it here if you like [comment by thedarkcolour (owner)] I don't know how you have the proje

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 2/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: bm25_b#2@r04c, hybrid_b#5@r04l, bm25_b#10@r04l
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 2/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: dense_b#7@r04c, hybrid_a#3@r04l
  - excerpt: .ModuleClassLoader.findClass(ModuleClassLoader.java:298) [17:35:52 ERROR] [STDERR]: at cpw.mods.securejarhandler/cpw.mods.cl.ModuleClassLoader.loadClass(ModuleClassLoader.java:214) [17:35:52 ERROR] [STDERR]: at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) [17:35:52 ERROR] [STDERR]: at java.base/java.lang.Class.getDeclaredMethods0(Native Method) [17:35:52 ERROR] [STDERR]: at java.base/java.lang.Class.privateGetDeclaredMethods(Class.java:3578) [17:35:52 ERROR] [STDERR]: at java.base/java.lang.Class.getMethodsRecursive(Class.java:3719) [17:35:52 ERROR]

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 2/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: dense_b#4@r04c, hybrid_c#10@r04l, dense_b#5@r04l
  - excerpt: jar:?] {} at cpw.mods.modlauncher.Launcher.main(Launcher.java:66) [modlauncher-8.0.9.jar:?] {} at io.github.zekerzhayard.forgewrapper.installer.Main.main(Main.java:50) [ForgeWrapper-1.4.2.jar:?] {} at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[?:1.8.0_271] {} at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at [... truncated] [comment by khorvo77 (none)] Sorry, Modlist: Mods: [✔️] [1.16.5]+SecurityCraft+v1.8.21.1 [✔️] abnormals_core-1.16

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_b#7@r04c, hybrid_c#6@r04c, hybrid_c#7@r04l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 2/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: bm25_b#8@r04c, dense_b#9@r04c, bm25_b#8@r04l
  - excerpt: [issue by gamebastian-creator] ### Bug Description Hello, I am experiencing a crash when launching Minecraft 1.21.1 on NeoForge with my modpack. I use Sable for Aeronautics, and Sable requires a newer version of Sodium. However, after installing the required Sodium version, the game crashes during startup. Environment: * Minecraft 1.21.1 * NeoForge 21.1.233 * Sable 2.0.3 * Aeronautics * Sodium 0.8.12-alpha.2+ (required by Sable) Because Sable requires this version of Sodium, removing Sodium is not a viable workaround for my setup. Could you please help determine whether this is a known

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#2@r04c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 1/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: hybrid_a#6@r04c, hybrid_a#2@r04l
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#2@r04c, hybrid_a#4@r04l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#3@r04c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:bernie-g/geckolib#844** (github_issue, 1/6 conditions)
  - geckolib issue #844: Geckolib doesn't like owo-lib
  - https://github.com/bernie-g/geckolib/issues/844
  - retrieved by: dense_b#3@r04l
  - excerpt: tributor)] Using MultiMC and Neoforge 21.1.233 create-1.21.1-6.0.10.jar dragonlib-neoforge-1.21.1-beta-3.0.28.jar geckolib-neoforge-1.21.1-4.8.4.jar jei-1.21.1-neoforge-19.27.0.340.jar owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar pantographsandwires-neoforge-1.21.1-beta-0.2.3-C6.jar I can launch just fine with no errors, get to the main menu, etc. My recommendation would be you binary search your pack, start with this bunch of mods, and slowly add mods in packs until you can replicate the issue and isolate the minimum required mods to have this.

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#4@r04c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 1/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: dense_b#4@r04l
  - excerpt: to dig into it a bit and sadly "Mo´ Structures" was the mod using that configfile and causing the crash. It´s a bit dissapointing not to be able to use the mod (liked it very much) but at least i can play again. Again, thank you very much for your patience and helping me out :-) [comment by SirTwsted (none)] ![Screenshot_308](https://github.com/user-attachments/assets/285348a0-af89-42a0-ad0a-6fa574b0772e) [crash-2024-07-19_08.55.05-client.txt](https://github.com/user-attachments/files/16312649/crash-2024-07-19_08.55.05-client.txt) Using MC v1.21 and on NEOForge v21.0.109 . [comme

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#4@r04c, bm25_b#4@r04l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 1/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#4@r04c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#5@r04c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#5@r04c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#5@r04c, bm25_b#6@r04l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: bm25_a#5@r04l
  - excerpt: [issue by Andaros210] Here's the log copy and paste. MultiMC version: 0.6.16-3430 Launched instance in online mode authserver.mojang.com resolves to: [108.138.149.51, 108.138.149.48, 108.138.149.65, 108.138.149.64] session.minecraft.net resolves to: [107.20.118.247, 52.72.238.122, 54.172.106.247] textures.minecraft.net resolves to: [108.156.211.10, 108.156.211.34, 108.156.211.26, 108.156.211.76] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instanc

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: hybrid_a#6@r04l
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:TwelveIterations/Balm#123** (github_issue, 1/6 conditions)
  - Balm issue #123: [Crash] ticking hopper below Cooking for blockheads' Oven tries to take item from slot 4 (only 3 slots)
  - https://github.com/TwelveIterations/Balm/issues/123
  - retrieved by: bm25_a#6@r04l
  - excerpt: [issue by MindStudioOfficial] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader Fabric ### Describe the Issue placing a hopper below a cooking for blockheads oven which has 3 input slots and 3 output slots crashes the server whenever the block is loaded and ticked because it tries to take items from slot 4 of 3 (IndexOutOfBounds) ``` java.lang.IndexOutOfBoundsException: Index 4 out of bounds for length 3 at java.base/jdk.internal.util.Preconditions.outOfBounds(Unknown Source) at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Unknown Source) at java.base/jdk.internal.u

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 1/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: hybrid_c#7@r04c, hybrid_c#6@r04l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#6@r04c, bm25_b#7@r04l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#7@r04c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#7@r04c
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 1/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#8@r04c, dense_b#7@r04l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 1/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: hybrid_b#7@r04l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#8@r04c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:Keksuccino/Konkrete#7** (github_issue, 1/6 conditions)
  - Konkrete issue #7: Using Konkrete with some mods i have used before make my game crash
  - https://github.com/Keksuccino/Konkrete/issues/7
  - retrieved by: hybrid_b#8@r04c
  - excerpt: [issue by NATuan123] ``` ---- Minecraft Crash Report ---- // Why did you do that? Time: 12/6/21, 10:21 PM Description: Initializing game java.lang.NoClassDefFoundError: Could not initialize class net.minecraft.class_1921 at Not Enough Crashes deobfuscated stack trace.(1.17.1+build.61) at net.minecraft.client.font.EmptyGlyphRenderer.<init>(EmptyGlyphRenderer:10) at net.minecraft.client.font.FontStorage.<clinit>(FontStorage:27) at net.minecraft.client.font.FontManager.<init>(FontManager:48) at net.minecraft.client.MinecraftClient.<init>(MinecraftClient:527) at net.minecraft.

- [ ] **gh-issue:TwelveIterations/Balm#227** (github_issue, 1/6 conditions)
  - Balm issue #227: ClassNotFoundException: FabricPermissionsAPIIntegration when fabric-permissions-api is present on 26.1
  - https://github.com/TwelveIterations/Balm/issues/227
  - retrieved by: hybrid_c#8@r04l
  - excerpt: [issue by LegitMeme] ### Minecraft Version 26.1 (LTS) ### Mod Loader Fabric ### Describe the Issue When fabric-permissions-api is present on MC 26.1 (in this case bundled by Fzzy Config), Balm attempts to load FabricPermissionsAPIIntegration but the class doesn't exist in Balm's own jar, causing a ClassNotFoundException and crashing on startup. Steps to reproduce: 1. Install Balm 26.1.0.2 and Fzzy Config 0.7.6+26.1 together. 2. Launch the game. ### Logs Latest: https://mclo.gs/HVJabRm Crash report: https://mclo.gs/Jqx9OUD [comment by BlayTheNinth (member)] Fixed in Balm 26.1.0.3 [com

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#8@r04l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#8@r04c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#68** (github_issue, 1/6 conditions)
  - KotlinForForge issue #68: KotlinForForge with Ktor: Class not found
  - https://github.com/thedarkcolour/KotlinForForge/issues/68
  - retrieved by: dense_b#8@r04l
  - excerpt: ttp) { install(HttpTimeout) { connectTimeoutMillis = 5_000L } } } ``` [comment by thedarkcolour (owner)] Use https://github.com/MinecraftForge/ForgeGradle/wiki/Dependencies#non-minecraft-dependencies [comment by Icosider (none)] It doesn't work if you use your library [comment by thedarkcolour (owner)] Come to Discord server I can help you more easily there

- [ ] **gh-issue:CaffeineMC/sodium#2731** (github_issue, 1/6 conditions)
  - sodium issue #2731: Problem with launching minecraft 1.21.1 with sodium
  - https://github.com/CaffeineMC/sodium/issues/2731
  - retrieved by: hybrid_a#9@r04l
  - excerpt: to errors, provided by 'sodium' at 'net.caffeinemc.mods.sodium.fabric.SodiumPreLaunch'! at net.fabricmc.loader.impl.FabricLoaderImpl.lambda$invokeEntrypoints$2(FabricLoaderImpl.java:403) at net.fabricmc.loader.impl.util.ExceptionUtil.gatherExceptions(ExceptionUtil.java:33) at net.fabricmc.loader.impl.FabricLoaderImpl.invokeEntrypoints(FabricLoaderImpl.java:401) at net.fabricmc.loader.impl.launch.knot.Knot.init(Knot.java:160) ... 5 more Caused by: java.lang.UnsatisfiedLinkError: C:\Users\?????\AppData\Local\Temp\jna-1007792265\jna6873146617604809216.dll: Can't find dependent librarie

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r04c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 1/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#9@r04c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 1/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: hybrid_b#9@r04l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#9@r04c, bm25_b#9@r04l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:Creators-of-Create/Create#10549** (github_issue, 1/6 conditions)
  - Create issue #10549: Crushing wheel not damaging cows in survival, but can if in creative
  - https://github.com/Creators-of-Create/Create/issues/10549
  - retrieved by: bm25_a#10@r04c
  - excerpt: [issue by goody420] ### Description im currently playing in a survival world and built a cow farm with conveyor leading the baby`s to crushing wheels that are placed directly above where they stand. when they grow to full size the cow should be getting crushed but it does not? however when i tried testing this in a creative world, exact same set up and it worked fine. once the cow grew fullsize the crushing wheel ia supposed to deal damage to it. ### Game Log https://mclo.gs/7jWaWtA ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: bm25_a#10@r04l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#10@r04c
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

## Added by hand

(none)
