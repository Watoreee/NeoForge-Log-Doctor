# Judging sheet 01: `r01_missing_dependency_curios` (test)

- **Category:** `missing_dependency`  |  **Culprit:** `curios`  |  **Acceptable:** curios, allthearcanistgear, ars_nouveau, occultism
- **What was broken:** disabled curios in CurseForge
- **Logs in this scenario:** r01_crash, r01_latest
- **Documents to judge:** 56

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 4/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#8@r01c, hybrid_b#1@r01c, hybrid_c#2@r01c, bm25_b#3@r01c, hybrid_a#7@r01l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:TheIllusiveC4/Curios#477** (github_issue, 4/6 conditions)
  - Curios issue #477: curios "spongepowered" error and crash while loading mods
  - https://github.com/TheIllusiveC4/Curios/issues/477
  - retrieved by: hybrid_b#5@r01c, hybrid_c#5@r01c, dense_b#1@r01c, hybrid_b#2@r01l, bm25_b#4@r01l
  - excerpt: [issue by ButtWizard] **Versions** Curios: 5.11.1 Forge: 47.3.22 Minecraft: 1.20.1 **What Happened?** Curios encountered error while loading mods. **How to trigger this bug** Open game Begins loading screen Error During Mod Loading Crash Crashlog: https://pastebin.com/4W9g1hXF I haven't done this before so if I'm missing any information, let me know and I'll update asap. [comment by TheIllusiveC4 (owner)] This is a crash from Inventorio's mixin into Curios.

- [ ] **gh-issue:TheIllusiveC4/Curios#502** (github_issue, 4/6 conditions)
  - Curios issue #502: [Bug]: Mixin issue in the 1.20.1 forge development environment
  - https://github.com/TheIllusiveC4/Curios/issues/502
  - retrieved by: hybrid_b#2@r01c, dense_b#6@r01c, hybrid_b#3@r01l, hybrid_c#9@r01l, bm25_b#5@r01l, dense_b#2@r01l
  - excerpt: [issue by CuBr202] # Version minecraft_version=1.20.1 forge_version=47.4.0 curios_version=5.12.1+1.20.1 jei_version=15.20.0.106 # Description Hello! I'm new in MC mod development, and I encountered a problem when I'm making my mod based on curios api. I added the repository, mixin and dependencies in the build.gradle according to the guide: ``` plugins { id 'eclipse' id 'idea' id 'maven-publish' id 'net.minecraftforge.gradle' version '[6.0,6.2)' id 'org.spongepowered.mixin' version '[0.7,)' } version = mod_version group = mod_group_id base { archivesName = mod_id }

- [ ] **gh-issue:TheIllusiveC4/Curios#507** (github_issue, 4/6 conditions)
  - Curios issue #507: [Bug]: i am so confused
  - https://github.com/TheIllusiveC4/Curios/issues/507
  - retrieved by: hybrid_a#10@r01c, dense_b#7@r01c, hybrid_a#8@r01l, hybrid_b#4@r01l, hybrid_c#10@r01l, dense_b#6@r01l
  - excerpt: [issue by Vadewolf] ### Minecraft Version 1.21.1 ### What happened? i updated curios to 9.4.2 - 1.21.1 and my game would crash repeatedly but it would say a different mod caused the crash yet i downgraded back to 9.4.1 and the game loads so info needed please [crash-2025-04-09_10.05.01-client.txt](https://github.com/user-attachments/files/19671603/crash-2025-04-09_10.05.01-client.txt) [crash-2025-04-09_10.04.07-client.txt](https://github.com/user-attachments/files/19671604/crash-2025-04-09_10.04.07-client.txt) ### Relevant Log Outputs _No response_ [comment by TheIllusiveC4 (owner)] Unf

- [ ] **gh-issue:TheIllusiveC4/Curios#454** (github_issue, 4/6 conditions)
  - Curios issue #454: [Bug]: sided_setup crash 1.20.1 even when uninstalled?
  - https://github.com/TheIllusiveC4/Curios/issues/454
  - retrieved by: hybrid_a#9@r01l, hybrid_b#5@r01l, hybrid_c#5@r01l, dense_b#5@r01l
  - excerpt: [issue by Aceplante] ### Minecraft Version 1.20.1 ### What happened? I have been having this crash regardless of whether your mod in installed or not? ### How do you trigger this bug? unknown ### Loader Forge ### Loader Version 47.3.0 ### Mod Version latest/none ### Relevant Log Outputs ![image](https://github.com/user-attachments/assets/f759a6f7-0090-4432-9ba7-6851cac4b959) [comment by TheIllusiveC4 (owner)] It's impossible for the mod to crash if it's uninstalled, so you do have it installed in some manner. Did you check the correct folder when you wer

