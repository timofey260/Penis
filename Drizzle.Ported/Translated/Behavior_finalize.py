from Drizzle.Runtime import *## Behavior script: finalize#class finalize(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         cols = None        rows = None        extrarect = None        extrapoint = None        lightmargin = None        q = None        dp = None        pstrct = None        inv = None        smpl = None        smpl2 = None        smplps = None        q2 = None        l = None        bd = None        lr = None        getrect = None        cols = LingoNumber(100)        rows = LingoNumber(60)        self._global.member("finalImage").image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoNumber(32))        self._global.member("shadowImage").image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoNumber(32))        self._global.member("finalDecalImage").image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoNumber(32))        self._movieScript.gDecalColors = LingoList()        extrarect = LingoGlobal.rect(-LingoNumber(50),-LingoNumber(50),LingoNumber(50),LingoNumber(50))        extrapoint = LingoGlobal.point(extrarect.right,extrarect.bottom)        lightmargin = LingoNumber(150)        self._movieScript.gRenderCameraPixelPos = LingoGlobal.op_add(self._movieScript.gRenderCameraPixelPos,LingoGlobal.point(LingoGlobal.op_mul(LingoNumber(15),LingoNumber(20)),LingoGlobal.op_mul(LingoNumber(10),LingoNumber(20))))        self._global.member("dumpImage").image = self._global.image(LingoGlobal.op_add(LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(lightmargin,LingoNumber(2))),LingoGlobal.op_add(LingoGlobal.op_mul(rows,LingoNumber(20)),LingoGlobal.op_mul(lightmargin,LingoNumber(2))),LingoNumber(32))        tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(30):             q = tmp_q            dp = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(30),q),LingoNumber(5))            self._global.member("dumpImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)))).image,LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20))),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20))))
            self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)))).image.copypixels(self._global.member("dumpImage").image,self._global.member("dumpImage").image.rect,self._global.member("dumpImage").image.rect)
            pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),extrapoint),dp),self._movieScript.depthpnt(LingoGlobal.op_add(LingoGlobal.point(LingoNumber(1400),LingoNumber(800)),extrapoint),dp))            self._global.member("shadowImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)))).image,pstrct,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),extrarect),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            self._global.member("shadowImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)),"sh")).image,pstrct,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),extrarect),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36)))
            tmp_q = q            tmp_q += 1                    inv = self._global.image(LingoNumber(1400),LingoNumber(800),LingoNumber(1))        inv.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), LingoNumber(255)))
        inv.copypixels(self._global.member("shadowImage").image,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
        self._global.member("shadowImage").image.copypixels(inv,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)))
        self._global.member("fogImage").image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoSymbol("l8"))        self._global.member("dpImage").image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoSymbol("l8"))        self._global.member("dpImage").image.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), LingoNumber(255)))
        smpl = self._global.image(LingoNumber(4),LingoNumber(1),LingoNumber(32))        smpl2 = self._global.image(LingoNumber(30),LingoNumber(1),LingoNumber(32))        smplps = LingoNumber(0)        self._movieScript.dptsL = LingoList()        self._movieScript.fogDptsL = LingoList()        tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(30):             q = tmp_q            dp = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(30),q),LingoNumber(5))            pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),extrapoint),dp),self._movieScript.depthpnt(LingoGlobal.op_add(LingoGlobal.point(LingoNumber(1400),LingoNumber(800)),extrapoint),dp))            self._global.member("dpImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)))).image,pstrct,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),extrarect),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            smpl.copypixels(LingoImage.Pxl,LingoGlobal.rect(smplps,LingoNumber(0),LingoNumber(4),LingoNumber(1)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("color"), LingoNumber(0)))
            if ((LingoGlobal.op_eq_b(LingoGlobal.op_add(dp,LingoNumber(5)), LingoNumber(12)) or LingoGlobal.op_eq_b(LingoGlobal.op_add(dp,LingoNumber(5)), LingoNumber(8))) or LingoGlobal.op_eq_b(LingoGlobal.op_add(dp,LingoNumber(5)), LingoNumber(4))):                 smpl.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(4),LingoNumber(1)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("blend"), LingoNumber(10),LingoSymbol("color"), LingoNumber(255)))
                smplps = LingoGlobal.op_add(smplps,LingoNumber(1))                self._global.member("dpImage").image.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("blend"), LingoNumber(10),LingoSymbol("color"), LingoNumber(255)))            self._global.member("fogImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)))).image,pstrct,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),extrarect),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
            self._global.member("fogImage").image.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("blend"), LingoNumber(5),LingoSymbol("color"), LingoNumber(255)))
            smpl2.setpixel(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(0),self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255)))
            smpl2.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(30),LingoNumber(1)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(LingoSymbol("blend"), LingoNumber(5),LingoSymbol("color"), LingoNumber(255)))
            tmp_q = q            tmp_q += 1                    tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(4):             q = tmp_q            self._movieScript.dptsL.add(smpl.getpixel(LingoGlobal.op_sub(LingoNumber(4),q),LingoNumber(0)))
            tmp_q = q            tmp_q += 1                    tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(30):             q = tmp_q            self._movieScript.fogDptsL.add(smpl2.getpixel(LingoGlobal.op_sub(LingoNumber(30),q),LingoNumber(0)))
            tmp_q = q            tmp_q += 1                    tmp_q2=int(LingoNumber(1))        while tmp_q2 < LingoNumber(25):             q2 = tmp_q2            dp = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(30),q2),LingoNumber(5))            pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),extrapoint),dp),self._movieScript.depthpnt(LingoGlobal.op_add(LingoGlobal.point(LingoNumber(1400),LingoNumber(800)),extrapoint),dp))            self._global.member("finalImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q2)))).image,pstrct,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),extrarect),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36)))
            if LingoGlobal.op_eq_b(LingoGlobal.op_sub(LingoNumber(30),q2), LingoNumber(10)):                 inv = self._movieScript.makesilhouttefromimg(self._global.member("finalImage").image,LingoNumber(1))                tmp_q=int(LingoNumber(1))                while tmp_q < self._movieScript.gLOprops.size.loch:                     q = tmp_q                    tmp_c=int(LingoNumber(1))                    while tmp_c < self._movieScript.gLOprops.size.locv:                         self._movieScript.c = tmp_c                        if ((self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(5)) > LingoNumber(0) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(1)][LingoNumber(1)], LingoNumber(0))) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(2)][LingoNumber(1)], LingoNumber(1))):                             self._movieScript.pasteshortcuthole("finalImage",LingoGlobal.point(q,self._movieScript.c),LingoNumber(5),"BORDER")
                            self._movieScript.pasteshortcuthole("finalImage",LingoGlobal.point(q,self._movieScript.c),LingoNumber(5),self._global.color(LingoNumber(51),LingoNumber(10),LingoNumber(0)))                        tmp_c = self._movieScript.c                        tmp_c += 1                                            tmp_q = q                    tmp_q += 1                                    self._global.member("finalImage").image.copypixels(inv,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))            elif LingoGlobal.op_eq_b(LingoGlobal.op_sub(LingoNumber(30),q2), LingoNumber(20)):                 inv = self._movieScript.makesilhouttefromimg(self._global.member("finalImage").image,LingoNumber(1))                tmp_q=int(LingoNumber(1))                while tmp_q < self._movieScript.gLOprops.size.loch:                     q = tmp_q                    tmp_c=int(LingoNumber(1))                    while tmp_c < self._movieScript.gLOprops.size.locv:                         self._movieScript.c = tmp_c                        if (((self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(5)) > LingoNumber(0) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(1)][LingoNumber(1)], LingoNumber(0))) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(2)][LingoNumber(1)], LingoNumber(0))) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(3)][LingoNumber(1)], LingoNumber(1))):                             self._movieScript.pasteshortcuthole("finalImage",LingoGlobal.point(q,self._movieScript.c),LingoNumber(15),"BORDER")
                            self._movieScript.pasteshortcuthole("finalImage",LingoGlobal.point(q,self._movieScript.c),LingoNumber(15),self._global.color(LingoNumber(41),LingoNumber(9),LingoNumber(0)))                        tmp_c = self._movieScript.c                        tmp_c += 1                                            tmp_q = q                    tmp_q += 1                                    self._global.member("finalImage").image.copypixels(inv,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))            tmp_q2 = q2            tmp_q2 += 1                    tmp_q=int(LingoNumber(25))        while tmp_q < LingoNumber(30):             q = tmp_q            dp = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(30),q),LingoNumber(5))            pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),extrapoint),dp),self._movieScript.depthpnt(LingoGlobal.op_add(LingoGlobal.point(LingoNumber(1400),LingoNumber(800)),extrapoint),dp))            self._global.member("finalImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(LingoGlobal.op_sub(LingoNumber(30),q)))).image,pstrct,LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),extrarect),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36)))
            tmp_q = q            tmp_q += 1                    inv = self._movieScript.makesilhouttefromimg(self._global.member("finalImage").image,LingoNumber(1))        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLOprops.size.loch:             q = tmp_q            tmp_c=int(LingoNumber(1))            while tmp_c < self._movieScript.gLOprops.size.locv:                 self._movieScript.c = tmp_c                if (self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(5)) > LingoNumber(0) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][self._movieScript.c][LingoNumber(1)][LingoNumber(1)], LingoNumber(1))):                     self._movieScript.pasteshortcuthole("finalImage",LingoGlobal.point(q,self._movieScript.c),-LingoNumber(5),"BORDER")
                    self._movieScript.pasteshortcuthole("finalImage",LingoGlobal.point(q,self._movieScript.c),-LingoNumber(5),self._global.color(LingoNumber(31),LingoNumber(8),LingoNumber(0)))                tmp_c = self._movieScript.c                tmp_c += 1                            tmp_q = q            tmp_q += 1                    self._global.member("finalImage").image.copypixels(inv,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoPropertyList(LingoSymbol("ink"), LingoNumber(36),LingoSymbol("color"), self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))))
        self._global.member("rainBowMask").image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoNumber(1))        for tmp_L in LingoList("A","B"):             l = tmp_L            self._global.member(LingoGlobal.concat("flattenedGradient",l)).image = self._global.image(LingoNumber(1400),LingoNumber(800),LingoNumber(16))            tmp_bd=int(LingoNumber(0))            while tmp_bd < LingoNumber(29):                 bd = tmp_bd                lr = LingoGlobal.op_sub(LingoNumber(29),bd)                dp = LingoGlobal.op_sub(lr,LingoNumber(5))                self._global.member("dumpImage").image.copypixels(self._global.member(LingoGlobal.concat("gradient",l,self._global.str(lr))).image,LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20))),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20))))
                pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),extrapoint),dp),self._movieScript.depthpnt(LingoGlobal.op_add(LingoGlobal.point(LingoNumber(1400),LingoNumber(800)),extrapoint),dp))                getrect = LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),extrarect)                self._global.member(LingoGlobal.concat("flattenedGradient",l)).image.copypixels(self._global.member("dumpImage").image,pstrct,getrect,LingoPropertyList(LingoSymbol("maskimage"), self._movieScript.makesilhouttefromimg(self._global.member(LingoGlobal.concat("layer",lr)).image,LingoNumber(0)).createmask()))
                self._global.member(LingoGlobal.concat("flattenedGradient",l)).image.setpixel(LingoNumber(0),LingoNumber(0),self._global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))
                self._global.member(LingoGlobal.concat("flattenedGradient",l)).image.setpixel(LingoGlobal.op_sub(LingoNumber(1400),LingoNumber(1)),LingoGlobal.op_sub(LingoNumber(800),LingoNumber(1)),self._global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))
                tmp_bd = bd                tmp_bd += 1                                    if LingoGlobal.ToBool(self._movieScript.gAnyDecals):             tmp_bd=int(LingoNumber(0))            while tmp_bd < LingoNumber(29):                 bd = tmp_bd                lr = LingoGlobal.op_sub(LingoNumber(29),bd)                dp = LingoGlobal.op_sub(lr,LingoNumber(5))                self._global.member("dumpImage").image.copypixels(self._global.member(LingoGlobal.concat("layer",self._global.str(lr),"dc")).image,LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20))),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(cols,LingoNumber(20)),LingoGlobal.op_mul(rows,LingoNumber(20))))
                pstrct = LingoGlobal.rect(self._movieScript.depthpnt(LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),extrapoint),dp),self._movieScript.depthpnt(LingoGlobal.op_add(LingoGlobal.point(LingoNumber(1400),LingoNumber(800)),extrapoint),dp))                getrect = LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1400),LingoNumber(800)),LingoGlobal.rect(self._movieScript.gRenderCameraPixelPos,self._movieScript.gRenderCameraPixelPos)),LingoGlobal.rect(lightmargin,lightmargin,lightmargin,lightmargin)),extrarect)                self._global.member("finalDecalImage").image.copypixels(self._global.member("dumpImage").image,pstrct,getrect,LingoPropertyList(LingoSymbol("maskimage"), self._movieScript.makesilhouttefromimg(self._global.member(LingoGlobal.concat("layer",lr)).image,LingoNumber(0)).createmask()))
                self._global.member("finalDecalImage").image.setpixel(LingoNumber(0),LingoNumber(0),self._global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))
                self._global.member("finalDecalImage").image.setpixel(LingoGlobal.op_sub(LingoNumber(1400),LingoNumber(1)),LingoGlobal.op_sub(LingoNumber(800),LingoNumber(1)),self._global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))
                tmp_bd = bd                tmp_bd += 1                                    self._movieScript.c = LingoNumber(1)        if LingoGlobal.op_eq_b(self._movieScript.gLevel.lighttype, "No Light"):             self._global.member("shadowImage").image.copypixels(LingoImage.Pxl,self._global.member("shadowImage").image.rect,LingoImage.Pxl.rect)        self._movieScript.keepLooping = LingoNumber(1)                return None            