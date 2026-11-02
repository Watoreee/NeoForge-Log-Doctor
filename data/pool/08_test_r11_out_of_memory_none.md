# Judging sheet 08: `r11_out_of_memory_none` (test)

- **Category:** `out_of_memory`  |  **Culprit:** `None`  |  **Acceptable:** (none)
- **What was broken:** set the pack's max RAM to 1000 MB; ran out of memory during mod loading
- **Logs in this scenario:** r11_latest
- **Documents to judge:** 42

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:mezz/JustEnoughItems#4351** (github_issue, 4/6 conditions)
  - JustEnoughItems issue #4351: [Bug]: UI error when opening inventory
  - https://github.com/mezz/JustEnoughItems/issues/4351
  - retrieved by: hybrid_b#1@r11l, hybrid_c#1@r11l, bm25_b#4@r11l, dense_b#4@r11l
  - excerpt: I still have 12 GiB of free space. I thought it might be COW (Copy-on-Write) corrupting data, so I created a new instance/profile, and only installed Fabric API and JEI. I also tried restarting the game multiple times. It's still happening. I tried giving myself /op, setting myself to Creative mode, doing /recipe give @s *, but none of them helped. The game does not crash, only the JEI UI does, so I can still play the game normally. ### latest.log https://gist.github.com/Syntrait/41c04b9450d3e65c524d2ff8ae82b582 [comment by mezz (owner)] Thanks for the report! Can you please include the s

- [ ] **gh-issue:Creators-of-Create/Create#10508** (github_issue, 3/6 conditions)
  - Create issue #10508: Super glue not working
  - https://github.com/Creators-of-Create/Create/issues/10508
  - retrieved by: hybrid_b#9@r11l, hybrid_c#9@r11l, dense_b#1@r11l
  - excerpt: -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx12224M Memory: 2043631496 bytes (1948 MiB) / 9177137152 bytes (8752 MiB) up to 12817793024 bytes (12224 MiB) Total Memory: 7225780344 bytes (6891 MiB) / 9177137152 bytes (8752 MiB) CPU: Intel(R) CC150 CPU @ 3.50GHz @ 3.50 GHz; 7 cores / 7 threads on 1 socket(s) Graphics cards: none Other Mods: YUNG's Better Dungeons: 1.21.1-NeoForge-5.1.4 Sky Aesthetics: 2.0.13-beta KubeJS: 2101.7.2-build.348 SuperMartijn642's Config Library: 1.1.8 Horseman: 1.5.9 Alex's Mobs: 1.22.17 Create Deco: 2.1.3 Pl

- [ ] **gh-issue:mrh0/createaddition#636** (github_issue, 3/6 conditions)
  - createaddition issue #636: Accumulator in Spawn Chunks causing Crash?
  - https://github.com/mrh0/createaddition/issues/636
  - retrieved by: hybrid_b#10@r11l, hybrid_c#10@r11l, bm25_b#1@r11l
  - excerpt: tity` ![screenshot](https://github.com/mrh0/createaddition/assets/83117017/4f07083b-9250-40f5-8b20-1a2e67346add) CSV file of the snapshot: [createaddition.csv](https://github.com/mrh0/createaddition/files/12577000/createaddition.csv) After closing Minecraft it produces error code -805306369 When I encountered this issue first time I tried to do some memory profiling with Spark: `[09:28:40] [spark-worker-pool-1-thread-1/INFO] [minecraft/ChatComponent]: [System] [CHAT] [?] Young Gen GC lasting 198 ms. (cause = G1 Evacuation Pause)\n 298.0 MB moved to G1 Old Gen\n 2.4 GB ? 2.7 GB\n 6

