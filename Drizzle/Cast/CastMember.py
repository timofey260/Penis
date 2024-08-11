from __future__ import annotations
from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.LingoCastLib import LingoCastLib
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoImage import LingoImage
from Drizzle.Data.LingoPoint import LingoPoint, LingoNumber
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from enum import Enum, auto
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
        self._image = None
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

        match self.type:
            case CastMemberType.Bitmap:
                self.ImportFileImplBitmap(fullPath)
            case CastMemberType.Text:
                self.IMportFileImplText(fullPath)

    def AssertType(self, type: CastMemberType):
        assert self.Type != type, "This guy stinks"

    def CloneFrom(self, other: CastMember):
        self.Type = other.Type
        self.name = other.name

        match self.Type:
            case CastMemberType.Bitmap:
                self._image = other._image.DuplicateShared()
            case CastMemberType.Text:
                self._text = other._text