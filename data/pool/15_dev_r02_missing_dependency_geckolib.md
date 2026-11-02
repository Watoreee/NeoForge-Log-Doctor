# Judging sheet 15: `r02_missing_dependency_geckolib` (dev)

- **Category:** `missing_dependency`  |  **Culprit:** `geckolib`  |  **Acceptable:** geckolib, ars_nouveau
- **What was broken:** disabled geckolib in CurseForge; theurgy was auto-disabled as its dependent
- **Logs in this scenario:** r02_crash, r02_latest
- **Documents to judge:** 57

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 5/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#4@r02c, hybrid_b#1@r02c, hybrid_c#1@r02c, bm25_b#7@r02c, dense_b#1@r02c, hybrid_a#9@r02l, dense_b#6@r02l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 5/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_a#9@r02c, hybrid_b#2@r02c, hybrid_c#2@r02c, bm25_b#4@r02c, dense_b#6@r02c, hybrid_a#1@r02l, dense_b#3@r02l
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 5/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: hybrid_b#3@r02c, bm25_b#5@r02c, dense_b#9@r02c, hybrid_a#4@r02l, hybrid_b#1@r02l, hybrid_c#2@r02l, bm25_b#1@r02l, dense_b#1@r02l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:bernie-g/geckolib#642** (github_issue, 4/6 conditions)
  - geckolib issue #642: [Bug] Crash on neoforge 21.1.61
  - https://github.com/bernie-g/geckolib/issues/642
  - retrieved by: hybrid_b#4@r02c, hybrid_c#3@r02c, dense_b#2@r02c, hybrid_a#10@r02l, hybrid_b#4@r02l, hybrid_c#8@r02l, dense_b#8@r02l
  - excerpt: [issue by schindlershadow] geckolib-neoforge-1.21.1-4.6.6 crashed neoforge 21.1.61 with no other mods installed https://pastebin.com/raw/XzKcguYD [comment by Witixin1512 (contributor)] Does this issue still happen with latest NeoForge? [comment by Seggellion (none)] Yes i'm getting the same issue on NeoForge 21.1.37: ``` Caused by: org.spongepowered.asm.mixin.injection.throwables.InjectionError: Critical injection failure: Callback method geckolib$wrapArmorPieceRender(Lnet/minecraft/client/renderer/entity/layers/HumanoidArmorLayer;Lcom/mojang/blaze3d/vertex/PoseStack;Lnet/minecraft/cli

