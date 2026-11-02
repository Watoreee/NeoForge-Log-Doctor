# Judging sheet 16: `r10_out_of_memory_none` (dev)

- **Category:** `out_of_memory`  |  **Culprit:** `None`  |  **Acceptable:** (none)
- **What was broken:** set the pack's max RAM to 3000 MB in the launcher; opening a world failed with the data pack error screen
- **Logs in this scenario:** r10_latest
- **Documents to judge:** 37

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:mezz/JustEnoughItems#4351** (github_issue, 4/6 conditions)
  - JustEnoughItems issue #4351: [Bug]: UI error when opening inventory
  - https://github.com/mezz/JustEnoughItems/issues/4351
  - retrieved by: hybrid_b#1@r10l, hybrid_c#1@r10l, bm25_b#4@r10l, dense_b#4@r10l
  - excerpt: I still have 12 GiB of free space. I thought it might be COW (Copy-on-Write) corrupting data, so I created a new instance/profile, and only installed Fabric API and JEI. I also tried restarting the game multiple times. It's still happening. I tried giving myself /op, setting myself to Creative mode, doing /recipe give @s *, but none of them helped. The game does not crash, only the JEI UI does, so I can still play the game normally. ### latest.log https://gist.github.com/Syntrait/41c04b9450d3e65c524d2ff8ae82b582 [comment by mezz (owner)] Thanks for the report! Can you please include the s

- [ ] **gh-issue:Creators-of-Create/Create#10508** (github_issue, 3/6 conditions)
  - Create issue #10508: Super glue not working
  - https://github.com/Creators-of-Create/Create/issues/10508
  - retrieved by: hybrid_b#9@r10l, hybrid_c#9@r10l, dense_b#1@r10l
  - excerpt: -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx12224M Memory: 2043631496 bytes (1948 MiB) / 9177137152 bytes (8752 MiB) up to 12817793024 bytes (12224 MiB) Total Memory: 7225780344 bytes (6891 MiB) / 9177137152 bytes (8752 MiB) CPU: Intel(R) CC150 CPU @ 3.50GHz @ 3.50 GHz; 7 cores / 7 threads on 1 socket(s) Graphics cards: none Other Mods: YUNG's Better Dungeons: 1.21.1-NeoForge-5.1.4 Sky Aesthetics: 2.0.13-beta KubeJS: 2101.7.2-build.348 SuperMartijn642's Config Library: 1.1.8 Horseman: 1.5.9 Alex's Mobs: 1.22.17 Create Deco: 2.1.3 Pl

