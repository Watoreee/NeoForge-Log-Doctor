# Judging sheet 08: `r04_missing_dependency_simpletms` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `simpletms`  |  **Acceptable:** simpletms, allthemons
- **What was broken:** disabled cloth-config in CurseForge; cloth_config stayed loaded via fightorflight but simpletms was missing too
- **Logs in this scenario:** r04_crash, r04_latest
- **Documents to judge:** 32

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

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
  - retrieved by: hybrid_b#4@r04l, hybrid_c#1@r04l, bm25_b#2@r04l
  - excerpt: knot//net.minecraft.client.main.Main.main(Main.java:250) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:514) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:72) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(Unknown Source) at java.base/java.lang.reflect.Method.invoke(Unknown Source) at com.modrinth.theseus.MinecraftLaunch.relaunch(MinecraftLaunch.java:63) at com.modrinth.theseus.MinecraftLaunch.main(MinecraftLaunch.java:28) C

- [ ] **gh-issue:embeddedt/ModernFix#535** (github_issue, 3/6 conditions)
  - ModernFix issue #535: Caught exception in thread: java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab (net.minecraft.client.gui.tab.Tab)
  - https://github.com/embeddedt/ModernFix/issues/535
  - retrieved by: hybrid_b#1@r04c, hybrid_c#1@r04c, dense_b#1@r04c
  - excerpt: [issue by meyverick] ### Bug Description ``` [08:01:30] [Worker-ResourceReload-0/ERROR]: Caught exception in thread Thread[#178,Worker-ResourceReload-0,8,main] java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab at java.base/java.lang.ClassLoader.defineClass1(Native Method) ~[?:?] at java.base/java.lang.ClassLoader.defineClass(ClassLoader.java:1026) ~[?:?] at java.base/java.security.SecureClassLoader.defineClass(SecureClassLoader.java:150) ~[?:?] at net.fabricmc.loader.impl.launch.knot.KnotClassLoader.defineClassFwd(KnotClassLoader.java:160) ~[fabr

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#5@r04c, bm25_b#1@r04c, dense_b#5@r04c, hybrid_b#3@r04l, bm25_b#1@r04l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 3/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_b#4@r04c, hybrid_c#4@r04c, dense_b#3@r04c, hybrid_c#4@r04l
  - excerpt: legacy\Minecraft\game\libraries\net\minecraftforge\javafmllanguage\1.19.2-43.4.20\javafmllanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\lowcodelanguage\1.19.2-43.4.20\lowcodelanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\mclanguage\1.19.2-43.4.20\mclangu

