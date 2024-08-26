from __future__ import annotations

import os.path
from enum import Enum
from multipledispatch import dispatch
from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoRect import LingoRect, LingoPoint
from Drizzle.Data.LingoColor import LingoColor, colorpalette
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoMask import LingoMask
from PySide6.QtGui import QImage, QColor, QPainter
from PySide6.QtCore import QRect, QPoint


class ImageType(Enum):
    Palette1 = 1
    Palette2 = 2
    Palette4 = 4
    Palette8 = 8
    B5G5R5A1 = 16
    B8G8R8A8 = 32
    L8 = 33

class CopyPixelsInk(Enum):
    Copy = 0
    BackgroundTransparent = 36
    Darkest = 39


class CopyPixelsParameters:
    def __init__(self):
        self.Ink = CopyPixelsInk.Copy
        self.Blend = 0
        self.ForeColor = LingoColor(0, 0, 0)
        self.Mask: LingoMask | None = None

    @staticmethod
    def parse(params: LingoPropertyList):
        parameters = CopyPixelsParameters()
        parameters.Blend = 1
        if params[LingoSymbol("blend")] is not None:
            parameters.Blend = params[LingoSymbol("blend")].DecimalValue / 100
        if params[LingoSymbol("color")] is not None:
            parameters.ForeColor = params[LingoSymbol("color")]
        if params[LingoSymbol("ink")] is not None:
            parameters.Ink = CopyPixelsInk(params[LingoSymbol("ink")])
        if params[LingoSymbol("mask")] is not None:
            parameters.Mask = params[LingoSymbol("mask")]
        if params[LingoSymbol("maskimage")] is not None:
            parameters.Mask = params[LingoSymbol("maskimage")]


class LingoImage:
    @property
    def Pxl(self):
        return self.MakePxl()

    @dispatch(int, int, ImageType)
    def __init__(self, width: int, height: int, Type: ImageType):
        self.Width = width
        self.Height = height
        self.Type = Type

        self.image = QImage(width, height, LingoImage.getFormat(Type))
        self.IsPxl = False
        self.ImageBufferShared = False
        if self.Type == ImageType.Palette8:
            self.image.setColorTable(colorpalette)

    @dispatch(int, int, int)
    def __init__(self, width: int, height: int, bitDepth: int):
        self.__init__(width, height, ImageType(bitDepth))

    @dispatch(QImage, int, int, ImageType)
    def __init__(self, image: QImage, width: int, height: int, Type: ImageType):
        self.__init__(width, height, Type)
        self.image = image

    @staticmethod
    def getFormat(Type: ImageType) -> QImage.Format:
        match Type:
            case ImageType.Palette1:
                return QImage.Format.Format_Mono
            case ImageType.Palette8:
                return QImage.Format.Format_Indexed8
            case ImageType.B5G5R5A1:
                return QImage.Format.Format_ARGB8555_Premultiplied  # i hope it's correct
            case ImageType.B8G8R8A8:
                return QImage.Format.Format_ARGB32
            case ImageType.L8:
                return QImage.Format.Format_ARGB32
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

    @dispatch(LingoPoint)
    def getpixel(self, point: LingoPoint):
        return self.getpixel(point.loch, point.locv)

    @dispatch(LingoNumber, LingoNumber)
    def getpixel(self, x: LingoNumber, y: LingoNumber):
        return self.getpixel(x.IntValue, y.IntValue)

    @dispatch(int, int)
    def getpixel(self, x: int, y: int):
        if x < 0 or x >= self.Width or y < 0 or y >= self.Height:
            return LingoColor.White
        pixel = self.image.pixelColor(x, y)
        return LingoColor(pixel.red(), pixel.green(), pixel.blue())

    @dispatch(LingoPoint, LingoColor)
    def setpixel(self, point: LingoPoint, value: LingoColor):
        return self.setpixel(point.loch, point.locv, value)

    @dispatch(LingoNumber, LingoNumber, LingoColor)
    def setpixel(self, x: LingoNumber, y: LingoNumber, value: LingoColor):
        return self.setpixel(x.IntValue, y.IntValue, value)

    @dispatch(int, int, LingoColor)
    def setpixel(self, x: int, y: int, value: LingoColor):
        if x < 0 or x >= self.Width or y < 0 or y >= self.Height:
            return
        self.CopyIfShared()  # we copy image buffer to change it if we had it shared for some reason
        self.image.setPixel(x, y, self.color_to_value(value))

    def color_to_value(self, color: LingoColor):
        if self.Type == ImageType.Palette1:
            return color.RedByte
        elif self.Type == ImageType.Palette8:
            raise NotImplementedError("fuckyoy")
        elif self.Type == ImageType.L8 or self.Type == ImageType.B8G8R8A8:
            return QColor(color.RedByte, color.GreenByte, color.BlueByte).rgba()
        else:
            raise NotImplementedError("fuckyoy")

    def duplicate(self):
        newimg = self.image.copy()
        img = LingoImage(self.Width, self.Height, self.Type)
        img.image = newimg
        return img

    def DuplicateShared(self):
        self.ImageBufferShared = True
        newimg = LingoImage(self.image, self.Width, self.Height, self.Type)
        newimg.IsPxl = self.IsPxl
        newimg.ImageBufferShared = True
        return newimg

    def createmask(self):
        pass # todo

    def CopyIfShared(self):
        if not self.ImageBufferShared:
            return

        self.ImageBufferShared = False
        self.image = self.image.copy()

    def Trimmed(self):
        # todo trim
        # box = ImageOps.invert(self.image.convert("RGB")).getbbox(alpha_only=False)
        minX = 9999  # works hood enough
        maxX = -9999
        minY = 9999
        maxY = -9999
        any = False

        for y in range(0, self.Height):
            for x in range(0, self.Width):
                px = self.getpixel(x, y)
                if px == LingoColor(255, 255, 255):
                    minX = min(minX, x)
                    minY = min(minY, y)

                    maxX = max(maxX, x + 1)
                    maxY = max(maxY, y + 1)
                    any = True
        if not any:
            return LingoImage(1, 1, self.Type)

        if minX == 0 and minY == 0 and maxX == self.Width - 1 and maxY == self.Height - 1:
            return self
        image = LingoImage(maxX - minX, maxY - minY, self.Type)
        print(minX, minY, maxX, maxY)

        return image

    def fill(self, color: LingoColor):
        self.CopyIfShared()
        self.image.fill(self.color_to_value(color))

    def copypixels(self, source: LingoImage, dest, sourceRect: LingoRect, paramlist: LingoPropertyList = None):
        if paramlist is None:
            params = CopyPixelsParameters()
            params.Blend = 1
            params.Ink = CopyPixelsInk.Copy
        else:
            params = CopyPixelsParameters.parse(paramlist)
        if isinstance(dest, LingoList):
            quad = (*dest[0].asPoint(), *dest[3].asPoint(), *dest[2].asPoint(), *dest[1].asPoint())
            pass
        elif isinstance(dest, LingoRect):
            pass

    @staticmethod
    def LoadFromPath(path):
        if os.path.exists(path):
            image = QImage(path)
        else:
            image = QImage(1, 1, QImage.Format.Format_ARGB32)
        print(f"imported {path}")
        return LingoImage(image, image.width(), image.height(), ImageType.B8G8R8A8)

    def MakePxl(self):
        img = LingoImage(1, 1, 32)
        img.IsPxl = True
        img.setpixel(0, 0, LingoColor(0, 0, 0).Black)
        return img
