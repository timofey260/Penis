from Drizzle.Data.LingoRect import LingoRect, LingoPoint, LingoNumber
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoColor import LingoColor


class LingoSprite:
    def __init__(self):
        self.rect = LingoRect(LingoNumber(0))
        self.loc = LingoPoint()
        self.quad = LingoList()
        self.member = None
        self.text = ""
        self.blend = 100
        self.visibility = None
        self.visible = LingoNumber()
        self.linesize = LingoNumber()
        self.color = LingoColor(0, 0, 0)
        self.bgcolor = LingoColor(0, 0, 0)

    @property
    def loch(self):
        return self.loc.loch

    @loch.setter
    def loch(self, value):
        self.loc.loch = value

    @property
    def locv(self):
        return self.loc.locv

    @locv.setter
    def locv(self, value):
        self.loc.locv = value

    @property
    def forecolor(self):
        return self.color

    @forecolor.setter
    def forecolor(self, value):
        self.color = value

    @property
    def backcolor(self):
        return self.bgcolor

    @backcolor.setter
    def backcolor(self, value):
        self.bgcolor = value

