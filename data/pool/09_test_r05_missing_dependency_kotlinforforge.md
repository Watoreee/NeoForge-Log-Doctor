# Judging sheet 09: `r05_missing_dependency_kotlinforforge` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `kotlinforforge`  |  **Acceptable:** kotlinforforge, cobbleworkers, torchmastercobblemoncompat
- **What was broken:** disabled KotlinForForge in CurseForge; Cobblemon and its dependents then failed to load
- **Logs in this scenario:** r05_crash, r05_latest
- **Documents to judge:** 25

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 5/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#3@r05c, hybrid_b#2@r05c, dense_b#1@r05c, hybrid_a#1@r05l, hybrid_b#2@r05l, hybrid_c#2@r05l, bm25_b#2@r05l, dense_b#2@r05l
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 5/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: hybrid_a#2@r05l, hybrid_b#4@r05l, hybrid_c#3@r05l, bm25_a#3@r05l, dense_b#5@r05l
  - excerpt: main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=ModLauncher Env=CLIENT [19:57:11] [pool-2-thread-1/INFO]: GL info: NVIDIA GeForce RTX 2060 SUPER/PCIe/SSE2 GL version 4.6.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 4/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: hybrid_b#1@r05c, hybrid_c#3@r05c, bm25_b#2@r05c, dense_b#3@r05c, hybrid_b#1@r05l, hybrid_c#1@r05l, bm25_b#1@r05l, dense_b#3@r05l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#65** (github_issue, 3/6 conditions)
  - KotlinForForge issue #65: 1.19.4 file crashes game
  - https://github.com/thedarkcolour/KotlinForForge/issues/65
  - retrieved by: hybrid_b#4@r05c, dense_b#2@r05c, hybrid_b#3@r05l, bm25_b#3@r05l, dense_b#1@r05l
  - excerpt: [issue by Droolphobia] Hello I'm currently in the process of installing the Cobblemon mod, it requires Kotlin, and I've made sure it was this specific file that is causing the issue. I need version 1.19.4 for the mod, but whenever I launch the game with the file installed, the game crashes before launch and I get a crash exit code:1. I'm not familiar at all with programming, and I'm not the brightest with tech in general, so perhaps I'm doing something wrong here. I should say that I'm putting this file in my mods folder. I appreciate any help I can get, thank you! [comment by davidromrell (n

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#3@r05c, hybrid_a#3@r05l, bm25_a#1@r05l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 3/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#3@r05c, hybrid_c#2@r05c, hybrid_c#5@r05l, dense_b#4@r05l
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 3/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: hybrid_b#5@r05c, hybrid_c#4@r05c, hybrid_b#5@r05l, hybrid_c#4@r05l, bm25_b#5@r05l
  - excerpt: lementation("dev.isxander:yet-another-config-lib:${rootProject.yacl_version}-neoforge") { exclude(group: "net.neoforged.fancymodloader", module: "loader") } ``` I get _almost_ the same error as before, except it says `fml_loader` found multiple copies of `fml_loader`, instead of KFF finding them: ``` Exception in thread "main" java.lang.module.ResolutionException: Module fml_loader reads another module named fml_loader ``` I can't really tell if this is progress or just a shifting goalpost. Edit: If it's better for me to create a new ticket and/or move the conversation to Discord, I am

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r05c, bm25_a#4@r05c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 2/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_c#1@r05c, bm25_b#1@r05c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r05c, bm25_a#3@r05c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_a#5@r05l, bm25_a#4@r05l
  - excerpt: \javafmllanguage\1.19-41.0.63\javafmllanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.958] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\lowcodelanguage\1.19-41.0.63\lowcodelanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.960] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\mclanguage\1.19-41.0.63\mclanguage-1.19-41.0.63

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r05c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 1/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: bm25_a#2@r05l
  - excerpt: loading phase: Mod sodium_extra requires sodium 0.8.12-alpha.3+mc1.21.1 or above Currently, sodium is 0.6.13+mc1.21.1 Error during pre-loading phase: Mod reeses_sodium_options requires sodium 0.8.12-alpha.3 or above Currently, sodium is 0.6.13+mc1.21.1 ``` [comment by Official-V-Zer0 (none)] It may be due to the crashlog only formed after getting through the load screen hence Sodium being 0.6.13, but using 0.8.12-beta.1 is the issue [comment by jellysquid3 (member)] Your log files and crash logs do not relate to each other. The log file contains the actual error, not the crash report. Pleas

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 1/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: bm25_a#2@r05c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 1/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: hybrid_a#4@r05c
  - excerpt: ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.234 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:instancing OpenGL Renderer: Intel(R) UHD Graphics OpenGL Version: 4.6.0 - Build 31.0.101.2127 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecr

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#4@r05l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#4@r05c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#4@r05l
  - excerpt: cpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\librari

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 1/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: dense_b#4@r05c
  - excerpt: ge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod file B2e20f83d9414-B2e20f83d9414.jar of type MOD with locator net.minecraftforge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod fi [... truncated] [comment by thedarkcolour (owner)] Do you have a GitHub repo for this? [comment by KP2048 (none)] Yes but I haven’t committed the switch to kotlin yet [comment by KP2048 (none)] I can zip it up and post it here if you like [comment by thedarkcolour (owner)] I don't know how you have the proje

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r05c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: bm25_b#5@r05c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#5@r05c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:bernie-g/geckolib#850** (github_issue, 1/6 conditions)
  - geckolib issue #850: Animation Parsing Error
  - https://github.com/bernie-g/geckolib/issues/850
  - retrieved by: bm25_a#5@r05l
  - excerpt: [issue by Filan-glitch] GeckoLib V4.8.4 NeoForge 21.1.228 MC1.21.1 Error Logs: [05May2026 11:30:01.258] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.258] [Worker-Main-5/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.261] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.290] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: attack sadly no further information in logs... [comment by Tslat (collaborator)] Provide the mod jar so I can test it I can't do anything with this [comment

- [ ] **gh-issue:thedarkcolour/KotlinForForge#122** (github_issue, 1/6 conditions)
  - KotlinForForge issue #122: [1.21.1-Neoforge] Kotlin crashes on NeoForge 1.21.1
  - https://github.com/thedarkcolour/KotlinForForge/issues/122
  - retrieved by: dense_b#5@r05c
  - excerpt: [issue by overlappingd] Mod `fzzy_config` requires Kotlin, Kotlin crashes the game when the Mod Construction stage is about to finish Crash Report: https://mclo.gs/FEz1bUZ `latest.log`: https://mclo.gs/59pOEet Using the [Just Create SMP](https://www.curseforge.com/minecraft/modpacks/just-create-smp) modpack. [comment by thedarkcolour (owner)] Not a KFF issue. Vanilla Backport bug from the looks of it

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_c#5@r05c
  - excerpt: .fml.ModList.forEachModInOrder(ModList.java:174) ~[loader-4.0.42.jar%23107!/:4.0] {re:mixin} at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModLoader.postEvent(ModLoader.java:358) ~[loader-4.0.42.jar%23107!/:4.0] {} at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.client.ClientHooks.initClientHooks(ClientHooks.java:1028) ~[neoforge-21.1.234-universal.jar%23196!/:?] {re:mixin,re:classloading,pl:mixin:APP:sodium-neoforge.mixins.json:platform.neoforge.ClientHooksMixin from mod sodium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.<init>(Minecraft.java:60

## Added by hand

(none)