- [ ] **gh-issue:TheIllusiveC4/Curios#521** (github_issue, 3/6 conditions)
  - Curios issue #521: [Bug]: Incorrect slot config syntax corrupts all save games and crashes new world creation
  - https://github.com/TheIllusiveC4/Curios/issues/521
  - retrieved by: hybrid_a#7@r10l, bm25_a#1@r10l, dense_b#3@r10l
  - excerpt: assets/32453c00-e99b-43e8-b642-7f9e48b5d845) ![Image](https://github.com/user-attachments/assets/2ac94a63-a0d0-4a48-a423-be214ae18b20) **Crash log** [crash-2025-05-20_15.21.58-client.txt](https://github.com/user-attachments/files/20348587/crash-2025-05-20_15.21.58-client.txt) ### Relevant Log Outputs Error when trying to load the world with incorrect slot syntax: ```java [15:29:17] [Render thread/WARN] [ModernFix/]: Initial datapack load took 312.0 ms [15:29:17] [Render thread/WARN] [minecraft/WorldOpenFlows]: Failed to load level data or datapacks, can't proceed with server load java.util.

- [ ] **gh-issue:mrh0/createaddition#636** (github_issue, 3/6 conditions)
  - createaddition issue #636: Accumulator in Spawn Chunks causing Crash?
  - https://github.com/mrh0/createaddition/issues/636
  - retrieved by: hybrid_b#10@r10l, hybrid_c#10@r10l, bm25_b#1@r10l
  - excerpt: tity` ![screenshot](https://github.com/mrh0/createaddition/assets/83117017/4f07083b-9250-40f5-8b20-1a2e67346add) CSV file of the snapshot: [createaddition.csv](https://github.com/mrh0/createaddition/files/12577000/createaddition.csv) After closing Minecraft it produces error code -805306369 When I encountered this issue first time I tried to do some memory profiling with Spark: `[09:28:40] [spark-worker-pool-1-thread-1/INFO] [minecraft/ChatComponent]: [System] [CHAT] [?] Young Gen GC lasting 198 ms. (cause = G1 Evacuation Pause)\n 298.0 MB moved to G1 Old Gen\n 2.4 GB ? 2.7 GB\n 6

- [ ] **gh-issue:Creators-of-Create/Create#9688** (github_issue, 3/6 conditions)
  - Create issue #9688: Not really a bug but more of a oversight
  - https://github.com/Creators-of-Create/Create/issues/9688
  - retrieved by: hybrid_b#3@r10l, hybrid_c#3@r10l, bm25_b#6@r10l
  - excerpt: 8489271296 bytes (8096 MiB) Total Memory: 3022383296 bytes (2882 MiB) / 6459228160 bytes (6160 MiB) CPU: AMD Custom APU 0405 @ -0.00 GHz; 4 cores / 8 threads on 1 socket(s) Graphics cards: none Other Mods: Enhanced Extinguishing: 1.0.0 YUNG's Better Dungeons: 1.21.1-NeoForge-5.1.4 Forgified Fabric Renderer API (v1): 3.4.0+acb05a3919 YUNG's Better Witch Huts: 1.21.1-NeoForge-4.1.1 GeckoLib 4: 4.8.2 scena: 21.1.18 Forgified Fabric Item API (v1): 11.1.1+57cdfa8219 The Aether: 1.5.10 Saecularia Caudices: 21.1.5 Forgified Fabric Rendering Fluids (v1): 3.1.6+857185bc19 YUNG's Better O

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 3/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_a#4@r10l, hybrid_b#6@r10l, hybrid_c#6@r10l
  - excerpt: m: 21.0.56 Mekanism: Generators: 10.7.19 Vista: All The Tapes: 1.1.0+neoforge.mc1.21.1 Exposure: 1.9.16 Cloth Config v15 API: 15.0.140 Pride Lib: 1.2.4+1.21.1 LowDragLib2: 2.2.8 Universal Trinkets: 1.1.0 Vista: 1.21.1-4.2.0 Create: Connected: 1.1.16-mc1.21.1 Block Outline Customizer: 1.2 Create: Break It All: 1.0.0 Create: Ultimate Factory: 2.2.4 Just Hammers: 21.1.4 Building Gadgets 2 GUI: 0.2.0-beta.1 Mekanism ↔ TFMG Compat: 0.3-1.21.1 Civillis: 1.3.3-release Curios API: 9.5.1+1.21.1 Underground Village, Stoneholm: 1.5.7 Veinminer: 3.1.2+mc1.21.1 Sophisticated Storage Cre

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8938** (github_issue, 2/6 conditions)
  - Applied-Energistics-2 issue #8938: [NeoForge 1.21.1 / 19.2.17] Divide-by-zero crash in CraftingTreeNode.request() — fix from #7611 appears to be missing
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8938
  - retrieved by: hybrid_a#8@r10l, bm25_a#2@r10l
  - excerpt: $25(CraftingCalculation.java) at appeng.crafting.CraftingCalculation.wrapMethod$ifm000$molecularmanipulator$trackOmniCalculation(CraftingCalculation.java:1590) at appeng.crafting.CraftingCalculation.run(CraftingCalculation.java) at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:317) at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144) at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642) at java.base/java.lang.Thread.run(Thread.java:1583) [Server thread/WARN] [AE2:S/]: Failed

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 2/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: hybrid_b#2@r10l, hybrid_c#2@r10l
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:bernie-g/geckolib#767** (github_issue, 2/6 conditions)
  - geckolib issue #767: Mod causes resource loading errors for non-geckolib animation files
  - https://github.com/bernie-g/geckolib/issues/767
  - retrieved by: hybrid_a#2@r10l, bm25_a#5@r10l
  - excerpt: [issue by DarksideAlex] Geckolib tries to load all `animations/*.json` files, even from unrelated namespaces. Non-geckolib files cause a `GeckoLibException` and prevent further resources from loading. **Versions**: - Minecraft: 1.20.1 - Quilt: 0.29.1 - GeckoLib: 4.8 **Relevant Log Snippet**: ``` [14:49:39] [Render thread/INFO]: Caught error loading resourcepacks, removing all selected resourcepacks java.util.concurrent.CompletionException: software.bernie.geckolib.GeckoLibException: mcinspects:animations/inspect.json: Error loading animation file at java.util.concurrent.CompletableFuture.en

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 2/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#3@r10l, bm25_a#6@r10l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 2/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: hybrid_a#10@r10l, bm25_a#3@r10l
  - excerpt: [issue by ToxinZangoose] Hello, I have recently been trying to diagnose an issue with my modpack and the log files point to this mod when I try launching. When launching, owo lib tries to load shaders for Spectrum which is not supported for NeoForge. Below is the log file for the crash I've been experiencing since I've tried removing 19 mods from this pack. https://mclo.gs/wDKVGtH Thank you for your time! [comment by Dragon-Seeker (member)] ``` [02Nov2024 11:04:06.859] [modloading-worker-0/ERROR] [io.github.lightman314.lightmanscurrency.LightmansCurrency/]: Error setting up C

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#639** (github_issue, 2/6 conditions)
  - SophisticatedStorage issue #639: Odd Factory Gauge Behavior When Paired With Sophisticated Storage
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/639
  - retrieved by: hybrid_b#4@r10l, hybrid_c#4@r10l
  - excerpt: : Flywheel Version: 1.0.2 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce GTX 1070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 572.83 Graphics Mode: Fancy System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.3, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx8192m Memory: 2006231608 bytes (1913 MiB) / 8589934592 bytes (8192 MiB) up to 8589934592 bytes (8192 MiB) Total Memory: 6588243616 bytes (6283 MiB) / 8589934592 bytes (8192 MiB) CPU: Intel(R) Co

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 2/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: hybrid_b#5@r10l, hybrid_c#5@r10l
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:CaffeineMC/sodium#2731** (github_issue, 2/6 conditions)
  - sodium issue #2731: Problem with launching minecraft 1.21.1 with sodium
  - https://github.com/CaffeineMC/sodium/issues/2731
  - retrieved by: hybrid_a#6@r10l, bm25_b#10@r10l
  - excerpt: to errors, provided by 'sodium' at 'net.caffeinemc.mods.sodium.fabric.SodiumPreLaunch'! at net.fabricmc.loader.impl.FabricLoaderImpl.lambda$invokeEntrypoints$2(FabricLoaderImpl.java:403) at net.fabricmc.loader.impl.util.ExceptionUtil.gatherExceptions(ExceptionUtil.java:33) at net.fabricmc.loader.impl.FabricLoaderImpl.invokeEntrypoints(FabricLoaderImpl.java:401) at net.fabricmc.loader.impl.launch.knot.Knot.init(Knot.java:160) ... 5 more Caused by: java.lang.UnsatisfiedLinkError: C:\Users\?????\AppData\Local\Temp\jna-1007792265\jna6873146617604809216.dll: Can't find dependent librarie

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_b#7@r10l, hybrid_c#7@r10l
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_b#8@r10l, hybrid_c#8@r10l
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:CaffeineMC/sodium#3013** (github_issue, 1/6 conditions)
  - sodium issue #3013: Texture Bleeding with Custom Models using half pixel translations
  - https://github.com/CaffeineMC/sodium/issues/3013
  - retrieved by: hybrid_a#1@r10l
  - excerpt: the texture of weeping vines to plain orange and the texture bleeding is visible like seen in the image above. ### Log File [20:01:14] [main/INFO]: Loading Minecraft 1.21.4 with Fabric Loader 0.16.9 [20:01:14] [main/INFO]: Loading 11 mods: - fabricloader 0.16.9 \-- mixinextras 0.4.1 - java 21 - minecraft 1.21.4 - sodium 0.6.6+mc1.21.4 |-- fabric-api-base 0.4.54+b47eab6b04 |-- fabric-block-view-api-v2 1.0.19+7feeb73304 |-- fabric-renderer-api-v1 5.0.2+84404cdd04 |-- fabric-rendering-data-attachment-v1 0.3.57+73761d2e04 |-- fabric-rendering-fluids-v1 3.1.19+7feeb733

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8793** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8793: DOUMENTATION IS INCOMPLETE!!!!
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8793
  - retrieved by: bm25_b#2@r10l
  - excerpt: with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with data from the block, get the error: "Could not load configuration from an incompatible device" ### Expected behavior 1. Get yourself a Memory Card. 2. Get an AE2 block that you can load data from into the cad (any machine, or a pattern provider or a P2P tunnel, anything, doesn't matter) and place it in the world. 3. Put any random item in your off hand. 4. Attempt to load data from the block in step two with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with dat

