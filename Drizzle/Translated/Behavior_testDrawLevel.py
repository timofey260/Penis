from Drizzle.Runtime import *## Behavior script: testDrawLevel#class testDrawLevel(LingoBehaviorScript):     def __init__(self):         super().__init__()            def exitframe(self):         self._movieScript.gFullRender = LingoNumber(0)        self._movieScript.lightRects = LingoList(LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0)),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(0),LingoNumber(0)))        self._movieScript.drawtestlevel()
        self._global.member("finalfg").image.setpixel(LingoNumber(0),LingoNumber(0),self._movieScript.gSkyColor)
        self._global.member("finalfg").image.setpixel(LingoNumber(1),LingoNumber(0),self._movieScript.gSkyColor)
        self._global.member("finalfg").image.setpixel(LingoNumber(2),LingoNumber(0),self._global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        self._global.member("finalfg").image.setpixel(LingoNumber(3),LingoNumber(0),self._global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        self._global.member("finalfg").image.setpixel(LingoNumber(0),LingoNumber(1),self._global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        self._global.member("finalfg").image.setpixel(LingoNumber(1),LingoNumber(1),self._global.color(LingoNumber(10),LingoNumber(10),LingoNumber(10)))
        self._movieScript.levelName = self._movieScript.gLoadedName        self._global.member("TextInput").text = self._movieScript.gLoadedName        self._global.put("I'M DOING A TEST RENDER!")
        self._global.alert("I'M DOING A TEST RENDER!")
        self._global.go(LingoNumber(76))        return None            