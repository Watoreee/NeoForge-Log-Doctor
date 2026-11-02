# Judging sheet 06: `r08_version_mismatch_create` (test)

- **Category:** `version_mismatch`  |  **Culprit:** `create`  |  **Acceptable:** create, ars_creo, ars_technica, bellsandwhistles, create_aquatic_ambitions, create_dragons_plus, create_enchantment_industry, create_hypertube, createaddition, framedblocks, sophisticatedbackpackscreateintegration, sophisticatedstoragecreateintegration
- **What was broken:** downgraded Create to 6.0.0 (create-1.21.1-6.0.0.jar); 11 mods require a newer Create
- **Logs in this scenario:** r08_crash, r08_latest
- **Documents to judge:** 71

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 4/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_a#2@r08c, hybrid_b#6@r08c, bm25_a#3@r08c, dense_b#8@r08c
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:CaffeineMC/sodium#3743** (github_issue, 3/6 conditions)
  - sodium issue #3743: Sodium mc1.21.1-0.8.12-beta.1 (NeoForge) lacks config
  - https://github.com/CaffeineMC/sodium/issues/3743
  - retrieved by: bm25_b#9@r08c, hybrid_a#1@r08l, bm25_a#3@r08l
  - excerpt: loading phase: Mod sodium_extra requires sodium 0.8.12-alpha.3+mc1.21.1 or above Currently, sodium is 0.6.13+mc1.21.1 Error during pre-loading phase: Mod reeses_sodium_options requires sodium 0.8.12-alpha.3 or above Currently, sodium is 0.6.13+mc1.21.1 ``` [comment by Official-V-Zer0 (none)] It may be due to the crashlog only formed after getting through the load screen hence Sodium being 0.6.13, but using 0.8.12-beta.1 is the issue [comment by jellysquid3 (member)] Your log files and crash logs do not relate to each other. The log file contains the actual error, not the crash report. Pleas

- [ ] **gh-issue:CaffeineMC/sodium#3789** (github_issue, 3/6 conditions)
  - sodium issue #3789: Issue when loading alongside Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3789
  - retrieved by: hybrid_a#5@r08c, hybrid_c#1@r08c, hybrid_a#2@r08l, hybrid_c#1@r08l, bm25_a#4@r08l
  - excerpt: [issue by laji233] ### Bug Description If you launch the game once with both Create: Aeronautics and Sodium loaded, uninstalling Create: Aeronautics and restarting the game will cause the game to crash. ### Reproduction Steps 1.Neoforge 21.1.233 for Minecraft 1.21.1 2.Sodium 0.8.12 and Create Aeronautics 1.3.0 3.launch the game 4.exit the game 5.delete Create Aeronautics 6.restart the game ### Log File [latest.log](https://github.com/user-attachments/files/29452105/latest.log) ### Crash Report [crash-2026-06-29_13.26.29-client.txt](https://github.com/user-attachments/files/29452110/cras

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/modfiles** (neoforge_docs, 3/6 conditions)
  - NeoForge docs: Mod Files
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/
  - retrieved by: hybrid_b#7@r08c, dense_b#9@r08c, hybrid_b#1@r08l, bm25_b#1@r08l, dense_b#1@r08l
  - excerpt: ning to the user. | `type="incompatible"` | | `reason` | string | _nothing_ | An optional user-facing message to describe why this dependency is required, or why it is incompatible. | `reason="integration"`

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 3/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: hybrid_a#9@r08c, hybrid_b#10@r08l, dense_b#2@r08l
  - excerpt: ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.234 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:instancing OpenGL Renderer: Intel(R) UHD Graphics OpenGL Version: 4.6.0 - Build 31.0.101.2127 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecr

- [ ] **gh-issue:malte0811/FerriteCore#189** (github_issue, 3/6 conditions)
  - FerriteCore issue #189: ferrite core crashing 1.19.2 small modpack
  - https://github.com/malte0811/FerriteCore/issues/189
  - retrieved by: hybrid_a#7@r08c, hybrid_a#3@r08l, hybrid_b#8@r08l, dense_b#9@r08l
  - excerpt: cpVersion, 20220805.130853] [11:31:53] [main/INFO] [cp.mo.mo.Launcher/MODLAUNCHER]: ModLauncher 10.0.8+10.0.8+main.0ef7e830 starting: java version 17.0.8 by Microsoft; OS Windows 11 arch amd64 version 10.0 [11:31:59] [main/INFO] [mixin/]: SpongePowered MIXIN Subsystem Version=0.8.5 Source=union:/C:/Users/<user>/AppData/Roaming/.tlauncher/legacy/Minecraft/game/libraries/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar%2398!/ Service=ModLauncher Env=CLIENT [11:32:01] [main/WARN] [ne.mi.fm.lo.mo.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.tlauncher\legacy\Minecraft\game\librari

- [ ] **gh-issue:mezz/JustEnoughItems#4450** (github_issue, 3/6 conditions)
  - JustEnoughItems issue #4450: [Bug]: Create: Aeronautics mixin mismatch causing client crash
  - https://github.com/mezz/JustEnoughItems/issues/4450
  - retrieved by: hybrid_b#4@r08c, hybrid_c#6@r08c, bm25_b#6@r08c, hybrid_c#6@r08l
  - excerpt: [issue by viralhysteria] ### Steps to Reproduce the Bug The recent 19.44.0.406 update causes a client crash on world load when running the game with only Create, Create: Aeronautics and Sable enabled. All aforementioned mods are on the latest release channel. <details> <summary>Error 1</summary> [Render thread/ERROR] [net.neoforged.bus.EventBus/EVENTBUS]: Exception caught during firing event: An unexpected critical error was encountered Index: 1 Listeners: 0: mezz.jei.neoforge.JustEnoughItemsClient$$Lambda/0x0000025398eba5c8@7a90d6de 1: mezz.jei.neoforge.startup.StartEventObserver$$Lam

- [ ] **gh-issue:mrh0/createaddition#897** (github_issue, 3/6 conditions)
  - createaddition issue #897: No support for create 6.0.0?
  - https://github.com/mrh0/createaddition/issues/897
  - retrieved by: hybrid_a#5@r08l, hybrid_b#6@r08l, dense_b#5@r08l
  - excerpt: [issue by EhBrokenToaster] **Describe the bug** A clear and concise description of what the bug is. Encountered an error when booting, 1 Mod has errors loading and the game points to createadditions. Says it requires 6.0.1 or above and the next version down doesn't support 6.0.0 either as it requires an even older version of Create, that then requires flywheel, of which wont run with create being version 6.0. I've been attempting to make a giant conglomeration mod pack to put on a server with a few buddies to stream and most mods aren't currently updated to 6.0.1 as of yet. Removing the mod d

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#1@r08c, bm25_a#4@r08c, hybrid_a#10@r08l
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:Creators-of-Create/Create#10508** (github_issue, 2/6 conditions)
  - Create issue #10508: Super glue not working
  - https://github.com/Creators-of-Create/Create/issues/10508
  - retrieved by: hybrid_b#1@r08c, dense_b#7@r08c, dense_b#8@r08l
  - excerpt: mod pack. I wanted to install the Create mod so I could build and use blueprints, because I play with a friend on another server and I really need this mod. Unfortunately, I have a problem. I cannot find a working version of Create for Fabric on Minecraft 1.21.1, and Forge also does not work properly for me, even though I installed all the required files and patches needed for NeoForge to run it. Even so, it still does not work — I have all the required dependencies for the mod installed, but Forge/NeoForge still fails to run. I also tried NeoForge separately, but it still does not work. Other

- [ ] **gh-issue:shedaniel/cloth-config#159** (github_issue, 2/6 conditions)
  - cloth-config issue #159: Cloth Config API 7.0.72 seen as 7.0.65
  - https://github.com/shedaniel/cloth-config/issues/159
  - retrieved by: hybrid_b#9@r08c, bm25_b#1@r08c
  - excerpt: [issue by Harras420] When I try to use the Cloth Config API 7.0.72 for the DragonLoot mod, it crashes the game on start up and says: Incompatible mod set! net.fabricmc.loader.impl.FormattedException: Mod resolution encountered an incompatible mod set! A potential solution has been determined: - Replace mod 'Cloth Config v6' (cloth-config) 7.0.65 with mod 'Cloth Config v6' (cloth-config), version 7.0.69 or later. Unmet dependency listing: - Mod 'DragonLoot' (dragonloot) 1.1.1 requires version 7.0.69 or later of mod 'Cloth Config v6' (cloth-config), but only the wrong version i

- [ ] **neoforge-docs:docs/1.21.1/gettingstarted/versioning** (neoforge_docs, 2/6 conditions)
  - NeoForge docs: Versioning
  - https://docs.neoforged.net/docs/1.21.1/gettingstarted/versioning/
  - retrieved by: hybrid_b#8@r08c, dense_b#1@r08c
  - excerpt: As you probably know, NeoForge is not the only mod loader out there, and many mod developers develop on multiple platforms. As a result, a way to distinguish between two files of the same mod of the same version, but for different mod loaders is needed. Usually, this is done by including the mod loader somewhere in the name. `jei-neoforge-1.20.2-16.0.0.28`, `jei-1.20.2-neoforge-16.0.0.28` or `jei-1.20.2-16.0.0.28-neoforge` are all valid ways to do it. For other mod loaders, the `neoforge` bit would be replaced with `forge`, `fabric`, `quilt` or whatever different mod loader you might be devel

- [ ] **gh-issue:Creators-of-Create/Create#10531** (github_issue, 2/6 conditions)
  - Create issue #10531: Strange cogwheel Behavior
  - https://github.com/Creators-of-Create/Create/issues/10531
  - retrieved by: hybrid_c#2@r08c, bm25_a#9@r08c, hybrid_c#2@r08l
  - excerpt: Spells x Sable Compat: 1.0.3 Create Diesel Generators: 1.21.1-1.3.13 Balm: 21.0.59 CreateBetterFps: 1.1.4 Chat Heads: 0.15.2 Exposure: 1.9.18 Cloth Config v15 API: 15.0.140 Supplementaries: 1.21.1-3.6.8 Geophilic: 3.5 Athena: 4.0.6 Create: Oxidized: 0.1.3 Vista: 1.21.1-4.4.13 Industrial Foregoing: 1.21-3.6.38 Cataclysm & BetterCombat - Compatibility: 1.0.2 Biomes O' Plenty: 21.1.0.13 Integrated Cataclysm: 1.0.6+1.21.1-neoforge Iron's Spells 'n Spellbooks Dynamic Skill Tree: 1.1.0 Sticky Wheels: 0.0.2 Design n' Decor: 2.2b VanillaBackport: 1.1.7.10 Apothic Attributes: 2.9.1

- [ ] **gh-issue:TwelveIterations/Balm#203** (github_issue, 2/6 conditions)
  - Balm issue #203: Latest version dependency failure
  - https://github.com/TwelveIterations/Balm/issues/203
  - retrieved by: dense_b#6@r08c, hybrid_b#2@r08l, dense_b#6@r08l
  - excerpt: [issue by rpghearthbreaker-lab] ### Minecraft Version 1.21.10 ### Mod Loader Forge ### Describe the Issue Updating balm-forge-1.21.10-21.10.6-all.jar to balm-forge-1.21.10-21.10.8-all.jar via the "update all" function caused a complete dependency failure for every single mod that references it. The exact error from crash assistant was that the mod was not installed *at all* rather than being the wrong version, so something in the dependent mods are requesting something that isn't correctly available in the x.8 version. ### Logs I already fixed it by just downgrading. The logs are gone.

- [ ] **gh-issue:TwelveIterations/Balm#56** (github_issue, 2/6 conditions)
  - Balm issue #56: Startup Crash MC 1.18.1
  - https://github.com/TwelveIterations/Balm/issues/56
  - retrieved by: hybrid_b#4@r08l, bm25_b#2@r08l
  - excerpt: [issue by Khan8615] ### Minecraft Version Other (specify below) ### Mod Loader Forge ### Mod Loader Version forge-1.18.1-39.1.0-universal.jar ### Mod Version netherportalfix-forge-1.18-9.0.0 ### Balm Version balm-3.2.6.jar ### Describe the Issue I installed a Minecraft server with Forge & nothing else. Boots fine. I only added the 1 mod & its dependency file nothing else on a fresh server install to try it out & it fails to boot. The docs on curseforge state balm-3.2.6.jar is supposed to support 1.18.1 but it doesn't appear to. Failure message: Mod File balm-3.2.6.jar needs

- [ ] **gh-issue:embeddedt/ModernFix#565** (github_issue, 2/6 conditions)
  - ModernFix issue #565: incompatible with VMP-Forge
  - https://github.com/embeddedt/ModernFix/issues/565
  - retrieved by: hybrid_b#10@r08c, dense_b#2@r08c
  - excerpt: [issue by dghodgson] ### Bug Description Attempting to load Modernfix alongside VMP-Forge will cause the minecraft client to crash. Tested with following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Modernfix 5.18.0+mc1.20.1 seems to launch without any issues. All older versions tested failed with a different error than the one found in the attached log. ### Reproduction Steps Install the following versions: - VMP mc1.20.1-0.2.0+beta.7.102-all - Modernfix 5.23.0+mc1.20.1 Forge: 47.4.1 ### Log File ``` MultiMC version: 0.7.0-4230 Launched instance in onlin