- [ ] **gh-issue:Creators-of-Create/Create#10778** (github_issue, 1/6 conditions)
  - Create issue #10778: The encased fan blows air through the non‑ventilated blocks.
  - https://github.com/Creators-of-Create/Create/issues/10778
  - retrieved by: dense_b#2@r10l
  - excerpt: Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx16384M Memory: 1213959216 bytes (1157 MiB) / 6803161088 bytes (6488 MiB) up to 17179869184 bytes (16384 MiB) Total Memory: 5625451472 bytes (5364 MiB) / 6803161088 bytes (6488 MiB) CPU: 12th Gen Intel(R) Core(TM) i5-12500 @ 3.00 GHz; 6 cores / 12 threads on 1 socket(s) Graphics cards: none Other Mods: Saturn: 0.1.5 Concurrent Chunk Management Engine (Fixes/WorldGen/Threading Issues): 0.4.0-alpha.0.117+1.21.1 KubeJS: 2101.7.2-build.368 Create: Deep Seas - Lava Fix: 1.0.1 SuperM

- [ ] **neoforge-docs:docs/1.21.1/networking/streamcodecs** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Stream Codecs
  - https://docs.neoforged.net/docs/1.21.1/networking/streamcodecs/
  - retrieved by: bm25_b#3@r10l
  - excerpt: Additionally, there are some static instances that encode and decode primitives and objects using a different method. #### Unsigned Shorts `UNSIGNED_SHORT` is an alternative of `SHORT` that is meant to be treated as an unsigned number. As numbers are signed in Java, unsigned shorts are sent and received as `Integer`s with the upper two bytes masked out. #### Variable-Sized Number `VAR_INT` and `VAR_LONG` are stream codecs where the value is encoded to be as small as possible. This is done by encoding seven bits at a time, using the upper bit as a marker of whether there is more data for th

