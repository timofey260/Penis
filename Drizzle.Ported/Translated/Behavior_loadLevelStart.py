from Drizzle.Runtime import *## Behavior script: loadLevelStart#class loadLevelStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         self._global._movie.exitlock = LingoGlobal.TRUE        self._movieScript.INT_EXIT = self._movieScript.getstrconfig("Exit button")        self._movieScript.INT_EXRD = self._movieScript.getstrconfig("Exit render button")        self._movieScript.showControls = self._movieScript.getboolconfig("Show controls")        if ((LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(self._global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(self._global._movie.window.sizestate, LingoSymbol("minimized"))):             self._global._player.appminimize()        if LingoGlobal.ToBool(self._movieScript.checkexit()):             self._global._player.quit()        self._movieScript.projects = LingoList()        pth = LingoGlobal.concat(self._global.the_moviePath,"LevelEditorProjects",self._global.the_dirSeparator)        for tmp_f in self._movieScript.gLOADPATH:             f = tmp_f            pth = LingoGlobal.concat(pth,self._global.the_dirSeparator,f)                    filelist = LingoList()        tmp_i = LingoNumber(1)        while tmp_i.IntValue < LingoNumber(300):             i = tmp_i            n = self._global.getnthfilenameinfolder(pth,i)            if LingoGlobal.op_eq_b(n, LingoGlobal.EMPTY):                 break                            if LingoGlobal.op_ne_b(LingoGlobal.charof_helper(LingoGlobal.op_sub(LingoGlobal.lengthmember_helper(n),LingoNumber(3)),n), "."):                 self._movieScript.projects.add(LingoGlobal.concat("#",n))            else:                filelist.append(n)            tmp_i = i            tmp_i += LingoNumber(1)                    for tmp_l in filelist:             l = tmp_l            if LingoGlobal.op_eq_b(LingoGlobal.chars(l,LingoGlobal.op_sub(LingoGlobal.lengthmember_helper(l),LingoNumber(3)),LingoGlobal.lengthmember_helper(l)), ".txt"):                 self._movieScript.projects.add(LingoGlobal.chars(l,LingoNumber(1),LingoGlobal.op_sub(LingoGlobal.lengthmember_helper(l),LingoNumber(4))))                    txt = "Use the arrow keys to select a project. Use enter to open it."        txt += str(LingoGlobal.RETURN)        for tmp_f in self._movieScript.gLOADPATH:             f = tmp_f            txt += str(LingoGlobal.concat(f,"/"))                    txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        for tmp_q in self._movieScript.projects:             q = tmp_q            txt += str(q)            txt += str(LingoGlobal.RETURN)                    self._movieScript.ldPrps = LingoPropertyList(LingoSymbol("lstup"), LingoNumber(1),LingoSymbol("lstDwn"), LingoNumber(1),LingoSymbol("lft"), LingoNumber(1),LingoSymbol("rgth"), LingoNumber(1),LingoSymbol("currproject"), LingoNumber(1),LingoSymbol("listscrollpos"), LingoNumber(1),LingoSymbol("listshowtotal"), LingoNumber(30))        self._global.member("ProjectsL").text = txt        self._global.member("PalName").text = "Press 'N' to create a new level. Use left and right arrows to step in and out of subfolders"                return None            