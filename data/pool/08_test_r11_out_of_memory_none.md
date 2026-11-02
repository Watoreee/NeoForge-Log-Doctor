# Judging sheet 08: `r11_out_of_memory_none` (test)

- **Category:** `out_of_memory`  |  **Culprit:** `None`  |  **Acceptable:** (none)
- **What was broken:** set the pack's max RAM to 1000 MB; ran out of memory during mod loading
- **Logs in this scenario:** r11_latest
- **Documents to judge:** 38

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:TwelveIterations/Balm#211** (github_issue, 4/6 conditions)
  - Balm issue #211: JEI integration causes massive memory leak / system crash on Fabric 1.21.11
  - https://github.com/TwelveIterations/Balm/issues/211
  - retrieved by: hybrid_b#1@r11l, hybrid_c#1@r11l, bm25_b#1@r11l, dense_b#10@r11l
  - excerpt: stable (~2 GB) Exit the game Add Just Enough Items (JEI) (latest Fabric build) Launch Minecraft again Load a world and open the inventory Result Memory usage rapidly increases from ~2 GB to 5–6 GB JVM heap remains limited to 4 GB, but total system memory keeps growing Severe lag occurs, followed by a full system freeze or crash Control Test Removing JEI while keeping all other mods installed returns memory usage to normal and the game runs stably. Machine Specs CPU: Intel i3 (older generation) RAM: 8 GB GPU: Intel HD Graphics (shared memory) OS: Windows Java: Java 25 (also repr

- [ ] **gh-issue:mezz/JustEnoughItems#4351** (github_issue, 4/6 conditions)
  - JustEnoughItems issue #4351: [Bug]: UI error when opening inventory
  - https://github.com/mezz/JustEnoughItems/issues/4351
  - retrieved by: hybrid_b#2@r11l, hybrid_c#2@r11l, bm25_b#5@r11l, dense_b#5@r11l
  - excerpt: I still have 12 GiB of free space. I thought it might be COW (Copy-on-Write) corrupting data, so I created a new instance/profile, and only installed Fabric API and JEI. I also tried restarting the game multiple times. It's still happening. I tried giving myself /op, setting myself to Creative mode, doing /recipe give @s *, but none of them helped. The game does not crash, only the JEI UI does, so I can still play the game normally. ### latest.log https://gist.github.com/Syntrait/41c04b9450d3e65c524d2ff8ae82b582 [comment by mezz (owner)] Thanks for the report! Can you please include the s

- [ ] **gh-issue:TwelveIterations/Balm#123** (github_issue, 3/6 conditions)
  - Balm issue #123: [Crash] ticking hopper below Cooking for blockheads' Oven tries to take item from slot 4 (only 3 slots)
  - https://github.com/TwelveIterations/Balm/issues/123
  - retrieved by: hybrid_b#7@r11l, hybrid_c#7@r11l, dense_b#1@r11l
  - excerpt: [issue by MindStudioOfficial] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader Fabric ### Describe the Issue placing a hopper below a cooking for blockheads oven which has 3 input slots and 3 output slots crashes the server whenever the block is loaded and ticked because it tries to take items from slot 4 of 3 (IndexOutOfBounds) ``` java.lang.IndexOutOfBoundsException: Index 4 out of bounds for length 3 at java.base/jdk.internal.util.Preconditions.outOfBounds(Unknown Source) at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Unknown Source) at java.base/jdk.internal.u

- [ ] **gh-issue:Creators-of-Create/Create#10508** (github_issue, 3/6 conditions)
  - Create issue #10508: Super glue not working
  - https://github.com/Creators-of-Create/Create/issues/10508
  - retrieved by: hybrid_b#8@r11l, hybrid_c#8@r11l, dense_b#2@r11l
  - excerpt: -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx12224M Memory: 2043631496 bytes (1948 MiB) / 9177137152 bytes (8752 MiB) up to 12817793024 bytes (12224 MiB) Total Memory: 7225780344 bytes (6891 MiB) / 9177137152 bytes (8752 MiB) CPU: Intel(R) CC150 CPU @ 3.50GHz @ 3.50 GHz; 7 cores / 7 threads on 1 socket(s) Graphics cards: none Other Mods: YUNG's Better Dungeons: 1.21.1-NeoForge-5.1.4 Sky Aesthetics: 2.0.13-beta KubeJS: 2101.7.2-build.348 SuperMartijn642's Config Library: 1.1.8 Horseman: 1.5.9 Alex's Mobs: 1.22.17 Create Deco: 2.1.3 Pl

- [ ] **gh-issue:mrh0/createaddition#636** (github_issue, 3/6 conditions)
  - createaddition issue #636: Accumulator in Spawn Chunks causing Crash?
  - https://github.com/mrh0/createaddition/issues/636
  - retrieved by: hybrid_b#10@r11l, hybrid_c#10@r11l, bm25_b#2@r11l
  - excerpt: tity` ![screenshot](https://github.com/mrh0/createaddition/assets/83117017/4f07083b-9250-40f5-8b20-1a2e67346add) CSV file of the snapshot: [createaddition.csv](https://github.com/mrh0/createaddition/files/12577000/createaddition.csv) After closing Minecraft it produces error code -805306369 When I encountered this issue first time I tried to do some memory profiling with Spark: `[09:28:40] [spark-worker-pool-1-thread-1/INFO] [minecraft/ChatComponent]: [System] [CHAT] [?] Young Gen GC lasting 198 ms. (cause = G1 Evacuation Pause)\n 298.0 MB moved to G1 Old Gen\n 2.4 GB ? 2.7 GB\n 6

- [ ] **gh-issue:Creators-of-Create/Create#10778** (github_issue, 3/6 conditions)
  - Create issue #10778: The encased fan blows air through the non‑ventilated blocks.
  - https://github.com/Creators-of-Create/Create/issues/10778
  - retrieved by: hybrid_b#9@r11l, hybrid_c#9@r11l, dense_b#3@r11l
  - excerpt: Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx16384M Memory: 1213959216 bytes (1157 MiB) / 6803161088 bytes (6488 MiB) up to 17179869184 bytes (16384 MiB) Total Memory: 5625451472 bytes (5364 MiB) / 6803161088 bytes (6488 MiB) CPU: 12th Gen Intel(R) Core(TM) i5-12500 @ 3.00 GHz; 6 cores / 12 threads on 1 socket(s) Graphics cards: none Other Mods: Saturn: 0.1.5 Concurrent Chunk Management Engine (Fixes/WorldGen/Threading Issues): 0.4.0-alpha.0.117+1.21.1 KubeJS: 2101.7.2-build.368 Create: Deep Seas - Lava Fix: 1.0.1 SuperM

- [ ] **gh-issue:GlodBlock/ExtendedAE#422** (github_issue, 2/6 conditions)
  - ExtendedAE issue #422: kubejs error with extended ae
  - https://github.com/GlodBlock/ExtendedAE/issues/422
  - retrieved by: hybrid_a#1@r11l, bm25_a#3@r11l
  - excerpt: [issue by baka4n] etails: Mod file: /C:/Users/<user>/.gradle/caches/modules-2/files-2.1/dev.latvian.mods/kubejs-neoforge/2101.7.2-build.233/7c5dbc2e152f819c929b51fcf1247747770af4c9/kubejs-neoforge-2101.7.2-build.233.jar Failure message: KubeJS (kubejs) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.NoSuchMethodError: 'void dev.latvian.mods.kubejs.registry.BuilderTypeRegistry$Callback.add(java.lang.String, java.lang.Class, dev.latvian.mods.kubejs.registry.BuilderFactory)' Mod version: 2101.7.2-build.233 Mod issues URL: https://ku

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 2/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: hybrid_a#10@r11l, bm25_a#1@r11l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 2/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#2@r11l, bm25_a#8@r11l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:Creators-of-Create/Create#10533** (github_issue, 2/6 conditions)
  - Create issue #10533: ~~deployer issue~~ I just didnt know how it worked
  - https://github.com/Creators-of-Create/Create/issues/10533
  - retrieved by: hybrid_b#3@r11l, hybrid_c#3@r11l
  - excerpt: [issue by judeaf100-alt] ### Description ~~Deployer on mechanical bearing are throwing the stuff away its schematic filtered~~ but it wont work ### Game Log https://mclo.gs/Ya0eY4d ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.233 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: irisflw:iris_instancing OpenGL Renderer: NVIDIA GeForce RTX 5070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 596

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#12** (github_issue, 2/6 conditions)
  - YUNGs-API issue #12: server crash
  - https://github.com/YUNG-GANG/YUNGs-API/issues/12
  - retrieved by: hybrid_b#4@r11l, hybrid_c#4@r11l
  - excerpt: transformer:B} at net.minecraft.server.MinecraftServer.func_240802_v_(MinecraftServer.java:774) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at net.minecraft.server.MinecraftServer.func_240783_a_(MinecraftServer.java:269) ~[?:?] {re:classloading,pl:accesstransformer:B,pl:runtimedistcleaner:A} at java.lang.Thread.run(Thread.java:831) [?:?] {} A detailed walkthrough of the error, its code path and all known details is as follows: --------------------------------------------------------------------------------------- -- System Details -- Details: Minec