- [ ] **gh-issue:mezz/JustEnoughItems#4180** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4180: [Crash]: [1.21.1] Game Crash when rendering Create Spout category (ArrayIndexOutOfBoundsException)
  - https://github.com/mezz/JustEnoughItems/issues/4180
  - retrieved by: bm25_a#4@r10l
  - excerpt: .github.com/jim139129/53125d5f5e81ccbe594a3de187b4acab [comment by mezz (owner)] Thanks for the report! I pushed some fixes that will allow JEI to catch this type of error and continue to run. Here's what it looks like for your case now: <img width="966" height="620" alt="Image" src="https://github.com/user-attachments/assets/90843f9e-5213-4b48-835f-10ab73ece55c" /> Please make sure to report this to the other mods and link back to this issue so that they can reference it. ``` [00:04:52] [Render thread/ERROR] [me.je.gu.re.RecipeGuiLayouts/]: Recipe layout crashed while drawing java.lang.Ar

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8922** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8922: Pattern provider UI is unnaccessible without error
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8922
  - retrieved by: hybrid_a#5@r10l
  - excerpt: Unknown Source) ~[?:?] at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.network.handlers.ClientPayloadHandler.createMenuScreen(ClientPayloadHandler.java:131) ~[neoforge-21.1.234-universal.jar%23554!/:?] at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.network.handlers.ClientPayloadHandler.handle(ClientPayloadHandler.java:120) ~[neoforge-21.1.234-universal.jar%23554!/:?] at TRANSFORMER/neoforge@21.1.234/net.neoforged.neoforge.network.handling.MainThreadPayloadHandler.lambda$handle$0(MainThreadPayloadHandler.java:16) ~[neoforge-21.1.234-universal.jar%23554!/:?] at TRANSFORMER/m

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 1/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: bm25_b#5@r10l
  - excerpt: [issue by Bread-NiceCat] Minecraft: 1.21 NeoForge: 21.0.143 Architect Plugin: 3.4.159 Architectury Loom: 1.7.412 ``` modImplementation("thedarkcolour:kotlinforforge-neoforge:5.5.0") ``` ``` Exception in thread "main" java.lang.module.ResolutionException: Module thedarkcolour.kotlinforforge reads more than one module named fml_loader at java.base/java.lang.module.Resolver.resolveFail(Resolver.java:900) at java.base/java.lang.module.Resolver.checkExportSuppliers(Resolver.java:721) at java.base/java.lang.module.Resolver.finish(Resolver.java:380) at java.base/java.lang.module.Confi

- [ ] **gh-issue:wisp-forest/owo-lib#29** (github_issue, 1/6 conditions)
  - owo-lib issue #29: [1.18.2] Crash in the end on chunk gen, light engine maybe?
  - https://github.com/wisp-forest/owo-lib/issues/29
  - retrieved by: dense_b#5@r10l
  - excerpt: [issue by itsdinkd] ```java ---- Minecraft Crash Report ---- // I just don't know what went wrong :( Time: 6/6/22, 1:51 AM Description: Feature placement java.util.ConcurrentModificationException at java.util.HashMap.forEach(HashMap.java:1424) at net.minecraft.world.gen.feature.OreFeature.handler$iln001$coping(OreFeature:1054) at net.minecraft.world.gen.feature.OreFeature.generateVeinPart(OreFeature:175) at net.minecraft.world.gen.feature.OreFeature.generate(OreFeature:52) at net.minecraft.world.gen.feature.Feature.generateIfValid(Feature:163) at net.minecraft.world.gen.fe

