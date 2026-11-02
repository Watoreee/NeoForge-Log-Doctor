# Judging sheet 17: `r13_missing_dependency_extendedae` (dev)

- **Category:** `missing_dependency`  |  **Culprit:** `extendedae`  |  **Acceptable:** extendedae
- **What was broken:** ExtendedAE and MEGA Cells were left auto-disabled after the AE2 run; the pack's KubeJS startup script ExtendedAE/InfinityCells.js failed with Unknown type 'kubejs:custom_infinity_cell'
- **Logs in this scenario:** r13_latest
- **Documents to judge:** 40

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 4/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_b#1@r13l, hybrid_c#3@r13l, bm25_b#4@r13l, dense_b#1@r13l
  - excerpt: some sort. [comment by RubixDev (none)] I get the same error with kff 5.9.0 and Minecraft 1.20.6 with NeoForge 20.6.139, and I don't have the `atomicfu` plugin configured (at least not manually). I have not yet found a fix for this. Of note is also, that building the mod and using it in a normal Minecraft instance works fine, it's only broken in the dev environment.

- [ ] **gh-issue:TwelveIterations/Waystones#1118** (github_issue, 4/6 conditions)
  - Waystones issue #1118: Waystones mod looks for a missing KumaAPI and crashes when clicking on any waystone
  - https://github.com/TwelveIterations/Waystones/issues/1118
  - retrieved by: hybrid_b#2@r13l, hybrid_c#5@r13l, bm25_b#2@r13l, dense_b#8@r13l
  - excerpt: knot//net.minecraft.client.main.Main.main(Main.java:250) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:514) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:72) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(Unknown Source) at java.base/java.lang.reflect.Method.invoke(Unknown Source) at com.modrinth.theseus.MinecraftLaunch.relaunch(MinecraftLaunch.java:63) at com.modrinth.theseus.MinecraftLaunch.main(MinecraftLaunch.java:28) C

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#3@r13l, hybrid_c#1@r13l, bm25_b#1@r13l
  - excerpt: mixin configuration file. | `config="examplemod.mixins.json"` | ### Dependency Configurations Mods can specify their dependencies, which are checked by NeoForge before loading the mods. These configurations are created using the [array of tables][array] `[[dependencies.<modid>]]`, where `modid` is the identifier of the mod that consumes the dependency. | Property | Type | Default | Description

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 3/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_b#7@r13l, hybrid_c#2@r13l, dense_b#10@r13l
  - excerpt: [issue by goldswim] ### Describe the bug Hello, Version: Minecraft 1.21.1 NeoForge 21.1.234 Applied Energistics 2 19.2.17 ExpandedAE 2.1.1 ExtendedAE 2.2.33 AdvancedAE 1.6.11 Here's the log causing the disconnect: Screen is missing required image: toolbox at appeng.client.gui.implementations.PatternProviderScreen.handler$jal000$expandedae$init ### How to reproduce the bug it happens when i try to access any pattern provider's UI by right-clicking it. ### Expected behavior Display pattern provider's UI ### Additional details _No response_ ### Which minecraft version are you using?

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 3/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: hybrid_b#4@r13l, hybrid_c#4@r13l, dense_b#5@r13l
  - excerpt: [issue by Official-V-Zer0] ### Bug Description So I am working on a new pack after encountering this issue once before, And Sodium extra and Reese's settings needed the most recent update so you see. No supplementaries. Funnily used to run fine kinda with the alphas quote the crashlog: java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.1+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.1+mc1.21.1-mod.jar%23337!/:?] {re:mixin,re:classloading} ###

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 2/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: hybrid_a#7@r13l, bm25_a#1@r13l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#9021** (github_issue, 2/6 conditions)
  - Applied-Energistics-2 issue #9021: Item duplication when AE2 interface/storage bus pushes more than 8 items into Kaleidoscope Cookery's Millstone
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/9021
  - retrieved by: hybrid_a#9@r13l, bm25_a#2@r13l
  - excerpt: [issue by Arc149] ### Describe the bug AE2 version is 19.2.18,Kaleidoscope Cookery is 1.6.0,Minecraft is 1.21.1 neoforge 21.1.250.When I want let the ore in the ME Interface use ME Storage Bus to the millstone sometime will make a bug,if I take in ME Interface is more 8(8 is millstone's max capacity),so the bug will come,in the ME Interface ore will keep a same number,if I take number is at 8 lower the bug will not have. ### How to reproduce the bug When I want let the ore in the ME Interface use ME Storage Bus to the millstone sometime will make a bug,if I take in ME Interface is more 8

