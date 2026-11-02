# Judging sheet 10: `r14_mixin_conflict_cobblemonraiddens` (test)

- **Category:** `mixin_conflict`  |  **Culprit:** `cobblemonraiddens`  |  **Acceptable:** cobblemonraiddens, owo
- **What was broken:** disabled owo-lib in CurseForge (its dependents, incl. Mega Showdown, were auto-disabled); Cobblemon Raid Dens' mixin plugin crashed with a NullPointerException in isModAndNewerThan while checking for a mod that was no longer loaded
- **Logs in this scenario:** r14_latest
- **Documents to judge:** 27

Judge the **document**, not the one chunk shown (open the URL if the excerpt does not settle it).
Mark `[x]` if the document helps diagnose or fix THIS failure; leave `[ ]` if not. Pool = union of the top-10 documents of six no-floor retrieval conditions, so a relevant document that none of them ranked in the top 10 is not here: add it by hand under *Added by hand* (and note how you found it).

If nothing is relevant after one deliberate search of the corpus, fill in **Support search** below.

**Support search:** `none_found` / `uncertain` / (leave blank if any doc is relevant)  ->  

---

- [ ] **gh-issue:embeddedt/ModernFix#542** (github_issue, 6/6 conditions)
  - ModernFix issue #542: Incompatibility w/ RuntimeTrims
  - https://github.com/embeddedt/ModernFix/issues/542
  - retrieved by: hybrid_a#1@r14l, hybrid_b#2@r14l, hybrid_c#5@r14l, bm25_a#3@r14l, bm25_b#7@r14l, dense_b#3@r14l
  - excerpt: .MinecraftGameProvider.launch(MinecraftGameProvider.java:480) at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Caused by: org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at org.spongepowered.asm.mixin.transformer.MixinProcessor.applyMixins(MixinProcessor.java:392) at org.spongepowered.asm.mixin.transformer.MixinTransformer.transformClass(MixinTransformer.java:234) at org.spongepowered.asm.mixin.transformer.MixinTransformer.tran

