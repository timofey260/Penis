from Drizzle.Runtime import *## Behavior script: loadLevelStart#class loadLevelStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         pth = None        f = None        filelist = None        i = None        n = None        l = None        txt = None        q = None        _global._movie.exitlock = LingoGlobal.TRUE        _movieScript.INT_EXIT = _movieScript.getstrconfig("Exit button")        _movieScript.INT_EXRD = _movieScript.getstrconfig("Exit render button")        _movieScript.showControls = _movieScript.getboolconfig("Show controls")        if ((LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             _global._player.appminimize()        if LingoGlobal.ToBool(_movieScript.checkexit()):             _global._player.quit()        _movieScript.projects = LingoList()        pth = LingoGlobal.concat(_global.the_moviePath,"LevelEditorProjects",_global.the_dirSeparator)        for tmp_f in _movieScript.gLOADPATH:             f = tmp_f            pth = LingoGlobal.concat(pth,_global.the_dirSeparator,f)                    filelist = LingoList()        for tmp_i in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(300)):             i = tmp_i            n = _global.getnthfilenameinfolder(pth,i)            if LingoGlobal.op_eq_b(n, LingoGlobal.EMPTY):                 break                            if LingoGlobal.op_ne_b(LingoGlobal.charof_helper(LingoGlobal.op_sub(LingoGlobal.lengthmember_helper(n),LingoNumber(3)),n), "."):                 _movieScript.projects.add(LingoGlobal.concat("#",n))            else:                filelist.append(n)            tmp_i = i                    for tmp_l in filelist:             l = tmp_l            if LingoGlobal.op_eq_b(LingoGlobal.chars(l,LingoGlobal.op_sub(LingoGlobal.lengthmember_helper(l),LingoNumber(3)),LingoGlobal.lengthmember_helper(l)), ".txt"):                 _movieScript.projects.add(LingoGlobal.chars(l,LingoNumber(1),LingoGlobal.op_sub(LingoGlobal.lengthmember_helper(l),LingoNumber(4))))                    txt = "Use the arrow keys to select a project. Use enter to open it."        txt += str(LingoGlobal.RETURN)        for tmp_f in _movieScript.gLOADPATH:             f = tmp_f            txt += str(LingoGlobal.concat(f,"/"))                    txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        for tmp_q in _movieScript.projects:             q = tmp_q            txt += str(q)            txt += str(LingoGlobal.RETURN)                    _movieScript.ldPrps = LingoPropertyList(dict(lstup = LingoNumber(1),lstDwn = LingoNumber(1),lft = LingoNumber(1),rgth = LingoNumber(1),currproject = LingoNumber(1),listscrollpos = LingoNumber(1),listshowtotal = LingoNumber(30)))        _global.member("ProjectsL").text = txt        _global.member("PalName").text = "Press 'N' to create a new level. Use left and right arrows to step in and out of subfolders"                return None            