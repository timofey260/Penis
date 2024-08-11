from Drizzle.Runtime import *## Behavior script: testDrawLevel#class testDrawLevel(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         _movieScript.gFullRender = LingoNumber(0)        _movieScript.lightRects = LingoList(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0)))        _movieScript.drawtestlevel()
        _global.member("finalfg").image.setpixel(LingoNumber(0),LingoNumber(0),_movieScript.gSkyColor)
        _global.member("finalfg").image.setpixel(LingoNumber(1),LingoNumber(0),_movieScript.gSkyColor)
        _global.member("finalfg").image.setpixel(LingoNumber(2),LingoNumber(0),_global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        _global.member("finalfg").image.setpixel(LingoNumber(3),LingoNumber(0),_global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        _global.member("finalfg").image.setpixel(LingoNumber(0),LingoNumber(1),_global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        _global.member("finalfg").image.setpixel(LingoNumber(1),LingoNumber(1),_global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        _movieScript.levelName = _movieScript.gLoadedName        _global.member("TextInput").text = _movieScript.gLoadedName        _global.put("I'M DOING A TEST RENDER!")
        _global.alert("I'M DOING A TEST RENDER!")
        _global.go(LingoNumber(76))        return None            