from Drizzle.Runtime import *## Behavior script: saveProject#class saveProject(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         str = None        objfileio = None        pth = None        f = None        gimgxtra = None        nwimg = None        props = None        ok = None        _global._movie.exitlock = LingoGlobal.TRUE        if ((LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             _global._player.appminimize()        if LingoGlobal.ToBool(_movieScript.checkexit()):             _global._player.quit()        if ((LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(36))) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)) and LingoGlobal.op_ne_b(_movieScript.levelName, LingoGlobal.VOID)):             str = ""            str += str(_movieScript.gLEProps.matrix)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gTEprops)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gEEprops)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gLightEProps)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gLevel)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gLOprops)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gCameraProps)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gEnvEditorProps)            str += str(LingoGlobal.RETURN)            str += str(_movieScript.gPEprops)            str += str(LingoGlobal.RETURN)            objfileio = _global.new(_global.xtra("fileio"))            pth = LingoGlobal.concat(_global.the_moviePath,"LevelEditorProjects",_global.the_dirSeparator)            for tmp_f in _movieScript.gLOADPATH:                 f = tmp_f                pth = LingoGlobal.concat(pth,f,_global.the_dirSeparator)                            _global.createfile(objfileio,LingoGlobal.concat(pth,_movieScript.levelName,".txt"))
            objfileio.openfile(LingoGlobal.concat(pth,_movieScript.levelName,".txt"),LingoNumber(0))
            objfileio.writestr(str)
            objfileio.closefile()
            _global.member("lightImage").image.setpixel(LingoNumber(0),LingoNumber(0),_global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))
            _global.member("lightImage").image.setpixel(LingoGlobal.op_sub(_global.member("lightImage").rect.width,LingoNumber(1)),LingoGlobal.op_sub(_global.member("lightImage").rect.height,LingoNumber(1)),_global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))
            gimgxtra = _global.xtra("ImgXtra").new()            nwimg = _global.image(_global.member("lightImage").image.rect.width,_global.member("lightImage").image.rect.height,LingoNumber(32))            nwimg.copypixels(_global.member("lightImage").image,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),_global.member("lightImage").image.rect.width,_global.member("lightImage").image.rect.height),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),_global.member("lightImage").image.rect.width,_global.member("lightImage").image.rect.height))
            props = LingoPropertyList(image=nwimg,filename=LingoGlobal.concat(pth,_movieScript.levelName,".png"))            ok = gimgxtra.ix_saveimage(props)            _movieScript.gLoadedName = _movieScript.levelName            _global.member("Level Name").text = _movieScript.gLoadedName            _global._movie.go(LingoNumber(7))        elif ((LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(51))) and LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(56)))) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             _global._movie.go(LingoNumber(7))        else:            _global.go(_global.the_frame)                return None            