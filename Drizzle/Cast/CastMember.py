from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Drizzle.LingoRuntime import LingoRuntime
    from Drizzle.LingoCastLib import LingoCastLib
from Drizzle.Data.LingoImage import LingoImage
from Drizzle.Data.LingoRect import LingoRect, LingoNumber
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from Drizzle.Data.LingoColor import LingoColor
from enum import Enum, auto
from multipledispatch import dispatch
import os


class CastMemberType(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count
    Empty = auto()
    Bitmap = auto()
    Script = auto()
    Text = auto()
    Shape = auto()


class CastMember:
    def __init__(self, runtime: LingoRuntime, castLib: LingoCastLib, number: int, cast: str):
        self._castLib = castLib
        self.Runtime = runtime
        self.Number = number
        self.Cast = cast
        self._text = ""
        self._name = None
        self.alignment = LingoSymbol("")
        self._image: LingoImage = None
        self.regpoint = None
        self._lineDirection = None
        self.Type: CastMemberType = CastMemberType.Empty

    @property
    def type(self):
        return {CastMemberType.Empty: LingoSymbol(""),
                CastMemberType.Bitmap: LingoSymbol("bitmap"),
                CastMemberType.Script: LingoSymbol("script"),
                CastMemberType.Text: LingoSymbol("text"),
                CastMemberType.Shape: LingoSymbol("shape"),
                }[self.Type]

    def erase(self):
        self.Type = CastMemberType.Empty
        self._text = ""
        self._image = None
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._castLib.NameIndexDirty()

    def importfileinto(self, path: str, proplist: LingoPropertyList = None):
        fullPath = self.Runtime.GetFilePath(path)
        name, ext = os.path.splitext(path)
        ext = ext[1:]
        self.ImportFile(fullPath, ext, name)

    def ImportFile(self, fullPath: str, ext: str, name: str = None):
        self.erase()

        type = CastMemberType.Empty
        match ext:
            case "png" | "bmp":
                type = CastMemberType.Bitmap
            case "lingo":
                type = CastMemberType.Script
            case "txt":
                type = CastMemberType.Text
        self.Type = type
        if name is not None:
            self.name = name

        match self.Type:
            case CastMemberType.Bitmap:
                self.ImportFileImplBitmap(fullPath)
            case CastMemberType.Text:
                self.ImportFileImplText(fullPath)

    def AssertType(self, Type: CastMemberType):
        assert self.Type == Type, "This guy stinks"

    def CloneFrom(self, other: CastMember):
        self.Type = other.Type
        self.name = other.name

        match self.Type:
            case CastMemberType.Bitmap:
                self._image = other._image.DuplicateShared()
            case CastMemberType.Text:
                self._text = other._text

    @property
    def image(self):
        self.AssertType(CastMemberType.Bitmap)
        return self._image

    @image.setter
    def image(self, value):
        self.AssertType(CastMemberType.Bitmap)
        self._image = value

    @property
    def rect(self) -> LingoRect:
        self.AssertType(CastMemberType.Bitmap)
        return self._image.rect

    @property
    def width(self) -> LingoNumber:
        self.AssertType(CastMemberType.Bitmap)
        return self.image.width

    @property
    def height(self) -> LingoNumber:
        self.AssertType(CastMemberType.Bitmap)
        return self.image.height

    @dispatch(int, int)
    def getpixel(self, x: int, y: int) -> LingoColor:
        self.AssertType(CastMemberType.Bitmap)
        return self.image.getpixel(x, y)

    @dispatch(LingoNumber, LingoNumber)
    def getpixel(self, x: LingoNumber, y: LingoNumber):
        return self.getpixel(int(x), int(y))

    def ImportFileImplBitmap(self, path: str):
        self.image = LingoImage.LoadFromPath(path).Trimmed()

    @property
    def linedirection(self):
        self.AssertType(CastMemberType.Shape)
        return self._lineDirection

    @linedirection.setter
    def linedirection(self, value):
        self.AssertType(CastMemberType.Shape)
        self._lineDirection = value

    @property
    def text(self):
        self.AssertType(CastMemberType.Text)
        return self._text

    @text.setter
    def text(self, value):
        self.AssertType(CastMemberType.Text)
        self._text = value

    def ImportFileImplText(self, path: str):
        try:
            with open(path) as sr:
                self.text = "\r".join(sr.readlines())

        except FileNotFoundError:
            self.text = ""

        except NotADirectoryError:
            self.text = ""