- [ ] **gh-issue:bernie-g/geckolib#823** (github_issue, 4/6 conditions)
  - geckolib issue #823: rendering entity in world Error: java.lang.NullPointerException: Cannot read field "rotationValueX" because "boneSnapshot" is null
  - https://github.com/bernie-g/geckolib/issues/823
  - retrieved by: hybrid_b#1@r14l, hybrid_c#3@r14l, bm25_b#2@r14l, dense_b#4@r14l
  - excerpt: variantloader.mixins.json:client.isleofberk.dragon.GronckleModelMixin,pl:mixin:A,pl:runtimedistcleaner:A} at com.GACMD.isleofberk.entity.dragons.gronckle.GronckleModel.setLivingAnimations(GronckleModel.java:15) ~[isleofberk-1.2.0.jar%23114!/:1.2.0] {re:mixin,pl:runtimedistcleaner:A,re:classloading,pl:mixin:APP:iobvariantloader.mixins.json:client.isleofberk.dragon.GronckleModelMixin,pl:mixin:A,pl:runtimedistcleaner:A} at software.bernie.geckolib3.renderers.geo.GeoEntityRenderer.render(GeoEntityRenderer.java:185) ~[geckolib-forge-1.18-3.0.57.jar%23104!/:3.0.57] {re:mixin,re:classloading,pl:mix

- [ ] **gh-issue:wisp-forest/owo-lib#246** (github_issue, 4/6 conditions)
  - owo-lib issue #246: [incompatibility report] Update for 1.21
  - https://github.com/wisp-forest/owo-lib/issues/246
  - retrieved by: hybrid_a#7@r14l, hybrid_b#10@r14l, hybrid_c#1@r14l, bm25_a#10@r14l
  - excerpt: [issue by c0nstexpr] As title suggested. Currently the mod is broken > [14:14:36] [main/ERROR]: Mixin apply for mod owo failed owo.mixins.json:ui.ScreenMixin from mod owo -> net.minecraft.class_437: org.spongepowered.asm.mixin.injection.throwables.InvalidInjectionException Critical injection failure: @ModifyArg annotation on injectProperLinkSource could not find any targets matching 'Lnet/minecraft/class_437;method_25428(Z)V' in net.minecraft.class_437. Using refmap owo-lib-refmap.json [PREINJECT Applicator Phase -> owo.mixins.json:ui.ScreenMixin from mod owo -> Prepare Injections -> -> mo

- [ ] **gh-issue:wisp-forest/owo-lib#357** (github_issue, 4/6 conditions)
  - owo-lib issue #357: 1.21 Fabric - When i try to start my server this show up:
  - https://github.com/wisp-forest/owo-lib/issues/357
  - retrieved by: hybrid_a#8@r14l, hybrid_c#6@r14l, bm25_a#1@r14l, bm25_b#8@r14l
  - excerpt: java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) at knot//io.gitlab.jfronny.libjf.LibJf.bootstrap(LibJf.java:51) at knot//io.gitlab.jfronny.libjf.LibJf.setup(LibJf.java:35) at knot//io.gitlab.jfronny.libjf.LibJf.onPreLaunch(LibJf.java:29) at net.fabricmc.loader.impl.FabricLoaderImpl.invokeEntrypoints(FabricLoaderImpl.java:399) ... 5 more Caused by: org.spongepowered.asm.mixin.throwables.MixinApplyError: Mixin [owo.mixins.json:DataResultMixin from mod owo] from phase [DEFAULT] in config [owo.mixins.json] FAILED during PREPARE at org.spongepowered.asm.mixin.transformer.Mixin

- [ ] **gh-issue:CaffeineMC/sodium#3722** (github_issue, 4/6 conditions)
  - sodium issue #3722: 0.8.12-alpha.1 & above Incompatible with Supplementaries
  - https://github.com/CaffeineMC/sodium/issues/3722
  - retrieved by: hybrid_a#2@r14l, hybrid_b#9@r14l, bm25_a#2@r14l, dense_b#6@r14l
  - excerpt: Lorg/spongepowered/asm/mixin/injection/callback/CallbackInfo;)V in supplementaries.mixins.json:compat.CompatSodiumFluidRendererMixin from mod supplementaries failed injection check, (0/1) succeeded. Scanned 0 target(s). No refMap loaded. at MC-BOOTSTRAP/org.spongepowered.mixin/org.spongepowered.asm.mixin.injection.struct.InjectionInfo.postInject(InjectionInfo.java:531) ~[sponge-mixin-0.15.2+mixin.0.8.7.jar:0.15.2+mixin.0.8.7] {} at MC-BOOTSTRAP/org.spongepowered.mixin/org.spongepowered.asm.mixin.transformer.MixinTargetContext.applyInjections(MixinTargetContext.java:1490) ~[sponge-mixin-0.15.2

- [ ] **gh-issue:embeddedt/ModernFix#608** (github_issue, 4/6 conditions)
  - ModernFix issue #608: [1.21.1 NeoForge] CRITICAL: NullPointerException Cascade (Create/AE2/Apotheosis) caused by registry_event_progress
  - https://github.com/embeddedt/ModernFix/issues/608
  - retrieved by: hybrid_b#3@r14l, hybrid_c#8@r14l, bm25_b#10@r14l, dense_b#2@r14l
  - excerpt: e2** | v19.2.17 | `NullPointerException: Trying to access unbound value: ResourceKey[minecraft:item / ae2:inscriber]` | | **apotheosis** | v8.4.0 | `NullPointerException: Trying to access unbound value: ResourceKey[... apotheosis:sigil_of_withdrawal]` | | **cataclysm_spellbooks** | v1.1.9 | *This mod also crashed, but as a side-effect of the initial registry collapse.* | ### 3. The Final Fix (The Most Effective Optimization) The crash is resolved by disabling the specific `ModernFix` mixin that accelerates the registry progress bar, thereby allowing `DeferredRegister` logic to complete safel

- [ ] **gh-issue:TwelveIterations/Waystones#1007** (github_issue, 4/6 conditions)
  - Waystones issue #1007: Something About Failure to Load Correctly Because Balm Config is Null
  - https://github.com/TwelveIterations/Waystones/issues/1007
  - retrieved by: hybrid_a#10@r14l, hybrid_b#4@r14l, hybrid_c#9@r14l, bm25_b#5@r14l
  - excerpt: .4.30] {re:classloading} -- Mod loading issue for: waystones -- Details: Mod file: /D:/curseforge/minecraft/Instances/Real Magic - [Spell Mastery - Enchantments - Crafting - Exploration]/mods/waystones-neoforge-1.21.4-21.4.1.jar Failure message: Waystones (waystones) has failed to load correctly java.lang.NullPointerException: Cannot invoke "net.blay09.mods.balm.api.config.LoadedConfig.getRaw(net.blay09.mods.balm.api.config.schema.ConfiguredProperty)" because "config" is null Mod version: 21.4.1 Mod issues URL: https://github.com/TwelveIterationMods/Waystones/issues Exception message: j

