from __future__ import annotations
from multipledispatch import dispatch
from Drizzle.Data.LingoNumber import LingoNumber


class LingoColor:
    PackWhite = 0xFF_FF_FF_FF
    PackBlack = 0xFF_00_00_00
    PackRed = 0xFF_FF_00_00

    Palette = [0 for i in range(256)]
    Palette[0] = PackWhite
    Palette[6] = PackRed
    Palette[255] = PackBlack

    @dispatch(int, int, int)
    def __init__(self, r: int, g: int, b: int):
        self.RedByte = r
        self.GreenByte = g
        self.BlueByte = b

    @dispatch(LingoNumber, LingoNumber, LingoNumber)
    def __init__(self, r: LingoNumber, g: LingoNumber, b: LingoNumber):
        self.RedByte = r.IntValue
        self.GreenByte = g.IntValue
        self.BlueByte = b.IntValue

    @property
    def red(self):
        return LingoNumber(self.RedByte)

    @red.setter
    def red(self, value):
        self.RedByte = value.IntValue

    @property
    def green(self):
        return LingoNumber(self.GreenByte)

    @green.setter
    def green(self, value):
        self.GreenByte = value.IntValue

    @property
    def blue(self):
        return LingoNumber(self.BlueByte)

    @blue.setter
    def blue(self, value):
        self.BlueByte = value.IntValue

    def BitPack(self):
        return 0xFF000000 | self.RedByte << 16 | self.GreenByte << 8 | self.BlueByte

    @staticmethod
    def BitUnpack(packed: int):
        return LingoColor((packed & 0x00FF0000) >> 16, (packed & 0x0000FF00) >> 8, packed & 0x000000FF)

    @staticmethod
    @dispatch(int)
    def getitem(item: int):
        palcol = LingoColor.Palette[item]
        if palcol == 0:
            print(f"Unknown palette color {item}")
            return LingoColor.White
        return LingoColor.BitUnpack(palcol)

    @staticmethod
    @dispatch(LingoNumber)
    def getitem(item: LingoNumber):
        LingoColor.getitem(item.IntValue)

    def __eq__(self, other: LingoColor):
        return self.RedByte == other.RedByte and self.GreenByte == other.GreenByte and self.BlueByte == self.BlueByte

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"color( {self.RedByte}, {self.GreenByte}, {self.BlueByte} )"

    @property
    def White(self):
        return LingoColor(255, 255, 255)

    @property
    def Black(self):
        return LingoColor(0, 0, 0)