- [ ] **gh-issue:thedarkcolour/KotlinForForge#122** (github_issue, 2/6 conditions)
  - KotlinForForge issue #122: [1.21.1-Neoforge] Kotlin crashes on NeoForge 1.21.1
  - https://github.com/thedarkcolour/KotlinForForge/issues/122
  - retrieved by: hybrid_b#2@r08c, bm25_b#10@r08c
  - excerpt: [issue by overlappingd] Mod `fzzy_config` requires Kotlin, Kotlin crashes the game when the Mod Construction stage is about to finish Crash Report: https://mclo.gs/FEz1bUZ `latest.log`: https://mclo.gs/59pOEet Using the [Just Create SMP](https://www.curseforge.com/minecraft/modpacks/just-create-smp) modpack. [comment by thedarkcolour (owner)] Not a KFF issue. Vanilla Backport bug from the looks of it

- [ ] **gh-issue:TwelveIterations/Balm#27** (github_issue, 2/6 conditions)
  - Balm issue #27: Forge Crash
  - https://github.com/TwelveIterations/Balm/issues/27
  - retrieved by: hybrid_b#3@r08l, dense_b#7@r08l
  - excerpt: \javafmllanguage\1.19-41.0.63\javafmllanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.958] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\lowcodelanguage\1.19-41.0.63\lowcodelanguage-1.19-41.0.63.jar is missing mods.toml file [07lip2022 18:29:07.960] [main/WARN] [net.minecraftforge.fml.loading.moddiscovery.ModFileParser/LOADING]: Mod file C:\Users\<user>\AppData\Roaming\.minecraft\libraries\net\minecraftforge\mclanguage\1.19-41.0.63\mclanguage-1.19-41.0.63

