from Drizzle.Runtime import *## Behavior script: renderLight#class renderLight(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        if LingoGlobal.ToBool(self._movieScript.gViewRender):             if LingoGlobal.ToBool(self._movieScript.checkexitrender()):                 self._global._movie.go(LingoNumber(9))            self.newframe()
            if LingoGlobal.ToBool(self._movieScript.keepLooping):                 self._global.go(self._global.the_frame)                    else:            while LingoGlobal.ToBool(self._movieScript.keepLooping):                 self.newframe()                            return None            def newframe(self):         cols = None        rows = None        marginpixels = None        marginrect = None        fullrect = None        inv = None        svpos = None        activesilhouette = None        dir = None        layersilhouette = None        cols = LingoNumber(100)        rows = LingoNumber(60)        marginpixels = LingoNumber(150)        marginrect = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_add(LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(marginpixels,LingoNumber(2))),LingoGlobal.op_add(LingoGlobal.op_mul(rows,LingoNumber(20)),LingoGlobal.op_mul(marginpixels,LingoNumber(2))))        fullrect = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20)))        inv = self._global.image(marginrect.right,marginrect.bottom,LingoNumber(1))        svpos = self._movieScript.pos        activesilhouette = self._movieScript.makesilhouttefromimg(self._global.member("activeLightImage").image,LingoNumber(1))        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLightEProps.flatness:             self._movieScript.q = tmp_q            inv.copypixels(activesilhouette,LingoGlobal.op_add(marginrect,LingoGlobal.rect(self._movieScript.pos,self._movieScript.pos)),marginrect,LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(0),LingoNumber(0))))
            self._movieScript.pos = LingoGlobal.op_add(self._movieScript.pos,self._movieScript.degtovec(self._movieScript.gLightEProps.lightangle))            tmp_q = self._movieScript.q            tmp_q += 1                    inv = self._movieScript.makesilhouttefromimg(inv,LingoNumber(1))        for tmp_dir in LingoList(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1))):             dir = tmp_dir            self._global.member(LingoGlobal.concat("layer",self._movieScript.c,"sh")).image.copypixels(inv,LingoGlobal.op_add(marginrect,LingoGlobal.rect(dir,dir)),marginrect,LingoPropertyList(LingoSymbol("ink"), LingoNumber(36)))        self._global.member(LingoGlobal.concat("layer",self._movieScript.c,"sh")).image.copypixels(self._movieScript.makesilhouttefromimg(self._global.member(LingoGlobal.concat("layer",self._movieScript.c)).image,LingoNumber(1)),LingoGlobal.op_add(fullrect,LingoGlobal.rect(marginpixels,marginpixels,marginpixels,marginpixels)),fullrect,LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
        layersilhouette = self._movieScript.makesilhouttefromimg(self._global.member(LingoGlobal.concat("layer",self._movieScript.c)).image,LingoNumber(0))        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLightEProps.flatness:             self._movieScript.q = tmp_q            self._global.member("activeLightImage").image.copypixels(layersilhouette,LingoGlobal.op_add(LingoGlobal.op_sub(fullrect,LingoGlobal.rect(svpos,svpos)),LingoGlobal.rect(marginpixels,marginpixels,marginpixels,marginpixels)),fullrect,LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            svpos = LingoGlobal.op_add(svpos,self._movieScript.degtovec(self._movieScript.gLightEProps.lightangle))            tmp_q = self._movieScript.q            tmp_q += 1                    self._movieScript.c = LingoGlobal.op_add(self._movieScript.c,LingoNumber(1))        if self._movieScript.c > LingoNumber(29):             self._movieScript.keepLooping = LingoNumber(0)                            return None            def newframe2(self):         inv = None        svpos = None        dir = None        dp = None        pstrct = None        inv = self._global.image(LingoGlobal.op_add(LingoNumber(1040),LingoNumber(200)),LingoGlobal.op_add(LingoNumber(800),LingoNumber(200)),LingoNumber(1))        svpos = self._movieScript.pos        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLightEProps.flatness:             self._movieScript.q = tmp_q            inv.copypixels(self._movieScript.makesilhouttefromimg(self._global.member("activeLightImage").image,LingoNumber(1)),LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_add(LingoNumber(1040),LingoNumber(200)),LingoGlobal.op_add(LingoNumber(800),LingoNumber(200))),LingoGlobal.rect(self._movieScript.pos,self._movieScript.pos)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_add(LingoNumber(1040),LingoNumber(200)),LingoGlobal.op_add(LingoNumber(800),LingoNumber(200))),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(0),LingoNumber(0))))
            self._movieScript.pos = LingoGlobal.op_add(self._movieScript.pos,self._movieScript.degtovec(self._movieScript.gLightEProps.lightangle))            tmp_q = self._movieScript.q            tmp_q += 1                    inv = self._movieScript.makesilhouttefromimg(inv,LingoNumber(1))        inv.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),self._movieScript.pos.loch,LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
        inv.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),self._movieScript.pos.locv),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
        for tmp_dir in LingoList(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1))):             dir = tmp_dir            self._global.member(LingoGlobal.concat("layer",self._movieScript.c,"sh")).image.copypixels(inv,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(dir,dir)),LingoGlobal.rect(-LingoNumber(100),-LingoNumber(100),LingoNumber(100),LingoNumber(100))),LingoGlobal.rect(LingoNumber(0),LingoNumber(8),LingoNumber(0),LingoNumber(8))),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_add(LingoNumber(1040),LingoNumber(200)),LingoGlobal.op_add(LingoNumber(800),LingoNumber(200))),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(0),LingoNumber(0))))        self._global.member(LingoGlobal.concat("layer",self._movieScript.c,"sh")).image.copypixels(self._movieScript.makesilhouttefromimg(self._global.member(LingoGlobal.concat("layer",self._movieScript.c)).image,LingoNumber(1)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLightEProps.flatness:             self._movieScript.q = tmp_q            self._global.member("activeLightImage").image.copypixels(self._movieScript.makesilhouttefromimg(self._global.member(LingoGlobal.concat("layer",self._movieScript.c)).image,LingoNumber(0)),LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(svpos,svpos)),LingoGlobal.rect(LingoNumber(100),LingoNumber(100),LingoNumber(100),LingoNumber(100))),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            svpos = LingoGlobal.op_add(svpos,self._movieScript.degtovec(self._movieScript.gLightEProps.lightangle))            tmp_q = self._movieScript.q            tmp_q += 1                    self._movieScript.c = LingoGlobal.op_add(self._movieScript.c,LingoNumber(1))        if (self._movieScript.c > LingoNumber(29) or LingoGlobal.op_eq_b(self._movieScript.gLevel.lighttype, "no Light")):             self._global.member("shadowImage").image = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(20)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(20)),LingoNumber(32))            tmp_q=int(LingoNumber(1))            while tmp_q < LingoNumber(30):                 self._movieScript.q = tmp_q                dp = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(30),self._movieScript.q),LingoNumber(5))                pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),dp),self._movieScript.depthpnt(LingoGlobal.point(LingoNumber(1040),LingoNumber(800)),dp))                self._global.member("shadowImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),self._movieScript.q)))).image,pstrct,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
                self._global.member("shadowImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),self._movieScript.q)),"sh")).image,pstrct,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36)))
                tmp_q = self._movieScript.q                tmp_q += 1                            inv = self._global.image(LingoGlobal.op_mul(LingoNumber(52),LingoNumber(20)),LingoGlobal.op_mul(LingoNumber(40),LingoNumber(20)),LingoNumber(1))            inv.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), LingoNumber(255)))
            inv.copypixels(self._global.member("shadowImage").image,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            self._global.member("shadowImage").image.copypixels(inv,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1040),LingoNumber(800)))
            self._movieScript.keepLooping = LingoNumber(0)                            return None            