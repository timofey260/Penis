from __future__ import annotations
from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoPoint import LingoPoint
from multipledispatch import dispatch


class LingoRect:
    @dispatch(LingoNumber)
    def __init__(self, all: LingoNumber):
        self.__init__(all, all, all, all)

    @dispatch(LingoNumber, LingoNumber, LingoNumber, LingoNumber)
    def __init__(self, left: LingoNumber, top: LingoNumber, right: LingoNumber, bottom: LingoNumber):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @dispatch(LingoPoint, LingoPoint)
    def __init__(self, lt: LingoPoint, rb: LingoPoint):
        self.__init__(lt.loch.integer, lt.locv.integer, rb.loch.integer, rb.locv.integer)

    @property
    def width(self) -> LingoNumber:
        return self.right - self.left

    @property
    def height(self) -> LingoNumber:
        return self.bottom - self.top

    def __getitem__(self, item) -> LingoNumber:
        if isinstance(item, LingoNumber):
            return [self.left, self.top, self.right, self.bottom][item.IntValue]
        return [self.left, self.top, self.right, self.bottom][item]

    def __add__(self, other):
        if isinstance(other, LingoRect):
            return LingoRect(self.left + other.left, self.top + other.top,
                             self.right + other.right, self.bottom + other.bottom)
        if isinstance(other, LingoNumber):
            return self.__add__(LingoRect(other))

    def __radd__(self, other):
        if isinstance(other, LingoNumber):
            return LingoRect(other) + self
        return other.__add__(self)

    def __sub__(self, other):
        if isinstance(other, LingoRect):
            return LingoRect(self.left - other.left, self.top - other.top,
                             self.right - other.right, self.bottom - other.bottom)
        if isinstance(other, LingoNumber):
            return self.__add__(LingoRect(other))

    def __rsub__(self, other):
        if isinstance(other, LingoNumber):
            return LingoRect(other) - self
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, LingoRect):
            return LingoRect(self.left * other.left, self.top * other.top,
                             self.right * other.right, self.bottom * other.bottom)
        if isinstance(other, LingoNumber):
            return self.__add__(LingoRect(other))

    def __rmul__(self, other):
        if isinstance(other, LingoNumber):
            return LingoRect(other) * self
        return other.__mul__(self)

    def __truediv__(self, other):
        if isinstance(other, LingoRect):
            return LingoRect(self.left / other.left, self.top / other.top,
                             self.right / other.right, self.bottom / other.bottom)
        if isinstance(other, LingoNumber):
            return self.__add__(LingoRect(other))

    def __rtruediv__(self, other):
        if isinstance(other, LingoNumber):
            return LingoRect(other) / self
        return other.__truediv__(self)

    def __mod__(self, other):
        if isinstance(other, LingoRect):
            return LingoRect(self.left % other.left, self.top % other.top,
                             self.right % other.right, self.bottom % other.bottom)
        if isinstance(other, LingoNumber):
            return self.__add__(LingoRect(other))

    def __rmod__(self, other):
        if isinstance(other, LingoNumber):
            return LingoRect(other) % self
        return other.__mod__(self)

    def intersect(self, other: LingoRect):
        nLeft = other.left if self.left < other.left else self.left
        nRight = other.right if self.right > other.right else self.right
        nUp = other.top if self.top < other.top else self.top
        nDown = other.bottom if self.bottom > other.bottom else self.bottom
        return LingoRect(nLeft, nUp, nRight, nDown)

    def __eq__(self, other: LingoRect):
        return self.top == other.top and self.bottom == other.bottom and self.left == other.left and self.right == other.right

    def __ne__(self, other: LingoRect):
        return not self.__eq__(other)

    def __str__(self):
        return f"rect({self.left}, {self.top}, {self.right}, {self.bottom})"