- [ ] **gh-issue:Creators-of-Create/Create#10340** (github_issue, 2/6 conditions)
  - Create issue #10340: The problem with infinite storage
  - https://github.com/Creators-of-Create/Create/issues/10340
  - retrieved by: hybrid_b#5@r11l, hybrid_c#5@r11l
  - excerpt: [issue by pavel1992x] ### Description When using infinite storage in the logistics system of this mod, a temporary freeze occurs. ### Game Log https://mclo.gs/6peAUUQ ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Radeon RX 6700 OpenGL Version: 4.6.0 Core Profile Context 26.5.1.260407 Graphics Mode: f

- [ ] **gh-issue:Creators-of-Create/Create#10593** (github_issue, 2/6 conditions)
  - Create issue #10593: [BUG] Stock Links connected to same location reports contents multiple times [6.0.10]
  - https://github.com/Creators-of-Create/Create/issues/10593
  - retrieved by: hybrid_b#6@r11l, hybrid_c#6@r11l
  - excerpt: <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.10 Mod Git Commit: ac0c444d9828da3453ae8cc65338e8de063286fb Ponder Version: 1.0.82+mc1.21.1 NeoForge Version: 21.1.228 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.6 Flywheel Backend: flywheel:indirect OpenGL Renderer: NVIDIA GeForce RTX 3070/PCIe/SSE2 OpenGL Version: 4.6.0 NVIDIA 591.86 Graphics Mode: fancy PojavLauncher Detected: false System Information: Operating System: Windows 11 (amd64) version 10.0 Java Version: 21.0.7, Microsoft JVM Flags: 3 total; -XX:HeapDumpPath=MojangTricksIntelDriv

