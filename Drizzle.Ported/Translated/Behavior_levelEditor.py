from Drizzle.Runtime import *## Behavior script: levelEditor#class levelEditor(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         q = None        rct = None        if LingoGlobal.ToBool(self._movieScript.showControls):             self._global.sprite(LingoNumber(93)).blend = LingoNumber(100)                    else:            self._global.sprite(LingoNumber(93)).blend = LingoNumber(0)                    if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(4):             q = LingoNumber(tmp_q)            if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoList(LingoNumber(86),LingoNumber(91),LingoNumber(88),LingoNumber(84))[q])) and LingoGlobal.op_eq_b(self._movieScript.gDirectionKeys[q], LingoNumber(0))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):                 self._movieScript.gLEProps.campos = LingoGlobal.op_add(self._movieScript.gLEProps.campos,LingoGlobal.op_mul(LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1)))[q],LingoGlobal.op_add(LingoGlobal.op_add(LingoNumber(1),LingoGlobal.op_mul(LingoNumber(9),self._global._key.keypressed(LingoNumber(83)))),LingoGlobal.op_mul(LingoNumber(34),self._global._key.keypressed(LingoNumber(85))))))                if not LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(92))):                     if self._movieScript.gLEProps.campos.loch < -LingoNumber(1):                         self._movieScript.gLEProps.campos.loch = -LingoNumber(1)                                            if self._movieScript.gLEProps.campos.locv < -LingoNumber(1):                         self._movieScript.gLEProps.campos.locv = -LingoNumber(1)                                            if self._movieScript.gLEProps.campos.loch > LingoGlobal.op_sub(self._movieScript.gLEProps.matrix.count,LingoNumber(51)):                         self._movieScript.gLEProps.campos.loch = LingoGlobal.op_sub(self._movieScript.gLEProps.matrix.count,LingoNumber(51))                                            if self._movieScript.gLEProps.campos.locv > LingoGlobal.op_sub(self._movieScript.gLEProps.matrix[LingoNumber(1)].count,LingoNumber(39)):                         self._movieScript.gLEProps.campos.locv = LingoGlobal.op_sub(self._movieScript.gLEProps.matrix[LingoNumber(1)].count,LingoNumber(39))                                                            self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(1))
                self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(2))
                self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(3))
                self._movieScript.drawshortcutsimg(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoNumber(16))            self._movieScript.gDirectionKeys[q] = self._global._key.keypressed(LingoList(LingoNumber(86),LingoNumber(91),LingoNumber(88),LingoNumber(84))[q])            tmp_q = int(q)            tmp_q += 1                    self._global.call(LingoSymbol("newupdate"),self._movieScript.gLEProps.leveleditors)
        rct = LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoGlobal.rect(self._movieScript.gLOprops.extratiles[LingoNumber(1)],self._movieScript.gLOprops.extratiles[LingoNumber(2)],-self._movieScript.gLOprops.extratiles[LingoNumber(3)],-self._movieScript.gLOprops.extratiles[LingoNumber(4)])),LingoGlobal.rect(self._movieScript.gLEProps.campos,self._movieScript.gLEProps.campos))        self._global.sprite(LingoNumber(172)).rect = LingoGlobal.op_mul(LingoGlobal.op_add(rct.intersect(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(52),LingoNumber(40))),LingoGlobal.rect(LingoNumber(11),LingoNumber(1),LingoNumber(11),LingoNumber(1))),LingoGlobal.rect(LingoNumber(16),LingoNumber(16),LingoNumber(16),LingoNumber(16)))        if LingoGlobal.op_eq_b(self._movieScript.gEnvEditorProps.waterlevel, -LingoNumber(1)):             self._global.sprite(LingoNumber(169)).rect = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0))                    else:            rct = LingoGlobal.op_sub(LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_sub(LingoGlobal.op_sub(self._movieScript.gLOprops.size.locv,self._movieScript.gEnvEditorProps.waterlevel),self._movieScript.gLOprops.extratiles[LingoNumber(4)]),self._movieScript.gLOprops.size.loch,self._movieScript.gLOprops.size.locv),LingoGlobal.rect(self._movieScript.gLEProps.campos,self._movieScript.gLEProps.campos))            self._global.sprite(LingoNumber(169)).rect = LingoGlobal.op_add(LingoGlobal.op_mul(LingoGlobal.op_add(rct.intersect(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(52),LingoNumber(40))),LingoGlobal.rect(LingoNumber(11),LingoNumber(1),LingoNumber(11),LingoNumber(1))),LingoGlobal.rect(LingoNumber(16),LingoNumber(16),LingoNumber(16),LingoNumber(16))),LingoGlobal.rect(LingoNumber(0),-LingoNumber(8),LingoNumber(0),LingoNumber(0)))                    self._global.script("levelOverview").gotoeditor()
        self._global.go(self._global.the_frame)        return None            