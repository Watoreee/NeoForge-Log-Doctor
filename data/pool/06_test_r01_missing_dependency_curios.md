# Judging sheet 06: `r01_missing_dependency_curios` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `curios`  |  **Acceptable:** curios, allthearcanistgear, ars_nouveau, occultism
- **What was broken:** disabled curios in CurseForge
- **Logs in this scenario:** r01_crash, r01_latest
- **Documents to judge:** 34

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 3/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_b#1@r01c, hybrid_c#2@r01c, bm25_b#3@r01c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:TheIllusiveC4/Curios#159** (github_issue, 3/6 conditions)
  - Curios issue #159: Curios Menu won´t open when clicking the icon
  - https://github.com/TheIllusiveC4/Curios/issues/159
  - retrieved by: hybrid_b#1@r01l, hybrid_c#2@r01l, dense_b#1@r01l
  - excerpt: [issue by jaz0894] #### Versions (Be specific, do not write "latest"): * Curios: curios-forge-1.16.5-4.0.5.2 * Forge/Fabric: forge-1.16.5-36.2.0.jar <html> <body> When I click on the curios Icon of curios nothing happens, I also have the mod Sofisticated Backpacks and when Curios is bugged I cannot open backpack inventory. </body> </html> <html> <body> -- </body> </html> <html> <body> forge-1.16.5-36.2.0.jar -- </body> </html> #### Observed Behavior: #### Expected Behavior: #### Steps to Reproduce: 1. 2. 3. ... Crash Log: Please use

- [ ] **gh-issue:TheIllusiveC4/Curios#477** (github_issue, 3/6 conditions)
  - Curios issue #477: curios "spongepowered" error and crash while loading mods
  - https://github.com/TheIllusiveC4/Curios/issues/477
  - retrieved by: hybrid_b#5@r01c, dense_b#1@r01c, hybrid_b#2@r01l, bm25_b#4@r01l
  - excerpt: [issue by ButtWizard] **Versions** Curios: 5.11.1 Forge: 47.3.22 Minecraft: 1.20.1 **What Happened?** Curios encountered error while loading mods. **How to trigger this bug** Open game Begins loading screen Error During Mod Loading Crash Crashlog: https://pastebin.com/4W9g1hXF I haven't done this before so if I'm missing any information, let me know and I'll update asap. [comment by TheIllusiveC4 (owner)] This is a crash from Inventorio's mixin into Curios.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#4@r01c, hybrid_a#2@r01l, bm25_a#1@r01l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [x] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#2@r01c, hybrid_c#4@r01c, bm25_b#5@r01c, hybrid_b#5@r01l, hybrid_c#3@r01l, bm25_b#1@r01l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:TheIllusiveC4/Curios#502** (github_issue, 3/6 conditions)
  - Curios issue #502: [Bug]: Mixin issue in the 1.20.1 forge development environment
  - https://github.com/TheIllusiveC4/Curios/issues/502
  - retrieved by: hybrid_b#3@r01c, hybrid_b#3@r01l, bm25_b#5@r01l, dense_b#2@r01l
  - excerpt: [issue by CuBr202] # Version minecraft_version=1.20.1 forge_version=47.4.0 curios_version=5.12.1+1.20.1 jei_version=15.20.0.106 # Description Hello! I'm new in MC mod development, and I encountered a problem when I'm making my mod based on curios api. I added the repository, mixin and dependencies in the build.gradle according to the guide: ``` plugins { id 'eclipse' id 'idea' id 'maven-publish' id 'net.minecraftforge.gradle' version '[6.0,6.2)' id 'org.spongepowered.mixin' version '[0.7,)' } version = mod_version group = mod_group_id base { archivesName = mod_id }

- [ ] **gh-issue:TheIllusiveC4/Curios#619** (github_issue, 3/6 conditions)
  - Curios issue #619: [Bug]: Failure message: An uncaught parallel processing error has occurred. java.lang.NoClassDefFoundError: net/hazen/hazentouvelib/Items/Curios/WingCurioRenderer
  - https://github.com/TheIllusiveC4/Curios/issues/619
  - retrieved by: hybrid_b#4@r01c, hybrid_c#3@r01c, dense_b#2@r01c
  - excerpt: [issue by LordOfCinders] ### Minecraft Version 1.21.1 ### What happened? When I was logging onto Minecraft (NeoForge) - 1.21.1 - I had recently updated my Curse Forge with alongside with 7 other mods that depend on Curios API, thinking it was all good, then when I log into Minecraft itself, the error code shows up, suddenly it was working the day before, then now suddenly the game stopped working with the error code. As Curios API, is not only the mod has been affected by the error, but other mods too, such as, ("Ace's Spell Utils, Charm of Undying (Fabric/Forge/Quilt), Crystal Chronicles -

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r01c, bm25_a#4@r01c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#2@r01c, bm25_a#2@r01c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#4@r01l, bm25_a#3@r01l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#3@r01c, bm25_a#3@r01c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 2/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#4@r01c, hybrid_c#5@r01c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r01c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TheIllusiveC4/Curios#455** (github_issue, 1/6 conditions)
  - Curios issue #455: [Bug]: Curious API encountered am error during the sided_setup event phase
  - https://github.com/TheIllusiveC4/Curios/issues/455
  - retrieved by: hybrid_a#1@r01l
  - excerpt: [issue by Silverbolt666] ### Minecraft Version 1.20.1 ### What happened? **Curious API encountered am error during the sided_setup event phase** org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError; An unexpected critical error was encountered ### How do you trigger this bug? 1. Update to version curios-forge-5.11.0+1.20.1 2. Start the game in a custom moded setting ### Loader Forge ### Loader Version 47.3.10 ### Mod Version curios-forge-5.11.0+1.20.1 ### Relevant Log Outputs [Curious_latest.log](https://github.com/user-attachments/files/17668260/Curious_

