from Drizzle.Runtime import *## Behavior script: lightEditor#class lightEditor(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         q = None        dupl = None        era = None        l = None        curr = None        s = None        mv = None        dir1 = None        dir2 = None        angleadd = None        dsppos = None        rad = None        if LingoGlobal.ToBool(self._movieScript.showControls):             self._global.sprite(LingoNumber(189)).blend = LingoNumber(100)                    else:            self._global.sprite(LingoNumber(189)).blend = LingoNumber(0)                    tmp_q=int(LingoNumber(1))        while tmp_q < LingoNumber(4):             q = tmp_q            if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoList(LingoNumber(86),LingoNumber(91),LingoNumber(88),LingoNumber(84))[q])) and LingoGlobal.op_eq_b(self._movieScript.gDirectionKeys[q], LingoNumber(0))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLEProps.campos = LingoGlobal.op_add(self._movieScript.gLEProps.campos,LingoGlobal.op_mul(LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1)))[q],LingoGlobal.op_add(LingoGlobal.op_add(LingoNumber(1),LingoGlobal.op_mul(LingoNumber(9),self._global._key.keypressed(LingoNumber(83)))),LingoGlobal.op_mul(LingoNumber(34),self._global._key.keypressed(LingoNumber(85))))))                if not LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(92))):                     if self._movieScript.gLEProps.campos.loch < -LingoNumber(26):                         self._movieScript.gLEProps.campos.loch = -LingoNumber(26)                                            if self._movieScript.gLEProps.campos.locv < -LingoNumber(18):                         self._movieScript.gLEProps.campos.locv = -LingoNumber(18)                                            if self._movieScript.gLEProps.campos.loch > LingoGlobal.op_sub(self._movieScript.gLEProps.matrix.count,LingoNumber(56)):                         self._movieScript.gLEProps.campos.loch = LingoGlobal.op_sub(self._movieScript.gLEProps.matrix.count,LingoNumber(56))                                            if self._movieScript.gLEProps.campos.locv > LingoGlobal.op_sub(self._movieScript.gLEProps.matrix[LingoNumber(1)].count,LingoNumber(37)):                         self._movieScript.gLEProps.campos.locv = LingoGlobal.op_sub(self._movieScript.gLEProps.matrix[LingoNumber(1)].count,LingoNumber(37))                                                                        self._movieScript.gDirectionKeys[q] = self._global._key.keypressed(LingoList(LingoNumber(86),LingoNumber(91),LingoNumber(88),LingoNumber(84))[q])            tmp_q = q            tmp_q += 1                    if LingoGlobal.ToBool(self.checkkey("Z")):             self._movieScript.gLightEProps.col = LingoGlobal.op_sub(LingoNumber(1),self._movieScript.gLightEProps.col)                    if (LingoGlobal.ToBool(self._global._mouse.rightmousedown) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):             self._movieScript.gLightEProps.rot = self._movieScript.lookatpoint(self._movieScript.gLightEProps.pos,self._global._mouse.mouseloc)                    else:            self._movieScript.gLightEProps.pos = self._global._mouse.mouseloc                    if (LingoGlobal.ToBool(self._global._key.keypressed("C")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):             self._movieScript.glgtimgQuad[LingoNumber(1)] = LingoGlobal.op_add(self._global._mouse.mouseloc,LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))                    elif (LingoGlobal.ToBool(self._global._key.keypressed("V")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):             self._movieScript.glgtimgQuad[LingoNumber(2)] = LingoGlobal.op_add(self._global._mouse.mouseloc,LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))                    elif (LingoGlobal.ToBool(self._global._key.keypressed("B")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):             self._movieScript.glgtimgQuad[LingoNumber(3)] = LingoGlobal.op_add(self._global._mouse.mouseloc,LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))                    elif (LingoGlobal.ToBool(self._global._key.keypressed("N")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):             self._movieScript.glgtimgQuad[LingoNumber(4)] = LingoGlobal.op_add(self._global._mouse.mouseloc,LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))                    if LingoGlobal.ToBool(self.checkkey("M")):             dupl = self._global.image(self._global.member("lightImage").image.width,self._global.member("lightImage").image.height,LingoNumber(1))            dupl.copypixels(self._global.member("lightImage").image,dupl.rect,dupl.rect)
            era = self._global.image(self._global.member("lightImage").image.width,self._global.member("lightImage").image.height,LingoNumber(1))            self._global.member("lightImage").image.copypixels(era,self._global.member("lightImage").image.rect,era.rect)
            self._global.member("lightImage").image.copypixels(dupl,self._movieScript.glgtimgQuad,dupl.rect)
            self._movieScript.glgtimgQuad = LingoList(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),LingoGlobal.point(self._global.member("lightImage").image.width,LingoNumber(0)),LingoGlobal.point(self._global.member("lightImage").image.width,self._global.member("lightImage").image.height),LingoGlobal.point(LingoNumber(0),self._global.member("lightImage").image.height))                    if LingoGlobal.op_sub(self._global._system.milliseconds,self._movieScript.gLightEProps.lasttm) > LingoNumber(10):             if (LingoGlobal.ToBool(self._global._key.keypressed("W")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.sz.locv = LingoGlobal.op_add(self._movieScript.gLightEProps.sz.locv,LingoNumber(1))                            elif (LingoGlobal.ToBool(self._global._key.keypressed("S")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.sz.locv = LingoGlobal.op_sub(self._movieScript.gLightEProps.sz.locv,LingoNumber(1))                            if (LingoGlobal.ToBool(self._global._key.keypressed("D")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.sz.loch = LingoGlobal.op_add(self._movieScript.gLightEProps.sz.loch,LingoNumber(1))                            elif (LingoGlobal.ToBool(self._global._key.keypressed("A")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.sz.loch = LingoGlobal.op_sub(self._movieScript.gLightEProps.sz.loch,LingoNumber(1))                            if (LingoGlobal.ToBool(self._global._key.keypressed("Q")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.rot = LingoGlobal.op_sub(self._movieScript.gLightEProps.rot,LingoNumber(1))                            elif (LingoGlobal.ToBool(self._global._key.keypressed("E")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.rot = LingoGlobal.op_add(self._movieScript.gLightEProps.rot,LingoNumber(1))                            if (LingoGlobal.ToBool(self._global._key.keypressed("J")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.lightangle = self._movieScript.restrict(LingoGlobal.op_sub(self._movieScript.gLightEProps.lightangle,LingoNumber(1)),LingoNumber(0),LingoNumber(360))                if LingoGlobal.op_eq_b(self._movieScript.gLightEProps.lightangle, LingoNumber(0)):                     self._movieScript.gLightEProps.lightangle = LingoNumber(360)                                                elif (LingoGlobal.ToBool(self._global._key.keypressed("L")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                 self._movieScript.gLightEProps.lightangle = self._movieScript.restrict(LingoGlobal.op_add(self._movieScript.gLightEProps.lightangle,LingoNumber(1)),LingoNumber(0),LingoNumber(360))                if LingoGlobal.op_eq_b(self._movieScript.gLightEProps.lightangle, LingoNumber(360)):                     self._movieScript.gLightEProps.lightangle = LingoNumber(0)                                                if LingoGlobal.ToBool(self._movieScript.geverysecond):                 if (LingoGlobal.ToBool(self._global._key.keypressed("I")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                     self._movieScript.gLightEProps.flatness = self._movieScript.restrict(LingoGlobal.op_sub(self._movieScript.gLightEProps.flatness,LingoNumber(1)),LingoNumber(1),LingoNumber(10))                                    elif (LingoGlobal.ToBool(self._global._key.keypressed("K")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, minimized)):                     self._movieScript.gLightEProps.flatness = self._movieScript.restrict(LingoGlobal.op_add(self._movieScript.gLightEProps.flatness,LingoNumber(1)),LingoNumber(1),LingoNumber(10))                                    self._movieScript.geverysecond = LingoNumber(0)                            else:                self._movieScript.geverysecond = LingoNumber(1)                            self._movieScript.gLightEProps.lasttm = self._global._system.milliseconds                    l = LingoList("pxl","squareLightEmpty","bigCircle","discLightEmpty","leaves","oilyLight","directionalLight","blobLight1","blobLight2","wormsLight","crackLight","squareishLight","holeLight","roundedRectLight","roundedRectLightEmpty","triangleLight","triangleLightEmpty","curvedTriangleLight","curvedTriangleLightEmpty","pentagonLight","pentagonLightEmpty","hexagonLight","hexagonLightEmpty","octagonLight","octagonLightEmpty","DR1DestLight","DR2DestLight","DR3DestLight")        curr = LingoNumber(1)        tmp_s=int(LingoNumber(1))        while tmp_s < l.count:             s = tmp_s            if LingoGlobal.op_eq_b(l[s], self._movieScript.gLightEProps.paintshape):                 curr = s                break                            tmp_s = s            tmp_s += 1                    mv = LingoNumber(0)        if LingoGlobal.ToBool(self.checkkey("r")):             mv = -LingoNumber(1)                    elif LingoGlobal.ToBool(self.checkkey("f")):             mv = LingoNumber(1)                    if LingoGlobal.op_ne_b(mv, LingoNumber(0)):             curr = self._movieScript.restrict(LingoGlobal.op_add(curr,mv),LingoNumber(1),l.count)            self._global.sprite(LingoNumber(181)).member = self._global.member(l[curr])            self._global.sprite(LingoNumber(182)).member = self._global.member(l[curr])            self._movieScript.gLightEProps.paintshape = l[curr]                    dir1 = self._movieScript.degtovec(self._movieScript.gLightEProps.rot)        dir2 = self._movieScript.degtovec(LingoGlobal.op_add(self._movieScript.gLightEProps.rot,LingoNumber(90)))        angleadd = LingoGlobal.op_mul(self._movieScript.degtovec(self._movieScript.gLightEProps.lightangle),LingoGlobal.op_mul(self._movieScript.gLightEProps.flatness,LingoNumber(10)))        dsppos = LingoGlobal.point(LingoGlobal.op_sub(LingoGlobal.op_div(LingoNumber(1366),LingoNumber(2)),LingoGlobal.op_div(self._global.member("lightImage").image.width,LingoNumber(2))),LingoGlobal.op_sub(LingoGlobal.op_div(LingoNumber(768),LingoNumber(2)),LingoGlobal.op_div(self._global.member("lightImage").image.height,LingoNumber(2))))        dsppos = LingoGlobal.op_sub(dsppos,LingoGlobal.point(LingoNumber(150),LingoNumber(150)))        q = LingoGlobal.op_add(LingoList(self._movieScript.gLightEProps.pos,self._movieScript.gLightEProps.pos,self._movieScript.gLightEProps.pos,self._movieScript.gLightEProps.pos),LingoList(LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20))))        q = LingoGlobal.op_add(q,LingoList(LingoGlobal.op_sub(LingoGlobal.op_mul(-dir2,self._movieScript.gLightEProps.sz.loch),LingoGlobal.op_mul(dir1,self._movieScript.gLightEProps.sz.locv)),LingoGlobal.op_sub(LingoGlobal.op_mul(dir2,self._movieScript.gLightEProps.sz.loch),LingoGlobal.op_mul(dir1,self._movieScript.gLightEProps.sz.locv)),LingoGlobal.op_add(LingoGlobal.op_mul(dir2,self._movieScript.gLightEProps.sz.loch),LingoGlobal.op_mul(dir1,self._movieScript.gLightEProps.sz.locv)),LingoGlobal.op_add(LingoGlobal.op_mul(-dir2,self._movieScript.gLightEProps.sz.loch),LingoGlobal.op_mul(dir1,self._movieScript.gLightEProps.sz.locv))))        self._movieScript.gLightEProps.keys.m1 = LingoGlobal.op_and(self._global._mouse.mousedown,LingoGlobal.op_ne(self._global._movie.window.sizestate,minimized))        if (LingoGlobal.ToBool(self._movieScript.gLightEProps.keys.m1) and LingoGlobal.op_ne_b(self._movieScript.firstFrame, LingoNumber(1))):             self._global.member("lightImage").image.copypixels(self._global.member(self._movieScript.gLightEProps.paintshape).image,LingoGlobal.op_sub(q,LingoList(dsppos,dsppos,dsppos,dsppos)),self._global.member(self._movieScript.gLightEProps.paintshape).image.rect,LingoPropertyList(dict(color = LingoGlobal.op_mul(self._movieScript.gLightEProps.col,LingoNumber(255)),ink = LingoNumber(36))))        if LingoGlobal.op_eq_b(self._movieScript.gLightEProps.keys.m1, LingoNumber(0)):             self._movieScript.firstFrame = LingoNumber(0)                    self._movieScript.gLightEProps.lastkeys.m1 = self._movieScript.gLightEProps.keys.m1        self._global.sprite(LingoNumber(181)).quad = LingoGlobal.op_sub(q,LingoList(LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20))))        self._global.sprite(LingoNumber(182)).quad = LingoGlobal.op_sub(q,LingoList(LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20))))        self._global.sprite(LingoNumber(181)).color = self._global.color(LingoGlobal.op_mul(LingoGlobal.op_sub(LingoNumber(1),self._movieScript.gLightEProps.col),LingoNumber(255)),LingoGlobal.op_mul(LingoGlobal.op_sub(LingoNumber(1),self._movieScript.gLightEProps.col),LingoNumber(255)),LingoGlobal.op_mul(LingoGlobal.op_sub(LingoNumber(1),self._movieScript.gLightEProps.col),LingoNumber(255)))        self._global.sprite(LingoNumber(180)).quad = LingoGlobal.op_add(LingoGlobal.op_sub(self._movieScript.glgtimgQuad,LingoList(LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))),LingoList(dsppos,dsppos,dsppos,dsppos))        self._global.sprite(LingoNumber(185)).rect = LingoGlobal.op_add(LingoGlobal.rect(LingoGlobal.point(LingoNumber(850),LingoNumber(650)),LingoGlobal.point(LingoNumber(850),LingoNumber(650))),LingoGlobal.rect(-LingoNumber(50),-LingoNumber(50),LingoNumber(50),LingoNumber(50)))        rad = LingoGlobal.op_mul(self._movieScript.gLightEProps.flatness,LingoNumber(10))        self._global.sprite(LingoNumber(186)).rect = LingoGlobal.op_add(LingoGlobal.rect(LingoGlobal.point(LingoNumber(850),LingoNumber(650)),LingoGlobal.point(LingoNumber(850),LingoNumber(650))),LingoGlobal.rect(-rad,-rad,rad,rad))        self._global.sprite(LingoNumber(187)).loc = LingoGlobal.op_sub(LingoGlobal.point(LingoNumber(850),LingoNumber(650)),LingoGlobal.op_mul(self._movieScript.degtovec(self._movieScript.gLightEProps.lightangle),rad))        self._global.sprite(LingoNumber(176)).loc = LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.point(LingoGlobal.op_div(LingoNumber(1366),LingoNumber(2)),LingoGlobal.op_div(LingoNumber(768),LingoNumber(2))),LingoGlobal.point(LingoNumber(150),LingoNumber(150))),LingoGlobal.op_mul(angleadd,LingoNumber(2))),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))        self._global.sprite(LingoNumber(179)).loc = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoGlobal.point(LingoGlobal.op_div(LingoNumber(1366),LingoNumber(2)),LingoGlobal.op_div(LingoNumber(768),LingoNumber(2))),LingoGlobal.point(LingoNumber(150),LingoNumber(150))),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))        self._global.sprite(LingoNumber(175)).loc = LingoGlobal.op_sub(LingoGlobal.point(LingoGlobal.op_div(LingoNumber(1366),LingoNumber(2)),LingoGlobal.op_div(LingoNumber(768),LingoNumber(2))),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))        self._global.sprite(LingoNumber(178)).loc = LingoGlobal.op_sub(LingoGlobal.point(LingoGlobal.op_div(LingoNumber(1366),LingoNumber(2)),LingoGlobal.op_div(LingoNumber(768),LingoNumber(2))),LingoGlobal.op_mul(self._movieScript.gLEProps.campos,LingoNumber(20)))        self._global.script("levelOverview").gotoeditor()
        self._global.go(self._global.the_frame)        return None            def checkkey(self, key):         rtrn = None        rtrn = LingoNumber(0)        self._movieScript.gLightEProps.keys[LingoGlobal.symbol(key)] = LingoGlobal.op_and(self._global._key.keypressed(key),LingoGlobal.op_ne(self._global._movie.window.sizestate,minimized))        if (LingoGlobal.ToBool(self._movieScript.gLightEProps.keys[LingoGlobal.symbol(key)]) and LingoGlobal.op_eq_b(self._movieScript.gLightEProps.lastkeys[LingoGlobal.symbol(key)], LingoNumber(0))):             rtrn = LingoNumber(1)                    self._movieScript.gLightEProps.lastkeys[LingoGlobal.symbol(key)] = self._movieScript.gLightEProps.keys[LingoGlobal.symbol(key)]        return rtrn                    