- [ ] **gh-issue:TheIllusiveC4/Curios#472** (github_issue, 4/6 conditions)
  - Curios issue #472: Crash Report
  - https://github.com/TheIllusiveC4/Curios/issues/472
  - retrieved by: hybrid_b#8@r01c, hybrid_c#8@r01c, bm25_b#8@r01l, dense_b#8@r01l
  - excerpt: [issue by Make527] I have tried to load it in different versions and i keep getting the same error. org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered that pops up when i get into minecraft which sucks because its in my custom pack and this is one of my favorite go to mods. If you could fix it that would be awesome. [comment by TheIllusiveC4 (owner)] I would need the whole crash report to decipher the cause, but most likely your issue may be coming from either Tiered or Inventorio. Please check if you have either of these

- [ ] **gh-issue:TheIllusiveC4/Curios#159** (github_issue, 3/6 conditions)
  - Curios issue #159: Curios Menu won´t open when clicking the icon
  - https://github.com/TheIllusiveC4/Curios/issues/159
  - retrieved by: dense_b#8@r01c, hybrid_b#1@r01l, hybrid_c#2@r01l, dense_b#1@r01l
  - excerpt: [issue by jaz0894] #### Versions (Be specific, do not write "latest"): * Curios: curios-forge-1.16.5-4.0.5.2 * Forge/Fabric: forge-1.16.5-36.2.0.jar <html> <body> When I click on the curios Icon of curios nothing happens, I also have the mod Sofisticated Backpacks and when Curios is bugged I cannot open backpack inventory. </body> </html> <html> <body> -- </body> </html> <html> <body> forge-1.16.5-36.2.0.jar -- </body> </html> #### Observed Behavior: #### Expected Behavior: #### Steps to Reproduce: 1. 2. 3. ... Crash Log: Please use

- [ ] **gh-issue:TheIllusiveC4/Curios#473** (github_issue, 3/6 conditions)
  - Curios issue #473: game crashes on start up when Ars Nouveau is installed
  - https://github.com/TheIllusiveC4/Curios/issues/473
  - retrieved by: hybrid_c#1@r01c, hybrid_b#7@r01l, hybrid_c#1@r01l, bm25_b#3@r01l
  - excerpt: [issue by shoezons] i noticed that Curios is very not happy whenever Ars Nouveau is installed. i don't fully know whats causing it to happen. i need both mods since they are crucial for my modpack. here is the crash log if anyone could help me out with this. would be greatly appreciated. [latest.log](https://github.com/user-attachments/files/18428962/latest.log) [comment by TheIllusiveC4 (owner)] Duplicate of https://github.com/TheIllusiveC4/Curios/issues/344 This is not an issue with Ars Nouveau, but with the Tiered mod.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 3/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_b#4@r01c, hybrid_a#2@r01l, bm25_a#1@r01l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r01c, hybrid_c#4@r01c, bm25_b#5@r01c, hybrid_b#6@r01l, hybrid_c#3@r01l, bm25_b#1@r01l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:TheIllusiveC4/Curios#619** (github_issue, 3/6 conditions)
  - Curios issue #619: [Bug]: Failure message: An uncaught parallel processing error has occurred. java.lang.NoClassDefFoundError: net/hazen/hazentouvelib/Items/Curios/WingCurioRenderer
  - https://github.com/TheIllusiveC4/Curios/issues/619
  - retrieved by: hybrid_b#4@r01c, hybrid_c#3@r01c, dense_b#2@r01c, dense_b#9@r01l
  - excerpt: [issue by LordOfCinders] ### Minecraft Version 1.21.1 ### What happened? When I was logging onto Minecraft (NeoForge) - 1.21.1 - I had recently updated my Curse Forge with alongside with 7 other mods that depend on Curios API, thinking it was all good, then when I log into Minecraft itself, the error code shows up, suddenly it was working the day before, then now suddenly the game stopped working with the error code. As Curios API, is not only the mod has been affected by the error, but other mods too, such as, ("Ace's Spell Utils, Charm of Undying (Fabric/Forge/Quilt), Crystal Chronicles -

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 3/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: hybrid_a#9@r01c, bm25_b#8@r01c, bm25_a#2@r01l
  - excerpt: [issue by MaserPlay] I cannot open minecraft with mods: > Caused by: java.lang.UnsupportedOperationException: A mod tried to access the state neighbor table directly. Please report this at https://github.com/malte0811/FerriteCore/issues. As a temporary workaround you can enable "populateNeighborTable" in the FerriteCore config Minecraft log: ``` MultiMC version: 0.7.0-3826 Launched instance in online mode authserver.mojang.com resolves to: [13.33.243.103, 13.33.243.122, 13.33.243.48, 13.33.243.49] session.minecraft.net resolves to: [13.107.246.67, 13.107.213.67]

