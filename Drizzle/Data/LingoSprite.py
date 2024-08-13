from Drizzle.Data.LingoRect import LingoRect, LingoPoint, LingoNumber
from Drizzle.Data.LingoList import LingoList


class LingoSprite:
    def __init__(self):
        self.rect = LingoRect(LingoNumber(0))
        self.loc = LingoPoint()
        self.quad = LingoList()

