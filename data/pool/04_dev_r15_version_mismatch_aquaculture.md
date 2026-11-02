# Judging sheet 04: `r15_version_mismatch_aquaculture` (dev)

- **Category:** `version_mismatch`  |  **Culprit:** `aquaculture`  |  **Acceptable:** aquaculture
- **What was broken:** updated Aquaculture 2 to the 26.1 build (Aquaculture-26.1.2-2.9.3.jar) in a 1.21.1 pack; it requires neoforge 26.1.0.0 or above, pack has 21.1.224
- **Logs in this scenario:** r15_crash, r15_latest
- **Documents to judge:** 31

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#351** (github_issue, 5/6 conditions)
  - Aquaculture issue #351: Aquaculture 2 has failed to load correctly
  - https://github.com/TeamMetallurgy/Aquaculture/issues/351
  - retrieved by: hybrid_a#5@r15c, hybrid_b#2@r15c, hybrid_c#2@r15c, bm25_b#5@r15c, dense_b#2@r15c, hybrid_a#3@r15l, dense_b#1@r15l
  - excerpt: [issue by yeproblem] This is the Crash report log that I got and idk how to fix the problem I keep getting the same problem. ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 8/9/22, 3:48 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23158!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#391** (github_issue, 4/6 conditions)
  - Aquaculture issue #391: aquaculture 2 mod not working for my minecraft, I can't read this so I don't know what's wrong
  - https://github.com/TeamMetallurgy/Aquaculture/issues/391
  - retrieved by: hybrid_b#1@r15c, hybrid_c#1@r15c, bm25_b#1@r15c, dense_b#1@r15c, hybrid_b#1@r15l, hybrid_c#1@r15l, bm25_b#2@r15l, dense_b#3@r15l
  - excerpt: [issue by Antzoopoo] ---- Minecraft Crash Report ---- // This doesn't make any sense! Time: 3/27/23, 8:38 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.1.0-universal.jar%23188!/:?] {re:classloading,pl:runtimedistcleaner:A} at net.minecraft.client.Minecraft.la

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 3/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_b#3@r15c, hybrid_c#3@r15c, dense_b#3@r15c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#526** (github_issue, 3/6 conditions)
  - Aquaculture issue #526: fish spawn rates
  - https://github.com/TeamMetallurgy/Aquaculture/issues/526
  - retrieved by: hybrid_b#4@r15l, hybrid_c#4@r15l, dense_b#4@r15l
  - excerpt: [issue by AceAngelo98] Whatever new thing was tweaked upped the spawn rates of the fish and anytime I go near water my game crashes even if I am able to get to the kill entities command around the freezing and crashing they immediately respawn in an instant. trying to tweak the span rates myself isn't working out because I can't find where to do that so if this could be fixed I just want my cute turtles back man. another thing to add is that if I'm near a river and a pond it chooses to spawn 30-100 fish in that pond and leave the river empty. [comment by GirafiStudios (collaborator)] What Min

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 3/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_b#5@r15c, hybrid_c#5@r15c, bm25_b#4@r15c
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r15c, bm25_a#4@r15c
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#5@r15l, bm25_a#1@r15l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 2/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_a#2@r15l, bm25_a#2@r15l
  - excerpt: loading phase: Mod sodium_extra requires sodium 0.8.12-alpha.3+mc1.21.1 or above Currently, sodium is 0.6.13+mc1.21.1 Error during pre-loading phase: Mod reeses_sodium_options requires sodium 0.8.12-alpha.3 or above Currently, sodium is 0.6.13+mc1.21.1 ``` [comment by Official-V-Zer0 (none)] It may be due to the crashlog only formed after getting through the load screen hence Sodium being 0.6.13, but using 0.8.12-beta.1 is the issue [comment by jellysquid3 (member)] Your log files and crash logs do not relate to each other. The log file contains the actual error, not the crash report. Pleas

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r15c, bm25_a#3@r15c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#442** (github_issue, 2/6 conditions)
  - Aquaculture issue #442: [1.21] [Neoforge] Stone knife broken recipe tag
  - https://github.com/TeamMetallurgy/Aquaculture/issues/442
  - retrieved by: hybrid_b#2@r15l, hybrid_c#2@r15l
  - excerpt: [issue by ffuentesm] Aquaculture 2.7.0 The neoforge:cobblestone tag does not exist in the neoforge library: [Here](https://github.com/neoforged/NeoForge/tree/1.21.x/src/generated/resources/data/neoforge/tags) ![image](https://github.com/TeamMetallurgy/Aquaculture/assets/44974827/56ab68d8-69aa-4d5a-a959-1a2c6a05e119) I would suggest using the vanilla tag "minecraft:stone_tool_material" for this recipe. as it will allow Blackstone, cobblestone, and cobbled deepslate in the crafting. As it's what is used in Vanilla to make stone tools ![image](https://github.com/TeamMetallurgy/Aquacul

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_a#3@r15c, bm25_a#2@r15c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#446** (github_issue, 2/6 conditions)
  - Aquaculture issue #446: [1.21] [Neoforge] Game Crashes when I try to Fish using modded Fishing Rod 
  - https://github.com/TeamMetallurgy/Aquaculture/issues/446
  - retrieved by: hybrid_b#3@r15l, hybrid_c#3@r15l
  - excerpt: [issue by ffuentesm] Aquaculture-1.21-2.7.2.jar Neoforge: 21.0.42 Crashlog: https://pastebin.com/LptNpi3y I used an Iron Fishing Rod with a Gold Hook, and when I casted the line it crashed the game. [comment by thatkiddie (none)] Have a similar problem, a diamond fishing rod with a gold hook on 1.21, if that matters. Similar error code. [comment by GirafiStudios (collaborator)] Fixed in Dev already. Waiting for a fix in NeoForge, related to an other issue. Use NeoForge version 21.0.38 for now, or grab the latest AQ2 build from my Jenkins :) [comment by ffuentesm (none)] Yeah, can't

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#443** (github_issue, 2/6 conditions)
  - Aquaculture issue #443: [1.21] [Neoforge] update to breaking neo changes for damage events
  - https://github.com/TeamMetallurgy/Aquaculture/issues/443
  - retrieved by: hybrid_b#4@r15c, hybrid_c#4@r15c
  - excerpt: [issue by ffuentesm] ![image](https://github.com/TeamMetallurgy/Aquaculture/assets/44974827/c3a8cb98-6acf-4dde-a56b-d57da393caf5) New Neoforge 21.0.31 made the following changes to damage events: ``` import net.neoforged.neoforge.event.entity.living.LivingHurtEvent; ``` ``` import net.neoforged.neoforge.event.entity.living.LivingIncomingDamageEvent; ``` ``` public static void dodge(LivingHurtEvent event) { ``` ``` public static void dodge(LivingIncomingDamageEvent event) { ``` ``` public static void livingDamageEvent(LivingDamageEvent event) { if (!(eve

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#455** (github_issue, 2/6 conditions)
  - Aquaculture issue #455: [1.19.2] crash occurs after getting neptunium fillet knife
  - https://github.com/TeamMetallurgy/Aquaculture/issues/455
  - retrieved by: hybrid_b#5@r15l, hybrid_c#5@r15l
  - excerpt: [issue by GodPestilence] after getting the fillet knife from neptunes bounty, my game crashed and cannot successfully be relaunched ![Screenshot 2024-07-20 164508](https://github.com/user-attachments/assets/e0ba7208-6801-4b6d-b903-0b8f897baafb) i know its the fillet knife, as this occurred right after pulling from the chests inventory. [comment by GirafiStudios (collaborator)] What Aquaculture 2 and Forge/NeoForge version are you on? Also is this on a server? [comment by GodPestilence (none)] > What Aquaculture 2 and Forge/NeoForge version are you on? Also is this on a server? Forge 1.19

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r15c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#1@r15l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 1/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: bm25_b#1@r15l
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: bm25_b#2@r15c
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#344** (github_issue, 1/6 conditions)
  - Aquaculture issue #344: 1.19 Internal Exception
  - https://github.com/TeamMetallurgy/Aquaculture/issues/344
  - retrieved by: dense_b#4@r15c, dense_b#2@r15l
  - excerpt: [issue by SmaackBZ62] Heyo! I'm trying to run Aquaculture 2 on an Apex server and am running into an issue that seems to have happened in the past and I tried the solution that was used there (downloading and using the jenkins23 jar file) to no avail, this is my first time submitting an issue on Github so let me know if I need to give any other info! I'm excited to try out the mod! ![image](https://user-images.githubusercontent.com/109389771/179325817-011a28e8-f485-4e67-aff9-2f8ddb8e1980.png) [comment by antiwesley (none)] While I'm not a person who works on this, if you can provide the e

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 1/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: bm25_a#3@r15l
  - excerpt: 17 [07lip2022 18:29:10.993] [main/INFO] [cpw.mods.modlauncher.LaunchServiceHandler/MODLAUNCHER]: Launching target 'forgeclient' with arguments [--version, 1.19-forge-41.0.63, --gameDir, C:\Users\<user>\AppData\Roaming\.minecraft, --assetsDir, C:\Users\<user>\AppData\Roaming\.minecraft\assets, --uuid, <token>, --username, <player>, --assetIndex, 1.19, --accessToken, <token> truncated] [comment by BlayTheNinth (member)] Those logs are 99% OptiFine, are you sure that's the correct log? [comment by agabeluga (none)] I changed it. [comment by BlayTheNinth (member)] The Forge forum lied to you,

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: bm25_b#3@r15c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 1/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: bm25_b#3@r15l
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#516** (github_issue, 1/6 conditions)
  - Aquaculture issue #516: Missing Registry Crash
  - https://github.com/TeamMetallurgy/Aquaculture/issues/516
  - retrieved by: bm25_b#4@r15l
  - excerpt: [issue by XUrielX-Chosen] The game crashed: unexpected error Error: java.lang.NullPointerException: Registry Object not present: aquaculturedelight:roasted_tambaqui I keep getting this error when I crash. [comment by GirafiStudios (collaborator)] Wrong mod. The crash is from Aquaculture Delight

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#4@r15c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#4@r15l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#4@r15l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#5@r15c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#342** (github_issue, 1/6 conditions)
  - Aquaculture issue #342: Error message whenever I try loading my game
  - https://github.com/TeamMetallurgy/Aquaculture/issues/342
  - retrieved by: dense_b#5@r15c
  - excerpt: [issue by HICMGUN] The game crashed whilst rendering overlay Error: java.lang.NullPointerException: Registry Object not present: minecraft:empty Exit Code: -1 This is the error that keeps coming up. This mod is one of the couple that causes it. The other two are U TEAM CORE and USEFUL BACKPACKS. [crash-2022-07-08_22.45.21-client.txt](https://github.com/TeamMetallurgy/Aquaculture/files/9075743/crash-2022-07-08_22.45.21-client.txt) [comment by GirafiStudios (collaborator)] Pretty sure this is because you´re using an old version of Forge, please update to Forge version 41.0.63 (A lot of

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#350** (github_issue, 1/6 conditions)
  - Aquaculture issue #350: Crash on Startup
  - https://github.com/TeamMetallurgy/Aquaculture/issues/350
  - retrieved by: dense_b#5@r15l
  - excerpt: [issue by StarrSage] Trying to load this mod gives an error that says "Failed to load correctly java.lang.InvocationTargetException: null" [comment by GirafiStudios (collaborator)] Please provide a crash report, otherwise there is nowhere for me to even start attempting to look into the issue. [comment by StarrSage (none)] I’ve dealt with this issue on a few of my mods and have learned it has something to do with the mod needing to be updated for Forge. I am currently using the recommended 1.19 version. [comment by GirafiStudios (collaborator)] What version of Aquaculture 2 are you using?

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#5@r15l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 1/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: bm25_b#5@r15l
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

## Added by hand

(none)