- [ ] **gh-issue:thedarkcolour/KotlinForForge#108** (github_issue, 3/6 conditions)
  - KotlinForForge issue #108: [1.21] Mixins get ClassNotFoundException when referencing the mod's Kotlin classes
  - https://github.com/thedarkcolour/KotlinForForge/issues/108
  - retrieved by: hybrid_a#3@r14l, bm25_a#5@r14l, dense_b#8@r14l
  - excerpt: 0.4/cpw.mods.modlauncher.Launcher.main(Launcher.java:74) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:26) at MC-BOOTSTRAP/cpw.mods.modlauncher@11.0.4/cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(BootstrapLaunchConsumer.java:23) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.run(BootstrapLauncher.java:210) at cpw.mods.bootstraplauncher@2.0.2/cpw.mods.bootstraplauncher.BootstrapLauncher.main(BootstrapLauncher.java:69) at java.base/jdk.internal.reflect.DirectMethodHan

- [ ] **gh-issue:TheIllusiveC4/Curios#502** (github_issue, 2/6 conditions)
  - Curios issue #502: [Bug]: Mixin issue in the 1.20.1 forge development environment
  - https://github.com/TheIllusiveC4/Curios/issues/502
  - retrieved by: hybrid_b#6@r14l, bm25_b#1@r14l
  - excerpt: resources. args '--mod', mod_id, '--all', '--output', file('src/generated/resources/'), '--existing', file('src/main/resources/') } ``` But after cleaning up and rebuilding, it still come up with the same error: ``` Mixin apply failed curios.mixins.json:MixinInventory -> net.minecraft.world.entity.player.Inventory: org.spongepowered.asm.mixin.transformer.throwables.InvalidMixinException @Shadow field f_35978_ was not located in the target class net.minecraft.world.entity.player.Inventory. Using refmap curios.refmap.json ``` [comment by TheIllusiveC4 (owner)] In your `depen

- [ ] **gh-issue:wisp-forest/owo-lib#504** (github_issue, 2/6 conditions)
  - owo-lib issue #504: EdmOps throws a NullPointerException on null input instead of returning a DataResult error
  - https://github.com/wisp-forest/owo-lib/issues/504
  - retrieved by: hybrid_c#2@r14l, bm25_b#3@r14l
  - excerpt: member)] Resolved via https://github.com/wisp-forest/owo-lib/commit/991c00e30ca0d1eeaf38c4b03cee7c8a3f7e0fb6

- [ ] **gh-issue:TheIllusiveC4/Curios#472** (github_issue, 2/6 conditions)
  - Curios issue #472: Crash Report
  - https://github.com/TheIllusiveC4/Curios/issues/472
  - retrieved by: hybrid_a#5@r14l, bm25_a#4@r14l
  - excerpt: [issue by Make527] I have tried to load it in different versions and i keep getting the same error. org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered that pops up when i get into minecraft which sucks because its in my custom pack and this is one of my favorite go to mods. If you could fix it that would be awesome. [comment by TheIllusiveC4 (owner)] I would need the whole crash report to decipher the cause, but most likely your issue may be coming from either Tiered or Inventorio. Please check if you have either of these