- [ ] **gh-issue:bernie-g/geckolib#669** (github_issue, 4/6 conditions)
  - geckolib issue #669: Marvel Mod crashes with latest Geckolib version! Geckolib v. 4.7.2 works fine!
  - https://github.com/bernie-g/geckolib/issues/669
  - retrieved by: hybrid_b#10@r02c, hybrid_c#6@r02c, hybrid_b#2@r02l, hybrid_c#3@r02l, bm25_b#9@r02l, dense_b#5@r02l
  - excerpt: [issue by Tomatoe1] The error will show that Geckolib latest version 4.7.3 causes the Marvel mod to crash because of a missing model of the vibranium shield! I hope I did it right by including the error log, and I hope it's not too long either... ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 2025-01-02 13:46:53 Description: Rendering overlay java.lang.IllegalArgumentException: No model for layer marvel:vibranium_shield#main at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.model.geom.EntityModelSet.bakeLayer(EntityModelSet.java:17) ~[client-1.21.1-20240808.144430-sr

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 4/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_a#8@r02l, hybrid_b#9@r02l, bm25_a#4@r02l, dense_b#10@r02l
  - excerpt: mods.modlauncher.Launcher/MODLAUNCHER]: ModLauncher 10.0.1+10.0.1+main.e9521dc3 starting: java version 17.0.3 by Microsoft; OS Windows 10 arch amd64 version 10.0 [07lip2022 18:29:06.835] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.minecraft/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2390!/ Service=ModLauncher Env=CLIENT [07lip2022 18:29:07.952] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\fmlcore

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 4/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: hybrid_a#10@r02c, hybrid_b#7@r02c, hybrid_c#9@r02c, dense_b#9@r02l
  - excerpt: [issue by khorvo77] MultiMC version: 0.6.12-1530 Forge 36.1.0 Minecraft 1.16.5 Crash report: ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 5/15/21 8:40 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.fml.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:85) ~[forge:?] {re:classloading} at net.minecraftforge.fml.client.ClientModLoader.completeModLoading(ClientModLoader.java:188) ~[forge:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.lambda$null

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#6@r02c, hybrid_a#3@r02l, bm25_a#1@r02l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#5@r02c, hybrid_c#5@r02c, bm25_b#8@r02c, hybrid_b#7@r02l, hybrid_c#4@r02l, bm25_b#2@r02l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_b#6@r02c, hybrid_c#4@r02c, bm25_b#3@r02c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:bernie-g/geckolib#881** (github_issue, 3/6 conditions)
  - geckolib issue #881: game crashes on launch
  - https://github.com/bernie-g/geckolib/issues/881
  - retrieved by: hybrid_b#3@r02l, hybrid_c#7@r02l, bm25_b#6@r02l
  - excerpt: [issue by anthonyguzman1015-bot] game crashes after launch with the colossus mod and geckolib 1.15.2 <img width="4032" height="3024" alt="Image" src="https://github.com/user-attachments/assets/487b50d8-ec13-488f-a1cc-619a71cd853e" /> [comment by anthonyguzman1015-bot (none)] ********+ [comment by Tslat (collaborator)] Looks like you don't even have geckolib installed

- [ ] **gh-issue:bernie-g/geckolib#767** (github_issue, 3/6 conditions)
  - geckolib issue #767: Mod causes resource loading errors for non-geckolib animation files
  - https://github.com/bernie-g/geckolib/issues/767
  - retrieved by: hybrid_b#6@r02l, hybrid_c#5@r02l, dense_b#4@r02l
  - excerpt: :0/:4.8] at software.bernie.geckolib.cache.GeckoLibCache.lambda$loadAnimations$1(GeckoLibCache.java:86) ~[geckolib-4.8.i0:0/:4.8] at software.bernie.geckolib.cache.GeckoLibCache.lambda$loadResources$5(GeckoLibCache.java:128) ~[geckolib-4.8.i0:0/:4.8] at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1768) ~[?:?] ... 6 more ``` [comment by Tslat (collaborator)] What mod is using the animations folder? mcinspects isn't even on 1.20.1 is it? [comment by DarksideAlex (none)] Private fork of MCInspects with 1.20.1 support and data--driven animations. That shoul

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r02c, bm25_a#4@r02c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 2/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: hybrid_a#8@r02c, bm25_a#1@r02c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#2@r02l, bm25_a#3@r02l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#3@r02c, bm25_a#2@r02c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#2@r02c, bm25_a#3@r02c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 2/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: hybrid_b#9@r02c, bm25_b#3@r02l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:bernie-g/geckolib#766** (github_issue, 2/6 conditions)
  - geckolib issue #766: Crashing due to glowing
  - https://github.com/bernie-g/geckolib/issues/766
  - retrieved by: hybrid_b#5@r02l, bm25_b#5@r02l
  - excerpt: .dev/paste/mclogs/wq20Vpe>) | [crash_assistant_app.log](<https://gnomebot.dev/paste/mclogs/JSZhKDQ>) | [modlist.txt](<https://gnomebot.dev/paste/mclogs/DkTxDL8>) [comment by Tslat (collaborator)] You'd need to narrow it down to whatever mod is adding the armour it's crashing with =/ [comment by Cittycool (none)] > You'd need to narrow it down to whatever mod is adding the armour it's crashing with =/ Ah so is it due to armour, that is good to know, thank you- would you like an update if i figure it out? [comment by Tslat (collaborator)] Nevermind found it This is because EndermanO

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 2/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: hybrid_a#6@r02c, bm25_a#5@r02l
  - excerpt: .76, 108.156.211.10] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instances/1.19/.minecraft Java path is: /usr/lib/jvm/java-17-openjdk-amd64/bin/java Checking Java version... Java is version 17.0.4, using 64-bit architecture, from Private Build. Intel(R) Pentium(R) Silver N5000 CPU @ 1.10GHz Intel Corporation UHD Graphics 605 (rev 03) DeviceName: Onboard - Video Subsystem: Dell UHD Graphics 605 OpenGL version string: 4.6 (Compatibility Profile) Mesa 21

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 2/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: bm25_b#9@r02c, hybrid_a#6@r02l
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 2/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#8@r02c, hybrid_c#7@r02c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 2/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_c#10@r02l, bm25_b#10@r02l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:TheIllusiveC4/Curios#473** (github_issue, 1/6 conditions)
  - Curios issue #473: game crashes on start up when Ars Nouveau is installed
  - https://github.com/TheIllusiveC4/Curios/issues/473
  - retrieved by: hybrid_c#10@r02c, hybrid_c#1@r02l
  - excerpt: [issue by shoezons] i noticed that Curios is very not happy whenever Ars Nouveau is installed. i don't fully know whats causing it to happen. i need both mods since they are crucial for my modpack. here is the crash log if anyone could help me out with this. would be greatly appreciated. [latest.log](https://github.com/user-attachments/files/18428962/latest.log) [comment by TheIllusiveC4 (owner)] Duplicate of https://github.com/TheIllusiveC4/Curios/issues/344 This is not an issue with Ars Nouveau, but with the Tiered mod.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 1/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: bm25_b#1@r02c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#2@r02c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:bernie-g/geckolib#844** (github_issue, 1/6 conditions)
  - geckolib issue #844: Geckolib doesn't like owo-lib
  - https://github.com/bernie-g/geckolib/issues/844
  - retrieved by: dense_b#7@r02c, dense_b#2@r02l
  - excerpt: tributor)] Using MultiMC and Neoforge 21.1.233 create-1.21.1-6.0.10.jar dragonlib-neoforge-1.21.1-beta-3.0.28.jar geckolib-neoforge-1.21.1-4.8.4.jar jei-1.21.1-neoforge-19.27.0.340.jar owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar pantographsandwires-neoforge-1.21.1-beta-0.2.3-C6.jar I can launch just fine with no errors, get to the main menu, etc. My recommendation would be you binary search your pack, start with this bunch of mods, and slowly add mods in packs until you can replicate the issue and isolate the minimum required mods to have this.

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#2@r02l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:bernie-g/geckolib#635** (github_issue, 1/6 conditions)
  - geckolib issue #635: crash on neoforge 1.21.1 (.61)
  - https://github.com/bernie-g/geckolib/issues/635
  - retrieved by: dense_b#3@r02c
  - excerpt: [issue by VaporeonScripts] https://mclo.gs/7zc6O9W [comment by Tslat (collaborator)] Update to .62 [comment by VaporeonScripts (none)] alright,ty

- [ ] **gh-issue:bernie-g/geckolib#670** (github_issue, 1/6 conditions)
  - geckolib issue #670: Crash on launch | 1.21.4 Forge
  - https://github.com/bernie-g/geckolib/issues/670
  - retrieved by: dense_b#4@r02c
  - excerpt: [issue by EXESURUM] Hi ! I just started modding Minecraft and I'm getting this crash every time I launch the game using the latest release of Forge. It appears to be the only mod to cause a crash, whether if I put another mod that needs Geckolib or not. Is it an Apple problem or am I doing something wrong? Sorry if this is a really dumb question and thank you for all the help you give on here !! Here's the [log](https://pastebin.com/raw/N47qzLRG) [comment by Janabugg (none)] I have the same issue [comment by Tslat (collaborator)] > I have the same issue On what version of geckolib?

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#4@r02l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r02c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#5@r02l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:TwelveIterations/Balm#85** (github_issue, 1/6 conditions)
  - Balm issue #85: Server crashes on startup
  - https://github.com/TwelveIterations/Balm/issues/85
  - retrieved by: hybrid_a#5@r02c
  - excerpt: [issue by ashton727] ### Minecraft Version 1.21 ### Mod Loader NeoForge ### Mod Loader Version 21.0.46 ### Mod Version 21.0.11 ### Balm Version 21.0.11 ### Describe the Issue 1. Start neoforge 21.0.46 server with balm 2. Observe crash ### Logs https://pastebin.com/4asPjjkH ### Do you use any performance-enhancing mods (e.g. OptiFine) or custom server distributions (e.g. SpongeForge)? no [comment by BlayTheNinth (member)] Try Java 21 [comment by ashton727 (none)] This version of Neoforge requires Java 22 I believe. [comment by BlayTheNinth (member)] Minecraft 1.21 uses Java 2

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 1/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: dense_b#5@r02c
  - excerpt: ge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod file B2e20f83d9414-B2e20f83d9414.jar of type MOD with locator net.minecraftforge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod fi [... truncated] [comment by thedarkcolour (owner)] Do you have a GitHub repo for this? [comment by KP2048 (none)] Yes but I haven’t committed the switch to kotlin yet [comment by KP2048 (none)] I can zip it up and post it here if you like [comment by thedarkcolour (owner)] I don't know how you have the proje

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#6@r02c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:bernie-g/geckolib#804** (github_issue, 1/6 conditions)
  - geckolib issue #804: NullPointerException in GeoArmorRenderer when checking entity glow status
  - https://github.com/bernie-g/geckolib/issues/804
  - retrieved by: hybrid_c#6@r02l
  - excerpt: line (Accessories, Iris, etc.) ### Environment - **OS**: Windows 11 - **Java**: OpenJDK 21.0.9 - **Graphics**: AMD Radeon RX 7600 - **Total Mods**: 375+ installed ### Workarounds Attempted - ✗ Disabling Iron's Spellbooks glow features - ✗ Disabling Ars Nouveau entity lights - ✗ Adjusting client rendering configs - ✗ The crash persists in all cases ### Priority **HIGH** - This is a critical crash that prevents gameplay in the Nether dimension with any GeckoLib armor installed. [comment by Tslat (collaborator)] The entity shouldn't _be_ null, is the problem I don't check for null because the

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#6@r02l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_a#7@r02l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#7@r02c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:bernie-g/geckolib#850** (github_issue, 1/6 conditions)
  - geckolib issue #850: Animation Parsing Error
  - https://github.com/bernie-g/geckolib/issues/850
  - retrieved by: dense_b#8@r02c, dense_b#7@r02l
  - excerpt: ="741" alt="Image" src="https://github.com/user-attachments/assets/c56bde1b-cc3a-431c-98fe-c0fb76c9fd8c" /> [comment by Witixin1512 (contributor)] I've tried a similar mod posted on the discord and I cannot replicate this. Your crash report mentions a 3 year old GeckoLib version, which you should not be using. geckolib-forge-1.20.1-4.2.1 was published on July 6th, 2023. Update to 4.8.3 and post again the new crash report if it persists.

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#7@r02l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#7@r02c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: bm25_a#7@r02l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#8@r02c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#8@r02l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:bernie-g/geckolib#854** (github_issue, 1/6 conditions)
  - geckolib issue #854: crashing on world creation
  - https://github.com/bernie-g/geckolib/issues/854
  - retrieved by: hybrid_b#8@r02l
  - excerpt: [issue by NobodyH3re] trying to create a world with Geckolib installed, and crashes before world creation. only errors are from gecko lib. Log included for clarity https://mclo.gs/ORD1EHF [comment by Tslat (collaborator)] One of those mods has an invalid animation json

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#8@r02l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 1/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: hybrid_c#8@r02c
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r02c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 1/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: hybrid_c#9@r02l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:wisp-forest/owo-lib#413** (github_issue, 1/6 conditions)
  - owo-lib issue #413: Owolib causing crash
  - https://github.com/wisp-forest/owo-lib/issues/413
  - retrieved by: bm25_a#9@r02l
  - excerpt: [issue by stormchasersam2020] https://gnomebot.dev/paste/mclogs/RnmfQOR Heres the crash log [comment by stormchasersam2020 (none)] file:///C:/Users/<user>/curseforge/minecraft/Instances/Survival-Vanilla%20enhanced/crash-reports/crash-2025-07-29_21.15.48-server.txt [comment by stormchasersam2020 (none)] Heres the stack trace as well. Thread: Render thread Stacktrace: at knot//com.mojang.serialization.DataResult$Error.md029798$owo$lambda$addStackTraceToException$0$0(DataResult.java:565) at knot//com.mojang.serialization.DataResult$Error.getOrThrow(DataResult.java:287) at knot//com.mojang

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: bm25_a#10@r02c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 1/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: bm25_b#10@r02c
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#10@r02l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:bernie-g/geckolib#770** (github_issue, 1/6 conditions)
  - geckolib issue #770: Crashing with mowzie's mobs and epic fight (neoforge 1.21.1)
  - https://github.com/bernie-g/geckolib/issues/770
  - retrieved by: dense_b#10@r02c
  - excerpt: [issue by smoliv-tato] [latest.log](https://github.com/user-attachments/files/22724861/latest.log) If i have a mask from mowzie's mobs and open my inventory, the game crashes. The only mods I installed are mowzie's mobs and epic fight. [comment by Tslat (collaborator)] epicfight mod is broken nothing I can do here, take this to them

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_b#10@r02l
  - excerpt: legacy\Minecraft\game\libraries\net\minecraftforge\javafmllanguage\1.19.2-43.4.20\javafmllanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\lowcodelanguage\1.19.2-43.4.20\lowcodelanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\mclanguage\1.19.2-43.4.20\mclangu

## Added by hand

(none)
