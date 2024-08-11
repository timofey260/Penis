from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.LingoCastLib import LingoCastLib
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoImage import LingoImage
from Drizzle.Data.LingoPoint import LingoPoint, LingoNumber
from enum import Enum, auto


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