- [ ] **gh-issue:architectury/architectury-api#719** (github_issue, 2/6 conditions)
  - architectury-api issue #719: [NeoForge 26.1.0.11-beta] NoClassDefFoundError: net.neoforged.neoforge.event.level.block.BreakBlockEvent
  - https://github.com/architectury/architectury-api/issues/719
  - retrieved by: hybrid_b#3@r08c, hybrid_a#8@r08l
  - excerpt: file "neoforge-26.1.0.11-beta-minecraft-merged-deobf-26.1.jar" [locator: game locator] [23:03:15] [ForkJo [... truncated] [comment by st0x0ef (collaborator)] Thanks for the report, I'll check what version are incompatible and remove them. Please use latest 26.1.2. [comment by GallonEmilien (none)] It's working fine with 26.1.2 💪, thanks again for this port

- [ ] **gh-issue:mrh0/createaddition#1145** (github_issue, 2/6 conditions)
  - createaddition issue #1145: Grappling whisk crashing when shooting a create aeronautics/sable physics object
  - https://github.com/mrh0/createaddition/issues/1145
  - retrieved by: hybrid_c#3@r08c, bm25_b#4@r08c, hybrid_c#3@r08l
  - excerpt: [issue by AviRavi6009] **Describe the bug** Grappling whisking a sable physics object crashes the client immediately **To Reproduce** Steps to reproduce the behavior: Use grappling whisk on a sable physics object **Additional context** - Mod version: create-stuff-additions1.21.1_v2.1.0e - Forge version:FML: 4.0.42 NeoForge: 21.1.219 - Create version:1.21.1-6.0.10 [crash-2026-05-07_11.28.45-client.txt](https://github.com/user-attachments/files/27487065/crash-2026-05-07_11.28.45-client.txt) [comment by mrh0 (owner)] Wrong mod, this is Create crafts and additions

- [ ] **gh-issue:CaffeineMC/sodium#3606** (github_issue, 2/6 conditions)
  - sodium issue #3606: [1.21.1] [NeoForge] All world textures become invisible when Sodium is installed with Create: Aeronautics
  - https://github.com/CaffeineMC/sodium/issues/3606
  - retrieved by: bm25_a#6@r08l, bm25_b#4@r08l
  - excerpt: client.SODIUM-ON.txt](https://github.com/user-attachments/files/27023150/crash-2026-04-23_21.54.02-client.SODIUM-ON.txt) [crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt](https://github.com/user-attachments/files/27023139/crash-2026-04-23_21.59.05-client.SODIUM-OFF.txt) [comment by jellysquid3 (member)] Can you please provide information about your computer's hardware? The crash report and log file are both unusually vague. [comment by douira (contributor)] Please provide a reproduction with only the mods you've mentioned, and not the many dozens of other mods you're using. [comment by Gav

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#8** (github_issue, 2/6 conditions)
  - YUNGs-API issue #8: Fabric cannot find API
  - https://github.com/YUNG-GANG/YUNGs-API/issues/8
  - retrieved by: bm25_b#7@r08c, hybrid_b#9@r08l
  - excerpt: [issue by FabricStuff] When I launch Minecraft Fabric, I get a crash issue that says it "Could not find required mod: yungsapi requires {fabric @ [>=0.25.0]}". But I already have the latest ver. installed to my mods folder. [comment by yungnickyoung (member)] Double check. That is a message from the fabric loader itself, not my mod. So you may have accidentally downloaded the wrong version, or not placed it in your mods folder.

- [ ] **gh-issue:embeddedt/ModernFix#425** (github_issue, 2/6 conditions)
  - ModernFix issue #425: [Bug]: Missing items in search
  - https://github.com/embeddedt/ModernFix/issues/425
  - retrieved by: hybrid_b#7@r08l, bm25_b#10@r08l
  - excerpt: [issue by Unleashed75] ### Bug Description Using Fabric loader 1.21 - 0.15.11 Mods installed; fabric-api-0.100.1+1.21 jei-1.21-fabric-19.0.0.1 modernfix-fabric-5.18.2+mc1.21 In a new world where you are in creative, open inventory. In the tab for searching items, search for Lightning Rod. I expected to see Lightning Rods in the search results but it does not. (Unknown if other items are missing from searches) With both JEI and ModernFix installed, searching for Lightning Rod in the creative tab does not show up. With either or both JEI or ModernFix is not installed things work

- [ ] **gh-issue:Creators-of-Create/Create#10596** (github_issue, 1/6 conditions)
  - Create issue #10596: Jetpack enchantment Above The Clouds not working
  - https://github.com/Creators-of-Create/Create/issues/10596
  - retrieved by: bm25_a#1@r08c
  - excerpt: [issue by Vek10316] ### Description Above The Clouds enchantment's description depicts users able to ascend infinitely, but ascent height is still limited ### Game Log https://mclo.gs/uH5w2lK ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 4060/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 576.5

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 1/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: bm25_a#1@r08l
  - excerpt: event net.neoforged.neoforge.client.event.sound.SoundEngineLoadEvent to a broken mod state [28Apr2024 18:58:29.349] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Block to a broken mod state [28Apr2024 18:58:29.350] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.RegisterColorHandlersEvent$Item to a broke [... truncated] [comment by thedarkcolour (owner)] Good catch. I love reflection! [comment by bms-1984 (none)] Ye

- [ ] **gh-issue:TwelveIterations/Waystones#1144** (github_issue, 1/6 conditions)
  - Waystones issue #1144: Unable to edit names in UI
  - https://github.com/TwelveIterations/Waystones/issues/1144
  - retrieved by: bm25_b#2@r08c
  - excerpt: [issue by uwuboi273] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Every time I even attempt to edit a name the game completely crashes. ### Logs https://mclo.gs/c4BHmKR [comment by BlayTheNinth (member)] `Veinminer Client` is including an incompatible version of `fabric-permissions-api` for a newer version of Minecraft. Which is funny because on newer versions of Minecraft, the version they include is also incompatible, but instead for older versions of Minecraft. The only way around this is reporting the issue to Veinminer Client, and either removing that

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 1/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: bm25_a#2@r08c
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:malte0811/FerriteCore#150** (github_issue, 1/6 conditions)
  - FerriteCore issue #150: Issue / Bug.  I cannot open minecraft 
  - https://github.com/malte0811/FerriteCore/issues/150
  - retrieved by: bm25_a#2@r08l
  - excerpt: MultiMC/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar D:/programs/MultiMC/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar D:/programs/MultiMC/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar D:/programs/MultiMC/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar D: [... truncated] [comment by davidromrell (none)] This seems to be either canary or immediately fast, check and if it still shows as this mod rereport. [comment by malte0811 (owner)] You have missing dependencies, and both ImmediatelyFast and Canary do not

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#3@r08c
  - excerpt: [issue by LeapordLady639] ### Minecraft Version Other (specify below) ### Mod Loader NeoForge ### Describe the Issue I'm trying to launch a 1.21.4 modpack and it's saying that "Waystones (waystones) has failed to load correctly" before reaching the title page and all I can do from there is open the mod folder, open the log file, open the crash report, or quit the game. Given what the crash report says I looked at Balm's config file and does indeed contain no configurations, but I don't know what to do about that. I also looked at Waystone's config file and there doesn't seem to be any pro

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#5** (github_issue, 1/6 conditions)
  - YUNGs-API issue #5: YungsAPI listed as not installed, but it is?
  - https://github.com/YUNG-GANG/YUNGs-API/issues/5
  - retrieved by: dense_b#3@r08l
  - excerpt: jar:?] {} at cpw.mods.modlauncher.Launcher.main(Launcher.java:66) [modlauncher-8.0.9.jar:?] {} at io.github.zekerzhayard.forgewrapper.installer.Main.main(Main.java:50) [ForgeWrapper-1.4.2.jar:?] {} at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[?:1.8.0_271] {} at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) ~[?:1.8.0_271] {} at [... truncated] [comment by khorvo77 (none)] Sorry, Modlist: Mods: [✔️] [1.16.5]+SecurityCraft+v1.8.21.1 [✔️] abnormals_core-1.16