- [ ] **gh-issue:architectury/architectury-api#528** (github_issue, 2/6 conditions)
  - architectury-api issue #528: Error: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/528
  - retrieved by: hybrid_b#9@r13l, dense_b#2@r13l
  - excerpt: to dig into it a bit and sadly "Mo´ Structures" was the mod using that configfile and causing the crash. It´s a bit dissapointing not to be able to use the mod (liked it very much) but at least i can play again. Again, thank you very much for your patience and helping me out :-) [comment by SirTwsted (none)] ![Screenshot_308](https://github.com/user-attachments/assets/285348a0-af89-42a0-ad0a-6fa574b0772e) [crash-2024-07-19_08.55.05-client.txt](https://github.com/user-attachments/files/16312649/crash-2024-07-19_08.55.05-client.txt) Using MC v1.21 and on NEOForge v21.0.109 . [comme

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 2/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: hybrid_b#10@r13l, dense_b#3@r13l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 2/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: bm25_b#9@r13l, dense_b#6@r13l
  - excerpt: [issue by gamebastian-creator] ### Bug Description Hello, I am experiencing a crash when launching Minecraft 1.21.1 on NeoForge with my modpack. I use Sable for Aeronautics, and Sable requires a newer version of Sodium. However, after installing the required Sodium version, the game crashes during startup. Environment: * Minecraft 1.21.1 * NeoForge 21.1.233 * Sable 2.0.3 * Aeronautics * Sodium 0.8.12-alpha.2+ (required by Sable) Because Sable requires this version of Sodium, removing Sodium is not a viable workaround for my setup. Could you please help determine whether this is a known

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 2/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_b#6@r13l, hybrid_c#10@r13l
  - excerpt: :\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\javafmllanguage\1.19.2-43.4.20\javafmllanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecraftforge\lowcodelanguage\1.19.2-43.4.20\lowcodelanguage-1.19.2-43.4.20.jar is missing mods.toml file [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\net\minecr

- [ ] **gh-issue:wisp-forest/owo-lib#405** (github_issue, 2/6 conditions)
  - owo-lib issue #405: NeoForge 1.21.1 - Crash with Accessories and owo-lib
  - https://github.com/wisp-forest/owo-lib/issues/405
  - retrieved by: hybrid_c#6@r13l, bm25_b#7@r13l
  - excerpt: [issue by muggleorwizard] Install Accessories via curseforge, owo-lib will automatically install as a dependency. Load game, open world or create new world, game will crash when loading reaches 100% Crash error is: java.lang.NoClassDefFoundError: net/fabricmc/fabric/api/networking/v1/PlayerLookup Game crashes with owo-lib 0.12.15.1-beta.6+1.21 (latest version for NeoForge 1.21.1). Does not crash with owo-lib 0.12.15.1-beta.3+1.21 (previous version) Latest.log: https://gnomebot.dev/paste/mclogs/5FHQNvc Debug.log: https://gnomebot.dev/paste/mclogs/gMpJdRU Crash Report: https://gnomebot.dev/past

- [ ] **gh-issue:bernie-g/geckolib#684** (github_issue, 2/6 conditions)
  - geckolib issue #684: I crashed while running the rundata command while developing the 1.20.1forge module
  - https://github.com/bernie-g/geckolib/issues/684
  - retrieved by: hybrid_a#8@r13l, hybrid_c#8@r13l
  - excerpt: [issue by Zhixi-mc] The code I wrote should be fine, at least Idea did not report any errors, and there were no errors before adding this dependency. From the error message, the main error is java. lang. NoSuchMethodError: net.minecraft.client.Minecraft net.minecraft.client.Minecraft.m_91087_()'， Below, I will provide you with the complete error message, configuration file, and main class `content: build.gradle:`plugins { id 'eclipse' id 'idea' id 'maven-publish' id 'net.minecraftforge.gradle' version '[6.0,6.2)' } version = mod_version group = mod_group_id base { arc

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#1@r13l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#2@r13l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:CaffeineMC/sodium#3013** (github_issue, 1/6 conditions)
  - sodium issue #3013: Texture Bleeding with Custom Models using half pixel translations
  - https://github.com/CaffeineMC/sodium/issues/3013
  - retrieved by: hybrid_a#3@r13l
  - excerpt: the texture of weeping vines to plain orange and the texture bleeding is visible like seen in the image above. ### Log File [20:01:14] [main/INFO]: Loading Minecraft 1.21.4 with Fabric Loader 0.16.9 [20:01:14] [main/INFO]: Loading 11 mods: - fabricloader 0.16.9 \-- mixinextras 0.4.1 - java 21 - minecraft 1.21.4 - sodium 0.6.6+mc1.21.4 |-- fabric-api-base 0.4.54+b47eab6b04 |-- fabric-block-view-api-v2 1.0.19+7feeb73304 |-- fabric-renderer-api-v1 5.0.2+84404cdd04 |-- fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb733

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 1/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: bm25_a#3@r13l
  - excerpt: [issue by jrn907-lab] ### Description they are invisible once turned into a physics object ### Game Log USERNAME}\AppData\Roaming\ModrinthApp\profiles\Create_ Plane and Simple\dynamic-resource-pack-cache\amendments-generated_pack in 13.41 ms [17:56:09] [Worker-ResourceReload-0/INFO] [Moonlight/]: Regenerating Dynamic CLIENT_RESOURCES Resources Provider [moonlight:dynamic_resources], requested by strategy REGEN_ON_EVERY_RELOAD [17:56:09] [Worker-ResourceReload-0/INFO] [Moonlight/]: Generated runtime CLIENT_RESOURCES for pack moonlight:dynamic_resources in 629.7 ?s [17:56:09] [Worker-Resource

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#3@r13l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:architectury/architectury-api#195** (github_issue, 1/6 conditions)
  - architectury-api issue #195: [1.18.1] Crashes when using architectury and optifablic together.
  - https://github.com/architectury/architectury-api/issues/195
  - retrieved by: bm25_a#4@r13l
  - excerpt: [issue by mqnowa] Crashes when using architectury and optifablic together. #### minecraft version > Minecraft 1.18.1 > fablic 0.13.1 #### installd mods > fablic api 0.46.4+1.18 > optifablic 1.12.10 > optifine HD U H4 > Architectury 3.4.17 If this is a bug caused by using the unofficial launcher, multi MC, please close it. #### log ``` MultiMC version: 0.6.14-3001 Launched instance in online mode authserver.mojang.com resolves to: [99.86.219.75] session.minecraft.net resolves to: [34.231.157.213, 52.1.29.34, 18.210.95.126] textures.minecraft.net resolve

- [ ] **gh-issue:embeddedt/ModernFix#535** (github_issue, 1/6 conditions)
  - ModernFix issue #535: Caught exception in thread: java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab (net.minecraft.client.gui.tab.Tab)
  - https://github.com/embeddedt/ModernFix/issues/535
  - retrieved by: dense_b#4@r13l
  - excerpt: bricmc.loader.impl.launch.knot.KnotClassLoader.loadClass(KnotClassLoader.java:119) ~[fabric-loader-0.16.10.jar:?] at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:528) ~[?:?] at java.base/java.lang.ClassLoader.defineClass1(Native Method) ~[?:?] at java.base/java.lang.ClassLoader.defineClass(ClassLoader.java:1026) ~[?:?] at java.base/java.security.SecureClassLoader.defineClass(SecureClassLoader.java:150) ~[?:?] at net.fabricmc.loader.impl.launch.knot.KnotClassLoader.defineClassFwd(KnotClassLoader.java:160) ~[fabric-loader-0.16.10.jar:?]

- [ ] **gh-issue:malte0811/FerriteCore#90** (github_issue, 1/6 conditions)
  - FerriteCore issue #90: Crash On startup in 1.19
  - https://github.com/malte0811/FerriteCore/issues/90
  - retrieved by: hybrid_a#4@r13l
  - excerpt: [issue by Andaros210] Here's the log copy and paste. MultiMC version: 0.6.16-3430 Launched instance in online mode authserver.mojang.com resolves to: [108.138.149.51, 108.138.149.48, 108.138.149.65, 108.138.149.64] session.minecraft.net resolves to: [107.20.118.247, 52.72.238.122, 54.172.106.247] textures.minecraft.net resolves to: [108.156.211.10, 108.156.211.34, 108.156.211.26, 108.156.211.76] api.mojang.com resolves to: [108.138.167.43, 108.138.167.34, 108.138.167.17, 108.138.167.22] Minecraft folder is: /home/<user>/.local/share/multimc/instanc

- [ ] **gh-issue:TheIllusiveC4/Curios#521** (github_issue, 1/6 conditions)
  - Curios issue #521: [Bug]: Incorrect slot config syntax corrupts all save games and crashes new world creation
  - https://github.com/TheIllusiveC4/Curios/issues/521
  - retrieved by: hybrid_a#5@r13l
  - excerpt: assets/32453c00-e99b-43e8-b642-7f9e48b5d845) ![Image](https://github.com/user-attachments/assets/2ac94a63-a0d0-4a48-a423-be214ae18b20) **Crash log** [crash-2025-05-20_15.21.58-client.txt](https://github.com/user-attachments/files/20348587/crash-2025-05-20_15.21.58-client.txt) ### Relevant Log Outputs Error when trying to load the world with incorrect slot syntax: ```java [15:29:17] [Render thread/WARN] [ModernFix/]: Initial datapack load took 312.0 ms [15:29:17] [Render thread/WARN] [minecraft/WorldOpenFlows]: Failed to load level data or datapacks, can't proceed with server load java.util.

- [ ] **gh-issue:architectury/architectury-api#551** (github_issue, 1/6 conditions)
  - architectury-api issue #551: IClientFluidTypeExtension for Neo
  - https://github.com/architectury/architectury-api/issues/551
  - retrieved by: hybrid_b#5@r13l
  - excerpt: that break due to the texture being null incorrectly. If it is up to the modder to register these extensions, you may want to put in some safe guards to inform a dev that they are missing at the very least to try to mitigate the number that slip through. Example of a mod that has recently come by my issue tracker: https://github.com/st0x0ef/stellaris/issues/17 [comment by MaxNeedsSnacks (member)] I haven't worked on Architectury in a hot minute, but from a cursory glance I found out that the mod doesn't seem to actually register fluid types? This should probably additionally be looked at f

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#5@r13l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:wisp-forest/owo-lib#504** (github_issue, 1/6 conditions)
  - owo-lib issue #504: EdmOps throws a NullPointerException on null input instead of returning a DataResult error
  - https://github.com/wisp-forest/owo-lib/issues/504
  - retrieved by: bm25_a#5@r13l
  - excerpt: [issue by neonishere] ### Versions - Minecraft 1.21.1, NeoForge 21.1.248 - owo-lib 0.12.15.5-beta.1+1.21 - Accessories 1.1.0-beta.53+1.21.1 - Cold Sweat 2.4.3.1 ### What happens Putting armor that was insulated at Cold Sweat's sewing table into an Accessories cosmetic armor slot disconnects the player. The item stays in the slot, so the same packet is sent on every login and the player cannot rejoin until the save is edited. reports of the same crash: - wisp-forest/accessories#418 - Momo-Softworks/Cold-Sweat#605 - Momo-Softworks/Cold-Sweat#683 - Momo-Softworks/Cold-Sweat#699 ``` Interna

- [ ] **gh-issue:architectury/architectury-api#736** (github_issue, 1/6 conditions)
  - architectury-api issue #736: crash when create new world
  - https://github.com/architectury/architectury-api/issues/736
  - retrieved by: bm25_a#6@r13l
  - excerpt: shut down the game with console... and there is no crash report generated. and in the latest.log: ``` [297��2026 22:48:12.871] [Render thread/INFO] [KubeJS Tweaks/]: Testing [297��2026 22:48:12.881] [Render thread/WARN] [KubeJS Server/]: Due to the way Minecraft resource loading works, KubeJS' server.log may not contain everything that happened in your server scripts on initial world creation. [297��2026 22:48:12.882] [Render thread/WARN] [KubeJS Server/]: You can still see the full log (including past reloads) in your latest.log file. [297��2026 22:48:12.888] [Render thread/INFO] [FluxNetwor

- [ ] **gh-issue:bernie-g/geckolib#811** (github_issue, 1/6 conditions)
  - geckolib issue #811: bug
  - https://github.com/bernie-g/geckolib/issues/811
  - retrieved by: hybrid_a#6@r13l
  - excerpt: [issue by pit800] Uncaught exception in thread "main" java.lang.RuntimeException: Failed to read classTweaker file from mod geckolib at net.fabricmc.loader.impl.FabricLoaderImpl.loadClassTweakers(FabricLoaderImpl.java:534) at net.fabricmc.loader.impl.launch.knot.Knot.init(Knot.java:145) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:66) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Caused by: net.fabricmc.loader.impl.lib.classtweaker.reader.ClassTweakerFormatException: line 1: Namespace (named) does not match current runtime namespace (intermedi

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#6@r13l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:bernie-g/geckolib#767** (github_issue, 1/6 conditions)
  - geckolib issue #767: Mod causes resource loading errors for non-geckolib animation files
  - https://github.com/bernie-g/geckolib/issues/767
  - retrieved by: dense_b#7@r13l
  - excerpt: (ForkJoinTask.java:373) ~[?:?] at java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1182) ~[?:?] at java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1655) ~[?:?] at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1622) ~[?:?] at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:165) ~[?:?] Caused by: software.bernie.geckolib.GeckoLibException: mcinspects:animations/inspect.json: Error loading animation file at software.bernie.geckolib.cache.GeckoLibCache.lambda$loadAnimations$1(GeckoLibCache.java:89) ~[geckolib-4.8.i0:0/

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 1/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_c#7@r13l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:mezz/JustEnoughItems#4180** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4180: [Crash]: [1.21.1] Game Crash when rendering Create Spout category (ArrayIndexOutOfBoundsException)
  - https://github.com/mezz/JustEnoughItems/issues/4180
  - retrieved by: bm25_a#7@r13l
  - excerpt: .github.com/jim139129/53125d5f5e81ccbe594a3de187b4acab [comment by mezz (owner)] Thanks for the report! I pushed some fixes that will allow JEI to catch this type of error and continue to run. Here's what it looks like for your case now: <img width="966" height="620" alt="Image" src="https://github.com/user-attachments/assets/90843f9e-5213-4b48-835f-10ab73ece55c" /> Please make sure to report this to the other mods and link back to this issue so that they can reference it. ``` [00:04:52] [Render thread/ERROR] [me.je.gu.re.RecipeGuiLayouts/]: Recipe layout crashed while drawing java.lang.Ar

- [ ] **gh-issue:TwelveIterations/Waystones#905** (github_issue, 1/6 conditions)
  - Waystones issue #905: Game not saving after activating waystone
  - https://github.com/TwelveIterations/Waystones/issues/905
  - retrieved by: hybrid_b#8@r13l
  - excerpt: uld not parse version number component '1a'!), SemVer is recommended for reliably evaluating dependencies and prioritizing newer version [14:11:22] [main/WARN]: Warnings were found! - Mod 'ModMenu Badges Lib' (modmenu-badges-lib) 2023.6.1 recommends any version of modmenu, which is missing! - You should install any version of modmenu for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg) 2024.6.2 recommends any version of emi, which is missing! - You should install any version of emi for the optimal experience. - Mod 'Yet Another Cobblestone Generator' (yacg)

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 1/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: bm25_a#8@r13l
  - excerpt: ArchitecturyTransformer > Task :common:processIncludeJars UP-TO-DATE > Task :common:jar UP-TO-DATE > Task :neoforge:compileJava UP-TO-DATE > Task :neoforge:classes UP-TO-DATE > Task :neoforge:configureLaunch > Task :neoforge:downloadAssets UP-TO-DATE > Task :neoforge:configureClientLaunch > Task :neoforge:runClient [Architectury Transformer] Architectury Runtime 5.2.91 [Architectury Transformer] Read classpath in 1.061 s [Architectury Transformer] Listening at C:\Users\<user>\Documents\01Developpement\Projets\DopedHorses\common\build\libs\dopedhorses-common-1.2.4-26.1-dev.jar [23:03:14] [main

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#8@r13l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:CaffeineMC/sodium#2731** (github_issue, 1/6 conditions)
  - sodium issue #2731: Problem with launching minecraft 1.21.1 with sodium
  - https://github.com/CaffeineMC/sodium/issues/2731
  - retrieved by: dense_b#9@r13l
  - excerpt: to errors, provided by 'sodium' at 'net.caffeinemc.mods.sodium.fabric.SodiumPreLaunch'! at net.fabricmc.loader.impl.FabricLoaderImpl.lambda$invokeEntrypoints$2(FabricLoaderImpl.java:403) at net.fabricmc.loader.impl.util.ExceptionUtil.gatherExceptions(ExceptionUtil.java:33) at net.fabricmc.loader.impl.FabricLoaderImpl.invokeEntrypoints(FabricLoaderImpl.java:401) at net.fabricmc.loader.impl.launch.knot.Knot.init(Knot.java:160) ... 5 more Caused by: java.lang.UnsatisfiedLinkError: C:\Users\?????\AppData\Local\Temp\jna-1007792265\jna6873146617604809216.dll: Can't find dependent librarie

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 1/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_c#9@r13l
  - excerpt: .util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:507) [?:?] at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1491) [?:?] at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:2073) [?:?] at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2035) [?:?] at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187) [?:?] [28Apr2024 18:58:29.050] [Render thread/FATAL] [net.neoforged.fml.ModLoader/LOADING]: Failed to wait for future Mod Construction, 1 errors found [28Apr2024 18:

- [ ] **gh-issue:wisp-forest/owo-lib#455** (github_issue, 1/6 conditions)
  - owo-lib issue #455: [1.21.1] DataResult is class loaded to early causing a crash
  - https://github.com/wisp-forest/owo-lib/issues/455
  - retrieved by: bm25_a#9@r13l
  - excerpt: [issue by benio1394] Mc version: 1.21.1 Fabric: 0.18.2 Logs (there is no crash report): https://pastebin.com/t1SN82eY [comment by Dragon-Seeker (member)] `Caused by: org.spongepowered.asm.mixin.transformer.throwables.MixinTargetAlreadyLoadedException: Critical problem: owo.mixins.json:DataResultMixin from mod owo target com.mojang.serialization.DataResult was loaded too early.` It seems that DataResult has been loaded in some way by a Mixin Plugin or something else by another mod, leading to an inability to apply a mixin. You will need to go through your mods to figure out the problem mod.

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: hybrid_a#10@r13l
  - excerpt: [issue by MaserPlay] I cannot open minecraft with mods: > Caused by: java.lang.UnsupportedOperationException: A mod tried to access the state neighbor table directly. Please report this at https://github.com/malte0811/FerriteCore/issues. As a temporary workaround you can enable "populateNeighborTable" in the FerriteCore config Minecraft log: ``` MultiMC version: 0.7.0-3826 Launched instance in online mode authserver.mojang.com resolves to: [13.33.243.103, 13.33.243.122, 13.33.243.48, 13.33.243.49] session.minecraft.net resolves to: [13.107.246.67, 13.107.213.67]

- [ ] **gh-issue:mezz/JustEnoughItems#4344** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4344: [Bug]: Flashback replays of servers can't be opened if JEI is installed
  - https://github.com/mezz/JustEnoughItems/issues/4344
  - retrieved by: bm25_a#10@r13l
  - excerpt: a bug report to JEI. After disabling JEI, the replay file did load in successfully. https://gist.github.com/Syntrait/28f6c33621fd02ca2bf2c45051be7002 [comment by mezz (owner)] Thanks for confirming, that narrows down the issue a bit more. JEI requests a recipe sync from Fabric, and REI has its own recipe sync mechanism so it doesn't make that request. I think that Flashback is doing something unusual that causes Fabric to trigger the recipe sync at a bad time, causing the crash. I will see if I can figure out if the issue is really caused by Flashback in my dev environment, and then discus

- [ ] **gh-issue:thedarkcolour/KotlinForForge#89** (github_issue, 1/6 conditions)
  - KotlinForForge issue #89: KFF crash on MC 1.20.4 with MinecraftForge 49.0.8
  - https://github.com/thedarkcolour/KotlinForForge/issues/89
  - retrieved by: bm25_b#10@r13l
  - excerpt: .util.concurrent.CompletableFuture$AsyncRun.exec(CompletableFuture.java:1796) ~[?:?] at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:373) ~[?:?] at java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1182) ~[?:?] at java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1655) ~[?:?] at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1622) ~[?:?] at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:165) ~[?:?] Caused by: java.lang.ClassNotFoundException: net.minecraftforge.fml.loading.moddiscovery.ModAnnotatio

## Added by hand

(none)
