from Drizzle.Runtime import *## Behavior script: renderLightStart2#class renderLightStart2(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         smpl = None        smplps = None        dp = None        pstrct = None        ang = None        flatness = None        if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        self._movieScript.q = LingoNumber(1)        self._movieScript.c = LingoNumber(1)        self._movieScript.tm = self._global._system.milliseconds        tmp_q=int(LingoNumber(0))        while tmp_q < LingoNumber(19):             self._movieScript.q = LingoNumber(tmp_q)            self._global.sprite(LingoGlobal.op_sub(LingoNumber(40),self._movieScript.q)).loc = LingoGlobal.op_add(self._global.sprite(LingoGlobal.op_sub(LingoNumber(40),self._movieScript.q)).loc,LingoGlobal.point(-self._movieScript.q,-self._movieScript.q))            self._global.member(LingoGlobal.concat("layer",self._global.str(self._movieScript.q),"sh")).image = self._global.image(LingoNumber(1040),LingoNumber(800),LingoNumber(32))            tmp_q = int(self._movieScript.q)            tmp_q += 1                    self._global.member("dpImage").image = self._global.image(LingoNumber(1040),LingoNumber(800),LingoNumber(32))        self._global.member("dpImage").image.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), LingoNumber(255)))
        smpl = self._global.image(LingoNumber(4),LingoNumber(1),LingoNumber(32))        smplps = LingoNumber(0)        self._movieScript.dptsL = LingoList()        tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(20):             self._movieScript.q = LingoNumber(tmp_q)            dp = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(20),self._movieScript.q),LingoNumber(5))            pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),dp),self._movieScript.depthpnt(LingoGlobal.point(LingoNumber(1040),LingoNumber(800)),dp))            self._global.member("dpImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(20),self._movieScript.q)))).image,pstrct,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            smpl.copypixels(LingoImage.Pxl,LingoGlobal.rect(smplps,LingoNumber(0),LingoNumber(4),LingoNumber(1)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), LingoNumber(0)))
            if ((LingoGlobal.op_eq_b(LingoGlobal.op_add(dp,LingoNumber(5)), LingoNumber(12)) or LingoGlobal.op_eq_b(LingoGlobal.op_add(dp,LingoNumber(5)), LingoNumber(8))) or LingoGlobal.op_eq_b(LingoGlobal.op_add(dp,LingoNumber(5)), LingoNumber(4))):                 smpl.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(4),LingoNumber(1)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("blend"), LingoNumber(10),LingoSymbol("color"), LingoNumber(255)))
                smplps = LingoGlobal.op_add(smplps,LingoNumber(1))                self._global.member("dpImage").image.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("blend"), LingoNumber(10),LingoSymbol("color"), LingoNumber(255)))            tmp_q = int(self._movieScript.q)            tmp_q += 1                    tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(4):             self._movieScript.q = LingoNumber(tmp_q)            self._movieScript.dptsL.add(smpl.getpixel(LingoGlobal.op_sub(LingoNumber(4),self._movieScript.q),LingoNumber(0)))
            tmp_q = int(self._movieScript.q)            tmp_q += 1                    ang = self._movieScript.gLightEProps.lightangle        ang = LingoGlobal.op_mul(self._movieScript.degtovec(ang),LingoNumber(2.8000))        flatness = LingoNumber(1)        self._movieScript.mvL = LingoList(LingoList(ang.loch,ang.locv,LingoNumber(1)))        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLightEProps.flatness:             self._movieScript.q = LingoNumber(tmp_q)            self._movieScript.mvL.add(LingoList(ang.loch,ang.locv,LingoNumber(0)))
            tmp_q = int(self._movieScript.q)            tmp_q += 1                            return None            