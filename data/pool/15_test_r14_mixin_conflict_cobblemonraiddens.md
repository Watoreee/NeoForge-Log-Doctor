# Judging sheet 15: `r14_mixin_conflict_cobblemonraiddens` (test)

- **Category:** `mixin_conflict`  |  **Culprit:** `cobblemonraiddens`  |  **Acceptable:** cobblemonraiddens, owo
- **What was broken:** disabled owo-lib in CurseForge (its dependents, incl. Mega Showdown, were auto-disabled); Cobblemon Raid Dens' mixin plugin crashed with a NullPointerException in isModAndNewerThan while checking for a mod that was no longer loaded
- **Logs in this scenario:** r14_latest
- **Documents to judge:** 18

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
**Relevant** = someone with this exact crash would use it to diagnose or fix it: an issue about the same mod with the same kind of error, or a docs page that explains this specific error message. Generic pages that are merely on-topic don't count.
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-N documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in its top N is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  none_found

---

- [ ] **gh-issue:embeddedt/ModernFix#542** (github_issue, 5/6 conditions)
  - ModernFix issue #542: Incompatibility w/ RuntimeTrims
  - https://github.com/embeddedt/ModernFix/issues/542
  - retrieved by: hybrid_a#1@r14l, hybrid_b#1@r14l, hybrid_c#3@r14l, bm25_a#4@r14l, dense_b#3@r14l
  - excerpt: .MinecraftGameProvider.launch(MinecraftGameProvider.java:480) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Caused by: org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at org.spongepowered.asm.mixin.transformer.MixinProcessor.applyMixins(MixinProcessor.java:392) at org.spongepowered.asm.mixin.transformer.MixinTransformer.transformClass(MixinTransformer.java:234) at org.spongepowered.asm.mixin.transformer.MixinTransformer.tran

- [ ] **gh-issue:bernie-g/geckolib#823** (github_issue, 4/6 conditions)
  - geckolib issue #823: rendering entity in world Error: java.lang.NullPointerException: Cannot read field "rotationValueX" because "boneSnapshot" is null
  - https://github.com/bernie-g/geckolib/issues/823
  - retrieved by: hybrid_b#2@r14l, hybrid_c#4@r14l, bm25_b#2@r14l, dense_b#4@r14l
  - excerpt: variantloader.mixins.json:client.isleofberk.dragon.GronckleModelMixin,pl:mixin:A,pl:runtimedistcleaner:A} at com.GACMD.isleofberk.entity.dragons.gronckle.GronckleModel.setLivingAnimations(GronckleModel.java:15) ~[isleofberk-1.2.0.jar%23114!/:1.2.0] {re:mixin,pl:runtimedistcleaner:A,re:classloading,pl:mixin:APP:iobvariantloader.mixins.json:client.isleofberk.dragon.GronckleModelMixin,pl:mixin:A,pl:runtimedistcleaner:A} at software.bernie.geckolib3.renderers.geo.GeoEntityRenderer.render(GeoEntityRenderer.java:185) ~[geckolib-forge-1.18-3.0.57.jar%23104!/:3.0.57] {re:mixin,re:classloading,pl:mix

- [ ] **gh-issue:TheIllusiveC4/Curios#502** (github_issue, 2/6 conditions)
  - Curios issue #502: [Bug]: Mixin issue in the 1.20.1 forge development environment
  - https://github.com/TheIllusiveC4/Curios/issues/502
  - retrieved by: hybrid_b#4@r14l, bm25_b#1@r14l
  - excerpt: resources. args '--mod', mod_id, '--all', '--output', file('src/generated/resources/'), '--existing', file('src/main/resources/') } ``` But after cleaning up and rebuilding, it still come up with the same error: ``` Mixin apply failed curios.mixins.json:MixinInventory -> net.minecraft.world.entity.player.Inventory: org.spongepowered.asm.mixin.transformer.throwables.InvalidMixinException @Shadow field f_35978_ was not located in the target class net.minecraft.world.entity.player.Inventory. Using refmap curios.refmap.json ``` [comment by TheIllusiveC4 (owner)] In your `depen

