from __future__ import annotations

import os.path
from enum import Enum
from multipledispatch import dispatch
from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoRect import LingoRect, LingoPoint
from Drizzle.Data.LingoColor import LingoColor
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoMask import LingoMask
from PIL import Image, ImageOps, ImageTransform


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
        self.Mask: LingoMask = None

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

        self.image = Image.new(self.getFormat(Type), [self.Width, self.Height])
        self.IsPxl = False
        self.ImageBufferShared = False

    @dispatch(int, int, int)
    def __init__(self, width: int, height: int, bitDepth: int):
        self.__init__(width, height, ImageType(bitDepth))

    @dispatch(Image.Image, int, int, ImageType)
    def __init__(self, image: Image.Image, width: int, height: int, Type: ImageType):
        self.__init__(width, height, Type)
        self.image = image

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
        pixel = self.image.getpixel((x, y))
        if self.Type == ImageType.Palette1:
            pixel: int
            return LingoColor(pixel, pixel, pixel)
        elif self.Type == ImageType.Palette8:
            pixel: tuple[int, int, int]
            raise NotImplementedError("fuckyoy")
            return LingoColor(1, 1, 1)
        elif self.Type == ImageType.L8 or self.Type == ImageType.B8G8R8A8:
            pixel: tuple[int, int, int]
            return LingoColor(pixel[0], pixel[1], pixel[2])
        else:
            print("uh shit not implemented")
            return LingoColor(0, 0, 0)

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
        self.image.putpixel((x,y), self.color_to_value(value))

    def color_to_value(self, color: LingoColor):
        if self.Type == ImageType.Palette1:
            return color.RedByte
        elif self.Type == ImageType.Palette8:
            raise NotImplementedError("fuckyoy")
        elif self.Type == ImageType.L8 or self.Type == ImageType.B8G8R8A8:
            return color.RedByte, color.GreenByte, color.BlueByte
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
        box = ImageOps.invert(self.image.convert("RGB")).getbbox(alpha_only=False)
        return self.image.crop(box)

    def fill(self, color: LingoColor):
        self.CopyIfShared()
        self.image.paste(self.color_to_value(color), (0, 0, self.image.size[0], self.image.size[1]))

    def copypixels(self, source: LingoImage, dest, sourceRect: LingoRect, paramlist: LingoPropertyList = None):
        if paramlist is None:
            params = CopyPixelsParameters()
            params.Blend = 1
            params.Ink = CopyPixelsInk.Copy
        else:
            params = CopyPixelsParameters.parse(paramlist)
        if isinstance(dest, LingoList):
            quad = (*dest[0].asPoint(), *dest[3].asPoint(), *dest[2].asPoint(), *dest[1].asPoint())
            self.image.paste(source.image.transform(self.image.size, ImageTransform.AffineTransform(quad)))
        elif isinstance(dest, LingoRect):
            self.image.paste(source.image.resize((dest.width.IntValue, dest.height.IntValue)), (dest.left.IntValue, dest.top.IntValue))

    @staticmethod
    def LoadFromPath(path):
        if os.path.exists(path):
            image = Image.open(path)
        else:
            image = Image.new("RGBA", [1, 1])
        return LingoImage(image, image.width, image.height, ImageType.B8G8R8A8)

    def MakePxl(self):
        img = LingoImage(1, 1, 32)
        img.IsPxl = True
        img.setpixel(0, 0, LingoColor.Black)
        return img
