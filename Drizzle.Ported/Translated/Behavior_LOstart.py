from Drizzle.Runtime import *## Behavior script: LOstart#class LOstart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         cols = None        rows = None        q = None        l = None        self._global._movie.exitlock = LingoGlobal.TRUE        self._movieScript.newSize[LingoNumber(1)] = self._movieScript.gLOprops.size.loch        self._movieScript.newSize[LingoNumber(2)] = self._movieScript.gLOprops.size.locv        cols = self._movieScript.gLOprops.size.loch        rows = self._movieScript.gLOprops.size.locv        self._movieScript.gEditLizard = LingoList("pink",LingoNumber(0),LingoNumber(0),LingoNumber(0))        self._global.script("levelOverview").nexthole()
        self._global.member("addLizardTime").text = "0"        self._global.member("addLizardFlies").text = "0"        self._global.sprite(LingoNumber(43)).color = self._global.color(LingoNumber(255),LingoNumber(0),LingoNumber(255))        self._global.sprite(LingoNumber(2)).loc = LingoGlobal.op_add(LingoGlobal.point(LingoNumber(312),LingoNumber(312)),LingoGlobal.point(LingoGlobal.op_add(-LingoNumber(1000),LingoGlobal.op_mul(LingoNumber(1000),self._movieScript.gLevel.defaultterrain)),LingoNumber(0)))        self._global.sprite(LingoNumber(56)).visibility = LingoNumber(1)        self._global.sprite(LingoNumber(57)).visibility = LingoNumber(1)        self._global.sprite(LingoNumber(58)).visibility = LingoNumber(1)        self._global.sprite(LingoNumber(59)).visibility = LingoNumber(1)        self._global.sprite(LingoNumber(67)).loch = LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLevel.waterdrips,LingoNumber(8)),LingoNumber(50))        self._global.sprite(LingoNumber(68)).loch = LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLevel.maxflies,LingoNumber(10)),LingoNumber(50))        self._global.sprite(LingoNumber(69)).loch = LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLevel.flyspawnrate,LingoNumber(4)),LingoNumber(50))        self._global.member("lightTypeText").text = self._movieScript.gLevel.lighttype        self._global.sprite(LingoNumber(70)).loch = LingoGlobal.op_add(self._movieScript.gLOprops.tileseed,LingoNumber(50))        self._global.script("levelOverview").updatelizardslist()
        tmp_q=int(LingoNumber(0))        while tmp_q < LingoNumber(29):             q = tmp_q            self._global.member(LingoGlobal.concat("layer",q)).image = self._global.image(LingoNumber(1),LingoNumber(1),LingoNumber(1))            self._global.member(LingoGlobal.concat("layer",q,"sh")).image = self._global.image(LingoNumber(1),LingoNumber(1),LingoNumber(1))            tmp_q = q            tmp_q += 1                    l = LingoList("Dull","Reflective","Superflourescent")        self._global.member("color glow effects").text = LingoGlobal.concat_space(l[LingoGlobal.op_add(self._movieScript.gLOprops.colglows[LingoNumber(1)],LingoNumber(1))],LingoGlobal.RETURN,l[LingoGlobal.op_add(self._movieScript.gLOprops.colglows[LingoNumber(2)],LingoNumber(1))])        self._global.sprite(LingoNumber(22)).rect = LingoGlobal.rect(-LingoNumber(100),-LingoNumber(100),-LingoNumber(100),-LingoNumber(100))        if LingoGlobal.op_eq_b(self._movieScript.gPrioCam, LingoNumber(0)):             self._global.member("PrioCamText").text = ""                    else:            self._global.member("PrioCamText").text = LingoGlobal.concat("Will render camera ",self._movieScript.gPrioCam," first")                    self._global.the_randomSeed = self._global._system.milliseconds                return None            