- [ ] **gh-issue:CaffeineMC/sodium#3722** (github_issue, 2/6 conditions)
  - sodium issue #3722: 0.8.12-alpha.1 & above Incompatible with Supplementaries
  - https://github.com/CaffeineMC/sodium/issues/3722
  - retrieved by: hybrid_a#2@r14l, bm25_a#3@r14l
  - excerpt: Lorg/spongepowered/asm/mixin/injection/callback/CallbackInfo;)V in supplementaries.mixins.json:compat.CompatSodiumFluidRendererMixin from mod supplementaries failed injection check, (0/1) succeeded. Scanned 0 target(s). No refMap loaded. at MC-BOOTSTRAP/org.spongepowered.mixin/org.spongepowered.asm.mixin.injection.struct.InjectionInfo.postInject(InjectionInfo.java:531) ~[sponge-mixin-0.15.2+mixin.0.8.7.jar:0.15.2+mixin.0.8.7] {} at MC-BOOTSTRAP/org.spongepowered.mixin/org.spongepowered.asm.mixin.transformer.MixinTargetContext.applyInjections(MixinTargetContext.java:1490) ~[sponge-mixin-0.15.2

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#62** (github_issue, 2/6 conditions)
  - YUNGs-API issue #62: [1.20.4] fabric server won't start
  - https://github.com/YUNG-GANG/YUNGs-API/issues/62
  - retrieved by: hybrid_a#3@r14l, bm25_a#2@r14l
  - excerpt: .transformer.MixinTransformer.transformClass(MixinTransformer.java:234) at org.spongepowered.asm.mixin.transformer.MixinTransformer.transformClassBytes(MixinTransformer.java:202) at net.fabricmc.loader.impl.launch.knot.KnotClassDelegate.getPostMixinClassByteArray(KnotClassDelegate.java:422) ... 11 more Caused by: org.spongepowered.asm.mixin.throwables.MixinApplyError: Mixin [yungsapi.mixins.json:accessor.CriteriaTriggersAccessor from mod yungsapi] from phase [DEFAULT] in config [yungsapi.mixins.json] FAILED during APPLY at org.spongepowered.asm.mixin.transformer.MixinProcessor.handleM

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 2/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: hybrid_b#3@r14l, dense_b#2@r14l
  - excerpt: e2** | v19.2.17 | `NullPointerException: Trying to access unbound value: ResourceKey[minecraft:item / ae2:inscriber]` | | **apotheosis** | v8.4.0 | `NullPointerException: Trying to access unbound value: ResourceKey[... apotheosis:sigil_of_withdrawal]` | | **cataclysm_spellbooks** | v1.1.9 | *This mod also crashed, but as a side-effect of the initial registry collapse.* | ### 3. The Final Fix (The Most Effective Optimization) The crash is resolved by disabling the specific `ModernFix` mixin that accelerates the registry progress bar, thereby allowing `DeferredRegister` logic to complete safel

- [ ] **gh-issue:wisp-forest/owo-lib#504** (github_issue, 2/6 conditions)
  - owo-lib issue #504: EdmOps throws a NullPointerException on null input instead of returning a DataResult error
  - https://github.com/wisp-forest/owo-lib/issues/504
  - retrieved by: hybrid_c#2@r14l, bm25_b#3@r14l
  - excerpt: member)] Resolved via https://github.com/wisp-forest/owo-lib/commit/991c00e30ca0d1eeaf38c4b03cee7c8a3f7e0fb6

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 1/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: dense_b#1@r14l
  - excerpt: comment by caionodaryluz-ctrl (none)] Minecraft Crash Report ---- // Hey, that tickles! Hehehe! Time: 2026-09-25 22:02:55 Description: mouseClicked event handler java.lang.NullPointerException: Cannot invoke "com.cobblemon.mod.relocations.graalvm.polyglot.Value.execute(Object[])" because "receiveMoveDataFn" is null at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.lambda$movesLoad$0(Moves.java:48) at knot//com.cobblemon.mod.common.battles.ShowdownThread.queue(ShowdownThread.java:32) at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.movesLo

- [ ] **gh-issue:wisp-forest/owo-lib#246** (github_issue, 1/6 conditions)
  - owo-lib issue #246: [incompatibility report] Update for 1.21
  - https://github.com/wisp-forest/owo-lib/issues/246
  - retrieved by: hybrid_c#1@r14l
  - excerpt: [issue by c0nstexpr] As title suggested. Currently the mod is broken > [14:14:36] [main/ERROR]: Mixin apply for mod owo failed owo.mixins.json:ui.ScreenMixin from mod owo -> net.minecraft.class_437: org.spongepowered.asm.mixin.injection.throwables.InvalidInjectionException Critical injection failure: @ModifyArg annotation on injectProperLinkSource could not find any targets matching 'Lnet/minecraft/class_437;method_25428(Z)V' in net.minecraft.class_437. Using refmap owo-lib-refmap.json [PREINJECT Applicator Phase -> owo.mixins.json:ui.ScreenMixin from mod owo -> Prepare Injections -> -> mo

- [ ] **gh-issue:wisp-forest/owo-lib#357** (github_issue, 1/6 conditions)
  - owo-lib issue #357: 1.21 Fabric - When i try to start my server this show up:
  - https://github.com/wisp-forest/owo-lib/issues/357
  - retrieved by: bm25_a#1@r14l
  - excerpt: java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) at knot//io.gitlab.jfronny.libjf.LibJf.bootstrap(LibJf.java:51) at knot//io.gitlab.jfronny.libjf.LibJf.setup(LibJf.java:35) at knot//io.gitlab.jfronny.libjf.LibJf.onPreLaunch(LibJf.java:29) at net.fabricmc.loader.impl.FabricLoaderImpl.invokeEntrypoints(FabricLoaderImpl.java:399) ... 5 more Caused by: org.spongepowered.asm.mixin.throwables.MixinApplyError: Mixin [owo.mixins.json:DataResultMixin from mod owo] from phase [DEFAULT] in config [owo.mixins.json] FAILED during PREPARE at org.spongepowered.asm.mixin.transformer.Mixin