- [ ] **gh-issue:thedarkcolour/KotlinForForge#96** (github_issue, 2/6 conditions)
  - KotlinForForge issue #96: Missing enum constant EventBusSubscriber.Bus.FORGE
  - https://github.com/thedarkcolour/KotlinForForge/issues/96
  - retrieved by: hybrid_a#6@r11l, bm25_a#6@r11l
  - excerpt: .util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:507) [?:?] at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1491) [?:?] at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:2073) [?:?] at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2035) [?:?] at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187) [?:?] [28Apr2024 18:58:29.050] [Render thread/FATAL] [net.neoforged.fml.ModLoader/LOADING]: Failed to wait for future Mod Construction, 1 errors found [28Apr2024 18:

- [ ] **gh-issue:GlodBlock/ExtendedAE#341** (github_issue, 1/6 conditions)
  - ExtendedAE issue #341: [Render thread/ERROR] appeng/client/guidebook/color/ColorValue
  - https://github.com/GlodBlock/ExtendedAE/issues/341
  - retrieved by: bm25_a#2@r11l
  - excerpt: [issue by YoSiJo] ``` [21:54:01] [Render thread/ERROR] [ne.ne.fm.ModContainer/LOADING]: Caught exception during event net.neoforged.neoforge.client.event.RegisterMenuScreensEvent@2ba7828b dispatch for modid extendedae java.lang.NoClassDefFoundError: appeng/client/guidebook/color/ColorValue at TRANSFORMER/extendedae@1.21-2.0.1-neoforge/com.glodblock.github.extendedae.client.ClientRegistryHandler.registerGui(ClientRegistryHandler.java:108) ~[ExtendedAE-1.21-2.0.1-neoforge.jar%23219!/:?] {re:classloading} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) ~[bus

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8793** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8793: DOUMENTATION IS INCOMPLETE!!!!
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8793
  - retrieved by: bm25_b#3@r11l
  - excerpt: with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with data from the block, get the error: "Could not load configuration from an incompatible device" ### Expected behavior 1. Get yourself a Memory Card. 2. Get an AE2 block that you can load data from into the cad (any machine, or a pattern provider or a P2P tunnel, anything, doesn't matter) and place it in the world. 3. Put any random item in your off hand. 4. Attempt to load data from the block in step two with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with dat

- [ ] **gh-issue:thedarkcolour/KotlinForForge#18** (github_issue, 1/6 conditions)
  - KotlinForForge issue #18: Crashing with kotlinforforge installed
  - https://github.com/thedarkcolour/KotlinForForge/issues/18
  - retrieved by: hybrid_a#3@r11l
  - excerpt: ~[?:?] {re:classloading,xf:OptiFine:default} at net.minecraft.client.renderer.RenderType.func_228633_a_(RenderType.java:577) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType.lambda$getText$18(RenderType.java:495) ~[?:?] {re:classloading,xf:OptiFine:default,re:mixin} at net.minecraft.client.renderer.RenderType$$Lambda$10152/2010484538.get(Unknown Source) ~[?:?] {} at net.minecraft.cl [... truncated] [comment by thedarkcolour (owner)] Can you send the full log? [comment by ghoodsite (none)] I'm having the same issue with forge 36.1.2 / m

- [ ] **gh-issue:TheIllusiveC4/Curios#521** (github_issue, 1/6 conditions)
  - Curios issue #521: [Bug]: Incorrect slot config syntax corrupts all save games and crashes new world creation
  - https://github.com/TheIllusiveC4/Curios/issues/521
  - retrieved by: dense_b#4@r11l
  - excerpt: assets/32453c00-e99b-43e8-b642-7f9e48b5d845) ![Image](https://github.com/user-attachments/assets/2ac94a63-a0d0-4a48-a423-be214ae18b20) **Crash log** [crash-2025-05-20_15.21.58-client.txt](https://github.com/user-attachments/files/20348587/crash-2025-05-20_15.21.58-client.txt) ### Relevant Log Outputs Error when trying to load the world with incorrect slot syntax: ```java [15:29:17] [Render thread/WARN] [ModernFix/]: Initial datapack load took 312.0 ms [15:29:17] [Render thread/WARN] [minecraft/WorldOpenFlows]: Failed to load level data or datapacks, can't proceed with server load java.util.

- [ ] **gh-issue:architectury/architectury-api#674** (github_issue, 1/6 conditions)
  - architectury-api issue #674: [1.21.10] Crash between Architectury 18.0.6 and Neoforge 21.10.38-beta
  - https://github.com/architectury/architectury-api/issues/674
  - retrieved by: bm25_a#4@r11l
  - excerpt: [issue by ffuentesm] Changes in Neoforge 21.10.35-beta cause another incompatibility. Here is the log: When using Neoforge 21.10.37-beta: crash-2025-11-05_11.28.10-client.txt: https://gnomebot.dev/paste/mclogs/q5XwKon crash-2025-10-26_23.20.57-client.txt: https://gnomebot.dev/paste/mclogs/03RIhcH latest.log: https://gnomebot.dev/paste/mclogs/BKpoeXv `[461](https://gnomebot.dev/paste/mclogs/BKpoeXv#L461) [26Oct2025 23:20:54.060] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: architectury [462](https://gno

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#4@r11l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **neoforge-docs:docs/1.21.1/networking/streamcodecs** (neoforge_docs, 1/6 conditions)
  - NeoForge docs: Stream Codecs
  - https://docs.neoforged.net/docs/1.21.1/networking/streamcodecs/
  - retrieved by: bm25_b#4@r11l
  - excerpt: Additionally, there are some static instances that encode and decode primitives and objects using a different method. #### Unsigned Shorts `UNSIGNED_SHORT` is an alternative of `SHORT` that is meant to be treated as an unsigned number. As numbers are signed in Java, unsigned shorts are sent and received as `Integer`s with the upper two bytes masked out. #### Variable-Sized Number `VAR_INT` and `VAR_LONG` are stream codecs where the value is encoded to be as small as possible. This is done by encoding seven bits at a time, using the upper bit as a marker of whether there is more data for th

- [ ] **gh-issue:CaffeineMC/sodium#3771** (github_issue, 1/6 conditions)
  - sodium issue #3771: Sodium bug 8.2 beta  neoforge 1.21.1 crash
  - https://github.com/CaffeineMC/sodium/issues/3771
  - retrieved by: bm25_a#5@r11l
  - excerpt: !/:?] {re:mixin,pl:accesstransformer:B,pl:connector_pre_la [... truncated] [comment by jellysquid3 (member)] Your problem has nothing to do with Sodium. The crash is caused by another mod (Iron Spellbooks?) interacting poorly with the newer version of Create. ``` [25Jun2026 21:56:55.572] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to register automatic subscribers. ModID: irons_spellbooks java.lang.NoClassDefFoundError: it/hurts/sskirillss/relics/items/relics/base/IRelicItem ```

- [ ] **gh-issue:thedarkcolour/KotlinForForge#160** (github_issue, 1/6 conditions)
  - KotlinForForge issue #160: new update causing mod not to load
  - https://github.com/thedarkcolour/KotlinForForge/issues/160
  - retrieved by: hybrid_a#5@r11l
  - excerpt: [issue by ThunderHacker11] When updating to Kotlin for forge 5.12 it does not load causing all dependent mods to fail to load, here is a sample of the crash -- Mod loading issue -- Details: Mod file: <No mod information provided> Failure message: Mod File mods\Cobblemon-neoforge-1.7.3+1.21.1.jar needs language provider kotlinforforge:5.3 or above to load We have found - Mod version: <No mod information provided> Mod issues URL: <No issues URL found> Exception message: <No associated exception found> NeoForge 1.21.1 NeoForge Version: 21.1.233 [comment by thedarkcolour (owner)] Does 5.

- [ ] **gh-issue:Creators-of-Create/Create#9688** (github_issue, 1/6 conditions)
  - Create issue #9688: Not really a bug but more of a oversight
  - https://github.com/Creators-of-Create/Create/issues/9688
  - retrieved by: bm25_b#6@r11l
  - excerpt: [issue by ensign-labs] ### Description So I have been messing around with Create and the Aether mods. Apparently Skyroot isn't considered a woodtype in the mod ### Game Log https://mclo.gs/2FbrFip ### Debug Information <details> <summary>Client Info</summary> ``` Create: Mod Version: 6.0.8 Mod Git Commit: 5f1b407a97467157e7a0da0c560c7d1d5f378929 Ponder Version: 1.0.64 NeoForge Version: 21.1.215 Minecraft Version: 1.21.1 Graphics: Flywheel Version: 1.0.5 Flywheel Backend: flywheel:indirect OpenGL Renderer: AMD Custom GPU 0405 (radeonsi, vangogh, LLVM 19.1.7, DRM 3.59, 6.11.11-val

- [ ] **gh-issue:wisp-forest/owo-lib#29** (github_issue, 1/6 conditions)
  - owo-lib issue #29: [1.18.2] Crash in the end on chunk gen, light engine maybe?
  - https://github.com/wisp-forest/owo-lib/issues/29
  - retrieved by: dense_b#6@r11l
  - excerpt: [issue by itsdinkd] ```java ---- Minecraft Crash Report ---- // I just don't know what went wrong :( Time: 6/6/22, 1:51 AM Description: Feature placement java.util.ConcurrentModificationException at java.util.HashMap.forEach(HashMap.java:1424) at net.minecraft.world.gen.feature.OreFeature.handler$iln001$coping(OreFeature:1054) at net.minecraft.world.gen.feature.OreFeature.generateVeinPart(OreFeature:175) at net.minecraft.world.gen.feature.OreFeature.generate(OreFeature:52) at net.minecraft.world.gen.feature.Feature.generateIfValid(Feature:163) at net.minecraft.world.gen.fe

- [ ] **gh-issue:GlodBlock/ExtendedAE#399** (github_issue, 1/6 conditions)
  - ExtendedAE issue #399: I get this error when using ExtendedAE with KubeJS
  - https://github.com/GlodBlock/ExtendedAE/issues/399
  - retrieved by: hybrid_a#7@r11l
  - excerpt: [issue by Samu2004G] ![Image](https://github.com/user-attachments/assets/7ec997eb-9777-4a45-a738-301faba485fa) I already asked on the KubeJS Discord server, and they said the error was caused by ExtendedAE. The error was related to com.glodblock.github.extendedae.xmod.kjs.KJSPlugin. The mods I had installed were: Using NeoForge version 21.1.146 for Minecraft 1.21.1 Mod list: • AE2WTLib API 19.2.0 • Applied Energistics 2 19.2.8 • ExtendedAE 1.21-2.2.8-neoforge • Glodium 1.21-2.2-neoforge • GuideME 21.1.7 • KubeJS 2101.7.2-build.231 • Rhino 2101.2.7-build.74 [crash-2025-04-12_21

- [ ] **gh-issue:mezz/JustEnoughItems#4463** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4463: [Crash]: Viewing mob drops from JER causes an IndexOutOfBoundsException (1.21.1 NeoForge)
  - https://github.com/mezz/JustEnoughItems/issues/4463
  - retrieved by: dense_b#7@r11l
  - excerpt: [issue by Luviam] ### Steps to Reproduce the Crash 1. Open a world with the latest version of JER and a version of JEI that is > 19.50.0.414 2. Open the inventory menu and click on a mob drop within the JEI menu. 3. View mobs that drop said item. (You might need to wait a few seconds or click on the GUI) ### Mod Pack URL (Optional) _No response_ ### Mod Pack Version (Optional) _No response_ ### Extra Notes (Optional) _No response_ ### Crash Report https://mclo.gs/Nmn6USx [comment by mezz (owner)] Thanks for the report! This is a duplicate of * #4461 It has already been fixed on 1.2

- [ ] **gh-issue:thedarkcolour/KotlinForForge#106** (github_issue, 1/6 conditions)
  - KotlinForForge issue #106: Unable to load KotlinForForge correctly on Architectury 1.21
  - https://github.com/thedarkcolour/KotlinForForge/issues/106
  - retrieved by: bm25_b#7@r11l
  - excerpt: [issue by Bread-NiceCat] Minecraft: 1.21 NeoForge: 21.0.143 Architect Plugin: 3.4.159 Architectury Loom: 1.7.412 ``` modImplementation("thedarkcolour:kotlinforforge-neoforge:5.5.0") ``` ``` Exception in thread "main" java.lang.module.ResolutionException: Module thedarkcolour.kotlinforforge reads more than one module named fml_loader at java.base/java.lang.module.Resolver.resolveFail(Resolver.java:900) at java.base/java.lang.module.Resolver.checkExportSuppliers(Resolver.java:721) at java.base/java.lang.module.Resolver.finish(Resolver.java:380) at java.base/java.lang.module.Confi

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: bm25_a#7@r11l
  - excerpt: man's Currency and the issue is still present. [comment by Dragon-Seeker (member)] Also possibly this error as well: ``` [02Nov2024 11:04:07.644] [modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: everycomp, class net.mehvahdjukaar.every_compat.neoforge.EveryCompatForge java.lang.IllegalStateException: Bus is null. You must call RegHelper.startRegistering(IEventBus) before registering events at TRANSFORMER/moonlight@1.21-2.15.6/net.mehvahdjukaar.moonlight.neoforge.MoonlightForge.getCurrentBus(MoonlightForge.java:167)

- [ ] **gh-issue:GlodBlock/ExtendedAE#638** (github_issue, 1/6 conditions)
  - ExtendedAE issue #638: [Bug] Error During Mod Loading
  - https://github.com/GlodBlock/ExtendedAE/issues/638
  - retrieved by: hybrid_a#8@r11l
  - excerpt: [issue by Marioluigi7896] Trying to include ExtendedAE in a modpack with a bunch of other mods, however when including the mod AE2 fails to load, disabling the mod fixes the issue. The reported issue in the crashlog seems to be a duplicate resource key, unsure if this will end up being an AE2 issue but since it only appeared with this mod enabled I figured I'd report here first. ``java.lang.IllegalStateException: Adding duplicate key 'ResourceKey[minecraft:menu / extendedae:ex_emc_import_bus]' to registry`` Mincraft Version: 1.21.1 Java Version: 21.0.3, Eclipse Adoptium Mod Version: 1.21-2.2.

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#62** (github_issue, 1/6 conditions)
  - YUNGs-API issue #62: [1.20.4] fabric server won't start
  - https://github.com/YUNG-GANG/YUNGs-API/issues/62
  - retrieved by: bm25_b#8@r11l
  - excerpt: fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:470) ... 3 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.class_174 failed at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.getPostMixinClassByteArray(KnotClassDelegate.java:427) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.tryLoadClass(KnotClassDelegate.java:323) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.loadClass(KnotClassDelegate.java:218) at net.fabricmc.loader.impl.launch.knot.KnotClassLoader.loadClass(KnotClassLoad

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 1/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: dense_b#8@r11l
  - excerpt: # mixin.bugfix.ctm_resourceutil_cme=true # (default) # mixin.bugfix.ender_dragon_leak=true # (default) # mixin.bugfix.entity_pose_stack=true # (default) # mixin.bugfix.extra_experimental_screen=true # (default) # mixin.bugfix.fix_config_crashes=true # (default) # mixin.bugfix.missing_block_entities=false # (default) # mixin.bugfix.packet_leak=false # (default) # mixin.bugfix.paper_chunk_patches=false # (overridden for mod compat) # mixin.bugfix.recipe_book_type_desync=true # (default) # mixin.bugfix.restore_old_dragon_movement=false # (default) # mixin.bugfix.skip_redundant_saves=fa

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8983** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8983: Duplicate MenuType registration crash in InitMenuTypes.registerAll (AE2 19.2.17, NeoForge 1.21.1) — reproduces with all addons disabled
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8983
  - retrieved by: bm25_a#9@r11l
  - excerpt: [issue by JFloresAranda] ### Describe the bug As i have grown to enjoy a lot this mod an its addons, the pack im developing wouldnt be an exception. However i disabled all of them and the game would still crash. I disabled Ae2 and the game starts. AE2 throws `java.lang.IllegalStateException: Adding duplicate value 'net.minecraft.world.inventory.MenuType@...' to registry` during its own `RegisterEvent` handling, which causes a `ModLoadingException` ("Failed to register some entries") during game startup. The crash happens consistently, in the same place, in `InitMenuTypes.registerAll` (

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#931** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #931: [Create][1.21.1] Stack upgrades on max barrels kick players (IndexOutOfBoundsException
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/931
  - retrieved by: dense_b#9@r11l
  - excerpt: out of bounds exception, I thought it might be related, so I created the ticket. [comment by P3pp3rF1y (owner)] You will need to report this one to create, sounds like perhaps stock ticker isn't ready for that many slots.

- [ ] **gh-issue:architectury/architectury-api#290** (github_issue, 1/6 conditions)
  - architectury-api issue #290: Error could not initizlize class net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents
  - https://github.com/architectury/architectury-api/issues/290
  - retrieved by: bm25_b#9@r11l
  - excerpt: .fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at top.catowncraft.carpettctcaddition.CarpetTCTCAddition.onInitialize(CarpetTCTCAddition.java:68) at net.fabricmc.loader.impl.entrypoint.EntrypointUtils.invoke0(EntrypointUtils.java:47) ... 7 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at

- [ ] **gh-issue:mrh0/createaddition#1118** (github_issue, 1/6 conditions)
  - createaddition issue #1118: 1.21 - Recipe (Port?) Issue
  - https://github.com/mrh0/createaddition/issues/1118
  - retrieved by: hybrid_a#9@r11l
  - excerpt: [issue by CynSolveroftheAbsolute] **Describe the bug** Heyo, if you see this somewhere else, I'm bulk copy-pasting 'cuz I've got ~460 warnings in Kubejs and none of them are mine :D Not sure what the exact steps to reproduce are, but I do know your mod has an incorrect recipe or two. I'm attaching the KubeJS server script log so you can see what recipes are causing issues and try to understand why, but if they're like the first one that I made an issue for, which I knew a bit more about, you've left a residue of porting from 1.20 to 1.21 in a recipe (`"item": {"id": "minecraft:cobblestone"}` w

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#19** (github_issue, 1/6 conditions)
  - YUNGs-API issue #19: server crash in 1.18.2
  - https://github.com/YUNG-GANG/YUNGs-API/issues/19
  - retrieved by: bm25_b#10@r11l
  - excerpt: .main(FabricServerLauncher.java:66) Caused by: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.class_3218 failed at net.minecraft.class_2378.<clinit>(class_2378.java:189) at net.minecraft.class_2966.method_12851(class_2966.java:49) at net.minecraft.server.Main.main(Main.java:98) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Deleg

- [ ] **gh-issue:thedarkcolour/KotlinForForge#89** (github_issue, 1/6 conditions)
  - KotlinForForge issue #89: KFF crash on MC 1.20.4 with MinecraftForge 49.0.8
  - https://github.com/thedarkcolour/KotlinForForge/issues/89
  - retrieved by: bm25_a#10@r11l
  - excerpt: [issue by Prototik] ``` [13Dec2023 14:19:03.511] [modloading-worker-0/ERROR] [thedarkcolour.kotlinforforge.LoggerKt/LOADING]: Failed to register Automatic Kotlin subscribers. ModID: kotlinforforge, class thedarkcolour.kotlinforforge.test.KotlinForForge java.lang.NoClassDefFoundError: net/minecraftforge/fml/loading/moddiscovery/ModAnnotation$EnumHolder at thedarkcolour.kotlinforforge.AutoKotlinEventBusSubscriber.<clinit>(AutoKotlinEventBusSubscriber.kt:40) ~[kfflang-4.8.0.jar%239!/:4.8.0] at thedarkcolour.kotlinforforge.KotlinModContainer.constructMod(KotlinModContainer.kt:74) ~[kfflang-4

## Added by hand

(none)