- [ ] **gh-issue:TheIllusiveC4/Curios#473** (github_issue, 1/6 conditions)
  - Curios issue #473: game crashes on start up when Ars Nouveau is installed
  - https://github.com/TheIllusiveC4/Curios/issues/473
  - retrieved by: hybrid_c#1@r01c, hybrid_c#1@r01l
  - excerpt: [issue by shoezons] i noticed that Curios is very not happy whenever Ars Nouveau is installed. i don't fully know whats causing it to happen. i need both mods since they are crucial for my modpack. here is the crash log if anyone could help me out with this. would be greatly appreciated. [latest.log](https://github.com/user-attachments/files/18428962/latest.log) [comment by TheIllusiveC4 (owner)] Duplicate of https://github.com/TheIllusiveC4/Curios/issues/344 This is not an issue with Ars Nouveau, but with the Tiered mod.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 1/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: bm25_b#1@r01c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 1/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: bm25_b#2@r01l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#2@r01c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#2@r01l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:TheIllusiveC4/Curios#478** (github_issue, 1/6 conditions)
  - Curios issue #478: Game Crash
  - https://github.com/TheIllusiveC4/Curios/issues/478
  - retrieved by: dense_b#5@r01c, dense_b#3@r01l
  - excerpt: github.com/notifications/unsubscribe-auth/AJS7C6RCZFQNMIS66ORFLI32QQ2CTAVCNFSM6AAAAABWYKVQGKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDMNRXHAZDMOBXG4> > . > You are receiving this because you authored the thread.Message ID: > ***@***.***> > [image: TheIllusiveC4]*TheIllusiveC4* left a comment > (TheIllusiveC4/Curios#478) > <https://github.com/TheIllusiveC4/Curios/issues/478#issuecomment-2667826877> > > If it's a mod that uses Curios, and not Curios itself, then there isn't > much I can do on my end for this. Does your friend have exactly the same > mods on their client as the server d

- [ ] **gh-issue:TheIllusiveC4/Curios#509** (github_issue, 1/6 conditions)
  - Curios issue #509: [Bug]: Reforged (formerly Tiered) compatibility error
  - https://github.com/TheIllusiveC4/Curios/issues/509
  - retrieved by: dense_b#3@r01c
  - excerpt: happened? > > This has been reported to the Reforged dev team. I just want to make sure that this is not an issue on your end. > > **How to copy this issue:** **1.** Run the most recent version of 1.20.1 of the following mods: > > * [Reforged (formerly Tiered)](https://www.curseforge.com/minecraft/mc-mods/tiered) > > * [Curios API (Forge/NeoForge)](https://www.curseforge.com/minecraft/mc-mods/curios) > > * [UnionLib](https://www.curseforge.com/minecraft/mc-mods/unionlibl) > > > **2.** Run Minecraft I with the said mods with your pilfered launcher. I tested this with Cursefor

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 1/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_a#3@r01l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#3@r01l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:TheIllusiveC4/Curios#487** (github_issue, 1/6 conditions)
  - Curios issue #487: Curios API encountered an error during the common_setup event phase
  - https://github.com/TheIllusiveC4/Curios/issues/487
  - retrieved by: dense_b#4@r01l
  - excerpt: [issue by kun4x] Minecraft Version: 1.20.1 Curios API Version: curios-forge-5.12.1+1.20.1 Forge Version: 47.3.33 Every time I launch the game with curios enabled it shows with a crash screen and the message shown in the title, I have no idea how to fix this. Log: https://mclo.gs/kesuo5k Mod List: https://pastebin.com/9ZHjuVmd ![Image](https://github.com/user-attachments/assets/c57ba1ad-506f-4293-b7b0-c5cbcf0629b9) [comment by Mo9713 (none)] I also get this error on the new update. 5.12.0 version has no issue for me [comment by TheIllusiveC4 (owner)] This crash is coming from one of the mi

- [ ] **gh-issue:TheIllusiveC4/Curios#500** (github_issue, 1/6 conditions)
  - Curios issue #500: Curious error during sided_setup
  - https://github.com/TheIllusiveC4/Curios/issues/500
  - retrieved by: dense_b#4@r01c
  - excerpt: [issue by ImNamzz] Currently Forge 1.20.1 I encounter this while loading with few mods, below is the log file: [crash-2025-03-26_02.46.51-fml.txt](https://github.com/user-attachments/files/19455692/crash-2025-03-26_02.46.51-fml.txt) [comment by TheIllusiveC4 (owner)] This is a crash from the Tiered mod.

- [ ] **gh-issue:TheIllusiveC4/Curios#507** (github_issue, 1/6 conditions)
  - Curios issue #507: [Bug]: i am so confused
  - https://github.com/TheIllusiveC4/Curios/issues/507
  - retrieved by: hybrid_b#4@r01l
  - excerpt: [issue by Vadewolf] ### Minecraft Version 1.21.1 ### What happened? i updated curios to 9.4.2 - 1.21.1 and my game would crash repeatedly but it would say a different mod caused the crash yet i downgraded back to 9.4.1 and the game loads so info needed please [crash-2025-04-09_10.05.01-client.txt](https://github.com/user-attachments/files/19671603/crash-2025-04-09_10.05.01-client.txt) [crash-2025-04-09_10.04.07-client.txt](https://github.com/user-attachments/files/19671604/crash-2025-04-09_10.04.07-client.txt) ### Relevant Log Outputs _No response_ [comment by TheIllusiveC4 (owner)] Unf

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 1/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: hybrid_c#4@r01l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 1/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: bm25_a#4@r01l
  - excerpt: 17 [07lip2022 18:29:10.993] [main/INFO] [cpw.mods.modlauncher.LaunchServiceHandler/MODLAUNCHER]: Launching target 'forgeclient' with arguments [--version, 1.19-forge-41.0.63, --gameDir, C:\Users\<user>\AppData\Roaming\.minecraft, --assetsDir, C:\Users\<user>\AppData\Roaming\.minecraft\assets, --uuid, <token>, --username, <player>, --assetIndex, 1.19, --accessToken, <token> truncated] [comment by BlayTheNinth (member)] Those logs are 99% OptiFine, are you sure that's the correct log? [comment by agabeluga (none)] I changed it. [comment by BlayTheNinth (member)] The Forge forum lied to you,

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r01c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TheIllusiveC4/Curios#454** (github_issue, 1/6 conditions)
  - Curios issue #454: [Bug]: sided_setup crash 1.20.1 even when uninstalled?
  - https://github.com/TheIllusiveC4/Curios/issues/454
  - retrieved by: dense_b#5@r01l
  - excerpt: Silverbolt666 (none)] @Aceplante <del>that's for version 1.21 I suppose, in version 1.20.1 </del> (I'm an idiot and thought this was for 1.21...) I don't have that mod installed, maybe the closer one would be nerb https://www.curseforge.com/minecraft/mc-mods/notenoughrecipebook. I haven't had time to recreate Edit: Tbh, after checking this issue I understood that is not the same thing, I'm going to open a new issue. Mine has to do with the last version presenting the error above, but I do have the mod installed

- [ ] **gh-issue:TheIllusiveC4/Curios#519** (github_issue, 1/6 conditions)
  - Curios issue #519: [Bug]: Minecraft crashes when launching the mod from the very beginning
  - https://github.com/TheIllusiveC4/Curios/issues/519
  - retrieved by: hybrid_c#5@r01l
  - excerpt: [issue by Leon4ikys9380] ### Minecraft Version 1.20.1 ### What happened? When I launch other mods together with Ars Nouveau, I crash immediately after loading the mods, and before that, the "save the world" screen pops up. Removing this mod, the "save the world" screen disappeared. It's very strange to me, after a few seconds Minecraft crashes. Here is the file with the report. [crash-2025-05-11_19.49.31-client.txt](https://github.com/user-attachments/files/20150776/crash-2025-05-11_19.49.31-client.txt) ### Relevant Log Outputs _No response_ [comment by TheIllusiveC4 (owner)] Did you me

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#5@r01c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#5@r01l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:shedaniel/cloth-config#162** (github_issue, 1/6 conditions)
  - cloth-config issue #162: Duplicate Cloth Class
  - https://github.com/shedaniel/cloth-config/issues/162
  - retrieved by: bm25_a#5@r01l
  - excerpt: [issue by Chaosyr] [17:57:44] [main/INFO]: Loading Minecraft 1.19 with Fabric Loader 0.14.8 [17:57:44] [ForkJoinPool-1-worker-4/WARN]: Mod journeymap uses the version 5.8.5rc2 which isn't compatible with Loader's extended semantic version format (Could not parse version number component '5rc2'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [17:57:45] [ForkJoinPool-1-worker-3/WARN]: Mod saplanting uses the version fabric-1.19-1.1.2+fix-1 which isn't compatible with Loader's extended semantic version format (Could not parse version number component

## Added by hand

(none)