- [ ] **gh-issue:mezz/JustEnoughItems#4463** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4463: [Crash]: Viewing mob drops from JER causes an IndexOutOfBoundsException (1.21.1 NeoForge)
  - https://github.com/mezz/JustEnoughItems/issues/4463
  - retrieved by: dense_b#6@r10l
  - excerpt: [issue by Luviam] ### Steps to Reproduce the Crash 1. Open a world with the latest version of JER and a version of JEI that is > 19.50.0.414 2. Open the inventory menu and click on a mob drop within the JEI menu. 3. View mobs that drop said item. (You might need to wait a few seconds or click on the GUI) ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) _No response_ ### Crash Report https://mclo.gs/Nmn6USx [comment by mezz (owner)] Thanks for the report! This is a duplicate of * #4461 It has already been fixed on 1.2

- [ ] **gh-issue:Creators-of-Create/Create#10567** (github_issue, 1/6 conditions)
  - Create issue #10567: invisible physics shafts and cogwheels ect.
  - https://github.com/Creators-of-Create/Create/issues/10567
  - retrieved by: bm25_a#7@r10l
  - excerpt: [issue by jrn907-lab] ### Description they are invisible once turned into a physics object ### Game Log USERNAME}\AppData\Roaming\ModrinthApp\profiles\Create_ Plane and Simple\dynamic-resource-pack-cache\amendments-generated_pack in 13.41 ms [17:56:09] [Worker-ResourceReload-0/INFO] [Moonlight/]: Regenerating Dynamic CLIENT_RESOURCES Resources Provider [moonlight:dynamic_resources], requested by strategy REGEN_ON_EVERY_RELOAD [17:56:09] [Worker-ResourceReload-0/INFO] [Moonlight/]: Generated runtime CLIENT_RESOURCES for pack moonlight:dynamic_resources in 629.7 ?s [17:56:09] [Worker-Resource