- [ ] **gh-issue:mezz/JustEnoughItems#4255** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4255: [Bug]: Conflict with AE2 and Beyond Dimensions (Neoforge)
  - https://github.com/mezz/JustEnoughItems/issues/4255
  - retrieved by: dense_b#3@r08c
  - excerpt: :** [NeoForge](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548363) | [Fabric](https://www.curseforge.com/minecraft/mc-mods/jei/files/8548362) **Modrinth:** [NeoForge](https://modrinth.com/mod/u6dRKJwZ/version/rPLXajL0) | [Fabric](https://modrinth.com/mod/u6dRKJwZ/version/jEV5BTqf) _Note: CurseForge and Modrinth links may take a little time to work while new files are reviewed._ [comment by mezz-bot (collaborator)] 🚀 A fix for this issue is available in Just Enough Items version `15.33.0.174` for Minecraft `1.20.1`. Thanks for reporting this issue! **CurseForge:** [Fabric](https:

- [ ] **gh-issue:thedarkcolour/KotlinForForge#75** (github_issue, 1/6 conditions)
  - KotlinForForge issue #75: 1.19.2 crashes after installing KFF
  - https://github.com/thedarkcolour/KotlinForForge/issues/75
  - retrieved by: bm25_b#3@r08l
  - excerpt: [issue by BartholomewIII] Trying to install cobblemon which requires KFF. Everytime I install any version of KFF the game crashes with exit code 2. It loads just fine without KFF installed but says that I need to install KFF for the cobblemon mod to work. [comment by thedarkcolour (owner)] You're missing Architectury API. [comment by BartholomewIII (none)] This fixed it thanks.

- [ ] **gh-issue:wisp-forest/owo-lib#507** (github_issue, 1/6 conditions)
  - owo-lib issue #507: [1.21.1 NeoForge] NeoForge 21.1.262 breaks NetworkRegistryMixin (RETURN ordinal = 3): "Sided Packet Codec has not been unpacked", every player kicked on join
  - https://github.com/wisp-forest/owo-lib/issues/507
  - retrieved by: bm25_b#3@r08c
  - excerpt: loads) | | 1 | `return BUILTIN_PAYLOADS.get(id)` | | 2 | `return null` (no registration) | | 3 | `return null` (flow mismatch) ← owo now modifies this one | | 4 | `return registration.codec()` ← should be modified | | 5 | `return null` (wrong phase) | As a result, the `SidedPacketCodec` is never unpacked, and its `encode`/`decode` always throw. This breaks Accessories and every mod using owo networking on NeoForge 1.21.1. Hosts that auto-update the loader (for example Aternos) can't pin 21.1.259, so those servers are currently unjoinable. **Suggested fix:** drop the ordinal so the unpacking

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 1/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_a#4@r08c
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#4@r08l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:architectury/architectury-api#531** (github_issue, 1/6 conditions)
  - architectury-api issue #531: NeoForge 21.0.43-beta Not Working with Architectury 1.21
  - https://github.com/architectury/architectury-api/issues/531
  - retrieved by: dense_b#4@r08c
  - excerpt: ixin,re:classloading} at TRANSFORMER/minecraft@1.21/net.minecraft.client.Minecraft.handler$zib000$omegaconfig$onReturn(Minecraft.java:4020) ~[client-1.21-20240613.152323-srg.jar%23237!/:?] {re:mixin,pl:accesstransformer:B,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:APP:glitchcore.mixins.json:client.MixinMinecraft from mod glitchcore,pl:mixin:APP:resourcefulconfig.mixins.json:client.MinecraftMixin from mod resourcefulconfig,pl:mixin:APP:omega-config.mixins.json:ClientMixin from mod omegaconfig,pl:mixin:APP:architectury.mixins.json:MixinMinecraft from mod architectu

- [ ] **gh-issue:architectury/architectury-api#664** (github_issue, 1/6 conditions)
  - architectury-api issue #664: java.lang.IllegalStateException: Mod 'architectury' is not available!
  - https://github.com/architectury/architectury-api/issues/664
  - retrieved by: dense_b#4@r08l
  - excerpt: [issue by KellTayLieLor] I keep getting this error whenever I try to build a modpack. I am using Cursforge with Neoforge as my launcher. I am on 1.21.1. I first got the error on an already established modpack after a few mods were updated. This honestly happens fairly often and it is so frustrating. I literally cannot play modded minecraft without this mod because it is a dependency for so many others. I've been looking through the logs, debug, and crash reports to try and find out which mod is the main culprit here but I am struggling. I am not a programmer and I don't know how to code so if

- [ ] **gh-issue:mrh0/createaddition#820** (github_issue, 1/6 conditions)
  - createaddition issue #820: Create Additions 1.2.4c is incompatible with Immersive Engineering
  - https://github.com/mrh0/createaddition/issues/820
  - retrieved by: hybrid_c#4@r08c, hybrid_c#4@r08l
  - excerpt: latest.log) Edit: Lowest version of Additions I avoided the crash on is 1.2.3 [comment by karouvirae (none)] Just a heads-up from someone who's stumbled upon this: modrinth has a newer version that is compatible (1.2.4d) [comment by TheOneSalem (none)] Oh awesome! I didn't realize there was a compatible version out. Thanks for the info! [comment by mrh0 (owner)] Fixed in 1.2.4d

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_b#5@r08c
  - excerpt: [issue by gamebastian-creator] ### Bug Description Hello, I am experiencing a crash when launching Minecraft 1.21.1 on NeoForge with my modpack. I use Sable for Aeronautics, and Sable requires a newer version of Sodium. However, after installing the required Sodium version, the game crashes during startup. Environment: * Minecraft 1.21.1 * NeoForge 21.1.233 * Sable 2.0.3 * Aeronautics * Sodium 0.8.12-alpha.2+ (required by Sable) Because Sable requires this version of Sodium, removing Sodium is not a viable workaround for my setup. Could you please help determine whether this is a known