- [ ] **gh-issue:TheIllusiveC4/Curios#478** (github_issue, 3/6 conditions)
  - Curios issue #478: Game Crash
  - https://github.com/TheIllusiveC4/Curios/issues/478
  - retrieved by: dense_b#5@r01c, hybrid_b#9@r01l, hybrid_c#8@r01l, dense_b#3@r01l
  - excerpt: github.com/notifications/unsubscribe-auth/AJS7C6RCZFQNMIS66ORFLI32QQ2CTAVCNFSM6AAAAABWYKVQGKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDMNRXHAZDMOBXG4> > . > You are receiving this because you authored the thread.Message ID: > ***@***.***> > [image: TheIllusiveC4]*TheIllusiveC4* left a comment > (TheIllusiveC4/Curios#478) > <https://github.com/TheIllusiveC4/Curios/issues/478#issuecomment-2667826877> > > If it's a mod that uses Curios, and not Curios itself, then there isn't > much I can do on my end for this. Does your friend have exactly the same > mods on their client as the server d

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 3/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#3@r01c, hybrid_b#6@r01c, bm25_b#6@r01c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:TheIllusiveC4/Curios#492** (github_issue, 3/6 conditions)
  - Curios issue #492: Incompatibility Between Curios API and Inventorio Mod Causing Crash in Minecraft 1.20.1
  - https://github.com/TheIllusiveC4/Curios/issues/492
  - retrieved by: hybrid_a#10@r01l, hybrid_b#10@r01l, bm25_a#8@r01l
  - excerpt: [issue by icram0719] There is an incompatibility between the Curios API and the Inventorio mod that results in a crash when both are installed in Minecraft 1.20.1. This prevents the game from functioning properly and affects players using these mods together. Details: Crash Occurrence: The game crashes during the common_setup event phase when both Curios and Inventorio are loaded. Environment: Minecraft Version: 1.20.1 Curios Version: curios-forge-5.12.1+1.20.1.jar Inventorio Version: inventorio-mc1.20.1-forge-v1.10.3.jar The crash generates an error related to the Curios API, and the game f

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r01c, bm25_a#3@r01c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:TheIllusiveC4/Curios#455** (github_issue, 2/6 conditions)
  - Curios issue #455: [Bug]: Curious API encountered am error during the sided_setup event phase
  - https://github.com/TheIllusiveC4/Curios/issues/455
  - retrieved by: hybrid_a#1@r01l, bm25_a#7@r01l
  - excerpt: [issue by Silverbolt666] ### Minecraft Version 1.20.1 ### What happened? **Curious API encountered am error during the sided_setup event phase** org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError; An unexpected critical error was encountered ### How do you trigger this bug? 1. Update to version curios-forge-5.11.0+1.20.1 2. Start the game in a custom moded setting ### Loader Forge ### Loader Version 47.3.10 ### Mod Version curios-forge-5.11.0+1.20.1 ### Relevant Log Outputs [Curious_latest.log](https://github.com/user-attachments/files/17668260/Curious_

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 2/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_c#9@r01c, bm25_b#1@r01c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r01c, bm25_a#2@r01c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#3@r01l, bm25_a#3@r01l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:TheIllusiveC4/Curios#500** (github_issue, 2/6 conditions)
  - Curios issue #500: Curious error during sided_setup
  - https://github.com/TheIllusiveC4/Curios/issues/500
  - retrieved by: hybrid_c#10@r01c, dense_b#4@r01c
  - excerpt: [issue by ImNamzz] Currently Forge 1.20.1 I encounter this while loading with few mods, below is the log file: [crash-2025-03-26_02.46.51-fml.txt](https://github.com/user-attachments/files/19455692/crash-2025-03-26_02.46.51-fml.txt) [comment by TheIllusiveC4 (owner)] This is a crash from the Tiered mod.

- [ ] **gh-issue:TheIllusiveC4/Curios#519** (github_issue, 2/6 conditions)
  - Curios issue #519: [Bug]: Minecraft crashes when launching the mod from the very beginning
  - https://github.com/TheIllusiveC4/Curios/issues/519
  - retrieved by: hybrid_c#4@r01l, bm25_a#5@r01l
  - excerpt: [issue by Leon4ikys9380] ### Minecraft Version 1.20.1 ### What happened? When I launch other mods together with Ars Nouveau, I crash immediately after loading the mods, and before that, the "save the world" screen pops up. Removing this mod, the "save the world" screen disappeared. It's very strange to me, after a few seconds Minecraft crashes. Here is the file with the report. [crash-2025-05-11_19.49.31-client.txt](https://github.com/user-attachments/files/20150776/crash-2025-05-11_19.49.31-client.txt) ### Relevant Log Outputs _No response_ [comment by TheIllusiveC4 (owner)] Did you me

- [ ] **gh-issue:TheIllusiveC4/Curios#456** (github_issue, 2/6 conditions)
  - Curios issue #456: Error creative inventory
  - https://github.com/TheIllusiveC4/Curios/issues/456
  - retrieved by: hybrid_a#5@r01c, hybrid_a#5@r01l, dense_b#7@r01l
  - excerpt: [issue by Sebz102030] ### Minecraft Version 1.20.6 ### What happened? On server MohistMC curios API throws error when modern fix is present Mod list: ![Screenshot_20241110_194256_Termux](https://github.com/user-attachments/assets/ad0e7840-a59d-48f5-84c5-2290ccc31b4e) ### How do you trigger this bug? Install MohistMC on java 17 Install all mods from modlist above Run server Join server Go in creative and open inventory ### Loader Forge ### Loader Version 47.3.11 ### Mod Version 5.11.0 ### Relevant Log Outputs ---- Minecraft Crash Report ---- // Don't do that. Time: 20

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 2/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: bm25_b#9@r01c, hybrid_a#6@r01l
  - excerpt: lyServiceDiscovery) Found 2 early service jars (out of 117) in 21ms [23:03:14] [main/INFO] (FMLLoader) Loading FML Early Services: [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/earlydisplay/11.0.5/b2edeab4008c91772d61f8f98a5253a09a4e890d/earlydisplay-11.0.5.jar [23:03:14] [main/INFO] (FMLLoader) - C:/Users/<user>/.gradle/caches/modules-2/files-2.1/net.neoforged.fancymodloader/loader/11.0.5/3477e70d79fe8cd06962749f24e64f01edda3bb3/loader-11.0.5.jar [23:03:14] [main/INFO] (ImmediateWindowHandler) Loading ImmediateWindowProv

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 2/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_b#8@r01l, hybrid_c#6@r01l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 2/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_b#7@r01c, hybrid_c#7@r01c
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 2/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: hybrid_b#9@r01c, bm25_b#9@r01l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r01c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#2@r01c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#2@r01l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:TheIllusiveC4/Curios#509** (github_issue, 1/6 conditions)
  - Curios issue #509: [Bug]: Reforged (formerly Tiered) compatibility error
  - https://github.com/TheIllusiveC4/Curios/issues/509
  - retrieved by: dense_b#3@r01c, dense_b#10@r01l
  - excerpt: happened? > > This has been reported to the Reforged dev team. I just want to make sure that this is not an issue on your end. > > **How to copy this issue:** **1.** Run the most recent version of 1.20.1 of the following mods: > > * [Reforged (formerly Tiered)](https://www.curseforge.com/minecraft/mc-mods/tiered) > > * [Curios API (Forge/NeoForge)](https://www.curseforge.com/minecraft/mc-mods/curios) > > * [UnionLib](https://www.curseforge.com/minecraft/mc-mods/unionlibl) > > > **2.** Run Minecraft I with the said mods with your pilfered launcher. I tested this with Cursefor

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#4@r01c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TheIllusiveC4/Curios#487** (github_issue, 1/6 conditions)
  - Curios issue #487: Curios API encountered an error during the common_setup event phase
  - https://github.com/TheIllusiveC4/Curios/issues/487
  - retrieved by: dense_b#9@r01c, dense_b#4@r01l
  - excerpt: [issue by kun4x] Minecraft Version: 1.20.1 Curios API Version: curios-forge-5.12.1+1.20.1 Forge Version: 47.3.33 Every time I launch the game with curios enabled it shows with a crash screen and the message shown in the title, I have no idea how to fix this. Log: https://mclo.gs/kesuo5k Mod List: https://pastebin.com/9ZHjuVmd ![Image](https://github.com/user-attachments/assets/c57ba1ad-506f-4293-b7b0-c5cbcf0629b9) [comment by Mo9713 (none)] I also get this error on the new update. 5.12.0 version has no issue for me [comment by TheIllusiveC4 (owner)] This crash is coming from one of the mi

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#4@r01l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 1/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#4@r01c
  - excerpt: 9.2, --fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppDat

- [ ] **gh-issue:shedaniel/cloth-config#162** (github_issue, 1/6 conditions)
  - cloth-config issue #162: Duplicate Cloth Class
  - https://github.com/shedaniel/cloth-config/issues/162
  - retrieved by: bm25_a#4@r01l
  - excerpt: [issue by Chaosyr] [17:57:44] [main/INFO]: Loading Minecraft 1.19 with Fabric Loader 0.14.8 [17:57:44] [ForkJoinPool-1-worker-4/WARN]: Mod journeymap uses the version 5.8.5rc2 which isn't compatible with Loader's extended semantic version format (Could not parse version number component '5rc2'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [17:57:45] [ForkJoinPool-1-worker-3/WARN]: Mod saplanting uses the version fabric-1.19-1.1.2+fix-1 which isn't compatible with Loader's extended semantic version format (Could not parse version number component

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#5@r01c
  - excerpt: [issue by Nono2199] ### Description Every time I click the Tree fertilizer on a random sapling, my game will "lag" like in multiplayer (not stuttering, FPS is smoothly fine), such as 1) nothing opens/places when right-clicking, and 2) no block breaking when pressing left-click . After like 10-20 seconds, the tree pops up and things return normal. ### Game Log https://mclo.gs/QF0dNBo ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 1a1a9a2819b4f89f78caec41b55ed8cb222fa24b Ponder Version: 1.0.92 Forge Version: 47.4.0 Minecra

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#6@r01c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#6@r01l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#6@r01c
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 1/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: bm25_a#6@r01l
  - excerpt: fml.forgeGroup, net.minecraftforge, --fml.mcpVersion, 20230612.114412] [19:57:10] [main/INFO]: ModLauncher 10.0.9+10.0.9+main.dcd20f30 starting: java version 17.0.8 by Microsoft; OS Windows 10 arch amd64 version 10.0 [19:57:10] [main/INFO]: Loading ImmediateWindowProvider fmlearlywindow [19:57:11] [main/INFO]: Trying GL version 4.6 [19:57:11] [main/INFO]: Requested GL version 4.6 got version 4.6 [19:57:11] [main/INFO]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/Twitch/Minecraft/Install/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%23100!/ Service=M

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 1/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: hybrid_c#6@r01c
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#7@r01c
  - excerpt: Mob Farm Remastered: 1.5.1-1.21 Architectury: 13.0.8 Ragdoll Reactions: 0.7.0 Create Offroad: 1.3.0 ``` </details> <details> <summary>Server Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 9 total; -Xmx21793M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX

- [ ] **gh-issue:TheIllusiveC4/Curios#442** (github_issue, 1/6 conditions)
  - Curios issue #442: [Bug]: Toggle visibility JEI
  - https://github.com/TheIllusiveC4/Curios/issues/442
  - retrieved by: hybrid_c#7@r01l
  - excerpt: [issue by NikaDLaw] ### Minecraft Version 1.20.1 ### What happened? With Jei installed I cant toggle the visibility of the artifacts that i have in the curious inventory for them to not be seen in my body, it would hide jei's gui instead ### How do you trigger this bug? 1.Open curious inventory 2.Toggle the visibility of an artifact 3. ... ### Loader NeoForge ### Loader Version Neoforge 21.0.167 ### Mod Version Curios-neoForge-9.0.8+1.21.jar ### Relevant Log Outputs _No response_ [comment by TheIllusiveC4 (owner)] It looks like this is an issue report for 1.21, this repos

- [ ] **gh-issue:TheIllusiveC4/Curios#479** (github_issue, 1/6 conditions)
  - Curios issue #479: Glitch with multiple slots using the /add command
  - https://github.com/TheIllusiveC4/Curios/issues/479
  - retrieved by: bm25_b#7@r01l
  - excerpt: [issue by johnfromstatefarm] ### **Workaround found: Avoid using SHIFT+CLICK to place items into Curios slots. Instead, drag and drop them directly.** Using the `/curios add` command causes existing items to disappear, duplicate, or in very rare cases permanently deleted. I've tried altering the column count and maximum items per page in the configuration file without success. The glitch typically occurs after adding 5-10 slots, and happens earlier with the feet slot. I am using the following mods that requires or make use of the API: - **Baubles Heart Canisters** - **Ender's Cataclysm** -

- [ ] **gh-issue:bernie-g/geckolib#666** (github_issue, 1/6 conditions)
  - geckolib issue #666: geckolib-forge-1.21.4-4.8 causing Minecraft 1.24.1 to Crash
  - https://github.com/bernie-g/geckolib/issues/666
  - retrieved by: bm25_b#7@r01c
  - excerpt: [issue by ochoafabian18] Hello, this mod is causing an error code and will not load Minecraft, I even tested this with no other mods running, and still causing it to crash, here is the crash log. --- Minecraft Crash Report ---- // There are four lights! Time: 2024-12-20 11:39:09 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/net.minecraftforge.forge@54.0.6/net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:49) ~[forge-1.21.4-54.0.6-universal.jar:?] at TRANSFORMER/net.minecraft

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: hybrid_a#7@r01c
  - excerpt: .76, 108.156.211.10] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instances/1.19/.minecraft Java path is: /usr/lib/jvm/java-17-openjdk-amd64/bin/java Checking Java version... Java is version 17.0.4, using 64-bit architecture, from Private Build. Intel(R) Pentium(R) Silver N5000 CPU @ 1.10GHz Intel Corporation UHD Graphics 605 (rev 03) DeviceName: Onboard - Video Subsystem: Dell UHD Graphics 605 OpenGL version string: 4.6 (Compatibility Profile) Mesa 21

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: bm25_a#8@r01c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#9@r01c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:bernie-g/geckolib#850** (github_issue, 1/6 conditions)
  - geckolib issue #850: Animation Parsing Error
  - https://github.com/bernie-g/geckolib/issues/850
  - retrieved by: bm25_a#9@r01l
  - excerpt: [issue by Filan-glitch] GeckoLib V4.8.4 NeoForge 21.1.228 MC1.21.1 Error Logs: [05May2026 11:30:01.258] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.258] [Worker-Main-5/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.261] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.290] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: attack sadly no further information in logs... [comment by Tslat (collaborator)] Provide the mod jar so I can test it I can't do anything with this [comment

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 1/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: bm25_a#10@r01c
  - excerpt: [issue by Findingmyplace] ### Description For some reason when I try to connect cogwheels in this modpack it for some reason just breaks anywhere between 1 and 10 cogwheels in the network. Here is a video of it happening. https://www.youtube.com/watch?v=hGHgzQDOHG0 ### Game Log https://mclo.gs/OLcoLdD ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Bac

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: hybrid_b#10@r01c
  - excerpt: $registerEventHandlers$2(BetterModsButtonNeoForgeClient.java:53) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.ConsumerEventHandler.invoke(ConsumerEventHandler.java:26) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:315) at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.gui.screens.Screen.init [... truncated] [comment by P3pp3rF1y (owner)] I don't see anything related to sophisticated in this crash log other than the fact that it's one of the mods on the list.

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#10@r01l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#10@r01l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: dense_b#10@r01c
  - excerpt: [issue by ToxinZangoose] Hello, I have recently been trying to diagnose an issue with my modpack and the log files point to this mod when I try launching. When launching, owo lib tries to load shaders for Spectrum which is not supported for NeoForge. Below is the log file for the crash I've been experiencing since I've tried removing 19 mods from this pack. https://mclo.gs/wDKVGtH Thank you for your time! [comment by Dragon-Seeker (member)] ``` [02Nov2024 11:04:06.859] [modloading-worker-0/ERROR] [io.github.lightman314.lightmanscurrency.LightmansCurrency/]: Error setting up C

- [ ] **neoforge-docs:user/docs/server** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Installing a NeoForge Server
  - https://docs.neoforged.net/user/docs/server/
  - retrieved by: bm25_b#10@r01c
  - excerpt: import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; # Installing a NeoForge Server _This article assumes that you [have the correct version of Java installed][java]._ ## Installing <Tabs defaultValue="unix"> <TabItem value="unix" label="UNIX-like (Linux, macOS, FreeBSD, etc.)"> Running a NeoForge server on Linux, macOS, BSD, or any UNIX-like OS assumes your ability to use basic terminal commands. - Navigate to the folder you'd like to install the server into. - Download the installer `.jar` from the Maven using the following command (swap out version numbers and `-bet

## Added by hand

(none)
