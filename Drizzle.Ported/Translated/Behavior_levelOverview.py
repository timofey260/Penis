from Drizzle.Runtime import *## Behavior script: levelOverview#class levelOverview(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         lc = None        if LingoGlobal.ToBool(_movieScript.showControls):             _global.sprite(LingoNumber(120)).blend = LingoNumber(100)            _global.sprite(LingoNumber(121)).blend = LingoNumber(100)            _global.sprite(LingoNumber(150)).blend = LingoNumber(100)            _global.sprite(LingoNumber(151)).blend = LingoNumber(100)                    else:            _global.sprite(LingoNumber(120)).blend = LingoNumber(0)            _global.sprite(LingoNumber(121)).blend = LingoNumber(0)            _global.sprite(LingoNumber(150)).blend = LingoNumber(0)            _global.sprite(LingoNumber(151)).blend = LingoNumber(0)                    _movieScript.gLOprops.lastmouse = _movieScript.gLOprops.mouse        _movieScript.gLOprops.mouse = _global._mouse.mousedown        if LingoGlobal.ToBool(LingoGlobal.op_mul(_movieScript.gLOprops.mouse,LingoGlobal.op_eq(_movieScript.gLOprops.lastmouse,LingoNumber(0)))):             _movieScript.gLOprops.mouseclick = LingoNumber(1)                    if LingoGlobal.op_eq_b(_movieScript.gLOprops.mouse, LingoNumber(0)):             _movieScript.gLOprops.mouseclick = LingoNumber(0)                    lc = LingoGlobal.op_add(_global._mouse.mouseloc,LingoGlobal.point(LingoNumber(30),LingoNumber(30)))        if lc.loch > LingoGlobal.op_sub(LingoNumber(1366),LingoNumber(300)):             lc.loch = LingoGlobal.op_sub(LingoNumber(1366),LingoNumber(300))                    self.gotoeditor()
        _global.go(_global.the_frame)        return None            def buttonclicked(self, bttn):         l1 = None        curr = None        q = None        l = None        a = None        sav = None        cols = None        rows = None        maprect = None        cpos = None        match bttn.lower():             case "button geometry editor":                _global._movie.go(LingoNumber(15))            case "button tile editor":                _global._movie.go(LingoNumber(25))            case "button effects editor":                _global._movie.go(LingoNumber(34))            case "button light editor":                _global._movie.go(LingoNumber(38))            case "button render level":                _movieScript.gViewRender = LingoNumber(1)                _global._movie.go(LingoNumber(43))            case "button test render":                _movieScript.newmakelevel(_movieScript.gLoadedName)
                _global._movie.go(LingoNumber(8))            case "button save project":                _movieScript.levelName = _movieScript.gLoadedName                _global.member("projectNameInput").text = _movieScript.gLoadedName                _global._movie.go(LingoNumber(11))            case "button load project":                _global._movie.go(LingoNumber(2))            case "button previous palette":                _movieScript.gLOprops.pal = LingoGlobal.op_sub(_movieScript.gLOprops.pal,LingoNumber(1))                if _movieScript.gLOprops.pal < LingoNumber(1):                     _movieScript.gLOprops.pal = _movieScript.gLOprops.pals.count                                    _global.sprite(LingoNumber(21)).member = _global.member(LingoGlobal.concat("libPal",_global.str(_movieScript.gLOprops.pal)))                _global.member("palName").text = _movieScript.gLOprops.pals[_movieScript.gLOprops.pal].name                _movieScript.gBlurOptions = LingoPropertyList(blurlight=_movieScript.gLOprops.pals[_movieScript.gLOprops.pal].blurlight,blursky=_movieScript.gLOprops.pals[_movieScript.gLOprops.pal].blursky)                            case "button next palette":                _movieScript.gLOprops.pal = LingoGlobal.op_add(_movieScript.gLOprops.pal,LingoNumber(1))                if _movieScript.gLOprops.pal > _movieScript.gLOprops.pals.count:                     _movieScript.gLOprops.pal = LingoNumber(1)                                    _global.sprite(LingoNumber(21)).member = _global.member(LingoGlobal.concat("libPal",_global.str(_movieScript.gLOprops.pal)))                _global.member("palName").text = _movieScript.gLOprops.pals[_movieScript.gLOprops.pal].name                _movieScript.gBlurOptions = LingoPropertyList(blurlight=_movieScript.gLOprops.pals[_movieScript.gLOprops.pal].blurlight,blursky=_movieScript.gLOprops.pals[_movieScript.gLOprops.pal].blursky)                            case "button previous ec1":                _movieScript.gLOprops.ecol1 = LingoGlobal.op_sub(_movieScript.gLOprops.ecol1,LingoNumber(1))                if _movieScript.gLOprops.ecol1 < LingoNumber(1):                     _movieScript.gLOprops.ecol1 = _movieScript.gLOprops.totecols                                    _global.sprite(LingoNumber(22)).member = _global.member(LingoGlobal.concat("ecol",_global.str(_movieScript.gLOprops.ecol1)))                            case "button next ec1":                _movieScript.gLOprops.ecol1 = LingoGlobal.op_add(_movieScript.gLOprops.ecol1,LingoNumber(1))                if _movieScript.gLOprops.ecol1 > _movieScript.gLOprops.totecols:                     _movieScript.gLOprops.ecol1 = LingoNumber(1)                                    _global.sprite(LingoNumber(22)).member = _global.member(LingoGlobal.concat("ecol",_global.str(_movieScript.gLOprops.ecol1)))                            case "button previous ec2":                _movieScript.gLOprops.ecol2 = LingoGlobal.op_sub(_movieScript.gLOprops.ecol2,LingoNumber(1))                if _movieScript.gLOprops.ecol2 < LingoNumber(1):                     _movieScript.gLOprops.ecol2 = _movieScript.gLOprops.totecols                                    _global.sprite(LingoNumber(23)).member = _global.member(LingoGlobal.concat("ecol",_global.str(_movieScript.gLOprops.ecol2)))                            case "button next ec2":                _movieScript.gLOprops.ecol2 = LingoGlobal.op_add(_movieScript.gLOprops.ecol2,LingoNumber(1))                if _movieScript.gLOprops.ecol2 > _movieScript.gLOprops.totecols:                     _movieScript.gLOprops.ecol2 = LingoNumber(1)                                    _global.sprite(LingoNumber(23)).member = _global.member(LingoGlobal.concat("ecol",_global.str(_movieScript.gLOprops.ecol2)))                            case "button more flies":                _movieScript.gEditLizard[LingoNumber(2)] = _movieScript.restrict(LingoGlobal.op_add(_movieScript.gEditLizard[LingoNumber(2)],LingoNumber(1)),LingoNumber(0),LingoNumber(40))                _global.member("addLizardFlies").text = _global.str(_movieScript.gEditLizard[LingoNumber(2)])                            case "button less flies":                _movieScript.gEditLizard[LingoNumber(2)] = _movieScript.restrict(LingoGlobal.op_sub(_movieScript.gEditLizard[LingoNumber(2)],LingoNumber(1)),LingoNumber(0),LingoNumber(40))                _global.member("addLizardFlies").text = _global.str(_movieScript.gEditLizard[LingoNumber(2)])                            case "button more time":                _movieScript.gEditLizard[LingoNumber(3)] = _movieScript.restrict(LingoGlobal.op_add(_movieScript.gEditLizard[LingoNumber(3)],LingoNumber(1)),LingoNumber(0),LingoNumber(4000))                _global.member("addLizardTime").text = _global.str(_movieScript.gEditLizard[LingoNumber(3)])                            case "button less time":                _movieScript.gEditLizard[LingoNumber(3)] = _movieScript.restrict(LingoGlobal.op_sub(_movieScript.gEditLizard[LingoNumber(3)],LingoNumber(1)),LingoNumber(0),LingoNumber(4000))                _global.member("addLizardTime").text = _global.str(_movieScript.gEditLizard[LingoNumber(3)])                            case "button super more time":                _movieScript.gEditLizard[LingoNumber(3)] = _movieScript.restrict(LingoGlobal.op_add(_movieScript.gEditLizard[LingoNumber(3)],LingoNumber(100)),LingoNumber(0),LingoNumber(4000))                _global.member("addLizardTime").text = _global.str(_movieScript.gEditLizard[LingoNumber(3)])                            case "button super less time":                _movieScript.gEditLizard[LingoNumber(3)] = _movieScript.restrict(LingoGlobal.op_sub(_movieScript.gEditLizard[LingoNumber(3)],LingoNumber(100)),LingoNumber(0),LingoNumber(4000))                _global.member("addLizardTime").text = _global.str(_movieScript.gEditLizard[LingoNumber(3)])                            case "button lizard hole":                self.nexthole()            case "button delete lizard":                if _movieScript.gLevel.lizards.count > LingoNumber(0):                     _movieScript.gLevel.lizards.deleteat(_movieScript.gLevel.lizards.count)
                    self.updatelizardslist()                            case "button add lizard":                if _movieScript.gEditLizard[LingoNumber(4)] > LingoNumber(0):                     if _movieScript.gLevel.lizards.count < LingoNumber(4):                         _movieScript.gLevel.lizards.add(_movieScript.gEditLizard.duplicate())
                        self.updatelizardslist()                                    if LingoGlobal.op_ne_b(_movieScript.gEditLizard[LingoNumber(1)], "yellow"):                     self.nexthole()                            case "button lizard color":                l1 = LingoList("pink","green","blue","white","red","yellow")                curr = LingoNumber(1)                for tmp_q in LingoGlobal.pyrange(LingoNumber(1), l1.count):                     q = tmp_q                    if LingoGlobal.op_eq_b(_movieScript.gEditLizard[LingoNumber(1)], l1[q]):                         curr = q                        break                                            tmp_q = q                                    curr = LingoGlobal.op_add(curr,LingoNumber(1))                if curr > l1.count:                     curr = LingoNumber(1)                                    _movieScript.gEditLizard[LingoNumber(1)] = l1[curr]                _global.sprite(LingoNumber(43)).color = LingoList(_global.color(LingoNumber(255),LingoNumber(0),LingoNumber(255)),_global.color(LingoNumber(0),LingoNumber(255),LingoNumber(0)),_global.color(LingoNumber(0),LingoNumber(100),LingoNumber(255)),_global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255)),_global.color(LingoNumber(255),LingoNumber(0),LingoNumber(0)),_global.color(LingoNumber(255),LingoNumber(200),LingoNumber(0)))[curr]                            case "button standard medium":                _movieScript.gLevel.defaultterrain = LingoGlobal.op_sub(LingoNumber(1),_movieScript.gLevel.defaultterrain)                _global.sprite(LingoNumber(112)).loc = LingoGlobal.op_add(LingoGlobal.point(LingoNumber(312),LingoNumber(312)),LingoGlobal.point(LingoGlobal.op_add(-LingoNumber(1000),LingoGlobal.op_mul(LingoNumber(1000),_movieScript.gLevel.defaultterrain)),LingoNumber(0)))                            case "button light type":                _movieScript.gLOprops.light = LingoGlobal.op_sub(LingoNumber(1),_movieScript.gLOprops.light)                            case "button next color glow 1":                _movieScript.gLOprops.colglows[LingoNumber(1)] = LingoGlobal.op_add(_movieScript.gLOprops.colglows[LingoNumber(1)],LingoNumber(1))                if _movieScript.gLOprops.colglows[LingoNumber(1)] > LingoNumber(2):                     _movieScript.gLOprops.colglows[LingoNumber(1)] = LingoNumber(0)                                    l = LingoList("Dull","Reflective","Superflourescent")                _global.member("color glow effects").text = LingoGlobal.concat_space(l[LingoGlobal.op_add(_movieScript.gLOprops.colglows[LingoNumber(1)],LingoNumber(1))],LingoGlobal.RETURN,l[LingoGlobal.op_add(_movieScript.gLOprops.colglows[LingoNumber(2)],LingoNumber(1))])                            case "button next color glow 2":                _movieScript.gLOprops.colglows[LingoNumber(2)] = LingoGlobal.op_add(_movieScript.gLOprops.colglows[LingoNumber(2)],LingoNumber(1))                if _movieScript.gLOprops.colglows[LingoNumber(2)] > LingoNumber(2):                     _movieScript.gLOprops.colglows[LingoNumber(2)] = LingoNumber(0)                                    l = LingoList("Dull","Reflective","Superflourescent")                _global.member("color glow effects").text = LingoGlobal.concat_space(l[LingoGlobal.op_add(_movieScript.gLOprops.colglows[LingoNumber(1)],LingoNumber(1))],LingoGlobal.RETURN,l[LingoGlobal.op_add(_movieScript.gLOprops.colglows[LingoNumber(2)],LingoNumber(1))])                            case "button sound editor":                _global._movie.go(LingoNumber(18))            case "button mass render":                _movieScript.massRenderSelectL = LingoList()                _global._movie.go(LingoNumber(4))            case "button prop editor":                _global._movie.go(LingoNumber(23))            case "button level size":                _global._movie.go(LingoNumber(19))
                _global.member("widthInput").text = _movieScript.gLOprops.size.loch                _global.member("heightInput").text = _movieScript.gLOprops.size.locv                _movieScript.newSize = LingoList(_movieScript.gLOprops.size.loch,_movieScript.gLOprops.size.locv,LingoNumber(0),LingoNumber(0))                _movieScript.extraBufferTiles = _movieScript.gLOprops.extratiles.duplicate()                _global.member("extraTilesLeft").text = _movieScript.extraBufferTiles[LingoNumber(1)]                _global.member("extraTilesTop").text = _movieScript.extraBufferTiles[LingoNumber(2)]                _global.member("extraTilesRight").text = _movieScript.extraBufferTiles[LingoNumber(3)]                _global.member("extraTilesBottom").text = _movieScript.extraBufferTiles[LingoNumber(4)]                _global.member("addTilesTop").text = "0"                _global.member("addTilesLeft").text = "0"                            case "button cameras":                _global._movie.go(LingoNumber(32))            case "button environment editor":                _global._movie.go(LingoNumber(30))            case "button exit lock":                if (LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized) and LingoGlobal.op_eq_b(_global._movie.exitlock, LingoGlobal.TRUE)):                     _global._movie.exitlock = LingoGlobal.FALSE                                    else:                    _global._movie.exitlock = LingoGlobal.TRUE                                                case "button grid snap":                if (LingoGlobal.op_eq_b(_movieScript.snapToGrid, LingoNumber(0)) and LingoGlobal.op_eq_b(_movieScript.preciseSnap, LingoNumber(0))):                     _movieScript.snapToGrid = LingoNumber(1)                    _movieScript.preciseSnap = LingoNumber(0)                    _movieScript.stg = LingoNumber(1)                    _movieScript.ps = LingoNumber(0)                                    elif (LingoGlobal.op_eq_b(_movieScript.snapToGrid, LingoNumber(1)) and LingoGlobal.op_eq_b(_movieScript.preciseSnap, LingoNumber(0))):                     _movieScript.snapToGrid = LingoNumber(0)                    _movieScript.preciseSnap = LingoNumber(1)                    _movieScript.stg = LingoNumber(0)                    _movieScript.ps = LingoNumber(1)                                    elif (LingoGlobal.op_eq_b(_movieScript.preciseSnap, LingoNumber(1)) and LingoGlobal.op_eq_b(_movieScript.snapToGrid, LingoNumber(0))):                     _movieScript.snapToGrid = LingoNumber(0)                    _movieScript.preciseSnap = LingoNumber(0)                    _movieScript.stg = LingoNumber(0)                    _movieScript.ps = LingoNumber(0)                                    elif (LingoGlobal.op_eq_b(_movieScript.preciseSnap, LingoNumber(1)) and LingoGlobal.op_eq_b(_movieScript.snapToGrid, LingoNumber(1))):                     _movieScript.snapToGrid = LingoNumber(0)                    _movieScript.preciseSnap = LingoNumber(0)                    _movieScript.stg = LingoNumber(0)                    _movieScript.ps = LingoNumber(0)                                                case "button update preview":                for tmp_a in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(3)):                     a = tmp_a                    _movieScript.minilvleditdraw(a)
                    tmp_a = a                                    sav = _movieScript.gLEProps.campos                _movieScript.gLEProps.campos = LingoGlobal.point(LingoNumber(0),LingoNumber(0))                cols = _movieScript.gLOprops.size.loch                rows = _movieScript.gLOprops.size.locv                _global.member("levelEditImageShortCuts").image = _global.image(LingoGlobal.op_mul(cols,LingoNumber(5)),LingoGlobal.op_mul(rows,LingoNumber(5)),LingoNumber(1))                _movieScript.drawshortcutsimg(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),cols,rows),LingoNumber(5),LingoNumber(1))
                _movieScript.gLEProps.campos = sav                            case "button prio cam":                _movieScript.gPrioCam = LingoGlobal.op_add(_movieScript.gPrioCam,LingoNumber(1))                if _movieScript.gPrioCam > _movieScript.gCameraProps.cameras.count:                     _movieScript.gPrioCam = LingoNumber(0)                                    if LingoGlobal.op_eq_b(_movieScript.gPrioCam, LingoNumber(0)):                     _global.member("PrioCamText").text = "NONE"                    _global.sprite(LingoNumber(123)).rect = LingoGlobal.rect(-LingoNumber(100),-LingoNumber(100),-LingoNumber(100),-LingoNumber(100))                                    else:                    _global.member("PrioCamText").text = LingoGlobal.concat("Will render camera ",_movieScript.gPrioCam," first")                    maprect = _global.sprite(LingoNumber(115)).rect                    cpos = LingoGlobal.op_add(_movieScript.gCameraProps.cameras[_movieScript.gPrioCam],LingoGlobal.point(LingoNumber(0.0010),LingoNumber(0.0010)))                    _global.sprite(LingoNumber(123)).rect = LingoGlobal.rect(_movieScript.lerp(maprect.left,maprect.right,LingoGlobal.op_div(cpos.loch,LingoGlobal.op_mul(_movieScript.gLOprops.size.loch,LingoNumber(20)))),_movieScript.lerp(maprect.top,maprect.bottom,LingoGlobal.op_div(cpos.locv,LingoGlobal.op_mul(_movieScript.gLOprops.size.locv,LingoNumber(20)))),_movieScript.lerp(maprect.left,maprect.right,LingoGlobal.op_div(LingoGlobal.op_add(cpos.loch,LingoNumber(1366)),LingoGlobal.op_mul(_movieScript.gLOprops.size.loch,LingoNumber(20)))),_movieScript.lerp(maprect.top,maprect.bottom,LingoGlobal.op_div(LingoGlobal.op_add(cpos.locv,LingoNumber(768)),LingoGlobal.op_mul(_movieScript.gLOprops.size.locv,LingoNumber(20)))))                                                case "button lvlpropoutput":                if LingoGlobal.op_eq_b(_movieScript.lvlPropOutput, LingoGlobal.FALSE):                     _movieScript.lvlPropOutput = LingoGlobal.TRUE                                    else:                    _movieScript.lvlPropOutput = LingoGlobal.FALSE                                                                return None            def gotoeditor(self):         gofrm = None        q = None        gofrm = LingoNumber(0)        if (LingoGlobal.ToBool(_global._key.keypressed("1")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(9)                    elif (LingoGlobal.ToBool(_global._key.keypressed("2")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(15)                    elif (LingoGlobal.ToBool(_global._key.keypressed("3")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(25)                    elif (LingoGlobal.ToBool(_global._key.keypressed("4")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(32)                    elif (LingoGlobal.ToBool(_global._key.keypressed("5")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(38)                    elif (LingoGlobal.ToBool(_global._key.keypressed("6")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(19)            _global.member("widthInput").text = _movieScript.gLOprops.size.loch            _global.member("heightInput").text = _movieScript.gLOprops.size.locv            _movieScript.newSize = LingoList(_movieScript.gLOprops.size.loch,_movieScript.gLOprops.size.locv,LingoNumber(0),LingoNumber(0))            _movieScript.extraBufferTiles = _movieScript.gLOprops.extratiles.duplicate()            _global.member("extraTilesLeft").text = _movieScript.extraBufferTiles[LingoNumber(1)]            _global.member("extraTilesTop").text = _movieScript.extraBufferTiles[LingoNumber(2)]            _global.member("extraTilesRight").text = _movieScript.extraBufferTiles[LingoNumber(3)]            _global.member("extraTilesBottom").text = _movieScript.extraBufferTiles[LingoNumber(4)]            _global.member("addTilesTop").text = "0"            _global.member("addTilesLeft").text = "0"                    elif (LingoGlobal.ToBool(_global._key.keypressed("7")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(34)                    elif (LingoGlobal.ToBool(_global._key.keypressed("8")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(23)                    elif (LingoGlobal.ToBool(_global._key.keypressed("9")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             gofrm = LingoNumber(30)                    elif ((LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             _global._player.appminimize()        elif LingoGlobal.ToBool(_movieScript.checkexit()):             _global._player.quit()        elif (LingoGlobal.ToBool(_global._key.keypressed("0")) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             _movieScript.levelName = _movieScript.gLoadedName            _global.member("projectNameInput").text = _movieScript.gLoadedName            gofrm = LingoNumber(13)                    if LingoGlobal.op_ne_b(gofrm, LingoNumber(0)):             for tmp_q in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(5)):                 q = tmp_q                _global.sound(q).stop()
                tmp_q = q                            if LingoGlobal.op_ne_b(_movieScript.gSEprops.sounds, LingoGlobal.VOID):                 _movieScript.gLevel.ambientsounds = LingoList()                for tmp_q in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(4)):                     q = tmp_q                    if (LingoGlobal.op_ne_b(_movieScript.gSEprops.sounds[q].mem, "none") and _movieScript.gSEprops.sounds[q].vol > LingoNumber(0)):                         _movieScript.gLevel.ambientsounds.add(_movieScript.gSEprops.sounds[q].duplicate())
                        _movieScript.gSEprops.sounds[q].mem = "None"                                            tmp_q = q                                    _movieScript.gSEprops.sounds = LingoGlobal.VOID                            for tmp_q in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(22)):                 q = tmp_q                _global.sprite(q).visibility = LingoNumber(1)                tmp_q = q                            for tmp_q in LingoGlobal.pyrange(LingoNumber(800), LingoNumber(820)):                 q = tmp_q                _global.sprite(q).visibility = LingoGlobal.op_eq(gofrm,LingoNumber(15))                tmp_q = q                            _global._movie.go(gofrm)                return None            def updatelizardslist(self):         l1 = None        l2 = None        lz = None        q = None        c = None        pnt1 = None        pnt2 = None        l1 = LingoList("pink","green","blue","white","red","yellow")        l2 = LingoList(_global.color(LingoNumber(255),LingoNumber(0),LingoNumber(255)),_global.color(LingoNumber(0),LingoNumber(255),LingoNumber(0)),_global.color(LingoNumber(0),LingoNumber(100),LingoNumber(255)),_global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255)),_global.color(LingoNumber(255),LingoNumber(0),LingoNumber(0)),_global.color(LingoNumber(255),LingoNumber(200),LingoNumber(0)))        lz = LingoList()        for tmp_q in LingoGlobal.pyrange(LingoNumber(1), _movieScript.gLOprops.size.loch):             q = tmp_q            for tmp_c in LingoGlobal.pyrange(LingoNumber(1), _movieScript.gLOprops.size.locv):                 c = tmp_c                if _movieScript.gLEProps.matrix[q][c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(7)) > LingoNumber(0):                     lz.add(LingoGlobal.point(q,c))                tmp_c = c                            tmp_q = q                    if LingoGlobal.op_ne_b(lz, LingoList()):             for tmp_q in LingoGlobal.pyrange(LingoNumber(1), _movieScript.gLevel.lizards.count):                 q = tmp_q                _global.member(LingoGlobal.concat("lizard",q,"text")).text = LingoGlobal.concat_space(_movieScript.gLevel.lizards[q][LingoNumber(1)],"- Flies:",_movieScript.gLevel.lizards[q][LingoNumber(2)],"- Time:",_movieScript.gLevel.lizards[q][LingoNumber(3)])                _global.sprite(LingoGlobal.op_add(LingoNumber(51),q)).color = l2[l1.getpos(_movieScript.gLevel.lizards[q][LingoNumber(1)])]                _global.sprite(LingoGlobal.op_add(LingoNumber(55),q)).color = l2[l1.getpos(_movieScript.gLevel.lizards[q][LingoNumber(1)])]                if _movieScript.gLevel.lizards[q][LingoNumber(4)] > lz.count:                     _movieScript.gLevel.lizards[q][LingoNumber(4)] = lz.count                                    pnt1 = LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_mul(lz[_movieScript.gLevel.lizards[q][LingoNumber(4)]],LingoNumber(10)),LingoGlobal.point(LingoNumber(52),LingoNumber(112))),LingoGlobal.point(-LingoNumber(5),-LingoNumber(5)))                pnt2 = LingoGlobal.point(_global.sprite(LingoGlobal.op_add(LingoNumber(51),q)).rect.left,LingoGlobal.op_add(_global.sprite(LingoGlobal.op_add(LingoNumber(51),q)).rect.top,LingoGlobal.op_mul(_global.sprite(LingoGlobal.op_add(LingoNumber(51),q)).rect.height,LingoNumber(0.5000))))                _global.sprite(LingoGlobal.op_add(LingoNumber(55),q)).rect = LingoGlobal.rect(pnt1,pnt2)                _global.sprite(LingoGlobal.op_add(LingoNumber(55),q)).member = _global.member(LingoGlobal.concat("line",LingoGlobal.op_add(LingoNumber(1),LingoGlobal.op_gt(pnt1.locv,pnt2.locv))))                tmp_q = q                            for tmp_q in LingoGlobal.pyrange(LingoGlobal.op_add(_movieScript.gLevel.lizards.count,LingoNumber(1)), LingoNumber(4)):                 q = tmp_q                _global.member(LingoGlobal.concat("lizard",q,"text")).text = ""                _global.sprite(LingoGlobal.op_add(LingoNumber(55),q)).rect = LingoGlobal.rect(-LingoNumber(100),-LingoNumber(100),-LingoNumber(100),-LingoNumber(100))                tmp_q = q                                    else:            for tmp_q in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(4)):                 q = tmp_q                _global.member(LingoGlobal.concat("lizard",q,"text")).text = ""                _global.sprite(LingoGlobal.op_add(LingoNumber(55),q)).rect = LingoGlobal.rect(-LingoNumber(100),-LingoNumber(100),-LingoNumber(100),-LingoNumber(100))                tmp_q = q                                            return None            def nexthole(self):         lz = None        q = None        c = None        pnt = None        lz = LingoList()        for tmp_q in LingoGlobal.pyrange(LingoNumber(1), _movieScript.gLOprops.size.loch):             q = tmp_q            for tmp_c in LingoGlobal.pyrange(LingoNumber(1), _movieScript.gLOprops.size.locv):                 c = tmp_c                if _movieScript.gLEProps.matrix[q][c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(7)) > LingoNumber(0):                     lz.add(LingoGlobal.point(q,c))                tmp_c = c                            tmp_q = q                    if LingoGlobal.op_ne_b(lz, LingoList()):             _movieScript.gEditLizard[LingoNumber(4)] = LingoGlobal.op_add(_movieScript.gEditLizard[LingoNumber(4)],LingoNumber(1))            if _movieScript.gEditLizard[LingoNumber(4)] > lz.count:                 _movieScript.gEditLizard[LingoNumber(4)] = LingoNumber(1)                            pnt = LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_mul(lz[_movieScript.gEditLizard[LingoNumber(4)]],LingoNumber(10)),LingoGlobal.point(LingoNumber(52),LingoNumber(112))),LingoGlobal.point(-LingoNumber(5),-LingoNumber(5)))            _global.sprite(LingoNumber(60)).rect = LingoGlobal.op_add(LingoGlobal.rect(pnt,pnt),LingoGlobal.rect(-LingoNumber(5),-LingoNumber(5),LingoNumber(5),LingoNumber(5)))                    else:            _global.sprite(LingoNumber(60)).rect = LingoGlobal.rect(-LingoNumber(5),-LingoNumber(5),-LingoNumber(5),-LingoNumber(5))                            return None            