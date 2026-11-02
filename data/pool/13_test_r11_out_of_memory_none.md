# Judging sheet 13: `r11_out_of_memory_none` (test)

- **Category:** `out_of_memory`  |  **Culprit:** `None`  |  **Acceptable:** (none)
- **What was broken:** set the pack's max RAM to 1000 MB; ran out of memory during mod loading
- **Logs in this scenario:** r11_latest
- **Documents to judge:** 21

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:mezz/JustEnoughItems#4351** (github_issue, 4/6 conditions)
  - JustEnoughItems issue #4351: [Bug]: UI error when opening inventory
  - https://github.com/mezz/JustEnoughItems/issues/4351
  - retrieved by: hybrid_b#2@r11l, hybrid_c#2@r11l, bm25_b#5@r11l, dense_b#5@r11l
  - excerpt: I still have 12 GiB of free space. I thought it might be COW (Copy-on-Write) corrupting data, so I created a new instance/profile, and only installed Fabric API and JEI. I also tried restarting the game multiple times. It's still happening. I tried giving myself /op, setting myself to Creative mode, doing /recipe give @s *, but none of them helped. The game does not crash, only the JEI UI does, so I can still play the game normally. ### latest.log https://gist.github.com/Syntrait/41c04b9450d3e65c524d2ff8ae82b582 [comment by mezz (owner)] Thanks for the report! Can you please include the s

