from __future__ import annotations
from Drizzle.Data.LingoNumber import LingoNumber
from multipledispatch import dispatch


class LingoPoint:
    @dispatch(LingoNumber, LingoNumber)
    def __init__(self, loch: LingoNumber, locv: LingoNumber):
        self.loch = loch
        self.locv = locv

    @dispatch(int, int)
    def __init__(self, loch: int, locv: int):
        self.loch = LingoNumber(loch)
        self.locv = LingoNumber(locv)

    @dispatch()
    def __init__(self):
        self.loch = LingoNumber(0)
        self.locv = LingoNumber(0)

    def __getitem__(self, item) -> LingoNumber:
        if isinstance(item, LingoNumber):
            return [self.loch, self.locv][item.IntValue]
        return [self.loch, self.locv][item]

    def __len__(self):
        return 2

    def asPoint(self):
        return self.locv.DecimalValue, self.loch.DecimalValue

    def inside(self, rect) -> bool:
        from Drizzle.Data.LingoRect import LingoRect
        rect: LingoRect
        return rect.left <= self.loch < rect.right and rect.top <= self.locv < rect.bottom

    def __add__(self, other) -> LingoPoint:
        if isinstance(other, LingoPoint):
            return LingoPoint(self.loch + other.loch, self.locv + other.locv)
        elif isinstance(other, LingoNumber):
            return LingoPoint(self.loch + other, self.locv + other)

    def __radd__(self, other) -> LingoPoint:
        return self + other

    def __sub__(self, other) -> LingoPoint:
        if isinstance(other, LingoPoint):
            return LingoPoint(self.loch - other.loch, self.locv - other.locv)
        elif isinstance(other, LingoNumber):
            return LingoPoint(self.loch - other, self.locv - other)

    def __rsub__(self, other) -> LingoPoint:
        if isinstance(other, LingoNumber):
            return LingoPoint(other - self.loch, other - self.locv)
        return self.__rsub__(other)

    def __mul__(self, other) -> LingoPoint:
        if isinstance(other, LingoPoint):
            return LingoPoint(self.loch * other.loch, self.locv * other.locv)
        elif isinstance(other, LingoNumber):
            return LingoPoint(self.loch * other, self.locv * other)

    def __rmul__(self, other) -> LingoPoint:
        if isinstance(other, LingoNumber):
            return LingoPoint(other * self.loch, other * self.locv)
        return self.__rsub__(other)

    def __truediv__(self, other) -> LingoPoint:
        if isinstance(other, LingoPoint):
            return LingoPoint(self.loch / other.loch, self.locv / other.locv)
        elif isinstance(other, LingoNumber):
            return LingoPoint(self.loch / other, self.locv / other)

    def __rtruediv__(self, other) -> LingoPoint:
        if isinstance(other, LingoNumber):
            return LingoPoint(other / self.loch, other / self.locv)
        return self.__truediv__(other)

    def __neg__(self):
        return LingoPoint(-self.loch, -self.locv)

    def __eq__(self, other: LingoPoint):
        return self.asPoint() == other.asPoint()

    def __nq__(self, other: LingoPoint):
        return self.asPoint() != other.asPoint()

    def __str__(self):
        return f"point({self.loch}, {self.locv})"
