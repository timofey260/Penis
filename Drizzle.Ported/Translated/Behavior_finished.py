from Drizzle.Runtime import *## Behavior script: finished#class finished(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         q = None        if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)) and LingoGlobal.ToBool(self._movieScript.gViewRender)):             self._global._movie.go(LingoNumber(9))        if LingoGlobal.op_eq_b(self._movieScript.gViewRender, LingoNumber(0)):             self._movieScript.levelName = self._movieScript.gLoadedName                    tmp_q=int(LingoNumber(0))        while tmp_q < LingoGlobal.op_sub(self._movieScript.gDecalColors.count,LingoNumber(1)):             q = tmp_q            self._global.member("finalImage").image.setpixel(q,LingoNumber(0),self._movieScript.gDecalColors[LingoGlobal.op_add(q,LingoNumber(1))])
            tmp_q = q            tmp_q += 1                            return None            