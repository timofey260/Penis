from Drizzle.Runtime import *## Behavior script: levelEditStart#class levelEditStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         self._global._movie.exitlock = LingoGlobal.TRUE        if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        cols = self._movieScript.gLOprops.size.loch        rows = self._movieScript.gLOprops.size.locv        self._global.member("levelEditImage1").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImage2").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImage3").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._global.member("levelEditImageShortCuts").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(16)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(16)),LingoNumber(16))        self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),cols,rows),LingoNumber(1))
        self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),cols,rows),LingoNumber(2))
        self._movieScript.lvleditdraw(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),cols,rows),LingoNumber(3))
        self._movieScript.drawshortcutsimg(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),cols,rows),LingoNumber(16))
        self._movieScript.gDirectionKeys = LingoList(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0))        tmp_q = LingoNumber(800)        while tmp_q < LingoNumber(820):             q = tmp_q            self._global.sprite(q).visibility = LingoNumber(1)            tmp_q = q            tmp_q += LingoNumber(1)                    self._global.sprite(LingoNumber(94)).visibility = LingoNumber(1)        self._global.sprite(LingoNumber(168)).visibility = LingoNumber(1)        self._global.member("toolsImage2").image = self._global.image(LingoGlobal.op_mul(self._movieScript.gLEProps.toolmatrix[LingoNumber(1)].count,LingoNumber(32)),LingoGlobal.op_mul(self._movieScript.gLEProps.toolmatrix.count,LingoNumber(32)),LingoNumber(16))        tmp_q = LingoNumber(1)        while tmp_q < self._movieScript.gLEProps.toolmatrix.count:             q = tmp_q            tmp_c = LingoNumber(1)            while tmp_c < self._movieScript.gLEProps.toolmatrix[LingoNumber(1)].count:                 c = tmp_c                rct = LingoGlobal.rect(LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(32)),LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(32)),LingoGlobal.op_mul(c,LingoNumber(32)),LingoGlobal.op_mul(q,LingoNumber(32)))                nm = LingoGlobal.concat("icon",self._movieScript.gLEProps.toolmatrix[q][c])                self._global.member("toolsImage2").image.copypixels(self._global.member(LingoGlobal.concat("icon",self._movieScript.gLEProps.toolmatrix[q][c])).image,rct,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(32),LingoNumber(32)))
                tmp_c = c                tmp_c += LingoNumber(1)                            tmp_q = q            tmp_q += LingoNumber(1)                    self._movieScript.gLEProps.leveleditors[LingoNumber(1)].p.mirrorpos = LingoGlobal.op_div(self._movieScript.gLOprops.size.loch,LingoNumber(2))                return None            