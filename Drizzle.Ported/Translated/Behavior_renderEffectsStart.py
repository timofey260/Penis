from Drizzle.Runtime import *## Behavior script: renderEffectsStart#class renderEffectsStart(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         tm = None        q = None        val = None        if ((LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(56))) and LingoGlobal.ToBool(_global._key.keypressed(LingoNumber(48)))) and LingoGlobal.op_ne_b(_global._movie.window.sizestate, minimized)):             _global._player.appminimize()        if LingoGlobal.ToBool(_movieScript.checkexit()):             _global._player.quit()        if LingoGlobal.ToBool(_movieScript.checkexitrender()):             _global._movie.go(LingoNumber(9))        tm = _global._system.milliseconds        for tmp_q in LingoGlobal.pyrange(LingoNumber(0), LingoNumber(29)):             q = tmp_q            _global.sprite(LingoGlobal.op_sub(LingoNumber(50),q)).loc = LingoGlobal.point(LingoGlobal.op_sub(LingoGlobal.op_div(LingoNumber(1366),LingoNumber(2)),q),LingoGlobal.op_sub(LingoGlobal.op_div(LingoNumber(768),LingoNumber(2)),q))            val = LingoGlobal.op_div(LingoGlobal.op_add(q.float,LingoNumber(1.0000)),LingoNumber(30.0000))            _global.sprite(LingoGlobal.op_sub(LingoNumber(50),q)).color = _global.color(LingoGlobal.op_mul(val,LingoNumber(255)),LingoGlobal.op_mul(val,LingoNumber(255)),LingoGlobal.op_mul(val,LingoNumber(255)))            tmp_q = q                    _global.sprite(LingoNumber(57)).visibility = LingoNumber(0)        _global.sprite(LingoNumber(58)).visibility = LingoNumber(0)        _movieScript.vertRepeater = LingoNumber(100000)        if _movieScript.gEEprops.effects.count > LingoNumber(0):             _movieScript.r = LingoNumber(0)            _movieScript.keepLooping = LingoNumber(1)                    else:            _global.go(LingoNumber(56))                return None            