- [ ] **gh-issue:Creators-of-Create/Create#9565** (github_issue, 1/6 conditions)
  - Create issue #9565: Contraption Control
  - https://github.com/Creators-of-Create/Create/issues/9565
  - retrieved by: bm25_a#5@r08c
  - excerpt: [issue by aronilyas4] ### Description This item connected to an elevator contraption creates a huge amount of lag (fps drop). I go from ~165 fps to ~15fps. if you wan't to try and recreate the issue it happens on [my modpack](https://www.curseforge.com/minecraft/modpacks/blockscapeodyssey) ### Game Log https://mclo.gs/GPfYcyw ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.210 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 1/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: bm25_b#5@r08l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:mrh0/createaddition#804** (github_issue, 1/6 conditions)
  - createaddition issue #804: Latest version results in datapack error when trying to load a new world and a crash when creating new ones.
  - https://github.com/mrh0/createaddition/issues/804
  - retrieved by: hybrid_c#5@r08c, hybrid_c#5@r08l
  - excerpt: [issue by Nereithr] **Describe the bug** Attempting to load a world with Crafts and Additions v1.20 - 1.2.4 results in the following datapack-related error: <details> <summary>Image</summary> ![unknown_2024 06 23-12 28](https://github.com/mrh0/createaddition/assets/72263884/767f14b9-6639-4267-be58-e026c4c37929) </details> Attempting to create a new world results in a crash. [Here is the log file.](https://github.com/user-attachments/files/15944302/latest.log) Downpatching to version 1.20.-1.2.3 fixes the issue. **To Reproduce** Steps to reproduce the behavior: 1.

- [ ] **gh-issue:wisp-forest/owo-lib#384** (github_issue, 1/6 conditions)
  - owo-lib issue #384: Network error spam with particle systems on 1.21.1 Neoforge
  - https://github.com/wisp-forest/owo-lib/issues/384
  - retrieved by: bm25_b#5@r08c
  - excerpt: [issue by Rearth] Hi, I'm using the owo lib ParticleSystemController / ParticleSystem feature a lot in Oritech (both on fabric and neoforge). I recently was made aware that the neoforge version of owo lib logs an error every time a particle is spawned on the server side. The particles still spawn just fine, but with multiple machines potentially creating particles every tick, it quickly adds up to the logs being unusable. I hope it's okay for me to create issues about the Neoforge version of owo lib here, I wasn't able to create issues in the NF branch. Original issue with logs: https://githu

- [ ] **neoforge-docs:docs/1.21.1/resources/client/models/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Models
  - https://docs.neoforged.net/docs/1.21.1/resources/client/models/
  - retrieved by: bm25_a#5@r08l
  - excerpt: value(), ...); } ``` Item handlers work pretty much the same, except for some naming and the lambda parameters: ```java @SubscribeEvent // on the mod event bus only on the physical client public static void registerItemColorHandlers(RegisterColorHandlersEvent.Item event) { // Parameters are the item stack and the tint index. event.register((stack, tintIndex) -> { // Like above, replace with your own calculation. Vanilla values are in the ItemColors class. // Also like above, tint index -1 means no tint and should use a default value instead. return 0xFFFFFFFF;

- [ ] **neoforge-docs:docs/1.21.1/resources/server/recipes/builtin** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Built-In Recipe Types
  - https://docs.neoforged.net/docs/1.21.1/resources/server/recipes/builtin/
  - retrieved by: hybrid_b#5@r08l
  - excerpt: use a builder pattern, therefore no variable is created. Create a new builder by calling // ShapelessRecipeBuilder#shapeless with the recipe category (found in the RecipeCategory enum) // and a result item, a result item and count, or a result item stack. ShapelessRecipeBuilder.shapeless(RecipeCategory.MISC, Items.MUSHROOM_STEW) // Add the recipe ingredients. This can either accept Ingredients, TagKey<Item>s or ItemLikes. // Overloads also exist that additionally accept a count, adding the same ingredient multiple times. .requires(Blocks.BROWN_MUSHROOM) .require

