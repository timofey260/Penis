from __future__ import annotations
from enum import Enum
from multipledispatch import dispatch
from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoRect import LingoRect, LingoPoint
from Drizzle.Data.LingoColor import LingoColor
from PIL import Image


class ImageType(Enum):
    Palette1 = 1
    Palette2 = 2
    Palette4 = 4
    Palette8 = 8
    B5G5R5A1 = 16
    B8G8R8A8 = 32
    L8 = 33


class LingoImage:
    @dispatch(int, int, ImageType)
    def __init__(self, width: int, height: int, Type: ImageType):
        self.Width = width
        self.Height = height
        self.Type = Type

        self.image = Image.new(self.getFormat(Type), [self.Width, self.Height])
        self.IsPxl = False

    @dispatch(int, int, int)
    def __init__(self, width: int, height: int, bitDepth: int):
        self.__init__(width, height, ImageType(bitDepth))

    @staticmethod
    def getFormat(Type: ImageType) -> str:
        match Type:
            case ImageType.Palette1:
                return "1"
            case ImageType.Palette8:
                return "P"
            case ImageType.B5G5R5A1:
                return "I;16"
            case ImageType.B8G8R8A8:
                return "RGBA"
            case ImageType.L8:
                return "RGBA"
        raise NotImplementedError("Not supported")

    @property
    def height(self):
        return LingoNumber(self.Height)

    @property
    def width(self):
        return LingoNumber(self.Width)

    @property
    def Depth(self):
        return self.Type.value

    @property
    def depth(self):
        return self.Depth

    @property
    def rect(self):
        return LingoRect(LingoNumber(0), LingoNumber(0), self.width, self.height)

    def SaveAsPng(self, filename: str):
        self.image.save(filename)

    def copypixels(self, source: LingoImage, destQuad: LingoList, sourcerect: LingoRect):
        raise NotImplementedError()

    @dispatch(LingoPoint)
    def getpixel(self, point: LingoPoint):
        return self.getpixel(point.loch, point.locv)

    @dispatch(LingoNumber, LingoNumber)
    def getpixel(self, x: LingoNumber, y: LingoNumber):
        return self.getpixel(x.IntValue, y.IntValue)

    @dispatch(int, int)
    def getpixel(self, x: int, y: int):
        pixel = self.image.getpixel([x, y])
        if self.Type == ImageType.Palette1:
            pixel: int
            return LingoColor(pixel, pixel, pixel)
        elif self.Type == ImageType.Palette8:
            pixel: tuple[int, int, int]
            return LingoColor(pixel[0], pixel[1], pixel[2])
        return

    def setpixel(self, x: int, y: int):
        self.image.putpixel()