- [ ] **gh-issue:architectury/architectury-api#290** (github_issue, 1/6 conditions)
  - architectury-api issue #290: Error could not initizlize class net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents
  - https://github.com/architectury/architectury-api/issues/290
  - retrieved by: bm25_b#7@r10l
  - excerpt: .fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at top.catowncraft.carpettctcaddition.CarpetTCTCAddition.onInitialize(CarpetTCTCAddition.java:68) at net.fabricmc.loader.impl.entrypoint.EntrypointUtils.invoke0(EntrypointUtils.java:47) ... 7 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 1/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: dense_b#7@r10l
  - excerpt: # mixin.bugfix.ctm_resourceutil_cme=true # (default) # mixin.bugfix.ender_dragon_leak=true # (default) # mixin.bugfix.entity_pose_stack=true # (default) # mixin.bugfix.extra_experimental_screen=true # (default) # mixin.bugfix.fix_config_crashes=true # (default) # mixin.bugfix.missing_block_entities=false # (default) # mixin.bugfix.packet_leak=false # (default) # mixin.bugfix.paper_chunk_patches=false # (overridden for mod compat) # mixin.bugfix.recipe_book_type_desync=true # (default) # mixin.bugfix.restore_old_dragon_movement=false # (default) # mixin.bugfix.skip_redundant_saves=fa

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#931** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #931: [Create][1.21.1] Stack upgrades on max barrels kick players (IndexOutOfBoundsException
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/931
  - retrieved by: dense_b#8@r10l
  - excerpt: out of bounds exception, I thought it might be related, so I created the ticket. [comment by P3pp3rF1y (owner)] You will need to report this one to create, sounds like perhaps stock ticker isn't ready for that many slots.

- [ ] **gh-issue:malte0811/FerriteCore#155** (github_issue, 1/6 conditions)
  - FerriteCore issue #155: Crash running Create+
  - https://github.com/malte0811/FerriteCore/issues/155
  - retrieved by: bm25_b#8@r10l
  - excerpt: er.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@10.0.8/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@1.1.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:141) Caused by: java.lang.reflect.InvocationTargetException at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:119) at java.base/java.lang.reflect.Method.invoke(Method.java:578) at MC-BOOTSTRAP/fmlloader@1.19.2-43.3.0/net.minecraftforge.fml.loading.targets.Co

