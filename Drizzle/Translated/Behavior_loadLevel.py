from Drizzle.Runtime import *## Behavior script: loadLevel#class loadLevel(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         if LingoGlobal.ToBool(self._movieScript.showControls):             self._global.sprite(LingoNumber(32)).blend = LingoNumber(100)                    else:            self._global.sprite(LingoNumber(32)).blend = LingoNumber(0)                    if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        txt = "Use the up and down keys to select a project. Use enter to open it."        txt += str(LingoGlobal.RETURN)        for tmp_f in self._movieScript.gLOADPATH:             f = tmp_f            txt += str(LingoGlobal.concat(f,"/"))                    txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        tmp_q = self._movieScript.ldPrps.listscrollpos        while tmp_q < LingoGlobal.op_add(self._movieScript.ldPrps.listscrollpos,self._movieScript.ldPrps.listshowtotal):             q = tmp_q            if q > self._movieScript.projects.count:                 break                            else:                if LingoGlobal.op_ne_b(q, self._movieScript.ldPrps.currproject):                     txt += str(self._movieScript.projects[q])                                    else:                    txt += str(LingoGlobal.concat_space("<",self._movieScript.projects[q],">"))                                    txt += str(LingoGlobal.RETURN)                            tmp_q = q            tmp_q += LingoNumber(1)                    self._global.member("ProjectsL").text = txt        up = self._global._key.keypressed(LingoNumber(126))        dwn = self._global._key.keypressed(LingoNumber(125))        lft = self._global._key.keypressed(LingoNumber(123))        rgth = self._global._key.keypressed(LingoNumber(124))        if LingoGlobal.op_eq_b(self._global._movie.window.sizestate, LingoSymbol("minimized")):             up = LingoGlobal.FALSE            dwn = LingoGlobal.FALSE            lft = LingoGlobal.FALSE            rgth = LingoGlobal.FALSE                    if (LingoGlobal.ToBool(up) and LingoGlobal.op_eq_b(self._movieScript.ldPrps.lstup, LingoNumber(0))):             self._movieScript.ldPrps.currproject = LingoGlobal.op_sub(self._movieScript.ldPrps.currproject,LingoNumber(1))            if self._movieScript.ldPrps.currproject < LingoNumber(1):                 self._movieScript.ldPrps.currproject = self._movieScript.projects.count                                    if (LingoGlobal.ToBool(dwn) and LingoGlobal.op_eq_b(self._movieScript.ldPrps.lstdwn, LingoNumber(0))):             self._movieScript.ldPrps.currproject = LingoGlobal.op_add(self._movieScript.ldPrps.currproject,LingoNumber(1))            if self._movieScript.ldPrps.currproject > self._movieScript.projects.count:                 self._movieScript.ldPrps.currproject = LingoNumber(1)                                    if self._movieScript.ldPrps.currproject < self._movieScript.ldPrps.listscrollpos:             self._movieScript.ldPrps.listscrollpos = self._movieScript.ldPrps.currproject                    elif self._movieScript.ldPrps.currproject > LingoGlobal.op_add(self._movieScript.ldPrps.listscrollpos,self._movieScript.ldPrps.listshowtotal):             self._movieScript.ldPrps.listscrollpos = LingoGlobal.op_sub(self._movieScript.ldPrps.currproject,self._movieScript.ldPrps.listshowtotal)                    if ((LingoGlobal.ToBool(rgth) and LingoGlobal.op_eq_b(self._movieScript.ldPrps.rgth, LingoNumber(0))) and self._movieScript.projects.count > LingoNumber(0)):             if LingoGlobal.op_eq_b(LingoGlobal.chars(self._movieScript.projects[self._movieScript.ldPrps.currproject],LingoNumber(1),LingoNumber(1)), "#"):                 self.loadsubfolder(self._movieScript.projects[self._movieScript.ldPrps.currproject])                    elif (LingoGlobal.ToBool(lft) and LingoGlobal.op_eq_b(self._movieScript.ldPrps.lft, LingoNumber(0))):             if self._movieScript.gLOADPATH.count > LingoNumber(0):                 self._movieScript.gLOADPATH.deleteat(self._movieScript.gLOADPATH.count)                self._global._movie.go(LingoNumber(2))                    self._movieScript.ldPrps.lstup = up        self._movieScript.ldPrps.lstdwn = dwn        self._movieScript.ldPrps.lft = lft        self._movieScript.ldPrps.rgth = rgth        if (LingoGlobal.ToBool(self._global._key.keypressed("N")) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._movieScript.gLoadedName = "New Project"            self._global.member("level Name").text = "New Project"            self._global._movie.go(LingoNumber(7))        elif ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(36))) and self._movieScript.projects.count > LingoNumber(0)) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             if LingoGlobal.op_ne_b(LingoGlobal.chars(self._movieScript.projects[self._movieScript.ldPrps.currproject],LingoNumber(1),LingoNumber(1)), "#"):                 self.loadlevel(self._movieScript.projects[self._movieScript.ldPrps.currproject])                self._global._movie.go(LingoNumber(7))                    self._global.go(self._global.the_frame)        return None            def loadsubfolder(self, fldrname):         self._movieScript.gLOADPATH.add(LingoGlobal.chars(fldrname,LingoNumber(2),LingoGlobal.lengthmember_helper(fldrname)))        self._global._movie.go(LingoNumber(2))        return None            def loadlevel(self, lvlname, fullpath):         if LingoGlobal.ToBool(fullpath):             pth = ""                    else:            pth = LingoGlobal.concat(self._global.the_moviePath,"LevelEditorProjects",self._global.the_dirSeparator)            for tmp_f in self._movieScript.gLOADPATH:                 f = tmp_f                pth = LingoGlobal.concat(pth,f,self._global.the_dirSeparator)                                    objfileio = self._global.new(self._global.xtra("fileio"))        objfileio.openfile(LingoGlobal.concat(pth,lvlname,".txt"),LingoNumber(0))        if LingoGlobal.op_eq_b(fullpath, LingoNumber(1)):             self._movieScript.gLoadedName = ""            lastbackslash = LingoNumber(0)            tmp_q = LingoNumber(1)            while tmp_q < LingoGlobal.lengthmember_helper(lvlname):                 q = tmp_q                if LingoGlobal.op_eq_b(LingoGlobal.chars(lvlname,q,q), self._global.the_dirSeparator):                     lastbackslash = q                                    tmp_q = q                tmp_q += LingoNumber(1)                            self._movieScript.gLoadedName = LingoGlobal.chars(lvlname,LingoGlobal.op_add(lastbackslash,LingoNumber(1)),LingoGlobal.lengthmember_helper(lvlname))            self._global.put(self._movieScript.gLoadedName)        else:            self._movieScript.gLoadedName = lvlname                    self._global.member("level Name").text = lvlname        l2 = objfileio.readfile()        objfileio.closefile()        sv2 = self._movieScript.gLOprops.duplicate()        l1 = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(1)])        self._movieScript.gLEProps.matrix = l1        l1 = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(2)])        self._movieScript.gTEprops = l1        l1 = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(3)])        self._movieScript.gEEprops = l1        l1 = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(4)])        self._movieScript.gLightEProps = l1        l1 = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(5)])        self._movieScript.gLevel = l1        l1 = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(6)])        self._movieScript.gLOprops = l1        if LingoGlobal.op_eq_b(self._movieScript.gLOprops.findpos(LingoSymbol("light")), LingoGlobal.VOID):             self._movieScript.gLOprops.addprop(LingoSymbol("light"),LingoNumber(1))        if LingoGlobal.op_eq_b(self._movieScript.gTEprops.findpos(LingoSymbol("specialedit")), LingoGlobal.VOID):             self._movieScript.gTEprops.addprop(LingoSymbol("specialedit"),LingoNumber(0))        if LingoGlobal.op_eq_b(self._movieScript.gLOprops.findpos(LingoSymbol("size")), LingoGlobal.VOID):             self._movieScript.gLOprops.addprop(LingoSymbol("size"),LingoGlobal.point(LingoNumber(52),LingoNumber(40)))        if LingoGlobal.op_eq_b(self._movieScript.gLOprops.findpos(LingoSymbol("extratiles")), LingoGlobal.VOID):             self._movieScript.gLOprops.addprop(LingoSymbol("extratiles"),LingoList(LingoNumber(1),LingoNumber(1),LingoNumber(1),LingoNumber(3)))        self._movieScript.gLOprops.pals = LingoList(LingoPropertyList(LingoSymbol("detcol"), self._global.color(LingoNumber(255),LingoNumber(0),LingoNumber(0))))        if LingoGlobal.op_eq_b(self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(7)]), LingoGlobal.VOID):             self._movieScript.gCameraProps.cameras = LingoList(LingoGlobal.op_sub(LingoGlobal.point(LingoGlobal.op_mul(self._movieScript.gLOprops.size.loch,LingoNumber(10)),LingoGlobal.op_mul(self._movieScript.gLOprops.size.locv,LingoNumber(10))),LingoGlobal.point(LingoGlobal.op_mul(LingoNumber(35),LingoNumber(20)),LingoGlobal.op_mul(LingoNumber(20),LingoNumber(20)))))                    else:            self._movieScript.gCameraProps = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(7)])                    valenv = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(8)])        if ((LingoGlobal.op_eq_b(valenv, LingoGlobal.VOID) or LingoGlobal.op_ne_b(self._global.ilk(valenv), LingoSymbol("proplist"))) or LingoGlobal.op_eq_b(valenv.findpos(LingoSymbol("waterlevel")), LingoGlobal.VOID)):             self._movieScript.resetgenveditorprops()        else:            self._movieScript.gEnvEditorProps = valenv                    if (LingoGlobal.op_eq_b(self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(9)]), LingoGlobal.VOID) or LingoGlobal.op_ne_b(LingoGlobal.chars(LingoGlobal.linemember_helper(l2)[LingoNumber(9)],LingoNumber(1),LingoNumber(6)), "[#prop")):             self._movieScript.resetpropeditorprops()        else:            self._movieScript.gPEprops = self._global.value(LingoGlobal.linemember_helper(l2)[LingoNumber(9)])                    if LingoGlobal.op_eq_b(self._movieScript.gPEprops.findpos(LingoSymbol("color")), LingoGlobal.VOID):             self._movieScript.gPEprops.addprop(LingoSymbol("color"),LingoNumber(0))        if LingoGlobal.op_eq_b(self._movieScript.gPEprops.findpos(LingoSymbol("props")), LingoGlobal.VOID):             self._movieScript.gPEprops.addprop(LingoSymbol("props"),LingoList())        self._movieScript.gTEprops.tmpos = LingoGlobal.point(LingoNumber(2),LingoNumber(1))        self.versionfix()        self._global.member("lightImage").image = self._global.image(LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLOprops.size.loch,LingoNumber(20)),LingoNumber(300)),LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLOprops.size.locv,LingoNumber(20)),LingoNumber(300)),LingoNumber(1))        sav = self._global.member("lightImage")        self._global.member("lightImage").importfileinto(LingoGlobal.concat(pth,lvlname,".png"))        sav.name = "lightImage"        if LingoGlobal.op_ne_b(self._global.member("lightImage").image.rect, LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLOprops.size.loch,LingoNumber(20)),LingoNumber(300)),LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLOprops.size.locv,LingoNumber(20)),LingoNumber(300)))):             wantedrect = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLOprops.size.loch,LingoNumber(20)),LingoNumber(300)),LingoGlobal.op_add(LingoGlobal.op_mul(self._movieScript.gLOprops.size.locv,LingoNumber(20)),LingoNumber(300)))            img = self._global.image(wantedrect.width,wantedrect.height,LingoNumber(1))            img.copypixels(self._global.member("lightImage").image,LingoGlobal.op_add(LingoGlobal.rect(LingoGlobal.op_div(wantedrect.width,LingoNumber(2)),LingoGlobal.op_div(wantedrect.height,LingoNumber(2)),LingoGlobal.op_div(wantedrect.width,LingoNumber(2)),LingoGlobal.op_div(wantedrect.height,LingoNumber(2))),LingoGlobal.rect(LingoGlobal.op_div(-self._global.member("lightImage").rect.width,LingoNumber(2)),LingoGlobal.op_div(-self._global.member("lightImage").image.rect.height,LingoNumber(2)),LingoGlobal.op_div(self._global.member("lightImage").image.rect.width,LingoNumber(2)),LingoGlobal.op_div(self._global.member("lightImage").image.rect.height,LingoNumber(2)))),self._global.member("lightImage").image.rect)            self._global.member("lightImage").image = img            self._global.put("Adapted light rect")        self._movieScript.gLASTDRAWWASFULLANDMINI = LingoNumber(0)        self._global.put(LingoGlobal.concat(pth,self._global.the_dirSeparator,lvlname,".png"))        return None            def versionfix(self):         tmp_q = LingoNumber(1)        while tmp_q < self._movieScript.gLOprops.size.loch:             q = tmp_q            tmp_c = LingoNumber(1)            while tmp_c < self._movieScript.gLOprops.size.locv:                 c = tmp_c                tmp_d = LingoNumber(1)                while tmp_d < LingoNumber(3):                     d = tmp_d                    if LingoGlobal.op_eq_b(self._movieScript.gTEprops.tlmatrix[q][c][d].tp, "tileHead"):                         huntnew = ""                        if self._movieScript.gTEprops.tlmatrix[q][c][d].data.count < LingoNumber(2):                             huntnew = self._movieScript.gTEprops.tlmatrix[q][c][d].data.nm                                                    else:                            pnt = self._movieScript.gTEprops.tlmatrix[q][c][d].data[LingoNumber(1)]                            if self._movieScript.gTiles.count >= pnt.loch:                                 if self._movieScript.gTiles[pnt.loch].tls.count >= pnt.locv:                                     if LingoGlobal.op_ne_b(self._movieScript.gTiles[pnt.loch].tls[pnt.locv].nm, self._movieScript.gTEprops.tlmatrix[q][c][d].data[LingoNumber(2)]):                                         huntnew = self._movieScript.gTEprops.tlmatrix[q][c][d].data[LingoNumber(2)]                                                                                                            else:                                    huntnew = self._movieScript.gTEprops.tlmatrix[q][c][d].data[LingoNumber(2)]                                                                                                else:                                huntnew = self._movieScript.gTEprops.tlmatrix[q][c][d].data[LingoNumber(2)]                                                                                    found = LingoNumber(0)                        if LingoGlobal.op_ne_b(huntnew, ""):                             self._movieScript.gTEprops.tlmatrix[q][c][d].data = LingoList(LingoGlobal.point(LingoNumber(2),LingoNumber(1)),"NOT FOUND")                            tmp_cat = LingoNumber(1)                            while tmp_cat < self._movieScript.gTiles.count:                                 cat = tmp_cat                                tmp_tl = LingoNumber(1)                                while tmp_tl < self._movieScript.gTiles[cat].tls.count:                                     tl = tmp_tl                                    if LingoGlobal.op_eq_b(self._movieScript.gTiles[cat].tls[tl].nm, huntnew):                                         self._movieScript.gTEprops.tlmatrix[q][c][d].data = LingoList(LingoGlobal.point(cat,tl),huntnew)                                        found = LingoNumber(1)                                        break                                                                            tmp_tl = tl                                    tmp_tl += LingoNumber(1)                                                                    if LingoGlobal.ToBool(found):                                     break                                                                    tmp_cat = cat                                tmp_cat += LingoNumber(1)                                                            if not LingoGlobal.ToBool(found):                                 self._movieScript.writeexception("Tile Not Found",LingoGlobal.concat("the tile ",LingoGlobal.QUOTE,huntnew,LingoGlobal.QUOTE," is missing in the Init.txt file from your Graphics folder."))                                self._global.put(LingoGlobal.concat("Warning: unknown tile '",huntnew,"' in map file. Replacing with default material."))                                self._movieScript.gTEprops.tlmatrix[q][c][d] = LingoPropertyList(LingoSymbol("tp"), "default",LingoSymbol("data"), LingoNumber(0))                                                                                                        tmp_d = d                    tmp_d += LingoNumber(1)                                    tmp_c = c                tmp_c += LingoNumber(1)                            tmp_q = q            tmp_q += LingoNumber(1)                    tmp_q = LingoNumber(1)        while tmp_q < self._movieScript.gLEProps.toolmatrix.count:             q = tmp_q            tmp_c = LingoNumber(1)            while tmp_c < self._movieScript.gLEProps.toolmatrix[LingoNumber(1)].count:                 c = tmp_c                if LingoGlobal.op_eq_b(self._movieScript.gLEProps.toolmatrix[q][c], "save"):                     self._movieScript.gLEProps.toolmatrix[q][c] = ""                                    tmp_c = c                tmp_c += LingoNumber(1)                            tmp_q = q            tmp_q += LingoNumber(1)                    tmp_q = LingoNumber(1)        while tmp_q < self._movieScript.gPEprops.props.count:             q = tmp_q            correctreference = LingoGlobal.TRUE            if self._movieScript.gPEprops.props[q][LingoNumber(3)].loch > self._movieScript.gProps.count:                 correctreference = LingoGlobal.FALSE                            elif self._movieScript.gPEprops.props[q][LingoNumber(3)].locv > self._movieScript.gProps[self._movieScript.gPEprops.props[q][LingoNumber(3)].loch].prps.count:                 correctreference = LingoGlobal.FALSE                            elif LingoGlobal.op_ne_b(self._movieScript.gProps[self._movieScript.gPEprops.props[q][LingoNumber(3)].loch].prps[self._movieScript.gPEprops.props[q][LingoNumber(3)].locv].nm, self._movieScript.gPEprops.props[q][LingoNumber(2)]):                 correctreference = LingoGlobal.FALSE                            if LingoGlobal.op_eq_b(correctreference, LingoGlobal.FALSE):                 tmp_a = LingoNumber(1)                while tmp_a < self._movieScript.gProps.count:                     a = tmp_a                    tmp_b = LingoNumber(1)                    while tmp_b < self._movieScript.gProps[a].prps.count:                         b = tmp_b                        if LingoGlobal.op_eq_b(self._movieScript.gProps[a].prps[b].nm, self._movieScript.gPEprops.props[q][LingoNumber(2)]):                             correctreference = LingoGlobal.TRUE                            self._movieScript.gPEprops.props[q][LingoNumber(3)] = LingoGlobal.point(a,b)                            break                                                    tmp_b = b                        tmp_b += LingoNumber(1)                                            if LingoGlobal.op_eq_b(correctreference, LingoGlobal.TRUE):                         break                                            tmp_a = a                    tmp_a += LingoNumber(1)                                                if LingoGlobal.op_eq_b(self._movieScript.gPEprops.props[q].count, LingoNumber(4)):                 self._movieScript.gPEprops.props[q].add(LingoPropertyList(LingoSymbol("settings"), self._movieScript.gProps[self._movieScript.gPEprops.props[q][LingoNumber(3)].loch].prps[self._movieScript.gPEprops.props[q][LingoNumber(3)].locv].settings.duplicate()))            if LingoGlobal.op_eq_b(correctreference, LingoGlobal.FALSE):                 self._movieScript.writeexception("Prop Not Found",LingoGlobal.concat("the prop ",LingoGlobal.QUOTE,self._global.str(self._movieScript.gPEprops.props[q][LingoNumber(2)]),LingoGlobal.QUOTE," is missing in the Init.txt file from your Props folder."))                self._movieScript.gPEprops.props[q][LingoNumber(3)] = LingoGlobal.point(LingoNumber(1),LingoNumber(1))                            tmp_q = q            tmp_q += LingoNumber(1)                    for tmp_lz in self._movieScript.gLevel.lizards:             lz = tmp_lz            if LingoGlobal.op_eq_b(lz.count, LingoNumber(3)):                 lz.add(LingoNumber(1))                    if LingoGlobal.op_eq_b(self._movieScript.gLevel.findpos(LingoSymbol("waterdrips")), LingoGlobal.VOID):             self._movieScript.gLevel.addprop(LingoSymbol("waterdrips"),LingoNumber(1))        if LingoGlobal.op_eq_b(self._movieScript.gLevel.findpos(LingoSymbol("tags")), LingoGlobal.VOID):             self._movieScript.gLevel.addprop(LingoSymbol("tags"),LingoList())        if LingoGlobal.op_ne_b(self._movieScript.gLevel.findpos(LingoSymbol("lightdynamic")), LingoGlobal.VOID):             self._movieScript.gLevel.deleteprop(LingoSymbol("lightdynamic"))            self._movieScript.gLevel.addprop(LingoSymbol("lighttype"),"Static")        if LingoGlobal.op_ne_b(self._movieScript.gLevel.findpos(LingoSymbol("lightblend")), LingoGlobal.VOID):             self._movieScript.gLevel.deleteprop(LingoSymbol("lightblend"))        if LingoGlobal.op_eq_b(self._movieScript.gLOprops.findpos(LingoSymbol("tileseed")), LingoGlobal.VOID):             self._movieScript.gLOprops.addprop(LingoSymbol("tileseed"),self._global.random(LingoNumber(400)))        if LingoGlobal.op_eq_b(self._movieScript.gLOprops.findpos(LingoSymbol("colglows")), LingoGlobal.VOID):             self._movieScript.gLOprops.addprop(LingoSymbol("colglows"),LingoList(LingoNumber(0),LingoNumber(0)))        if LingoGlobal.op_eq_b(self._movieScript.gLEProps.findpos(LingoSymbol("campos")), LingoGlobal.VOID):             self._movieScript.gLEProps.addprop(LingoSymbol("campos"),LingoGlobal.point(LingoNumber(0),LingoNumber(0)))        if LingoGlobal.op_eq_b(self._movieScript.gCameraProps.findpos(LingoSymbol("quads")), LingoGlobal.VOID):             self._movieScript.gCameraProps.addprop(LingoSymbol("quads"),LingoList())            tmp_q = LingoNumber(1)            while tmp_q < self._movieScript.gCameraProps.cameras.count:                 q = tmp_q                self._movieScript.gCameraProps.quads.add(LingoList(LingoList(LingoNumber(0),LingoNumber(0)),LingoList(LingoNumber(0),LingoNumber(0)),LingoList(LingoNumber(0),LingoNumber(0)),LingoList(LingoNumber(0),LingoNumber(0))))                tmp_q = q                tmp_q += LingoNumber(1)                                    if LingoGlobal.op_eq_b(self._movieScript.gLevel.findpos(LingoSymbol("music")), LingoGlobal.VOID):             self._movieScript.gLevel.addprop(LingoSymbol("music"),"NONE")        for tmp_ef in self._movieScript.gEEprops.effects:             ef = tmp_ef            sd = LingoNumber(0)            for tmp_op in ef.options:                 op = tmp_op                if LingoGlobal.op_eq_b(op[LingoNumber(1)], "seed"):                     sd = LingoNumber(1)                    break                                                if LingoGlobal.op_eq_b(sd, LingoNumber(0)):                 ef.options.add(LingoList("Seed",LingoList(),self._global.random(LingoNumber(500))))            rotop = LingoNumber(0)            for tmp_op in ef.options:                 op = tmp_op                if LingoGlobal.op_eq_b(op[LingoNumber(1)], "Rotate"):                     rotop = LingoNumber(1)                    break                                                if (LingoGlobal.op_eq_b(rotop, LingoNumber(0)) and LingoGlobal.op_eq_b(ef.nm, "Little Flowers")):                 ef.options.add(LingoList("Rotate",LingoList("On","Off"),"Off"))            lay = LingoNumber(0)            for tmp_op2 in ef.options:                 op2 = tmp_op2                if LingoGlobal.op_eq_b(op2[LingoNumber(1)], "Layers"):                     lay = LingoNumber(1)                    if LingoGlobal.op_ne_b(op2[LingoNumber(2)], LingoList("All","1","2","3","1:st and 2:nd","2:nd and 3:rd")):                         op2[LingoNumber(2)] = LingoList("All","1","2","3","1:st and 2:nd","2:nd and 3:rd")                                            break                                                if (LingoGlobal.op_eq_b(lay, LingoNumber(0)) and LingoGlobal.op_eq_b(LingoList("BlackGoo","Super BlackGoo","Stained Glass Properties").getpos(ef.nm), LingoNumber(0))):                 if LingoList("Fungi Flowers","Lighthouse Flowers","Colored Fungi Flowers","Colored Lighthouse Flowers","Fern","Giant Mushroom","Sprawlbush","featherFern","Fungus Tree").getpos(ef.nm) > LingoNumber(0):                     ef.options.add(LingoList("Layers",LingoList("All","1","2","3","1:st and 2:nd","2:nd and 3:rd"),"1"))                else:                    ef.options.add(LingoList("Layers",LingoList("All","1","2","3","1:st and 2:nd","2:nd and 3:rd"),"All"))                            clr = LingoNumber(0)            for tmp_op3 in ef.options:                 op3 = tmp_op3                if LingoGlobal.op_eq_b(op3[LingoNumber(1)], "Color"):                     clr = LingoNumber(1)                    if LingoGlobal.op_ne_b(op3[LingoNumber(2)], LingoList("Color1","Color2","Dead")):                         op3[LingoNumber(2)] = LingoList("Color1","Color2","Dead")                                            break                                                if (LingoGlobal.op_eq_b(clr, LingoNumber(0)) and LingoList("DaddyCorruption").getpos(ef.nm) > LingoNumber(0)):                 ef.options.add(LingoList("Color",LingoList("Color1","Color2","Dead"),"Color2"))            gaf = LingoNumber(0)            for tmp_grd in ef.options:                 grd = tmp_grd                if LingoGlobal.op_eq_b(grd[LingoNumber(1)], "Affect Gradients and Decals"):                     gaf = LingoNumber(1)                    break                                                if (LingoGlobal.op_eq_b(gaf, LingoNumber(0)) and LingoList("Melt","Super Melt","Destructive Melt","Rust","Barnacles").getpos(ef.nm) > LingoNumber(0)):                 ef.options.add(LingoList("Affect Gradients and Decals",LingoList("Yes","No"),"No"))            if (LingoGlobal.op_eq_b(gaf, LingoNumber(0)) and LingoList("Slime","SlimeX3","Fat Slime").getpos(ef.nm) > LingoNumber(0)):                 ef.options.add(LingoList("Affect Gradients and Decals",LingoList("Yes","No"),"Yes"))            if LingoGlobal.op_eq_b(ef.findpos(LingoSymbol("crossscreen")), LingoGlobal.VOID):                 ef.addprop(LingoSymbol("crossscreen"),LingoNumber(0))                if LingoList("Hang Roots","Growers","Wires","Chains").getpos(ef.nm) > LingoNumber(0):                     ef.crossscreen = LingoNumber(1)                                                if LingoList("Arm Growers","Growers","Mini Growers","Rollers","Thorn Growers","Garbage Spirals","Spinets","Small Springs","Wires","Chains","Colored Wires","Colored Chains","Hang Roots","Thick Roots","Shadow Plants","Colored Hang Roots","Colored Thick Roots","Colored Shadow Plants","Root Plants").getpos(ef.nm) > LingoNumber(0):                 ef.crossscreen = LingoNumber(1)                            else:                ef.crossscreen = LingoNumber(0)                            if LingoList("Slime","Fat Slime","Scales","SlimeX3","DecalsOnlySlime","Melt","Rust","Barnacles","Colored Barnacles","Clovers","Erode","Sand","Super Erode","Ultra Super Erode","Roughen","Impacts","Super Melt","Destructive Melt").getpos(ef.nm) > LingoNumber(0):                 ef.tp = "standardErosion"                            else:                ef.tp = "nn"                            if LingoList("Slime","DecalsOnlySlime").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(130)                ef.affectopenareas = LingoNumber(0.5000)                            if LingoList("Fat Slime").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(200)                ef.affectopenareas = LingoNumber(0.5000)                            if LingoList("Scales").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(200)                ef.affectopenareas = LingoNumber(0.0500)                            if LingoList("SlimeX3").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoGlobal.op_mul(LingoNumber(130),LingoNumber(3))                ef.affectopenareas = LingoNumber(0.5000)                            if LingoList("Melt","Super Erode","Ultra Super Erode").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(60)                ef.affectopenareas = LingoNumber(0.5000)                            if LingoList("Rust").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(60)                ef.affectopenareas = LingoNumber(0.2000)                            if LingoList("Barnacles","Colored Barnacles").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(60)                ef.affectopenareas = LingoNumber(0.3000)                            if LingoList("Clovers").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(20)                ef.affectopenareas = LingoNumber(0.2000)                            if LingoList("Erode","Sand").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(80)                ef.affectopenareas = LingoNumber(0.5000)                            if LingoList("Roughen").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(30)                ef.affectopenareas = LingoNumber(0.0500)                            if LingoList("Impacts").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(75)                ef.affectopenareas = LingoNumber(0.0500)                            if LingoList("Super Melt","Destructive Melt").getpos(ef.nm) > LingoNumber(0):                 ef.repeats = LingoNumber(50)                ef.affectopenareas = LingoNumber(0.5000)                                            return None            