- [ ] **gh-issue:Creators-of-Create/Create#9688** (github_issue, 3/6 conditions)
  - Create issue #9688: Not really a bug but more of a oversight
  - https://github.com/Creators-of-Create/Create/issues/9688
  - retrieved by: hybrid_b#3@r11l, hybrid_c#3@r11l, bm25_b#6@r11l
  - excerpt: 8489271296 bytes (8096 MiB) Total Memory: 3022383296 bytes (2882 MiB) / 6459228160 bytes (6160 MiB) CPU: AMD Custom APU 0405 @ -0.00 GHz; 4 cores / 8 threads on 1 socket(s) Graphics cards: none Other Mods: Enhanced Extinguishing: 1.0.0 YUNG's Better Dungeons: 1.21.1-NeoForge-5.1.4 Forgified Fabric Renderer API (v1): 3.4.0+acb05a3919 YUNG's Better Witch Huts: 1.21.1-NeoForge-4.1.1 GeckoLib 4: 4.8.2 scena: 21.1.18 Forgified Fabric Item API (v1): 11.1.1+57cdfa8219 The Aether: 1.5.10 Saecularia Caudices: 21.1.5 Forgified Fabric Rendering Fluids (v1): 3.1.6+857185bc19 YUNG's Better O

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 2/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: hybrid_a#9@r11l, bm25_a#1@r11l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 2/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#1@r11l, bm25_a#5@r11l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 2/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: hybrid_b#2@r11l, hybrid_c#2@r11l
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#5@r11l, bm25_a#3@r11l
  - excerpt: .util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:507) [?:?] at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1491) [?:?] at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:2073) [?:?] at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2035) [?:?] at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187) [?:?] [28Apr2024 18:58:29.050] [Render thread/FATAL] [net.neoforged.fml.ModLoader/LOADING]: Failed to wait for future Mod Construction, 1 errors found [28Apr2024 18:

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#639** (github_issue, 2/6 conditions)
  - SophisticatedStorage issue #639: Odd Factory Gauge Behavior When Paired With Sophisticated Storage
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/639
  - retrieved by: hybrid_b#4@r11l, hybrid_c#4@r11l
  - excerpt: : Flywheel Version: 1.0.2 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce GTX 1070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 572.83 Graphics Mode: Fancy System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.3, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx8192m Memory: 2006231608 bytes (1913 MiB) / 8589934592 bytes (8192 MiB) up to 8589934592 bytes (8192 MiB) Total Memory: 6588243616 bytes (6283 MiB) / 8589934592 bytes (8192 MiB) CPU: Intel(R) Co

- [ ] **gh-issue:Creators-of-Create/Create#10519** (github_issue, 2/6 conditions)
  - Create issue #10519: Funnel Connected to Packager Incorrectly Extracts Items on a Contraption
  - https://github.com/Creators-of-Create/Create/issues/10519
  - retrieved by: hybrid_b#5@r11l, hybrid_c#5@r11l
  - excerpt: GL Version: 4.6.0 NVIDIA 596.36 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 10 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms512m -Xmx12288m Memory: 555394000 bytes (529 MiB) / 3925868544 bytes (3744 MiB) up to 12884901888 bytes (12288 MiB) Total Memory: 2049565264 bytes (1954 MiB) / 3925868544 bytes (3744 MiB) CPU: AMD Ryzen 7 7700 8-Core Processor @ 3.80 GHz; 8 cores / 16 threads on 1 socket(s) Graphics cards: n

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_b#6@r11l, hybrid_c#6@r11l
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_b#7@r11l, hybrid_c#7@r11l
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:Creators-of-Create/Create#10824** (github_issue, 2/6 conditions)
  - Create issue #10824: [1.21.1] NeoForge: Create: PSI on contraption can't access storage blocks
  - https://github.com/Creators-of-Create/Create/issues/10824
  - retrieved by: hybrid_b#8@r11l, hybrid_c#8@r11l
  - excerpt: : 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.256 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 3050/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 617.42 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.11, Azul Systems, Inc. JVM Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8793** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8793: DOUMENTATION IS INCOMPLETE!!!!
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8793
  - retrieved by: bm25_b#2@r11l
  - excerpt: with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with data from the block, get the error: "Could not load configuration from an incompatible device" ### Expected behavior 1. Get yourself a Memory Card. 2. Get an AE2 block that you can load data from into the cad (any machine, or a pattern provider or a P2P tunnel, anything, doesn't matter) and place it in the world. 3. Put any random item in your off hand. 4. Attempt to load data from the block in step two with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with dat

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: bm25_a#2@r11l
  - excerpt: !/:?] {re:mixin,pl:accesstransformer:B,pl:connector_pre_la [... truncated] [comment by jellysquid3 (member)] Your problem has nothing to do with Sodium. The crash is caused by another mod (Iron Spellbooks?) interacting poorly with the newer version of Create. ``` [25Jun2026 21:56:55.572] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: irons_spellbooks java.lang.NoClassDefFoundError: it/hurts/sskirillss/relics/items/relics/base/IRelicItem ```

- [ ] **gh-issue:Creators-of-Create/Create#10778** (github_issue, 1/6 conditions)
  - Create issue #10778: The encased fan blows air through the non‑ventilated blocks.
  - https://github.com/Creators-of-Create/Create/issues/10778
  - retrieved by: dense_b#2@r11l
  - excerpt: Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx16384M Memory: 1213959216 bytes (1157 MiB) / 6803161088 bytes (6488 MiB) up to 17179869184 bytes (16384 MiB) Total Memory: 5625451472 bytes (5364 MiB) / 6803161088 bytes (6488 MiB) CPU: 12th Gen Intel(R) Core(TM) i5-12500 @ 3.00 GHz; 6 cores / 12 threads on 1 socket(s) Graphics cards: none Other Mods: Saturn: 0.1.5 Concurrent Chunk Management Engine (Fixes/WorldGen/Threading Issues): 0.4.0-alpha.0.117+1.21.1 KubeJS: 2101.7.2-build.368 Create: Deep Seas - Lava Fix: 1.0.1 SuperM

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#2@r11l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:TheIllusiveC4/Curios#521** (github_issue, 1/6 conditions)
  - Curios issue #521: [Bug]: Incorrect slot config syntax corrupts all save games and crashes new world creation
  - https://github.com/TheIllusiveC4/Curios/issues/521
  - retrieved by: dense_b#3@r11l
  - excerpt: assets/32453c00-e99b-43e8-b642-7f9e48b5d845) ![Image](https://github.com/user-attachments/assets/2ac94a63-a0d0-4a48-a423-be214ae18b20) **Crash log** [crash-2025-05-20_15.21.58-client.txt](https://github.com/user-attachments/files/20348587/crash-2025-05-20_15.21.58-client.txt) ### Relevant Log Outputs Error when trying to load the world with incorrect slot syntax: ```java [15:29:17] [Render thread/WARN] [ModernFix/]: Initial datapack load took 312.0 ms [15:29:17] [Render thread/WARN] [minecraft/WorldOpenFlows]: Failed to load level data or datapacks, can't proceed with server load java.util.

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 1/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_a#3@r11l
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **neoforge-docs:docs/1.21.1/networking/streamcodecs** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Stream Codecs
  - https://docs.neoforged.net/docs/1.21.1/networking/streamcodecs/
  - retrieved by: bm25_b#3@r11l
  - excerpt: Additionally, there are some static instances that encode and decode primitives and objects using a different method. #### Unsigned Shorts `UNSIGNED_SHORT` is an alternative of `SHORT` that is meant to be treated as an unsigned number. As numbers are signed in Java, unsigned shorts are sent and received as `Integer`s with the upper two bytes masked out. #### Variable-Sized Number `VAR_INT` and `VAR_LONG` are stream codecs where the value is encoded to be as small as possible. This is done by encoding seven bits at a time, using the upper bit as a marker of whether there is more data for th

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#4@r11l
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: bm25_a#4@r11l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 1/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: bm25_b#5@r11l
  - excerpt: [issue by Bread-NiceCat] Minecraft: 1.21 NeoForge: 21.0.143 Architect Plugin: 3.4.159 Architectury Loom: 1.7.412 ``` modImplementation("thedarkcolour:kotlinforforge-neoforge:5.5.0") ``` ``` Exception in thread "main" java.lang.module.ResolutionException: Module thedarkcolour.kotlinforforge reads more than one module named fml_loader at java.base/java.lang.module.Resolver.resolveFail(Resolver.java:900) at java.base/java.lang.module.Resolver.checkExportSuppliers(Resolver.java:721) at java.base/java.lang.module.Resolver.finish(Resolver.java:380) at java.base/java.lang.module.Confi

- [ ] **gh-issue:wisp-forest/owo-lib#29** (github_issue, 1/6 conditions)
  - owo-lib issue #29: [1.18.2] Crash in the end on chunk gen, light engine maybe?
  - https://github.com/wisp-forest/owo-lib/issues/29
  - retrieved by: dense_b#5@r11l
  - excerpt: [issue by itsdinkd] ```java ---- Minecraft Crash Report ---- // I just don't know what went wrong :( Time: 6/6/22, 1:51 AM Description: Feature placement java.util.ConcurrentModificationException at java.util.HashMap.forEach(HashMap.java:1424) at net.minecraft.world.gen.feature.OreFeature.handler$iln001$coping(OreFeature:1054) at net.minecraft.world.gen.feature.OreFeature.generateVeinPart(OreFeature:175) at net.minecraft.world.gen.feature.OreFeature.generate(OreFeature:52) at net.minecraft.world.gen.feature.Feature.generateIfValid(Feature:163) at net.minecraft.world.gen.fe

- [ ] **gh-issue:embeddedt/ModernFix#535** (github_issue, 1/6 conditions)
  - ModernFix issue #535: Caught exception in thread: java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab (net.minecraft.client.gui.tab.Tab)
  - https://github.com/embeddedt/ModernFix/issues/535
  - retrieved by: hybrid_a#6@r11l
  - excerpt: [issue by meyverick] ### Bug Description ``` [08:01:30] [Worker-ResourceReload-0/ERROR]: Caught exception in thread Thread[#178,Worker-ResourceReload-0,8,main] java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab at java.base/java.lang.ClassLoader.defineClass1(Native Method) ~[?:?] at java.base/java.lang.ClassLoader.defineClass(ClassLoader.java:1026) ~[?:?] at java.base/java.security.SecureClassLoader.defineClass(SecureClassLoader.java:150) ~[?:?] at net.fabricmc.loader.impl.launch.knot.KnotClassLoader.defineClassFwd(KnotClassLoader.java:160) ~[fabr

- [ ] **gh-issue:mezz/JustEnoughItems#4463** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4463: [Crash]: Viewing mob drops from JER causes an IndexOutOfBoundsException (1.21.1 NeoForge)
  - https://github.com/mezz/JustEnoughItems/issues/4463
  - retrieved by: dense_b#6@r11l
  - excerpt: [issue by Luviam] ### Steps to Reproduce the Crash 1. Open a world with the latest version of JER and a version of JEI that is > 19.50.0.414 2. Open the inventory menu and click on a mob drop within the JEI menu. 3. View mobs that drop said item. (You might need to wait a few seconds or click on the GUI) ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) _No response_ ### Crash Report https://mclo.gs/Nmn6USx [comment by mezz (owner)] Thanks for the report! This is a duplicate of * #4461 It has already been fixed on 1.2

- [ ] **gh-issue:thedarkcolour/KotlinForForge#89** (github_issue, 1/6 conditions)
  - KotlinForForge issue #89: KFF crash on MC 1.20.4 with MinecraftForge 49.0.8
  - https://github.com/thedarkcolour/KotlinForForge/issues/89
  - retrieved by: bm25_a#6@r11l
  - excerpt: [issue by Prototik] ``` [13Dec2023 14:19:03.511] [modloading-worker-0/ERROR] [thedarkcolour.kotlinforforge.LoggerKt/LOADING]: Failed to register Automatic Kotlin subscribers. ModID: kotlinforforge, class thedarkcolour.kotlinforforge.test.KotlinForForge java.lang.NoClassDefFoundError: net/minecraftforge/fml/loading/moddiscovery/ModAnnotation$EnumHolder at thedarkcolour.kotlinforforge.AutoKotlinEventBusSubscriber.<clinit>(AutoKotlinEventBusSubscriber.kt:40) ~[kfflang-4.8.0.jar%239!/:4.8.0] at thedarkcolour.kotlinforforge.KotlinModContainer.constructMod(KotlinModContainer.kt:74) ~[kfflang-4

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8983** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8983: Duplicate MenuType registration crash in InitMenuTypes.registerAll (AE2 19.2.17, NeoForge 1.21.1) — reproduces with all addons disabled
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8983
  - retrieved by: bm25_a#7@r11l
  - excerpt: [issue by JFloresAranda] ### Describe the bug As i have grown to enjoy a lot this mod an its addons, the pack im developing wouldnt be an exception. However i disabled all of them and the game would still crash. I disabled Ae2 and the game starts. AE2 throws `java.lang.IllegalStateException: Adding duplicate value 'net.minecraft.world.inventory.MenuType@...' to registry` during its own `RegisterEvent` handling, which causes a `ModLoadingException` ("Failed to register some entries") during game startup. The crash happens consistently, in the same place, in `InitMenuTypes.registerAll` (

- [ ] **gh-issue:architectury/architectury-api#290** (github_issue, 1/6 conditions)
  - architectury-api issue #290: Error could not initizlize class net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents
  - https://github.com/architectury/architectury-api/issues/290
  - retrieved by: bm25_b#7@r11l
  - excerpt: .fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at top.catowncraft.carpettctcaddition.CarpetTCTCAddition.onInitialize(CarpetTCTCAddition.java:68) at net.fabricmc.loader.impl.entrypoint.EntrypointUtils.invoke0(EntrypointUtils.java:47) ... 7 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 1/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: dense_b#7@r11l
  - excerpt: # mixin.bugfix.ctm_resourceutil_cme=true # (default) # mixin.bugfix.ender_dragon_leak=true # (default) # mixin.bugfix.entity_pose_stack=true # (default) # mixin.bugfix.extra_experimental_screen=true # (default) # mixin.bugfix.fix_config_crashes=true # (default) # mixin.bugfix.missing_block_entities=false # (default) # mixin.bugfix.packet_leak=false # (default) # mixin.bugfix.paper_chunk_patches=false # (overridden for mod compat) # mixin.bugfix.recipe_book_type_desync=true # (default) # mixin.bugfix.restore_old_dragon_movement=false # (default) # mixin.bugfix.skip_redundant_saves=fa

- [ ] **gh-issue:thedarkcolour/KotlinForForge#98** (github_issue, 1/6 conditions)
  - KotlinForForge issue #98: Not working on Neoforge 20.6.14+
  - https://github.com/thedarkcolour/KotlinForForge/issues/98
  - retrieved by: hybrid_a#7@r11l
  - excerpt: [issue by <user>-1984] Okay so this might be my fault somehow, but I really can't figure it out. Everything was working fine on 20.6.1, but after updating to 20.6.14, I'm getting a weird crash report: <details><summary>Crash report</summary> ``` ---- Minecraft Crash Report ---- // There are four lights! Time: 2024-05-03 00:09:13 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at TRANSFORMER/neoforge@20.6.14-beta/net.neoforged.neoforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:56) ~[neoforge-20.6.14-beta

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#931** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #931: [Create][1.21.1] Stack upgrades on max barrels kick players (IndexOutOfBoundsException
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/931
  - retrieved by: dense_b#8@r11l
  - excerpt: out of bounds exception, I thought it might be related, so I created the ticket. [comment by P3pp3rF1y (owner)] You will need to report this one to create, sounds like perhaps stock ticker isn't ready for that many slots.

- [ ] **gh-issue:malte0811/FerriteCore#155** (github_issue, 1/6 conditions)
  - FerriteCore issue #155: Crash running Create+
  - https://github.com/malte0811/FerriteCore/issues/155
  - retrieved by: bm25_b#8@r11l
  - excerpt: er.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@10.0.8/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@1.1.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:141) Caused by: java.lang.reflect.InvocationTargetException at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:119) at java.base/java.lang.reflect.Method.invoke(Method.java:578) at MC-BOOTSTRAP/fmlloader@1.19.2-43.3.0/net.minecraftforge.fml.loading.targets.Co

