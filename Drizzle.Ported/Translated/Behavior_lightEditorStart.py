from Drizzle.Runtime import *## Behavior script: lightEditorStart#class lightEditorStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         l = None        _global._movie.exitlock = LingoGlobal.TRUE        _movieScript.firstFrame = LingoNumber(1)        l = LingoPropertyList(dict(m1 = LingoNumber(1),m2 = LingoNumber(0),w = LingoNumber(0),a = LingoNumber(0),s = LingoNumber(0),d = LingoNumber(0),r = LingoNumber(0),f = LingoNumber(0)))        _movieScript.gLightEProps.lastkeys = l.duplicate()        _movieScript.gLightEProps.keys = l.duplicate()        for tmp_l in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(3)):             l = tmp_l            _movieScript.minilvleditdraw(l)
            tmp_l = l                    _movieScript.geverysecond = LingoNumber(0)        _movieScript.gDirectionKeys = LingoList(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0))        _movieScript.glgtimgQuad = LingoList(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),LingoGlobal.point(_global.member("lightImage").image.width,LingoNumber(0)),LingoGlobal.point(_global.member("lightImage").image.width,_global.member("lightImage").image.height),LingoGlobal.point(LingoNumber(0),_global.member("lightImage").image.height))        _movieScript.gLightEProps.lasttm = _global._system.milliseconds        _global.sprite(LingoNumber(181)).member = _global.member("pxl")        _global.sprite(LingoNumber(182)).member = _global.member("pxl")        _movieScript.gLightEProps.paintshape = "pxl"        _global.sprite(LingoNumber(175)).rect = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(_movieScript.gLOprops.size.loch,LingoNumber(20)),LingoGlobal.op_mul(_movieScript.gLOprops.size.locv,LingoNumber(20)))        _global.sprite(LingoNumber(178)).rect = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoGlobal.op_mul(_movieScript.gLOprops.size.loch,LingoNumber(20)),LingoGlobal.op_mul(_movieScript.gLOprops.size.locv,LingoNumber(20)))        _global.sprite(LingoNumber(179)).member = _global.member("lightImage")        _global.sprite(LingoNumber(180)).member = _global.member("lightImage")        _global.sprite(LingoNumber(176)).member = _global.member("lightImage")                return None            