- [ ] **gh-issue:TwelveIterations/Balm#211** (github_issue, 3/6 conditions)
  - Balm issue #211: JEI integration causes massive memory leak / system crash on Fabric 1.21.11
  - https://github.com/TwelveIterations/Balm/issues/211
  - retrieved by: hybrid_b#1@r11l, hybrid_c#1@r11l, bm25_b#1@r11l
  - excerpt: stable (~2 GB) Exit the game Add Just Enough Items (JEI) (latest Fabric build) Launch Minecraft again Load a world and open the inventory Result Memory usage rapidly increases from ~2 GB to 5–6 GB JVM heap remains limited to 4 GB, but total system memory keeps growing Severe lag occurs, followed by a full system freeze or crash Control Test Removing JEI while keeping all other mods installed returns memory usage to normal and the game runs stably. Machine Specs CPU: Intel i3 (older generation) RAM: 8 GB GPU: Intel HD Graphics (shared memory) OS: Windows Java: Java 25 (also repr

- [ ] **gh-issue:GlodBlock/ExtendedAE#422** (github_issue, 2/6 conditions)
  - ExtendedAE issue #422: kubejs error with extended ae
  - https://github.com/GlodBlock/ExtendedAE/issues/422
  - retrieved by: hybrid_a#1@r11l, bm25_a#3@r11l
  - excerpt: [issue by baka4n] etails: Mod file: /C:/Users/<user>/.gradle/caches/modules-2/files-2.1/dev.latvian.mods/kubejs-neoforge/2101.7.2-build.233/7c5dbc2e152f819c929b51fcf1247747770af4c9/kubejs-neoforge-2101.7.2-build.233.jar Failure message: KubeJS (kubejs) encountered an error while dispatching the net.neoforged.neoforge.registries.RegisterEvent event java.lang.NoSuchMethodError: 'void dev.latvian.mods.kubejs.registry.BuilderTypeRegistry$Callback.add(java.lang.String, java.lang.Class, dev.latvian.mods.kubejs.registry.BuilderFactory)' Mod version: 2101.7.2-build.233 Mod issues URL: https://ku

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

- [ ] **gh-issue:TwelveIterations/Balm#123** (github_issue, 1/6 conditions)
  - Balm issue #123: [Crash] ticking hopper below Cooking for blockheads' Oven tries to take item from slot 4 (only 3 slots)
  - https://github.com/TwelveIterations/Balm/issues/123
  - retrieved by: dense_b#1@r11l
  - excerpt: [issue by MindStudioOfficial] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader Fabric ### Describe the Issue placing a hopper below a cooking for blockheads oven which has 3 input slots and 3 output slots crashes the server whenever the block is loaded and ticked because it tries to take items from slot 4 of 3 (IndexOutOfBounds) ``` java.lang.IndexOutOfBoundsException: Index 4 out of bounds for length 3 at java.base/jdk.internal.util.Preconditions.outOfBounds(Unknown Source) at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Unknown Source) at java.base/jdk.internal.u

- [ ] **gh-issue:TwelveIterations/Balm#186** (github_issue, 1/6 conditions)
  - Balm issue #186: [1.21.1] Any version above 21.0.46 causes a crash saying "Cannot get config value before config is loaded."
  - https://github.com/TwelveIterations/Balm/issues/186
  - retrieved by: bm25_a#1@r11l
  - excerpt: [issue by MundM2007] ### Minecraft Version 1.21.1 (LTS) ### Mod Loader NeoForge ### Describe the Issue Upon updated my mods, the game crashes with the error `java.lang.IllegalStateException: Cannot get config value before config is loaded.`. I've tried to replicate this error with a limited number of mods. Though because of the unclear error message i didn't succeed. ### Logs [latest.log](https://github.com/user-attachments/files/22186380/latest.log) [debug.log](https://github.com/user-attachments/files/22186381/debug.log) [comment by BlayTheNinth (member)] This has nothing to do with

- [ ] **gh-issue:Creators-of-Create/Create#10508** (github_issue, 1/6 conditions)
  - Create issue #10508: Super glue not working
  - https://github.com/Creators-of-Create/Create/issues/10508
  - retrieved by: dense_b#2@r11l
  - excerpt: -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx12224M Memory: 2043631496 bytes (1948 MiB) / 9177137152 bytes (8752 MiB) up to 12817793024 bytes (12224 MiB) Total Memory: 7225780344 bytes (6891 MiB) / 9177137152 bytes (8752 MiB) CPU: Intel(R) CC150 CPU @ 3.50GHz @ 3.50 GHz; 7 cores / 7 threads on 1 socket(s) Graphics cards: none Other Mods: YUNG's Better Dungeons: 1.21.1-NeoForge-5.1.4 Sky Aesthetics: 2.0.13-beta KubeJS: 2101.7.2-build.348 SuperMartijn642's Config Library: 1.1.8 Horseman: 1.5.9 Alex's Mobs: 1.22.17 Create Deco: 2.1.3 Pl

- [ ] **gh-issue:GlodBlock/ExtendedAE#341** (github_issue, 1/6 conditions)
  - ExtendedAE issue #341: [Render thread/ERROR] appeng/client/guidebook/color/ColorValue
  - https://github.com/GlodBlock/ExtendedAE/issues/341
  - retrieved by: bm25_a#2@r11l
  - excerpt: [issue by YoSiJo] ``` [21:54:01] [Render thread/ERROR] [ne.ne.fm.ModContainer/LOADING]: Caught exception during event net.neoforged.neoforge.client.event.RegisterMenuScreensEvent@2ba7828b dispatch for modid extendedae java.lang.NoClassDefFoundError: appeng/client/guidebook/color/ColorValue at TRANSFORMER/extendedae@1.21-2.0.1-neoforge/com.glodblock.github.extendedae.client.ClientRegistryHandler.registerGui(ClientRegistryHandler.java:108) ~[ExtendedAE-1.21-2.0.1-neoforge.jar%23219!/:?] {re:classloading} at MC-BOOTSTRAP/net.neoforged.bus/net.neoforged.bus.EventBus.post(EventBus.java:350) ~[bus

- [ ] **gh-issue:embeddedt/ModernFix#583** (github_issue, 1/6 conditions)
  - ModernFix issue #583: Server reports that certain features of ModernFix are attempting to load client-only Java classes on the server.
  - https://github.com/embeddedt/ModernFix/issues/583
  - retrieved by: hybrid_a#2@r11l
  - excerpt: [issue by MapleSugar365] **Description:** Although NeoForge prevents these classes from loading and avoids server crashes, this generates a large number of red error messages that flood the console. Can this issue be fixed? Thank you. **Version Information:** - Minecraft: 1.21.1 - NeoForge: 21.1.187 - ModernFix: modernfix-neoforge-5.24.3+mc1.21.1 **Error Log Information:** [17:35:52 ERROR] [n.n.f.c.a.RuntimeDistCleaner/DISTXFORM]: Attempted to load class net/minecraft/client/multiplayer/ClientLevel for invalid dist DEDICATED_SERVER [17:35:52 ERROR] [STDERR]: java.lang.RuntimeExcept

- [ ] **gh-issue:mrh0/createaddition#636** (github_issue, 1/6 conditions)
  - createaddition issue #636: Accumulator in Spawn Chunks causing Crash?
  - https://github.com/mrh0/createaddition/issues/636
  - retrieved by: bm25_b#2@r11l
  - excerpt: tity` ![screenshot](https://github.com/mrh0/createaddition/assets/83117017/4f07083b-9250-40f5-8b20-1a2e67346add) CSV file of the snapshot: [createaddition.csv](https://github.com/mrh0/createaddition/files/12577000/createaddition.csv) After closing Minecraft it produces error code -805306369 When I encountered this issue first time I tried to do some memory profiling with Spark: `[09:28:40] [spark-worker-pool-1-thread-1/INFO] [minecraft/ChatComponent]: [System] [CHAT] [?] Young Gen GC lasting 198 ms. (cause = G1 Evacuation Pause)\n 298.0 MB moved to G1 Old Gen\n 2.4 GB ? 2.7 GB\n 6

- [ ] **gh-issue:AppliedEnergistics/Applied-Energistics-2#8793** (github_issue, 1/6 conditions)
  - Applied-Energistics-2 issue #8793: DOUMENTATION IS INCOMPLETE!!!!
  - https://github.com/AppliedEnergistics/Applied-Energistics-2/issues/8793
  - retrieved by: bm25_b#3@r11l
  - excerpt: with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with data from the block, get the error: "Could not load configuration from an incompatible device" ### Expected behavior 1. Get yourself a Memory Card. 2. Get an AE2 block that you can load data from into the cad (any machine, or a pattern provider or a P2P tunnel, anything, doesn't matter) and place it in the world. 3. Put any random item in your off hand. 4. Attempt to load data from the block in step two with the memory card by shift right clicking. 5. Instead of the Memory Card being loaded with dat

- [ ] **gh-issue:Creators-of-Create/Create#10778** (github_issue, 1/6 conditions)
  - Create issue #10778: The encased fan blows air through the non‑ventilated blocks.
  - https://github.com/Creators-of-Create/Create/issues/10778
  - retrieved by: dense_b#3@r11l
  - excerpt: Flags: 2 total; -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xmx16384M Memory: 1213959216 bytes (1157 MiB) / 6803161088 bytes (6488 MiB) up to 17179869184 bytes (16384 MiB) Total Memory: 5625451472 bytes (5364 MiB) / 6803161088 bytes (6488 MiB) CPU: 12th Gen Intel(R) Core(TM) i5-12500 @ 3.00 GHz; 6 cores / 12 threads on 1 socket(s) Graphics cards: none Other Mods: Saturn: 0.1.5 Concurrent Chunk Management Engine (Fixes/WorldGen/Threading Issues): 0.4.0-alpha.0.117+1.21.1 KubeJS: 2101.7.2-build.368 Create: Deep Seas - Lava Fix: 1.0.1 SuperM

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

## Added by hand

(none)