- [ ] **gh-issue:mrh0/createaddition#1118** (github_issue, 1/6 conditions)
  - createaddition issue #1118: 1.21 - Recipe (Port?) Issue
  - https://github.com/mrh0/createaddition/issues/1118
  - retrieved by: hybrid_a#8@r11l
  - excerpt: [issue by CynSolveroftheAbsolute] **Describe the bug** Heyo, if you see this somewhere else, I'm bulk copy-pasting 'cuz I've got ~460 warnings in Kubejs and none of them are mine :D Not sure what the exact steps to reproduce are, but I do know your mod has an incorrect recipe or two. I'm attaching the KubeJS server script log so you can see what recipes are causing issues and try to understand why, but if they're like the first one that I made an issue for, which I knew a bit more about, you've left a residue of porting from 1.20 to 1.21 in a recipe (`"item": {"id": "minecraft:cobblestone"}` w

- [ ] **gh-issue:thedarkcolour/KotlinForForge#105** (github_issue, 1/6 conditions)
  - KotlinForForge issue #105: Wrong fml translation key used, leading to crash when displaying loading errors
  - https://github.com/thedarkcolour/KotlinForForge/issues/105
  - retrieved by: bm25_a#8@r11l
  - excerpt: [issue by Erdragh] ``` java.lang.IllegalArgumentException: When using FML translation keys, only use fml.modloadingissue. keys for mod loading issues: fml.modloading.javafml.dangling_entrypoint at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:30) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.<init>(ModLoadingIssue.java:24) ~[loader-4.0.24.jar%23132!/:4.0] {} at MC-BOOTSTRAP/fml_loader@4.0.24/net.neoforged.fml.ModLoadingIssue.error(ModLoadingIssue.java:35) ~[loader-4.0.24.jar%23132!/:

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#640** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #640: Multiple item removing bugs with limited barrel 1.21.1
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/640
  - retrieved by: dense_b#9@r11l
  - excerpt: java:124) ~[loader-4.0.38.jar%23111!/:4.0] at MC-BOOTSTRAP/fml_loader@4.0.38/net.neoforged.fml.loading.targets.CommonClientLaunchHandler.runService(CommonClientLaunchHandler.java:32) ~[loader-4.0.38.jar%23111!/:4.0] at MC-BOOTSTRAP/fml_loader@4.0.38/net.neoforged.fml.loading.targets.CommonLaunchHandler.lambda$launchService$4(CommonLaunchHandler.java:118) ~[loader-4.0.38.jar%23111!/:4.0] at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.LaunchServiceHandlerDecorator.launch(LaunchServiceHandlerDecorator.java:30) [modlauncher-11.0.4.jar%23119!/:?] at MC-BOOTSTRAP/cpw.mods.modla

- [ ] **gh-issue:architectury/architectury-api#432** (github_issue, 1/6 conditions)
  - architectury-api issue #432: Archiectury crashes during pre-load 
  - https://github.com/architectury/architectury-api/issues/432
  - retrieved by: bm25_b#9@r11l
  - excerpt: it>(class_310.java:458) at net.minecraft.client.main.Main.main(Main.java:211) at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:468) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.NoClassDefFoundError: Could not initialize class net.fabricmc.fabric.api.client.rendering.v1.HudRenderCallback at net.mehvahdjukaar.supplementaries.common.events.fabric.ClientEventsFabric.init(ClientEventsFabric.java:39) at net.mehvahdjuk

- [ ] **gh-issue:embeddedt/ModernFix#651** (github_issue, 1/6 conditions)
  - ModernFix issue #651: Crash on startup with `mixin.perf.dynamic_resources=true` — incompatibility with Create: Teleporters
  - https://github.com/embeddedt/ModernFix/issues/651
  - retrieved by: bm25_a#9@r11l
  - excerpt: [issue by Kur-Dev] ## Crash on startup with `mixin.perf.dynamic_resources=true` — incompatibility with Create: Teleporters **ModernFix version:** `modernfix-neoforge-5.26.1+mc1.21.1` **Minecraft version:** 1.21.1 **NeoForge version:** 21.1.224 **Create: Teleporters version:** `createteleporters-remastered-2.0.1d-neoforge-1.21.1.jar` (latest) [Create: Teleporters 2.0.2a](https://modrinth.com/mod/create-teleporters/version/2.0.2a) ### Description When `mixin.perf.dynamic_resources=true` is manually enabled in `config/modernfix-mixins.properties`, the game crashes at startup during the title s

- [ ] **gh-issue:CaffeineMC/sodium#2731** (github_issue, 1/6 conditions)
  - sodium issue #2731: Problem with launching minecraft 1.21.1 with sodium
  - https://github.com/CaffeineMC/sodium/issues/2731
  - retrieved by: bm25_b#10@r11l
  - excerpt: to errors, provided by 'sodium' at 'net.caffeinemc.mods.sodium.fabric.SodiumPreLaunch'! at net.fabricmc.loader.impl.FabricLoaderImpl.lambda$invokeEntrypoints$2(FabricLoaderImpl.java:403) at net.fabricmc.loader.impl.util.ExceptionUtil.gatherExceptions(ExceptionUtil.java:33) at net.fabricmc.loader.impl.FabricLoaderImpl.invokeEntrypoints(FabricLoaderImpl.java:401) at net.fabricmc.loader.impl.launch.knot.Knot.init(Knot.java:160) ... 5 more Caused by: java.lang.UnsatisfiedLinkError: C:\Users\?????\AppData\Local\Temp\jna-1007792265\jna6873146617604809216.dll: Can't find dependent librarie

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: hybrid_a#10@r11l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:mrh0/createaddition#980** (github_issue, 1/6 conditions)
  - createaddition issue #980: Portable drill incompatible with quark matrix enchanting
  - https://github.com/mrh0/createaddition/issues/980
  - retrieved by: bm25_a#10@r11l
  - excerpt: [issue by CorneliusCornbread] **Describe the bug** Attempting to enchant the portable drill with quark enchant system will results in a ticking exception. In this case it's caught by Neruina and the enchantment table is suspended from ticking to prevent server crashes. **To Reproduce** Steps to reproduce the behavior: 1. Install quark + quark oddities 2. Install create + create crafts and additions 3. Place enchantment table 4. Place portable drill in enchantment table 5. Crash **Additional context** - Mod version: 1.20.1-1.3.1 - Forge version: 47.4.0 - Create version: 6.0.4 ``` [21:50:35]

- [ ] **gh-issue:wisp-forest/owo-lib#251** (github_issue, 1/6 conditions)
  - owo-lib issue #251: Error in output
  - https://github.com/wisp-forest/owo-lib/issues/251
  - retrieved by: dense_b#10@r11l
  - excerpt: owo-lib-0.12.10+1.21.jar:?] at io.wispforest.owo.config.ui.ConfigScreen.createWithCustomModel(ConfigScreen.java:103) ~[owo-lib-0.12.10+1.21.jar:?] at io.wispforest.owo.config.ConfigWrapper.lambda$new$6(ConfigWrapper.java:93) ~[owo-lib-0.12.10+1.21.jar:?] [00:02:20] [Render thread/ERROR]: An owo-ui error has occurred during the initial resource reload (on thread Render thread). This is likely a bug caused by *some* other mod initializing an owo-config screen significantly too early - please report it at https://github.com/wisp-forest/owo-lib/issues at io.wispforest.owo.ui.util.UIErrorT

## Added by hand

(none)