- [ ] **gh-issue:GlodBlock/ExtendedAE#422** (github_issue, 2/6 conditions)
  - ExtendedAE issue #422: kubejs error with extended ae
  - https://github.com/GlodBlock/ExtendedAE/issues/422
  - retrieved by: hybrid_a#5@r04l, bm25_a#1@r04l
  - excerpt: [issue by baka4n] etails: Mod file: /C:/Users/<user>/.gradle/caches/modules-2/files-2.1/dev.latvian.mods/kubejs-neoforge/2101.7.2-build.233/7c5dbc2e152f819c929b51fcf1247747770af4c9/kubejs-neoforge-2101.7.2-build.233.jar Failure message: KubeJS (kubejs) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.NoSuchMethodError: 'void dev.latvian.mods.kubejs.registry.BuilderTypeRegistry$Callback.add(java.lang.String, java.lang.Class, dev.latvian.mods.kubejs.registry.BuilderFactory)' Mod version: 2101.7.2-build.233 Mod issues URL: https://ku

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 2/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: bm25_b#2@r04c, hybrid_b#5@r04l
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 2/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_c#3@r04l, bm25_b#5@r04l
  - excerpt: 0.4/cpw.mods.modlauncher.Launcher.main(Launcher.java:74) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.run(BootstrapLauncher.java:210) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:69) at java.base/jdk.internal.reflect.DirectMethodHan

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 1/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r04c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 1/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#3@r04c, hybrid_a#1@r04l
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_a#1@r04c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#2@r04c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 1/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: hybrid_a#2@r04l
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: bm25_a#2@r04l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#2@r04c, hybrid_a#4@r04l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 1/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: dense_b#2@r04l
  - excerpt: ge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod file B2e20f83d9414-B2e20f83d9414.jar of type MOD with locator net.minecraftforge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod fi [... truncated] [comment by thedarkcolour (owner)] Do you have a GitHub repo for this? [comment by KP2048 (none)] Yes but I haven’t committed the switch to kotlin yet [comment by KP2048 (none)] I can zip it up and post it here if you like [comment by thedarkcolour (owner)] I don't know how you have the proje

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#3@r04c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:TheIllusiveC4/Curios#619** (github_issue, 1/6 conditions)
  - Curios issue #619: [Bug]: Failure message: An uncaught parallel processing error has occurred. java.lang.NoClassDefFoundError: net/hazen/hazentouvelib/Items/Curios/WingCurioRenderer
  - https://github.com/TheIllusiveC4/Curios/issues/619
  - retrieved by: hybrid_c#3@r04c
  - excerpt: 01.07.02-fml.txt) [comment by TheIllusiveC4 (owner)] It looks like this was an issue with Hazen 'N Stuff and should be resolved as of their `1.4.0.14` update for that mod.

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 1/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: bm25_a#3@r04l
  - excerpt: ArchitecturyTransformer > Task :common:processIncludeJars UP-TO-DATE > Task :common:jar UP-TO-DATE > Task :neoforge:compileJava UP-TO-DATE > Task :neoforge:classes UP-TO-DATE > Task :neoforge:configureLaunch > Task :neoforge:downloadAssets UP-TO-DATE > Task :neoforge:configureClientLaunch > Task :neoforge:runClient [Architectury Transformer] Architectury Runtime 5.2.91 [Architectury Transformer] Read classpath in 1.061 s [Architectury Transformer] Listening at C:\Users\<user>\Documents\01Developpement\Projets\DopedHorses\common\build\libs\dopedhorses-common-1.2.4-26.1-dev.jar [23:03:14] [main

- [ ] **gh-issue:bernie-g/geckolib#844** (github_issue, 1/6 conditions)
  - geckolib issue #844: Geckolib doesn't like owo-lib
  - https://github.com/bernie-g/geckolib/issues/844
  - retrieved by: dense_b#3@r04l
  - excerpt: tributor)] Using MultiMC and Neoforge 21.1.233 create-1.21.1-6.0.10.jar dragonlib-neoforge-1.21.1-beta-3.0.28.jar geckolib-neoforge-1.21.1-4.8.4.jar jei-1.21.1-neoforge-19.27.0.340.jar owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar pantographsandwires-neoforge-1.21.1-beta-0.2.3-C6.jar I can launch just fine with no errors, get to the main menu, etc. My recommendation would be you binary search your pack, start with this bunch of mods, and slowly add mods in packs until you can replicate the issue and isolate the minimum required mods to have this.

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#3@r04l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#4@r04c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 1/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: dense_b#4@r04c, dense_b#5@r04l
  - excerpt: jar:?] {} at cpw.mods.modlauncher.Launcher.main(Launcher.java:66) [modlauncher-8.0.9.jar:?] {} at io.github.zekerzhayard.forgewrapper.installer.Main.main(Main.java:50) [ForgeWrapper-1.4.2.jar:?] {} at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[?:1.8.0_271] {} at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at [... truncated] [comment by khorvo77 (none)] Sorry, Modlist: Mods: [✔️] [1.16.5]+SecurityCraft+v1.8.21.1 [✔️] abnormals_core-1.16

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

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: bm25_a#4@r04l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

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
  - retrieved by: bm25_b#5@r04c
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: bm25_a#5@r04l
  - excerpt: [issue by Andaros210] Here's the log copy and paste. MultiMC version: 0.6.16-3430 Launched instance in online mode authserver.mojang.com resolves to: [108.138.149.51, 108.138.149.48, 108.138.149.65, 108.138.149.64] session.minecraft.net resolves to: [107.20.118.247, 52.72.238.122, 54.172.106.247] textures.minecraft.net resolves to: [108.156.211.10, 108.156.211.34, 108.156.211.26, 108.156.211.76] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instanc

## Added by hand

(none)
