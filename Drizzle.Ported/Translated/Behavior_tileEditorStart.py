from Drizzle.Runtime import *## Behavior script: tileEditorStart#class tileEditorStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         l = None        q = None        self._global._movie.exitlock = LingoGlobal.TRUE        self._global.member("tileMenu").alignment = LingoSymbol("left")        self._global.member("TEimg1").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("TEimg2").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("TEimg3").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImage1").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImage2").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImage3").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImageShortCuts").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._movieScript.tedraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(1))
        self._movieScript.tedraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(2))
        self._movieScript.tedraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(3))
        self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(1))
        self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(2))
        self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(3))
        self._movieScript.drawshortcutsimg(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(16))
        self._movieScript.gDirectionKeys = LingoList(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0))        self._global.sprite(LingoNumber(1)).blend = LingoNumber(10)        self._global.sprite(LingoNumber(2)).blend = LingoNumber(10)        self._global.sprite(LingoNumber(3)).blend = LingoNumber(60)        self._global.sprite(LingoNumber(4)).blend = LingoNumber(10)        self._global.sprite(LingoNumber(5)).blend = LingoNumber(70)        self._global.sprite(LingoNumber(6)).blend = LingoNumber(100)        self._global.sprite(LingoNumber(8)).blend = LingoNumber(80)        self._global.sprite(LingoNumber(8)).visibility = LingoNumber(0)        self._global.script("tileEditor").changelayer()
        self._global.member("default material").text = LingoGlobal.concat_space("Default material:",self._movieScript.gTEprops.defaultmaterial,"(Press 'E' to change)")        self._global.sprite(LingoNumber(19)).visibility = LingoNumber(1)        l = LingoPropertyList(LingoSymbol("l"), LingoNumber(0),LingoSymbol("m1"), LingoNumber(0),LingoSymbol("m2"), LingoNumber(0),LingoSymbol("w"), LingoNumber(0),LingoSymbol("a"), LingoNumber(0),LingoSymbol("s"), LingoNumber(0),LingoSymbol("d"), LingoNumber(0),LingoSymbol("c"), LingoNumber(0),LingoSymbol("q"), LingoNumber(0))        self._movieScript.gTEprops.lastkeys = l.duplicate()        self._movieScript.gTEprops.keys = l.duplicate()        self._global.script("tileEditor").updatetilemenu(LingoGlobal.point(LingoNumber(0),LingoNumber(0)))
        self._movieScript.gTEprops.tmsavposl = LingoList()        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gTiles.count:             q = LingoNumber(tmp_q)            self._movieScript.gTEprops.tmsavposl.add(LingoNumber(1))
            tmp_q = int(q)            tmp_q += 1                    self._global.member("Drought Reserve text").text = ""                return None            