- [ ] **neoforge-docs:user/docs/index** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: NeoForge User Guide
  - https://docs.neoforged.net/user/docs/
  - retrieved by: dense_b#5@r08c
  - excerpt: ` - Verify that the first number after the `version` bit matches the Java version needed for the desired Minecraft version. - E.g., `openjdk version "21.0.4" 2024-07-16 LTS` is a Java 21 version and as such fit for Minecraft 1.20.5 and newer. - If the version does not match, then you will have to [install the correct Java version][installingjava]. - If everything went smoothly, continue to [Installing NeoForge][installingneoforge]. ### Installing Java The way to install Java depends on your operating system. Always make sure you're grabbing the correct version of Java, and make sure you

- [ ] **gh-issue:Creators-of-Create/Create#10795** (github_issue, 1/6 conditions)
  - Create issue #10795: Experiencing server-like lagging in singleplayer when applying Tree Fertilizer
  - https://github.com/Creators-of-Create/Create/issues/10795
  - retrieved by: bm25_a#6@r08c
  - excerpt: tes (4572 MiB) / 8589934592 bytes (8192 MiB) up to 8589934592 bytes (8192 MiB) Total Memory: 3890826992 bytes (3710 MiB) / 8589934592 bytes (8192 MiB) CPU: AMD Ryzen 9 5900HS with Radeon Graphics @ 3.29 GHz; 8 cores / 16 threads on 1 socket(s) Graphics card #0: AMD Radeon(TM) Graphics (Advanced Micro Devices, Inc. (0x1002)); 512.00 MB of VRAM Graphics card #1: NVIDIA GeForce RTX 3050 Ti Laptop GPU (NVIDIA (0x10de)); 4095.00 MB of VRAM Other Mods: KubeJS: 2001.6.5-build.16 Horseman: 1.3.15 Simple Magnets: 1.1.12 KubeJSCurios: 1.0.4 Fabric Rendering Fluids (v1): 3.0.29+4ac5e37a77 Fabr

- [ ] **gh-issue:TeamMetallurgy/Aquaculture#343** (github_issue, 1/6 conditions)
  - Aquaculture issue #343: AC2 not loading
  - https://github.com/TeamMetallurgy/Aquaculture/issues/343
  - retrieved by: hybrid_a#6@r08c
  - excerpt: [issue by antiwesley] MC is erroring out when trying to load the mod. Here's the error log: ---- Minecraft Crash Report ---- // I'm sorry, Dave. Time: 7/14/22, 5:00 PM Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading} at net.minecraftforge.client.loading.ClientModLoader.completeModLoading(ClientModLoader.java:167) ~[forge-1.19-41.0.98-universal.jar%23157!/:?] {re:classloading,

- [ ] **gh-issue:embeddedt/ModernFix#660** (github_issue, 1/6 conditions)
  - ModernFix issue #660: mixin.perf.faster_ingredients breaks many recipes from Prefab mod (especially conditional recipes)
  - https://github.com/embeddedt/ModernFix/issues/660
  - retrieved by: bm25_b#6@r08l
  - excerpt: (Brian Wuest) confirmed this is a **ModernFix-side issue**, not a Prefab bug. Quote from Prefab developer: > "Found issue, turn off the setting: mixin.perf.faster_ingredients. This for some reason is what is causing ALL of Prefab's recipes to be broken! Not just the ones you pointed out. ... This needs to be reported to the Modern Fix mod team as this is not something I can fix within Prefab." Workaround: Setting `mixin.perf.faster_ingredients = false` immediately restores all affected recipes. ### Minimal Mod List **Minimal reproduction list:** - ModernFix 5.27.5+mc1.21.1 (NeoForge) - P

- [ ] **gh-issue:mrh0/createaddition#718** (github_issue, 1/6 conditions)
  - createaddition issue #718: Games crashes upon mod loading
  - https://github.com/mrh0/createaddition/issues/718
  - retrieved by: hybrid_a#6@r08l
  - excerpt: [issue by ferforious1] **Describe the bug** Game crashes with an error upon mod loading **To Reproduce** - **Additional context** - Mod version: 1.0.0b - Forge version: 47.2.20 - Create version: 0.5.1f - Minecraft version: 1.20.1 [crash-2024-01-17_09.03.21-fml.txt](https://github.com/mrh0/createaddition/files/13959323/crash-2024-01-17_09.03.21-fml.txt) [comment by mrh0 (owner)] please update to the latest version before submitting a report

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 1/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: bm25_a#7@r08c
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:TwelveIterations/Balm#228** (github_issue, 1/6 conditions)
  - Balm issue #228: 26.1 Neoforge 26.1.0.3-beta Server Side Crash On Start
  - https://github.com/TwelveIterations/Balm/issues/228
  - retrieved by: hybrid_a#7@r08l
  - excerpt: [issue by P3rf3ctXZer0] [12:24:46] [main/ERROR] [minecraft/Main]: Failed to start the minecraft server net.neoforged.fml.ModLoadingException: Loading errors encountered: - Balm (balm) has failed to load correctly java.lang.NoClassDefFoundError: net/minecraft/client/gui/screens/Screen at net.neoforged.fml.ModLoader.waitForFuture(ModLoader.java:253) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.dispatchParallelTask(ModLoader.java:216) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModLoader.constructMods(ModLoader.java:124) ~[loader-11.0.4.jar:11.0] {} at net.neoforged.fml.ModL

- [ ] **gh-issue:bernie-g/geckolib#850** (github_issue, 1/6 conditions)
  - geckolib issue #850: Animation Parsing Error
  - https://github.com/bernie-g/geckolib/issues/850
  - retrieved by: bm25_a#7@r08l
  - excerpt: [issue by Filan-glitch] GeckoLib V4.8.4 NeoForge 21.1.228 MC1.21.1 Error Logs: [05May2026 11:30:01.258] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.258] [Worker-Main-5/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.261] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: idle [05May2026 11:30:01.290] [Worker-Main-1/ERROR][GeckoLib/]: Unable to parse animation: attack sadly no further information in logs... [comment by Tslat (collaborator)] Provide the mod jar so I can test it I can't do anything with this [comment

- [ ] **gh-issue:malte0811/FerriteCore#147** (github_issue, 1/6 conditions)
  - FerriteCore issue #147: A mod tried to access the state neighbor table directly (1.20.1)
  - https://github.com/malte0811/FerriteCore/issues/147
  - retrieved by: bm25_b#7@r08l
  - excerpt: [issue by DangerMage] Modpack was working, then it started crashing on startup with this log: https://paste.ee/p/sUb00 (log contains the mod list, java version, forge version, minecraft version, JVM arguments, etc) [comment by DangerMage (none)] Looks like I was missing a dependency (https://www.curseforge.com/minecraft/mc-mods/astikor-carts-redux) probably a bug that it crashes instead of going to the missing dependencies screen [comment by davidromrell (none)] seems to be a bug with canary Imo, although for sure it is an optimization mod. [comment by malte0811 (owner)] Forge/NeoF

- [ ] **gh-issue:mrh0/createaddition#1148** (github_issue, 1/6 conditions)
  - createaddition issue #1148: possible compatibility issues
  - https://github.com/mrh0/createaddition/issues/1148
  - retrieved by: hybrid_c#7@r08c, hybrid_c#7@r08l
  - excerpt: zes, saves and crashes - The diagram opens but the buttons in the top right-hand corner do not appear; I have to close and reopen the diagram to refresh it. - The diagram does not open; the game freezes and crashes Furthermore, the lack of a visual cue to indicate the direction of thrust is really annoying. If you could add in futur, a particle effect (purple?) when holding the wrench to indicate the direction of thrust, it would save a lot of time on projects with many propellers i can send you my savegame if it's needed. or the blueprint of this project. ## Additional context - Minecra

- [ ] **gh-issue:Creators-of-Create/Create#10662** (github_issue, 1/6 conditions)
  - Create issue #10662: the cannon won't assemble/build in survival with the Big Cannons mod
  - https://github.com/Creators-of-Create/Create/issues/10662
  - retrieved by: bm25_a#8@r08c
  - excerpt: [issue by cuberPidor] ### Description My cannon from Create: Big Cannons builds and shoots fine in Creative mode, but fails to assemble or work in Survival. Am I missing something like glue, stress capacity, or assembly steps? ### Game Log https://mclo.gs/wti8vMj ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.243 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Rendere

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#8@r08c
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:mezz/JustEnoughItems#3709** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #3709: [Crash]: Lunar Client is incompatible with JEI mod 1.21/1.21.1
  - https://github.com/mezz/JustEnoughItems/issues/3709
  - retrieved by: bm25_b#8@r08c
  - excerpt: [issue by KR99991] ### Steps to Reproduce the Crash 1. Download lunar client. Select the 1.21.1 or 1.21 fabric version in lunar client. 3. Install jei mod to lunar client. 4. Launch game. ### Mod Pack URL (Optional) https://www.curseforge.com/minecraft/mc-mods/jei/files/5623551 ### Mod Pack Version (Optional) jei-1.21.1-fabric-19.8.4.113 ### Extra Notes (Optional) Please fix it, thanks! ### Crash Report https://gist.github.com/KR99991/7a9982edfe16b8328218399cd7687424 [comment by mezz (owner)] Thanks for the report! The crash log has this error: ``` [2024-08-25 17:02:10.802] [erro

- [ ] **gh-issue:mrh0/createaddition#1131** (github_issue, 1/6 conditions)
  - createaddition issue #1131: Compatability crash with Create Aeronautics
  - https://github.com/mrh0/createaddition/issues/1131
  - retrieved by: hybrid_c#8@r08c, hybrid_c#8@r08l
  - excerpt: [issue by Hoodstain] When you give a blaze burner with a straw on a physic contraption from Create Aeronautics and then try to view that with a contraption diagram also from Create Aeronautics the game crashes. This has also been reported to the simulated team just thought id be thorough in terms of reporting - Mod version: 1.5.10 - Forge version: Neoforge 21.1.225 - Create version: 6.0.9 -Minecraft Version: 1.21.1 [crash-2026-04-23_13.15.55-client.txt](https://github.com/user-attachments/files/27026437/crash-2026-04-23_13.15.55-client.txt) [comment by mrh0 (owner)] Crash seams to happen in

- [ ] **gh-issue:thedarkcolour/KotlinForForge#85** (github_issue, 1/6 conditions)
  - KotlinForForge issue #85: kotlinforforge-4.6.2 requires language provider kotlinforforge:4.3
  - https://github.com/thedarkcolour/KotlinForForge/issues/85
  - retrieved by: bm25_a#8@r08l
  - excerpt: [issue by GitVex] Hey there, I've been going through and watnted to add a whole lot of mods to a profile, though somehow kotlin for forge isn't recognised here: [19:57:10] [main/INFO]: ModLauncher running: args [--username, <player>, --version, forge-47.2.0, --gameDir, C:\Users\<user>\Twitch\Minecraft\Instances\Tome of Ahsenna, --assetsDir, C:\Users\<user>\Twitch\Minecraft\Install\assets, --assetIndex, 5, --uuid, <token>, --accessToken, <token>, --clientId, <token>, --xuid, <token>, --userType, msa, --versionType, release, --width, 1024, --height, 768, --quickPlayPath, C:\Users\<user>\Twitc

- [ ] **gh-issue:thedarkcolour/KotlinForForge#86** (github_issue, 1/6 conditions)
  - KotlinForForge issue #86: Unable to use other Kotlin libraries with KFF on Forge/NeoForge
  - https://github.com/thedarkcolour/KotlinForForge/issues/86
  - retrieved by: bm25_b#8@r08l
  - excerpt: [issue by Erdragh] I'm writing a Minecraft mod / Discord bot combo: https://github.com/Erdragh/AstralBot It uses [JDA](https://jda.wiki) to communicate with Discord. JDA has a dependency on okhttp3 which over multiple corners has a dependency on the kotlin stdlib. I'm excluding the `org.jetbrains.kotlin` dependency from JDA. I'm using Kotlin for the Mod itself and the build scripts. The Fabric server starts fine, the Forge server doesn't. To reproduce: - Clone repo mentioned above - Start the Forge server with the env variable `DISCORD_TOKEN` set to any value, just so it's defined.

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#728** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #728: Dedicated Server Crash Neoforge 21.1.206 for 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/728
  - retrieved by: hybrid_a#9@r08l
  - excerpt: [issue by peachmimosa15] Description: Mod loading failures have occurred; consult the issue messages for more details net.neoforged.neoforge.logging.CrashReportExtender$ModLoadingCrashException: Mod loading has failed I updated my modpack today and sophisiticated storage is not happy. I just uploaded the latest version on modrinth for 7 minutes ago and still not working. sophisticatedstorage-1.21.1-1.5.0.1254.jar [crash-2025-09-01_08.59.59-fml.txt](https://github.com/user-attachments/files/22078851/crash-2025-09-01_08.59.59-fml.txt) [comment by P3pp3rF1y (owner)] You need to update Soph

- [ ] **gh-issue:SuperMartijn642/TrashCans#12** (github_issue, 1/6 conditions)
  - TrashCans issue #12: [Crash] ...
  - https://github.com/SuperMartijn642/TrashCans/issues/12
  - retrieved by: hybrid_c#9@r08c, hybrid_c#9@r08l
  - excerpt: [issue by TheTechPny] Sorry forgot to edit the title **Version Info** - Minecraft, 1.16.5 - Trash Cans, trashcans-1.0.10-mc1.16.5.jar **Steps to Reproduce** A player mined a trash can with an Ars Nouveau spell "ars nouveau, so it was a custom spell touch+break+pickup" **Crash report (~/logs/latest.log)** https://pastebin.com/raw/Lwu3ge5E [comment by SuperMartijn642 (owner)] I fixed it now in [Core Lib version 1.0.10](https://www.curseforge.com/minecraft/mc-mods/supermartijn642s-core-lib/files/all). Thank you for the reporting the issue!

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 1/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: bm25_b#9@r08l
  - excerpt: .0 because the newer `Placebo` (v9.9.1) conflicted with `CreativeCore` (v2.13.13). This created a secondary crash, as `Apotheosis` (v8.4.0) required `Placebo v9.9.1`. 2. **The Solution that Revealed the Bug:** We resolved the dependency hell by forcing a clean installation of the latest dependency chain (`Apotheosis v8.4.0` + `Placebo v9.9.1` + `CreativeCore v2.13.13`). 3. **The Outcome (The ModernFix Crash):** Although the dependency chain was now correct, the game still crashed instantly upon loading registry events. This proved the crash was not a dependency issue, but a **ModernFix timin

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: bm25_a#9@r08l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:Creators-of-Create/Create#10575** (github_issue, 1/6 conditions)
  - Create issue #10575: Block value adjust handle not working for all blocks that have one.
  - https://github.com/Creators-of-Create/Create/issues/10575
  - retrieved by: bm25_a#10@r08c
  - excerpt: adjustment thingies? ### Game Log https://mclo.gs/cIV6rNQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6600 OpenGL Version: 4.6.0 Core Profile Context 25.10.2.250923 Graphics Mode: fast PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0

- [ ] **gh-issue:Creators-of-Create/Create#9745** (github_issue, 1/6 conditions)
  - Create issue #9745: Shaders with Create
  - https://github.com/Creators-of-Create/Create/issues/9745
  - retrieved by: hybrid_a#10@r08c
  - excerpt: assets/6cdfa570-13f8-4e8f-b69a-a7c0fd408475" /> ### Game Log https://mclo.gs/nJlYbPX ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.216 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.5 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: AMD Radeon RX 7600 (radeonsi, navi33, LLVM 21.1.6, DRM 3.64, 6.18.2-3-cachyos) OpenGL Version: 4.6 (Core Profile) Mesa 25.3.2-arch1.2 Graphics Mode: fancy PojavLauncher Dete

- [ ] **gh-issue:TwelveIterations/Balm#227** (github_issue, 1/6 conditions)
  - Balm issue #227: ClassNotFoundException: FabricPermissionsAPIIntegration when fabric-permissions-api is present on 26.1
  - https://github.com/TwelveIterations/Balm/issues/227
  - retrieved by: dense_b#10@r08l
  - excerpt: [issue by LegitMeme] ### Minecraft Version 26.1 (LTS) ### Mod Loader Fabric ### Describe the Issue When fabric-permissions-api is present on MC 26.1 (in this case bundled by Fzzy Config), Balm attempts to load FabricPermissionsAPIIntegration but the class doesn't exist in Balm's own jar, causing a ClassNotFoundException and crashing on startup. Steps to reproduce: 1. Install Balm 26.1.0.2 and Fzzy Config 0.7.6+26.1 together. 2. Launch the game. ### Logs Latest: https://mclo.gs/HVJabRm Crash report: https://mclo.gs/Jqx9OUD [comment by BlayTheNinth (member)] Fixed in Balm 26.1.0.3 [com

- [ ] **gh-issue:mrh0/createaddition#768** (github_issue, 1/6 conditions)
  - createaddition issue #768: Server crashing after breaking accumulator from Create: Crafts and Additions
  - https://github.com/mrh0/createaddition/issues/768
  - retrieved by: hybrid_c#10@r08c, hybrid_c#10@r08l
  - excerpt: [issue by rymusov] As soon as I want to break the accumulator, with energy and it is connected by wires - the server crashes. If I disconnect the connectors and wires beforehand, the crash does not happen. Version 1.20.1, Forge 47.2.21. Video: https://youtu.be/sEwVBQ1Fihs **To Reproduce** [Steps to reproduce the behavior:] https://youtu.be/sEwVBQ1Fihs **Additional context** - Mod version: 1.20.1-1.2.3 - Forge version: 47.2.21 - Create version: 0.5.1f [comment by mrh0 (owner)] Could you please provide the crash logs for the server? [comment by rymusov (none)] Oh, sorry, yes [2024-0

- [ ] **gh-issue:mrh0/createaddition#815** (github_issue, 1/6 conditions)
  - createaddition issue #815: game will crash when running 1.2.4c (most recent version)
  - https://github.com/mrh0/createaddition/issues/815
  - retrieved by: dense_b#10@r08c
  - excerpt: [issue by poly-1810] **Describe the bug** when running the most recent release for 1.20.1(neo)forge, the game crashes upon loading worlds or creating new ones due to "cannot modify empty stack" **To Reproduce** install mod alongside create, run game, try to load or create new world **Additional context** - Mod version: 1.2.4c - Forge version: 47.1.103 neoforge - Create version: 0.5.1f - Crash report: [crash-2024-07-01_18.32.19-client.txt](https://github.com/user-attachments/files/16059869/crash-2024-07-01_18.32.19-client.txt) [comment by mrh0 (owner)] try 1.2.4d [comment by tobi1

- [ ] **gh-issue:mrh0/createaddition#980** (github_issue, 1/6 conditions)
  - createaddition issue #980: Portable drill incompatible with quark matrix enchanting
  - https://github.com/mrh0/createaddition/issues/980
  - retrieved by: bm25_a#10@r08l
  - excerpt: [issue by CorneliusCornbread] **Describe the bug** Attempting to enchant the portable drill with quark enchant system will results in a ticking exception. In this case it's caught by Neruina and the enchantment table is suspended from ticking to prevent server crashes. **To Reproduce** Steps to reproduce the behavior: 1. Install quark + quark oddities 2. Install create + create crafts and additions 3. Place enchantment table 4. Place portable drill in enchantment table 5. Crash **Additional context** - Mod version: 1.20.1-1.3.1 - Forge version: 47.4.0 - Create version: 6.0.4 ``` [21:50:35]

## Added by hand

(none)