- [ ] **gh-issue:architectury/architectury-api#290** (github_issue, 2/6 conditions)
  - architectury-api issue #290: Error could not initizlize class net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents
  - https://github.com/architectury/architectury-api/issues/290
  - retrieved by: hybrid_b#8@r14l, bm25_b#4@r14l
  - excerpt: .fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) Suppressed: java.lang.BootstrapMethodError: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at top.catowncraft.carpettctcaddition.CarpetTCTCAddition.onInitialize(CarpetTCTCAddition.java:68) at net.fabricmc.loader.impl.entrypoint.EntrypointUtils.invoke0(EntrypointUtils.java:47) ... 7 more Caused by: java.lang.RuntimeException: Mixin transformation of net.minecraft.server.MinecraftServer failed at

- [ ] **gh-issue:thedarkcolour/KotlinForForge#161** (github_issue, 2/6 conditions)
  - KotlinForForge issue #161: Kotlin For Forge crashing issue | Required mod for Immersive Paintings | zero idea about modding please help
  - https://github.com/thedarkcolour/KotlinForForge/issues/161
  - retrieved by: hybrid_a#4@r14l, bm25_a#7@r14l
  - excerpt: [issue by orlandofff] ---- Minecraft Crash Report ---- // Hi. I'm Minecraft, and I'm a crashaholic. Time: 2026-06-28 20:59:17 Description: Initializing game net.neoforged.fml.ModLoadingException: Loading errors encountered: - Immersive Paintings (immersive_paintings) encountered an error while dispatching the net.neoforged.neoforge.client.event.EntityRenderersEvent$RegisterRenderers event org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at MC-BOOTSTRAP/fml_loader@4.0.42/net.neoforged.fml.ModContainer.acceptEvent(ModC

- [ ] **gh-issue:bernie-g/geckolib#887** (github_issue, 2/6 conditions)
  - geckolib issue #887: TextureManagerMixin fails to apply on Forge 1.20.1-47.4.10 (m_118506_ not found) - reproducible on vanilla MDK
  - https://github.com/bernie-g/geckolib/issues/887
  - retrieved by: hybrid_b#5@r14l, bm25_b#9@r14l
  - excerpt: [issue by ru95-afk] **GeckoLib version:** 4.8.3 (also reproduced on 4.7.3) **Forge version:** 1.20.1-47.4.10 (also reproduced on 47.2.20) **Mapping:** official, 1.20.1 **Java:** tried both Eclipse Adoptium 17.0.18 and 17.0.20 - same result ### Description The game crashes on startup (`runClient`) with a Mixin apply failure for `client.TextureManagerMixin`. The injection target method `m_118506_` (TextureManager, ResourceLocation -> AbstractTexture) cannot be found. ### Steps to reproduce 1. Download a fresh vanilla Forge MDK for 1.20.1-47.4.10 (no other mods). 2. Add GeckoLib as a dependency

- [ ] **gh-issue:embeddedt/ModernFix#535** (github_issue, 2/6 conditions)
  - ModernFix issue #535: Caught exception in thread: java.lang.NoClassDefFoundError: net/minecraft/client/gui/tab/Tab (net.minecraft.client.gui.tab.Tab)
  - https://github.com/embeddedt/ModernFix/issues/535
  - retrieved by: bm25_a#8@r14l, dense_b#5@r14l
  - excerpt: mc.loader.impl.launch.knot.KnotClassLoader.loadClass(KnotClassLoader.java:119) ~[fabric-loader-0.16.10.jar:?] at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:528) ~[?:?] at java.base/java.lang.Class.forName0(Native Method) ~[?:?] at java.base/java.lang.Class.forName(Class.java:578) ~[?:?] at java.base/java.lang.Class.forName(Class.java:557) ~[?:?] at net.fabricmc.loader.impl.launch.knot.MixinServiceKnot.findClass(MixinServiceKnot.java:101) ~[fabric-loader-0.16.10.jar:?] at org.spongepowered.asm.mixin.transformer.MixinProcessor.audit