- [ ] **gh-issue:thedarkcolour/KotlinForForge#40** (github_issue, 1/6 conditions)
  - KotlinForForge issue #40: Log marker crash on 1.19
  - https://github.com/thedarkcolour/KotlinForForge/issues/40
  - retrieved by: bm25_a#8@r10l
  - excerpt: .CompletableFuture$AsyncSupply.run(CompletableFuture.java:1768) ~[?:?] {} at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136) ~[?:?] {} at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635) ~[?:?] {} at java.lang.Thread.run(Thread.java:833) ~[?:?] {} ``` This is caused by Forge's move to SLF4J in 1.19, which means the [`LogMarkers` fields changed types](https://github.com/MinecraftForge/MinecraftForge/blob/1.19.x/fmlloader/src/main/java/net/minecraftforge/fml/loading/LogMarkers.java) (to SLF4J's `Marker`) and KFF can't find

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: hybrid_a#9@r10l
  - excerpt: /issues. ========================= // Shall we play a game? Time: 2026-06-25 21:57:03 Description: Rendering overlay java.lang.RuntimeException: Sodium mod config not found at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigs(ConfigManager.java:119) ~[net.caffeinemc.sodium-neoforge-0.8.12-beta.2+mc1.21.1-mod.jar%23319!/:?] {re:mixin,re:classloading} at TRANSFORMER/sodium@0.8.12-beta.2+mc1.21.1/net.caffeinemc.mods.sodium.client.config.ConfigManager.registerConfigsLate(ConfigManager.java:76) ~[net.caffeinemc.sodium-neoforge-0.8

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#640** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #640: Multiple item removing bugs with limited barrel 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/640
  - retrieved by: dense_b#9@r10l
  - excerpt: java:124) ~[loader-4.0.38.jar%23111!/:4.0] at MC-BOOTSTRAP/fml_loader@4.0.38/net.neoforged.fml.loading.targets.CommonClientLaunchHandler.runService(CommonClientLaunchHandler.java:32) ~[loader-4.0.38.jar%23111!/:4.0] at MC-BOOTSTRAP/fml_loader@4.0.38/net.neoforged.fml.loading.targets.CommonLaunchHandler.lambda$launchService$4(CommonLaunchHandler.java:118) ~[loader-4.0.38.jar%23111!/:4.0] at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.LaunchServiceHandlerDecorator.launch(LaunchServiceHandlerDecorator.java:30) [modlauncher-11.0.4.jar%23119!/:?] at MC-BOOTSTRAP/cpw.mods.modla

- [ ] **gh-issue:architectury/architectury-api#432** (github_issue, 1/6 conditions)
  - architectury-api issue #432: Archiectury crashes during pre-load 
  - https://github.com/architectury/architectury-api/issues/432
  - retrieved by: bm25_b#9@r10l
  - excerpt: it>(class_310.java:458) at net.minecraft.client.main.Main.main(Main.java:211) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:468) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.NoClassDefFoundError: Could not initialize class net.fabricmc.fabric.api.client.rendering.v1.HudRenderCallback at net.mehvahdjukaar.supplementaries.common.events.fabric.ClientEventsFabric.init(ClientEventsFabric.java:39) at net.mehvahdjuk

- [ ] **gh-issue:thedarkcolour/KotlinForForge#89** (github_issue, 1/6 conditions)
  - KotlinForForge issue #89: KFF crash on MC 1.20.4 with MinecraftForge 49.0.8
  - https://github.com/thedarkcolour/KotlinForForge/issues/89
  - retrieved by: bm25_a#9@r10l
  - excerpt: [issue by Prototik] ``` [13Dec2023 14:19:03.511] [modloading-worker-0/ERROR] [thedarkcolour.kotlinforforge.LoggerKt/LOADING]: Failed to register Automatic Kotlin subscribers. ModID: kotlinforforge, class thedarkcolour.kotlinforforge.test.KotlinForForge java.lang.NoClassDefFoundError: net/minecraftforge/fml/loading/moddiscovery/ModAnnotation$EnumHolder at thedarkcolour.kotlinforforge.AutoKotlinEventBusSubscriber.<clinit>(AutoKotlinEventBusSubscriber.kt:40) ~[kfflang-4.8.0.jar%239!/:4.8.0] at thedarkcolour.kotlinforforge.KotlinModContainer.constructMod(KotlinModContainer.kt:74) ~[kfflang-4

- [ ] **gh-issue:TwelveIterations/Waystones#905** (github_issue, 1/6 conditions)
  - Waystones issue #905: Game not saving after activating waystone
  - https://github.com/TwelveIterations/Waystones/issues/905
  - retrieved by: bm25_a#10@r10l
  - excerpt: Mode [13:51:49] [Render thread/INFO]: Loaded 846 advancements [13:51:52] [Worker-Main-24/ERROR]: Block-attached entity at invalid position: class_2338{x=-28, y=-59, z=-14} [13:51:52] [Worker-Main-24/ERROR]: Block-attached entity at invalid position: class_2338{x=-29, y=-59, z=-14} [13:51:52] [Worker-Main-24/ERROR]: Block-attached entity at invalid position: class_2338{x=-30, y=-59, z=-14} [13:51:52] [Worker-Main-24/ERROR]: Block-attached entity at invalid position: class_2338{x=-25, y=-57, z=-14} [13:51:52] [Worker-Main-24/ERROR]: Block-attached entity at invalid position: class_23

- [ ] **gh-issue:wisp-forest/owo-lib#251** (github_issue, 1/6 conditions)
  - owo-lib issue #251: Error in output
  - https://github.com/wisp-forest/owo-lib/issues/251
  - retrieved by: dense_b#10@r10l
  - excerpt: owo-lib-0.12.10+1.21.jar:?] at io.wispforest.owo.config.ui.ConfigScreen.createWithCustomModel(ConfigScreen.java:103) ~[owo-lib-0.12.10+1.21.jar:?] at io.wispforest.owo.config.ConfigWrapper.lambda$new$6(ConfigWrapper.java:93) ~[owo-lib-0.12.10+1.21.jar:?] [00:02:20] [Render thread/ERROR]: An owo-ui error has occurred during the initial resource reload (on thread Render thread). This is likely a bug caused by *some* other mod initializing an owo-config screen significantly too early - please report it at https://github.com/wisp-forest/owo-lib/issues at io.wispforest.owo.ui.util.UIErrorT

## Added by hand

(none)
