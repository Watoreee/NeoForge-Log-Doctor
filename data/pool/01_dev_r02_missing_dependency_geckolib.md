# Judging sheet 01: `r02_missing_dependency_geckolib` (dev)

- **Category:** `missing_dependency`  |  **Culprit:** `geckolib`  |  **Acceptable:** geckolib, ars_nouveau
- **What was broken:** disabled geckolib in CurseForge; theurgy was auto-disabled as its dependent
- **Logs in this scenario:** r02_crash, r02_latest
- **Documents to judge:** 31

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 5/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: hybrid_b#2@r02c, hybrid_c#2@r02c, bm25_b#4@r02c, hybrid_a#1@r02l, dense_b#3@r02l
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 5/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: hybrid_b#3@r02c, bm25_b#5@r02c, hybrid_a#4@r02l, hybrid_b#1@r02l, hybrid_c#2@r02l, bm25_b#1@r02l, dense_b#1@r02l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 4/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#4@r02c, hybrid_b#1@r02c, hybrid_c#1@r02c, dense_b#1@r02c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:bernie-g/geckolib#642** (github_issue, 3/6 conditions)
  - geckolib issue #642: [Bug] Crash on neoforge 21.1.61
  - https://github.com/bernie-g/geckolib/issues/642
  - retrieved by: hybrid_b#4@r02c, hybrid_c#3@r02c, dense_b#2@r02c, hybrid_b#4@r02l
  - excerpt: [issue by schindlershadow] geckolib-neoforge-1.21.1-4.6.6 crashed neoforge 21.1.61 with no other mods installed https://pastebin.com/raw/XzKcguYD [comment by Witixin1512 (contributor)] Does this issue still happen with latest NeoForge? [comment by Seggellion (none)] Yes i'm getting the same issue on NeoForge 21.1.37: ``` Caused by: org.spongepowered.asm.mixin.injection.throwables.InjectionError: Critical injection failure: Callback method geckolib$wrapArmorPieceRender(Lnet/minecraft/client/renderer/entity/layers/HumanoidArmorLayer;Lcom/mojang/blaze3d/vertex/PoseStack;Lnet/minecraft/cli