- [ ] **gh-issue:TwelveIterations/Waystones#1190** (github_issue, 2/6 conditions)
  - Waystones issue #1190: Crash due to Confluence on newest update [Solution: Remove Confluence or downgrade Waystones]
  - https://github.com/TwelveIterations/Waystones/issues/1190
  - retrieved by: hybrid_b#7@r14l, hybrid_c#10@r14l
  - excerpt: [issue by VaporeonScripts] ### Minecraft Version 1.21.1 ### Mod Loader NeoForge ### Describe the Issue crash after updating to the newest balm (required for waystone's anniversary update) ### Logs https://mclo.gs/pmbfo56 [comment by BlayTheNinth (member)] The crash is happening in Prefab and does not seem to be related to Balm. > java.lang.NullPointerException: Cannot invoke "net.minecraft.world.level.ItemLike.asItem()" because "itemlike" is null at TRANSFORMER/minecraft@1.21.1/net.minecraft.client.color.item.ItemColors.register(ItemColors.java:122) ~[client-1.21.1-20240808.144430-sr

- [ ] **gh-issue:embeddedt/ModernFix#693** (github_issue, 1/6 conditions)
  - ModernFix issue #693: Mods with jar integrity checks malfunction when ModernFix is present
  - https://github.com/embeddedt/ModernFix/issues/693
  - retrieved by: dense_b#1@r14l
  - excerpt: comment by caionodaryluz-ctrl (none)] Minecraft Crash Report ---- // Hey, that tickles! Hehehe! Time: 2026-09-25 22:02:55 Description: mouseClicked event handler java.lang.NullPointerException: Cannot invoke "com.cobblemon.mod.relocations.graalvm.polyglot.Value.execute(Object[])" because "receiveMoveDataFn" is null at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.lambda$movesLoad$0(Moves.java:48) at knot//com.cobblemon.mod.common.battles.ShowdownThread.queue(ShowdownThread.java:32) at knot//com.github.yajatkaul.mega_showdown.fabric.datapack.showdown.Moves.movesLo

- [ ] **gh-issue:wisp-forest/owo-lib#327** (github_issue, 1/6 conditions)
  - owo-lib issue #327: NeoForge 1.21.1 - Crash on Rendering Overlay/Loading Shaders When Spectrum is not Present
  - https://github.com/wisp-forest/owo-lib/issues/327
  - retrieved by: hybrid_c#4@r14l
  - excerpt: [issue by ToxinZangoose] Hello, I have recently been trying to diagnose an issue with my modpack and the log files point to this mod when I try launching. When launching, owo lib tries to load shaders for Spectrum which is not supported for NeoForge. Below is the log file for the crash I've been experiencing since I've tried removing 19 mods from this pack. https://mclo.gs/wDKVGtH Thank you for your time! [comment by Dragon-Seeker (member)] ``` [02Nov2024 11:04:06.859] [modloading-worker-0/ERROR] [io.github.lightman314.lightmanscurrency.LightmansCurrency/]: Error setting up C

- [ ] **gh-issue:bernie-g/geckolib#508** (github_issue, 1/6 conditions)
  - geckolib issue #508: GeckoLib3 has failed to load correctly
  - https://github.com/bernie-g/geckolib/issues/508
  - retrieved by: bm25_b#6@r14l
  - excerpt: [issue by ilovechiu] i've tried removing some mods, downgrading mods, and changing my version of forge to no avail. it also says that forge failed to load correctly too, but idk if those are correlated or not. ---- Minecraft Crash Report ---- // You should try our sister game, Minceraft! Time: 2023-10-19 18:07:03 Description: Mod loading error has occurred java.lang.Exception: Mod Loading has failed at net.minecraftforge.logging.CrashReportExtender.dumpModLoadingCrashReport(CrashReportExtender.java:55) ~[forge-1.19.2-43.3.0-universal.jar%23242!/:?] {re:classloading} at net.mine

