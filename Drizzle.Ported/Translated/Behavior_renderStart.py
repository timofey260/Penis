from Drizzle.Runtime import *## Behavior script: renderStart#class renderStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         nonsolidtilesets = None        q = None        l = None        c = None        cell = None        d = None        ad = None        tl = None        testmat = None        tlps = None        self._movieScript.DRPxl = LingoImage.Pxl        self._movieScript.DRPxlRect = LingoImage.Pxl.rect        self._movieScript.DRWhite = self._global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))        self._movieScript.slimeFxt = self._movieScript.getboolconfig("Slime always affects editor decals")        self._movieScript.gRRSpreadsMore = self._movieScript.getboolconfig("Rough Rock spreads more")        self._movieScript.grimeActive = self._movieScript.getboolconfig("Grime")        self._movieScript.grimeOnGradients = self._movieScript.getboolconfig("Grime on gradients")        self._movieScript.bkgFix = self._movieScript.getboolconfig("Gradients with BackgroundScenes fix")        self._movieScript.gDRMatFixes = self._movieScript.getboolconfig("Material fixes")        self._movieScript.gDRInvI = self._movieScript.getboolconfig("Invisible material fix")        self._global.member("blackOutImg1").image = self._global.image(LingoNumber(1),LingoNumber(1),LingoNumber(1))        self._global.member("blackOutImg2").image = self._global.image(LingoNumber(1),LingoNumber(1),LingoNumber(1))        self._global.member("GradientOutput").image = self._global.image(LingoNumber(1),LingoNumber(1),LingoNumber(1))        self._global._movie.exitlock = LingoGlobal.TRUE        if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        if LingoGlobal.ToBool(self._movieScript.checkexitrender()):             self._global._movie.go(LingoNumber(9))        self._global.put("Start render")
        self._movieScript.gLOprops.pal = LingoNumber(1)        self._movieScript.firstCamRepeat = LingoGlobal.TRUE        self._movieScript.gCurrentRenderCamera = LingoNumber(0)        self._movieScript.gAnyDecals = LingoNumber(0)        self.createshortcuts()
        self._movieScript.tileSetIndex = LingoList()        self._movieScript.solidMtrx = LingoList()        if LingoGlobal.ToBool(self._movieScript.getboolconfig("Trash and Small pipes non solid")):             nonsolidtilesets = LingoList("Small Pipes","Trash")                    else:            nonsolidtilesets = LingoList()                    if LingoGlobal.op_eq_b(self._movieScript.gDRInvI, LingoGlobal.FALSE):             nonsolidtilesets.add("Invisible")        tmp_q=int(LingoNumber(1))        while tmp_q < self._movieScript.gLOprops.size.loch:             q = LingoNumber(tmp_q)            l = LingoList()            tmp_c=int(LingoNumber(1))            while tmp_c < self._movieScript.gLOprops.size.locv:                 c = LingoNumber(tmp_c)                cell = LingoList()                tmp_d=int(LingoNumber(1))                while tmp_d < LingoNumber(3):                     d = LingoNumber(tmp_d)                    ad = LingoNumber(0)                    if (LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][c][d][LingoNumber(1)], LingoNumber(1)) and LingoGlobal.op_eq_b(self._movieScript.gLEProps.matrix[q][c][d][LingoNumber(2)].getpos(LingoNumber(11)), LingoNumber(0))):                         tl = self._movieScript.gTEprops.tlmatrix[q][c][d]                        if (LingoGlobal.op_eq_b(tl.tp, "default") or LingoGlobal.op_eq_b(tl.tp, "material")):                             testmat = tl.data                            if LingoGlobal.op_eq_b(tl.tp, "default"):                                 testmat = self._movieScript.gTEprops.defaultmaterial                                                            ad = LingoGlobal.op_eq(nonsolidtilesets.getpos(testmat),LingoNumber(0))                                                    elif (LingoGlobal.op_eq_b(tl.tp, "tileHead") or LingoGlobal.op_eq_b(tl.tp, "tileBody")):                             tlps = tl.data[LingoNumber(1)]                            if LingoGlobal.op_eq_b(tl.tp, "tileBody"):                                 tlps = LingoGlobal.VOID                                if (((tl.data[LingoNumber(1)].locv > LingoNumber(0) and tl.data[LingoNumber(1)].loch > LingoNumber(0)) and tl.data[LingoNumber(1)].locv < self._movieScript.gLOprops.size.locv) and tl.data[LingoNumber(1)].loch < self._movieScript.gLOprops.size.loch):                                     if LingoGlobal.op_eq_b(self._global.ilk(self._movieScript.gTEprops.tlmatrix[tl.data[LingoNumber(1)].loch][tl.data[LingoNumber(1)].locv][tl.data[LingoNumber(2)]].data), LingoSymbol("list")):                                         tlps = self._movieScript.gTEprops.tlmatrix[tl.data[LingoNumber(1)].loch][tl.data[LingoNumber(1)].locv][tl.data[LingoNumber(2)]].data[LingoNumber(1)]                                                                                                                                        ad = LingoNumber(1)                            if LingoGlobal.op_ne_b(tlps, LingoGlobal.VOID):                                 if (tlps.loch > LingoNumber(2) and tlps.loch <= self._movieScript.gTiles.count):                                     if tlps.locv <= self._movieScript.gTiles[tlps.loch].tls.count:                                         if LingoGlobal.op_ne_b(self._movieScript.gTiles[tlps.loch].tls[tlps.locv].tags, LingoGlobal.VOID):                                             ad = LingoGlobal.op_eq(self._movieScript.gTiles[tlps.loch].tls[tlps.locv].tags.getpos("nonSolid"),LingoNumber(0))                                                                                                                                                                                                                                cell.add(ad)
                    tmp_d = int(d)                    tmp_d += 1                                    l.add(cell)
                tmp_c = int(c)                tmp_c += 1                            self._movieScript.solidMtrx.add(l)
            tmp_q = int(q)            tmp_q += 1                            return None            def createshortcuts(self):         q = None        c = None        diditwork = None        tp = None        holedir = None        stps = None        pos = None        stp = None        lastdir = None        rpt = None        dirsl = None        dir = None        self._movieScript.gShortcuts = LingoPropertyList(LingoSymbol("scs"), LingoList(),LingoSymbol("indexl"), LingoList())        tmp_q=int(LingoNumber(2))        while tmp_q < LingoGlobal.op_sub(self._movieScript.gLEProps.matrix.count,LingoNumber(1)):             q = LingoNumber(tmp_q)            tmp_c=int(LingoNumber(2))            while tmp_c < LingoGlobal.op_sub(self._movieScript.gLEProps.matrix[LingoNumber(1)].count,LingoNumber(1)):                 c = LingoNumber(tmp_c)                if self._movieScript.gLEProps.matrix[q][c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(4)) > LingoNumber(0):                     diditwork = LingoNumber(1)                    tp = "shortCut"                    holedir = LingoGlobal.point(LingoNumber(0),LingoNumber(0))                    stps = LingoNumber(0)                    pos = LingoGlobal.point(q,c)                    stp = LingoNumber(0)                    lastdir = LingoGlobal.point(LingoNumber(0),LingoNumber(0))                    rpt = LingoNumber(0)                    while LingoGlobal.ToBool(LingoGlobal.op_eq(stp,LingoNumber(0))):                         rpt = LingoGlobal.op_add(rpt,LingoNumber(1))                        if rpt > LingoNumber(1000):                             diditwork = LingoNumber(0)                            stp = LingoNumber(1)                                                    dirsl = LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1)))                        dirsl.deleteone(lastdir)
                        dirsl.addat(LingoNumber(1),lastdir)
                        dirsl.deleteone(-lastdir)
                        for tmp_dir in dirsl:                             dir = LingoNumber(tmp_dir)                            if LingoGlobal.ToBool(LingoGlobal.op_add(pos,dir).inside(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),LingoGlobal.op_add(self._movieScript.gLOprops.size.loch,LingoNumber(1)),LingoGlobal.op_add(self._movieScript.gLOprops.size.locv,LingoNumber(1))))):                                 if self._movieScript.gLEProps.matrix[LingoGlobal.op_add(pos.loch,dir.loch)][LingoGlobal.op_add(pos.locv,dir.locv)][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(6)) > LingoNumber(0):                                     stp = LingoNumber(1)                                    tp = "playerHole"                                    pos = LingoGlobal.point(q,c)                                    lastdir = dir                                    break                                                                    elif self._movieScript.gLEProps.matrix[LingoGlobal.op_add(pos.loch,dir.loch)][LingoGlobal.op_add(pos.locv,dir.locv)][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(7)) > LingoNumber(0):                                     stp = LingoNumber(1)                                    tp = "lizardHole"                                    pos = LingoGlobal.point(q,c)                                    lastdir = dir                                    break                                                                    elif self._movieScript.gLEProps.matrix[LingoGlobal.op_add(pos.loch,dir.loch)][LingoGlobal.op_add(pos.locv,dir.locv)][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(19)) > LingoNumber(0):                                     stp = LingoNumber(1)                                    tp = "WHAMH"                                    pos = LingoGlobal.point(q,c)                                    lastdir = dir                                    break                                                                    elif self._movieScript.gLEProps.matrix[LingoGlobal.op_add(pos.loch,dir.loch)][LingoGlobal.op_add(pos.locv,dir.locv)][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(21)) > LingoNumber(0):                                     stp = LingoNumber(1)                                    tp = "scavengerHole"                                    pos = LingoGlobal.point(q,c)                                    lastdir = dir                                    break                                                                    elif self._movieScript.gLEProps.matrix[LingoGlobal.op_add(pos.loch,dir.loch)][LingoGlobal.op_add(pos.locv,dir.locv)][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(4)) > LingoNumber(0):                                     stp = LingoNumber(1)                                    pos = LingoGlobal.op_add(pos,dir)                                    lastdir = dir                                    break                                                                    elif self._movieScript.gLEProps.matrix[LingoGlobal.op_add(pos.loch,dir.loch)][LingoGlobal.op_add(pos.locv,dir.locv)][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(5)) > LingoNumber(0):                                     stps = LingoGlobal.op_add(stps,LingoNumber(1))                                    pos = LingoGlobal.op_add(pos,dir)                                    lastdir = dir                                    break                                                                                                                        if LingoGlobal.op_eq_b(holedir, LingoGlobal.point(LingoNumber(0),LingoNumber(0))):                             holedir = lastdir                                                                        if LingoGlobal.ToBool(diditwork):                         self._movieScript.gShortcuts.indexl.add(LingoGlobal.point(q,c))
                        self._movieScript.gShortcuts.scs.add(tp)                                    tmp_c = int(c)                tmp_c += 1                            tmp_q = int(q)            tmp_q += 1                            return None            