- [ ] **gh-issue:architectury/architectury-api#290** (github_issue, 1/6 conditions)
  - architectury-api issue #290: Error could not initizlize class net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents
  - https://github.com/architectury/architectury-api/issues/290
  - retrieved by: bm25_b#4@r14l
  - excerpt: .fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at top.catowncraft.carpettctcaddition.CarpetTCTCAddition.onInitialize(CarpetTCTCAddition.java:68) at net.fabricmc.loader.impl.entrypoint.EntrypointUtils.invoke0(EntrypointUtils.java:47) ... 7 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 1/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_a#4@r14l
  - excerpt: 0.4/cpw.mods.modlauncher.Launcher.main(Launcher.java:74) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.run(BootstrapLauncher.java:210) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:69) at java.base/jdk.internal.reflect.DirectMethodHan

- [ ] **gh-issue:TheIllusiveC4/Curios#472** (github_issue, 1/6 conditions)
  - Curios issue #472: Crash Report
  - https://github.com/TheIllusiveC4/Curios/issues/472
  - retrieved by: bm25_a#5@r14l
  - excerpt: [issue by Make527] I have tried to load it in different versions and i keep getting the same error. org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered that pops up when i get into minecraft which sucks because its in my custom pack and this is one of my favorite go to mods. If you could fix it that would be awesome. [comment by TheIllusiveC4 (owner)] I would need the whole crash report to decipher the cause, but most likely your issue may be coming from either Tiered or Inventorio. Please check if you have either of these

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 1/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_b#5@r14l
  - excerpt: .4.30] {re:classloading} -- Mod loading issue for: waystones -- Details: Mod file: /D:/curseforge/minecraft/Instances/Real Magic - [Spell Mastery - Enchantments - Crafting - Exploration]/mods/waystones-neoforge-1.21.4-21.4.1.jar Failure message: Waystones (waystones) has failed to load correctly java.lang.NullPointerException: Cannot invoke "net.blay09.mods.balm.api.config.LoadedConfig.getRaw(net.blay09.mods.balm.api.config.schema.ConfiguredProperty)" because "config" is null Mod version: 21.4.1 Mod issues URL: https://github.com/TwelveIterationMods/Waystones/issues Exception message: j

- [ ] **gh-issue:YUNG-GANG/YUNGs-API#19** (github_issue, 1/6 conditions)
  - YUNGs-API issue #19: server crash in 1.18.2
  - https://github.com/YUNG-GANG/YUNGs-API/issues/19
  - retrieved by: bm25_b#5@r14l
  - excerpt: .main(FabricServerLauncher.java:66) Caused by: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.class_3218 failed at net.minecraft.class_2378.<clinit>(class_2378.java:189) at net.minecraft.class_2966.method_12851(class_2966.java:49) at net.minecraft.server.Main.main(Main.java:98) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Deleg

- [ ] **gh-issue:embeddedt/ModernFix#535** (github_issue, 1/6 conditions)
  - ModernFix issue #535: Caught exception in thread: java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab (net.minecraft.client.gui.tab.Tab)
  - https://github.com/embeddedt/ModernFix/issues/535
  - retrieved by: dense_b#5@r14l
  - excerpt: asm.mixin.MixinEnvironment.audit(MixinEnvironment.java:1677) ~[sponge-mixin-0.15.4+mixin.0.8.7.jar:0.15.4+mixin.0.8.7] at knot/org.embeddedt.modernfix.util.ClassInfoManager.doClear(ClassInfoManager.java:70) ~[modernfix-fabric-5.20.3+mc1.21.4.jar:?] at java.base/java.util.concurrent.ForkJoinTask$RunnableExecuteAction.compute(For [... truncated] [comment by embeddedt (owner)] I don't think this error should cause the server to crash by itself, but if it does, disable `mixin.perf.clear_mixin_classinfo` (it's not enabled by default, anyways). The error is caused by another mod app

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 1/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#5@r14l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: hybrid_c#5@r14l
  - excerpt: [issue by ToxinZangoose] Hello, I have recently been trying to diagnose an issue with my modpack and the log files point to this mod when I try launching. When launching, owo lib tries to load shaders for Spectrum which is not supported for NeoForge. Below is the log file for the crash I've been experiencing since I've tried removing 19 mods from this pack. https://mclo.gs/wDKVGtH Thank you for your time! [comment by Dragon-Seeker (member)] ``` [02Nov2024 11:04:06.859] [modloading-worker-0/ERROR] [io.github.lightman314.lightmanscurrency.LightmansCurrency/]: Error setting up C

## Added by hand

(none)