- [ ] **gh-issue:embeddedt/ModernFix#685** (github_issue, 1/6 conditions)
  - ModernFix issue #685: [1.20.1] Crash with Dynamicresources
  - https://github.com/embeddedt/ModernFix/issues/685
  - retrieved by: hybrid_a#6@r14l
  - excerpt: )] Just a heads up, the "Reproduction Steps" are steps for the developer to be able to reproduce your issue in their testing environment, not the actions you took that led to it breaking. Regardless, the log reveals quite a few errors, with the likely crash culprit being a ConcurrentModificationException error from the mod **[Handcrafted](https://www.curseforge.com/minecraft/mc-mods/handcrafted)**: ``` [net.minecraftforge.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: handcrafted, class earth.terrarium.handcrafted.forge.HandcraftedForge org.spongepowered.as

- [ ] **gh-issue:mezz/JustEnoughItems#4450** (github_issue, 1/6 conditions)
  - JustEnoughItems issue #4450: [Bug]: Create: Aeronautics mixin mismatch causing client crash
  - https://github.com/mezz/JustEnoughItems/issues/4450
  - retrieved by: bm25_a#6@r14l
  - excerpt: [issue by viralhysteria] ### Steps to Reproduce the Bug The recent 19.44.0.406 update causes a client crash on world load when running the game with only Create, Create: Aeronautics and Sable enabled. All aforementioned mods are on the latest release channel. <details> <summary>Error 1</summary> [Render thread/ERROR] [net.neoforged.bus.EventBus/EVENTBUS]: Exception caught during firing event: An unexpected critical error was encountered Index: 1 Listeners: 0: mezz.jei.neoforge.JustEnoughItemsClient$$Lambda/0x0000025398eba5c8@7a90d6de 1: mezz.jei.neoforge.startup.StartEventObserver$$Lam

- [ ] **gh-issue:thedarkcolour/KotlinForForge#91** (github_issue, 1/6 conditions)
  - KotlinForForge issue #91: Possible Viruses ?
  - https://github.com/thedarkcolour/KotlinForForge/issues/91
  - retrieved by: dense_b#7@r14l
  - excerpt: [issue by EagleTheCreateEngineer] i gave this the wrong title sorry when ever i try and use kotlin my game crashs with the error of ---- Minecraft Crash Report ---- // There are four lights! Time: 1/1/24, 11:39 AM Description: Rendering overlay org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at org.spongepowered.asm.mixin.transformer.MixinProcessor.applyMixins(MixinProcessor.java:392) ~[mixin-0.8.5.jar:0.8.5+Jenkins-b310.git-155314e6e91465dad727e621a569906a410cd6f4] {} at org.spongepowered.asm.mixin.transfor

- [ ] **gh-issue:wisp-forest/owo-lib#302** (github_issue, 1/6 conditions)
  - owo-lib issue #302: Shaders Not Rendering
  - https://github.com/wisp-forest/owo-lib/issues/302
  - retrieved by: hybrid_c#7@r14l
  - excerpt: -srg.jar%23326!/:?] {re:mixin,pl:accesstransformer:B,pl:connector_pre_launch:A,pl:runtimedistcleaner:A,re:classloading,pl:accesstransformer:B,pl:mixin:APP:moonlight-common.mixins.json:GameRendererMixin from mod moonlight,pl:mixin:APP:supplementaries-common.mixins.json:GameRendererMixin from mod supplementaries,pl:mixin:APP:mixins.reach-entity-attributes.json:client.GameRendererMixin from mod reach_entity_attributes,pl:mixin:APP:mixins.oculus.json:GameRendererAccessor from mod oculus,pl:mixin:APP:mixins.oculus.json:MixinGameRenderer from mod oculus,pl:mixin:APP:mixins.oculus.json:MixinModelView

- [ ] **gh-issue:Creators-of-Create/Create#10344** (github_issue, 1/6 conditions)
  - Create issue #10344: Cannot read field "x" because "mf.axis" is null
  - https://github.com/Creators-of-Create/Create/issues/10344
  - retrieved by: dense_b#9@r14l
  - excerpt: Lambda/0x0000000077b74a38@1b3d14c4 11: rbasamoyai.createbigcannons.CBCCommonNeoForgeEvents$$Lambda/0x0000000077e61a48@22546ab6 12: net.neoforged.bus.EventListenerFactory$onServerWorldTick/0x00000000781c1c00@1561ec77 13: net.neoforged.bus.EventListenerFactory$onServerWorldTick/0x00000000781d1c00@7d2f1aef 14: net.neoforged.bus.EventListenerFactory$onServerWorldTick/0x00000000782b2800@529db953 java.lang.NullPointerException: Cannot read field "x" because "mf.axis" is null at TRANSFORMER/create@6.0.10/com.simibubi.create.foundation.collision.ContinuousOBBCollider.collideMany(ContinuousOBB

- [ ] **gh-issue:P3pp3rF1y/SophisticatedStorage#562** (github_issue, 1/6 conditions)
  - SophisticatedStorage issue #562: (1.21.1 Neoforge) Game crashes because of Cannot get config value before config is loaded
  - https://github.com/P3pp3rF1y/SophisticatedStorage/issues/562
  - retrieved by: bm25_a#9@r14l
  - excerpt: BalmClientEvents$$Lambda/0x00000296fbe78800@4911b7bf 17: net.neoforged.bus.EventListenerFactory$guiPostInit/0x00000296fcde3c00@41bb9bf6 java.lang.IllegalStateException: Cannot get config value before config is loaded. at MC-BOOTSTRAP/com.google.common@32.1.2-jre/com.google.common.base.Preconditions.checkState(Preconditions.java:512) at TRANSFORMER/neoforge@21.1.90/net.neoforged.neoforge.common.ModConfigSpec$ConfigValue.getRaw(ModConfigSpec.java:1235) at TRANSFORMER/neoforge@21.1.90/net.neoforged.neoforge.common.ModConfigSpec$ConfigValue.get(ModConfigSpec.java:1222) at TRANSFORMER/b

- [ ] **gh-issue:shedaniel/cloth-config#69** (github_issue, 1/6 conditions)
  - cloth-config issue #69: Bedrockify causes crash when opening mod settings in modmenu
  - https://github.com/shedaniel/cloth-config/issues/69
  - retrieved by: hybrid_a#9@r14l
  - excerpt: [issue by Mhowser] ---- Minecraft Crash Report ---- // I feel sad now :( Time: 2020-11-22 20:09:19 PST Description: Rendering screen org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered at Not Enough Crashes deobfuscated stack trace.(1.15.1+build.36) at org.spongepowered.asm.mixin.transformer.MixinProcessor.applyMixins(MixinProcessor.java:363) at org.spongepowered.asm.mixin.transformer.MixinTransformer.transformClass(MixinTransformer.java:208) at org.spongepowered.asm.mixin.transformer.MixinTransforme

- [ ] **gh-issue:TwelveIterations/Waystones#1207** (github_issue, 1/6 conditions)
  - Waystones issue #1207: Compatibility Issue with Riding in Cobblemon
  - https://github.com/TwelveIterations/Waystones/issues/1207
  - retrieved by: dense_b#10@r14l
  - excerpt: [issue by OutOfOrderCandy] ### Minecraft Version 1.21.1 ### Mod Loader Fabric ### Describe the Issue Version that is casing an issue : waystones-fabric-1.21.1-21.1.37.jar Balm version : balm-fabric-1.21.1-21.0.63 Fabric API : 0.116.14 Cobblemon : 1.7.3 If you try to use waystones while riding a pokemon, this leaves traces of the pokemon and sometimes causing crashes to server. https://imgur.com/a/mR9y5hl It works fine on version before 21.1.37 ### Logs [crash-2026-07-18_17.40.27-server.txt](https://github.com/user-attachments/files/30160941/crash-2026-07-18_17.40.27-server.txt) [c

## Added by hand

(none)