- [ ] **gh-issue:bernie-g/geckolib#669** (github_issue, 3/6 conditions)
  - geckolib issue #669: Marvel Mod crashes with latest Geckolib version! Geckolib v. 4.7.2 works fine!
  - https://github.com/bernie-g/geckolib/issues/669
  - retrieved by: hybrid_b#2@r02l, hybrid_c#3@r02l, dense_b#5@r02l
  - excerpt: [issue by Tomatoe1] The error will show that Geckolib latest version 4.7.3 causes the Marvel mod to crash because of a missing model of the vibranium shield! I hope I did it right by including the error log, and I hope it's not too long either... ---- Minecraft Crash Report ---- // Daisy, daisy... Time: 2025-01-02 13:46:53 Description: Rendering overlay java.lang.IllegalArgumentException: No model for layer marvel:vibranium_shield#main at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.model.geom.EntityModelSet.bakeLayer(EntityModelSet.java:17) ~[client-1.21.1-20240808.144430-sr

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#5@r02c, hybrid_c#5@r02c, hybrid_c#4@r02l, bm25_b#2@r02l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r02c, bm25_a#4@r02c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#3@r02l, bm25_a#1@r02l
  - excerpt: .util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:507) [?:?] at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1491) [?:?] at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:2073) [?:?] at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2035) [?:?] at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187) [?:?] [28Apr2024 18:58:29.050] [Render thread/FATAL] [net.neoforged.fml.ModLoader/LOADING]: Failed to wait for future Mod Construction, 1 errors found [28Apr2024 18:

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

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 2/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_c#4@r02c, bm25_b#3@r02c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:bernie-g/geckolib#767** (github_issue, 2/6 conditions)
  - geckolib issue #767: Mod causes resource loading errors for non-geckolib animation files
  - https://github.com/bernie-g/geckolib/issues/767
  - retrieved by: hybrid_c#5@r02l, dense_b#4@r02l
  - excerpt: :0/:4.8] at software.bernie.geckolib.cache.GeckoLibCache.lambda$loadAnimations$1(GeckoLibCache.java:86) ~[geckolib-4.8.i0:0/:4.8] at software.bernie.geckolib.cache.GeckoLibCache.lambda$loadResources$5(GeckoLibCache.java:128) ~[geckolib-4.8.i0:0/:4.8] at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1768) ~[?:?] ... 6 more ``` [comment by Tslat (collaborator)] What mod is using the animations folder? mcinspects isn't even on 1.20.1 is it? [comment by DarksideAlex (none)] Private fork of MCInspects with 1.20.1 support and data--driven animations. That shoul

- [ ] **gh-issue:bernie-g/geckolib#766** (github_issue, 2/6 conditions)
  - geckolib issue #766: Crashing due to glowing
  - https://github.com/bernie-g/geckolib/issues/766
  - retrieved by: hybrid_b#5@r02l, bm25_b#5@r02l
  - excerpt: .dev/paste/mclogs/wq20Vpe>) | [crash_assistant_app.log](<https://gnomebot.dev/paste/mclogs/JSZhKDQ>) | [modlist.txt](<https://gnomebot.dev/paste/mclogs/DkTxDL8>) [comment by Tslat (collaborator)] You'd need to narrow it down to whatever mod is adding the armour it's crashing with =/ [comment by Cittycool (none)] > You'd need to narrow it down to whatever mod is adding the armour it's crashing with =/ Ah so is it due to armour, that is good to know, thank you- would you like an update if i figure it out? [comment by Tslat (collaborator)] Nevermind found it This is because EndermanO

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r02c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TheIllusiveC4/Curios#473** (github_issue, 1/6 conditions)
  - Curios issue #473: game crashes on start up when Ars Nouveau is installed
  - https://github.com/TheIllusiveC4/Curios/issues/473
  - retrieved by: hybrid_c#1@r02l
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
  - retrieved by: dense_b#2@r02l
  - excerpt: tributor)] Using MultiMC and Neoforge 21.1.233 create-1.21.1-6.0.10.jar dragonlib-neoforge-1.21.1-beta-3.0.28.jar geckolib-neoforge-1.21.1-4.8.4.jar jei-1.21.1-neoforge-19.27.0.340.jar owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar pantographsandwires-neoforge-1.21.1-beta-0.2.3-C6.jar I can launch just fine with no errors, get to the main menu, etc. My recommendation would be you binary search your pack, start with this bunch of mods, and slowly add mods in packs until you can replicate the issue and isolate the minimum required mods to have this.

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#2@r02l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#3@r02l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:bernie-g/geckolib#635** (github_issue, 1/6 conditions)
  - geckolib issue #635: crash on neoforge 1.21.1 (.61)
  - https://github.com/bernie-g/geckolib/issues/635
  - retrieved by: dense_b#3@r02c
  - excerpt: [issue by VaporeonScripts] https://mclo.gs/7zc6O9W [comment by Tslat (collaborator)] Update to .62 [comment by VaporeonScripts (none)] alright,ty

- [ ] **gh-issue:bernie-g/geckolib#881** (github_issue, 1/6 conditions)
  - geckolib issue #881: game crashes on launch
  - https://github.com/bernie-g/geckolib/issues/881
  - retrieved by: hybrid_b#3@r02l
  - excerpt: [issue by anthonyguzman1015-bot] game crashes after launch with the colossus mod and geckolib 1.15.2 <img width="4032" height="3024" alt="Image" src="https://github.com/user-attachments/assets/487b50d8-ec13-488f-a1cc-619a71cd853e" /> [comment by anthonyguzman1015-bot (none)] ********+ [comment by Tslat (collaborator)] Looks like you don't even have geckolib installed

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 1/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: bm25_a#4@r02l
  - excerpt: 17 [07lip2022 18:29:10.993] [main/INFO] [cpw.mods.modlauncher.LaunchServiceHandler/MODLAUNCHER]: Launching target 'forgeclient' with arguments [--version, 1.19-forge-41.0.63, --gameDir, C:\Users\<user>\AppData\Roaming\.minecraft, --assetsDir, C:\Users\<user>\AppData\Roaming\.minecraft\assets, --uuid, <token>, --username, <player>, --assetIndex, 1.19, --accessToken, <token> truncated] [comment by BlayTheNinth (member)] Those logs are 99% OptiFine, are you sure that's the correct log? [comment by agabeluga (none)] I changed it. [comment by BlayTheNinth (member)] The Forge forum lied to you,

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

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: bm25_a#5@r02l
  - excerpt: [issue by Andaros210] Here's the log copy and paste. MultiMC version: 0.6.16-3430 Launched instance in online mode authserver.mojang.com resolves to: [108.138.149.51, 108.138.149.48, 108.138.149.65, 108.138.149.64] session.minecraft.net resolves to: [107.20.118.247, 52.72.238.122, 54.172.106.247] textures.minecraft.net resolves to: [108.156.211.10, 108.156.211.34, 108.156.211.26, 108.156.211.76] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instanc

- [ ] **gh-issue:thedarkcolour/KotlinForForge#37** (github_issue, 1/6 conditions)
  - KotlinForForge issue #37: crash
  - https://github.com/thedarkcolour/KotlinForForge/issues/37
  - retrieved by: dense_b#5@r02c
  - excerpt: ge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod file B2e20f83d9414-B2e20f83d9414.jar of type MOD with locator net.minecraftforge.fml.loading.moddiscovery.ClasspathLocator@77ec911 [09:56:16] [main/INFO] (ModDiscoverer) Found mod fi [... truncated] [comment by thedarkcolour (owner)] Do you have a GitHub repo for this? [comment by KP2048 (none)] Yes but I haven’t committed the switch to kotlin yet [comment by KP2048 (none)] I can zip it up and post it here if you like [comment by thedarkcolour (owner)] I don't know how you have the proje

## Added by hand

(none)
