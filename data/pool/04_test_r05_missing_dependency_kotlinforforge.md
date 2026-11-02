# Judging sheet 04: `r05_missing_dependency_kotlinforforge` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `kotlinforforge`  |  **Acceptable:** kotlinforforge, cobbleworkers, torchmastercobblemoncompat
- **What was broken:** disabled KotlinForForge in CurseForge; Cobblemon and its dependents then failed to load
- **Logs in this scenario:** r05_crash, r05_latest
- **Documents to judge:** 43

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 6/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#3@r05c, hybrid_b#2@r05c, hybrid_c#6@r05c, bm25_b#10@r05c, dense_b#1@r05c, hybrid_a#1@r05l, hybrid_b#2@r05l, hybrid_c#2@r05l, bm25_a#7@r05l, bm25_b#2@r05l, dense_b#2@r05l
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 6/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_c#10@r05c, bm25_b#3@r05c, hybrid_a#3@r05l, hybrid_b#10@r05l, hybrid_c#10@r05l, bm25_a#1@r05l, dense_b#10@r05l
  - excerpt: .0.0] at LAYER PLUGIN/kfflang@5.0.0/thedarkcolour.kotlinforforge.neoforge.KotlinModContainer.constructMod(KotlinModContainer.kt:108) ~[kfflang-5.0.0.jar%23217!/:5.0.0] at MC-BOOTSTRAP/fml_loader@3.0.18/net.neoforged.fml.ModLoader.lambda$constructMods$9(ModLoader.java:169) ~[loader-3.0.18.jar%23163!/:3.0] at MC-BOOTSTRAP/fml_loader@3.0.18/net.neoforged.fml.ModLoader.lambda$dispatchParallelTask$11(ModLoader.java:216) ~[loader-3.0.18.jar%23163!/:3.0] at java.base/java.util.concurrent.CompletableFuture$AsyncRun.run$$$capture(CompletableFuture.java:1804) [?:?] at java.base/java.util.concu

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 6/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: hybrid_a#2@r05l, hybrid_b#4@r05l, hybrid_c#3@r05l, bm25_a#3@r05l, bm25_b#7@r05l, dense_b#5@r05l
  - excerpt: main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=ModLauncher Env=CLIENT [19:57:11] [pool-2-thread-1/INFO]: GL info: NVIDIA GeForce RTX 2060 SUPER/PCIe/SSE2 GL version 4.6.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#65** (github_issue, 5/6 conditions)
  - KotlinForForge issue #65: 1.19.4 file crashes game
  - https://github.com/thedarkcolour/KotlinForForge/issues/65
  - retrieved by: hybrid_b#4@r05c, bm25_b#9@r05c, dense_b#2@r05c, hybrid_a#7@r05l, hybrid_b#3@r05l, hybrid_c#6@r05l, bm25_b#3@r05l, dense_b#1@r05l
  - excerpt: [issue by Droolphobia] Hello I'm currently in the process of installing the Cobblemon mod, it requires Kotlin, and I've made sure it was this specific file that is causing the issue. I need version 1.19.4 for the mod, but whenever I launch the game with the file installed, the game crashes before launch and I get a crash exit code:1. I'm not familiar at all with programming, and I'm not the brightest with tech in general, so perhaps I'm doing something wrong here. I should say that I'm putting this file in my mods folder. I appreciate any help I can get, thank you! [comment by davidromrell (n

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 5/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#3@r05c, hybrid_c#2@r05c, bm25_b#6@r05c, dense_b#7@r05c, hybrid_a#6@r05l, hybrid_b#6@r05l, hybrid_c#5@r05l, bm25_b#10@r05l, dense_b#4@r05l
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 5/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_b#8@r05c, hybrid_c#5@r05c, dense_b#6@r05c, hybrid_a#10@r05l, bm25_a#9@r05l, dense_b#9@r05l
  - excerpt: .fml.ModList.forEachModInOrder(ModList.java:174) ~[loader-4.0.42.jar%23107!/:4.0] {re:mixin} at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModLoader.postEvent(ModLoader.java:358) ~[loader-4.0.42.jar%23107!/:4.0] {} at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.client.ClientHooks.initClientHooks(ClientHooks.java:1028) ~[neoforge-21.1.234-universal.jar%23196!/:?] {re:mixin,re:classloading,pl:mixin:APP:sodium-neoforge.mixins.json:platform.neoforge.ClientHooksMixin from mod sodium,pl:mixin:A} at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.Minecraft.<init>(Minecraft.java:60

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 4/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: hybrid_b#1@r05c, hybrid_c#3@r05c, bm25_b#2@r05c, dense_b#3@r05c, hybrid_b#1@r05l, hybrid_c#1@r05l, bm25_b#1@r05l, dense_b#3@r05l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 4/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#6@r05c, hybrid_b#6@r05c, hybrid_c#1@r05c, bm25_b#1@r05c, hybrid_a#9@r05l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 4/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: hybrid_b#5@r05c, hybrid_c#4@r05c, bm25_b#7@r05c, hybrid_b#5@r05l, hybrid_c#4@r05l, bm25_b#5@r05l, dense_b#7@r05l
  - excerpt: lementation("dev.isxander:yet-another-config-lib:${rootProject.yacl_version}-neoforge") { exclude(group: "net.neoforged.fancymodloader", module: "loader") } ``` I get _almost_ the same error as before, except it says `fml_loader` found multiple copies of `fml_loader`, instead of KFF finding them: ``` Exception in thread "main" java.lang.module.ResolutionException: Module fml_loader reads another module named fml_loader ``` I can't really tell if this is progress or just a shifting goalpost. Edit: If it's better for me to create a new ticket and/or move the conversation to Discord, I am

- [ ] **gh-issue:thedarkcolour/KotlinForForge#122** (github_issue, 3/6 conditions)
  - KotlinForForge issue #122: [1.21.1-Neoforge] Kotlin crashes on NeoForge 1.21.1
  - https://github.com/thedarkcolour/KotlinForForge/issues/122
  - retrieved by: hybrid_b#9@r05c, hybrid_c#9@r05c, dense_b#5@r05c
  - excerpt: [issue by overlappingd] Mod `fzzy_config` requires Kotlin, Kotlin crashes the game when the Mod Construction stage is about to finish Crash Report: https://mclo.gs/FEz1bUZ `latest.log`: https://mclo.gs/59pOEet Using the [Just Create SMP](https://www.curseforge.com/minecraft/modpacks/just-create-smp) modpack. [comment by thedarkcolour (owner)] Not a KFF issue. Vanilla Backport bug from the looks of it

- [ ] **gh-issue:thedarkcolour/KotlinForForge#103** (github_issue, 3/6 conditions)
  - KotlinForForge issue #103: [1.21 NeoForge] Architectury - Module fml_loader reads another module named fml_loader
  - https://github.com/thedarkcolour/KotlinForForge/issues/103
  - retrieved by: hybrid_b#7@r05c, hybrid_c#7@r05c, bm25_b#8@r05c
  - excerpt: t figure out whether the issue is with KFF or Architectury so making [an issue for Architectury too](https://github.com/architectury/architectury-api/issues/543). Architectury Enabled Platforms: Fabric, NeoForge Minecraft Version: 1.21 Architectury API Version: 13.0.4 NeoForge Version: 21.0.86-beta KotlinForForge Version: 5.4.0 [comment by thedarkcolour (owner)] This is a bug in Loom. It doesn't happen in plain ModDevGradle/NeoGradle. That being said, have you tried excluding KFF's transitive dependency on FancyModLoader? Has group: `net.neoforged.fancymodloader` and name: `loader`.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#68** (github_issue, 3/6 conditions)
  - KotlinForForge issue #68: KotlinForForge with Ktor: Class not found
  - https://github.com/thedarkcolour/KotlinForForge/issues/68
  - retrieved by: dense_b#9@r05c, hybrid_b#8@r05l, hybrid_c#7@r05l
  - excerpt: [issue by Icosider] Hi, i create a mod with using KotlinForForge and Ktor Client, but when i will be launch the game, game was crash with log: [crash-2023-04-18_13.58.35-fml.txt](https://github.com/thedarkcolour/KotlinForForge/files/11260967/crash-2023-04-18_13.58.35-fml.txt) build.gradle ```groovy ktor_version=2.2.4 <- in gradle.properties dependencies { minecraft 'net.minecraftforge:forge:1.18.2-40.2.1' implementation "io.ktor:ktor-client-core:$ktor_version" implementation "io.ktor:ktor-client-cio:$ktor_version" implementation "io.ktor:ktor-client-okhttp:$ktor_

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 3/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_b#9@r05l, hybrid_c#8@r05l, dense_b#8@r05l
  - excerpt: [issue by filloax] Hi, I'm using KFF 5.6.0 in my 1.21 neoforge mod, but when it loads mixins I get this error when the mixin code tries to use a Kotlin class (even just a static reference): ``` Exception in thread "main" java.lang.RuntimeException: org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.LaunchServiceHandlerDecorator.launch(LaunchServiceHandlerDecorator.java:32) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.LaunchServiceHandl

- [ ] **gh-issue:thedarkcolour/KotlinForForge#88** (github_issue, 3/6 conditions)
  - KotlinForForge issue #88: KotlinForForge crash on startup on latest NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/88
  - retrieved by: hybrid_b#10@r05c, hybrid_c#8@r05c, dense_b#8@r05c
  - excerpt: [issue by Prototik] Due to changes in FML in https://github.com/neoforged/FancyModLoader/commit/a43f00e9aaf2e2e08498fcbcf453fc28c90f1d1a KFF crashes right on startup due to assignment to removed field here: https://github.com/thedarkcolour/KotlinForForge/blob/2183403f3851cd6b564cb4c8761d8abde629744a/neoforge/kfflang/src/main/kotlin/thedarkcolour/kotlinforforge/neoforge/KotlinModContainer.kt#L41 [comment by thedarkcolour (owner)] I'll fix it today when I'm out of class [comment by thedarkcolour (owner)] Fixed in 4.8.0

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r05c, bm25_a#4@r05c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#8@r05l, bm25_a#2@r05l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r05c, bm25_a#3@r05c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#8@r05c, bm25_a#2@r05c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_a#5@r05l, bm25_a#4@r05l
  - excerpt: \javafmllanguage\1.19-41.0.63\javafmllanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.958] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\lowcodelanguage\1.19-41.0.63\lowcodelanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.960] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\mclanguage\1.19-41.0.63\mclanguage-1.19-41.0.63

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 2/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#4@r05c, bm25_a#10@r05l
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 2/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#4@r05l, bm25_a#6@r05l
  - excerpt: cpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\librari

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 2/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: hybrid_b#7@r05l, bm25_b#6@r05l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r05c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

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

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 1/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: dense_b#4@r05c, dense_b#6@r05l
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

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#6@r05c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: hybrid_a#7@r05c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#7@r05c
  - excerpt: [issue by cuberPidor] ### Description My cannon from Create: Big Cannons builds and shoots fine in Creative mode, but fails to assemble or work in Survival. Am I missing something like glue, stress capacity, or assembly steps? ### Game Log https://mclo.gs/wti8vMj ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Rendere

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 1/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: bm25_a#8@r05c
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#8@r05l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:thedarkcolour/KotlinForForge#67** (github_issue, 1/6 conditions)
  - KotlinForForge issue #67: Crashes minecraft
  - https://github.com/thedarkcolour/KotlinForForge/issues/67
  - retrieved by: bm25_b#8@r05l
  - excerpt: [issue by AstroJoot] Whenever I launch Minecraft with it in my mod list it crashes and I have no clue why, exit code is: 1 [comment by thedarkcolour (owner)] Visit the Discord server of whatever mod you are using that requires KFF (Cobblemon? Better Foliage? InvProfiles Next?) [comment by AstroJoot (none)] But it's only KFF because I went through all my mods and it only stopped crashing when i disabled KFF [comment by thedarkcolour (owner)] I assure you it's not (it has never been in dozens of reports), it's whatever mod you're using that depends on KFF

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r05c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#9@r05c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:thedarkcolour/KotlinForForge#71** (github_issue, 1/6 conditions)
  - KotlinForForge issue #71: Error crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/71
  - retrieved by: hybrid_c#9@r05l
  - excerpt: [issue by LeonMazzoli] Exception in thread "main" java.lang.module.ResolutionException: Modules kotlin.stdlib and thedarkcolour.kotlinforforge export package kotlin.sequences to module usefulmachinery at java.base/java.lang.module.Resolver.resolveFail(Resolver.java:901) at java.base/java.lang.module.Resolver.failTwoSuppliers(Resolver.java:815) at java.base/java.lang.module.Resolver.checkExportSuppliers(Resolver.java:755) at java.base/java.lang.module.Resolver.finish(Resolver.java:380) at java.base/java.lang.module.Configuration.<init>(Configuration.java:140) at java.base/java.lang.

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: bm25_b#9@r05l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#10@r05c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#10@r05c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#105** (github_issue, 1/6 conditions)
  - KotlinForForge issue #105: Wrong fml translation key used, leading to crash when displaying loading errors
  - https://github.com/thedarkcolour/KotlinForForge/issues/105
  - retrieved by: dense_b#10@r05c
  - excerpt: .4.0] {} ``` The line mentioned in this stacktrace uses `fml.modloading.[...]` instead of `fml.modloadingissue.[...]`: https://github.com/thedarkcolour/KotlinForForge/blob/548c9dda4e4c184a05443e7bbbbcd16607a9008a/neoforge/kfflang/src/main/kotlin/thedarkcolour/kotlinforforge/neoforge/KotlinLanguageLoader.kt#L51 [comment by thedarkcolour (owner)] Gotta love breaking changes :/ [comment by thedarkcolour (owner)] Fixed in 5.5.0 [comment by btwonion (none)] Hi, would you mind releasing 5.5.0 or at least create a workflow for automatically building the mod? [comment by thedarkcolour (owner)]

## Added by hand

(none)
