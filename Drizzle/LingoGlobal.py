from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Data.LingoRect import LingoRect, LingoPoint, LingoNumber
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoColor import LingoColor
from Drizzle.Data.LingoImage import LingoImage
from Drizzle.Data.LingoSprite import LingoSprite
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from Drizzle.Xtra.ImgXtra import ImgXtra, BaseXtra
from Drizzle.Xtra.FileIOXtra import FileIOXtra
from Drizzle.LingoScriptRuntime import LingoScriptRuntime
import math
import os
from multipledispatch import dispatch
from typing import Any


class Global:
    def __init__(self, glob: LingoGlobal):
        self._global = glob

    def clearglobals(self):
        raise NotImplementedError("ahwhafowa")


class System:
    def __init__(self, glob: LingoGlobal):
        self._global = glob

    @property
    def milliseconds(self):
        return self._global.LingoRuntime.Stopwatch.ElapsedMilliseconds

    @property
    def desktoprectlist(self):
        return LingoPoint(1024, 768)


class Key:
    def keypressed(self, key) -> LingoNumber:
        return LingoNumber(0)


class Mouse:
    @property
    def mouseloc(self):
        return LingoPoint()
    
    @property
    def mousedown(self):
        return 0
    
    @property
    def rightmousedown(self):
        return 0


class Window:
    def __init__(self, glob: LingoGlobal):
        self.appearanceoptions = None
        self.resizable = LingoNumber()
        self.rect = LingoRect(LingoNumber(0))
        self.sizestate = LingoSymbol("normal")


class Movie:
    def __init__(self, glob: LingoGlobal):
        self._global = glob
        self.window = Window(glob)
        self.frame = 0
    @property
    def path(self):
        return self._global.the_moviePath

    @property
    def stage(self):
        raise NotImplementedError()

    @property
    def exitlock(self):
        return LingoNumber(0)

    def go(self, linenumber: LingoNumber):
        pass


class Player:
    def appminimize(self):
        pass

    def quit(self):
        pass


class StringLineData:
    def __init__(self):
        self.NewlineIndices: list[int] = []


class StringCharIndex:
    def __init__(self, s: str):
        self.String = s

    def __getitem__(self, item):
        if isinstance(item, LingoNumber):
            item = item.IntValue
        elif isinstance(item, list):
            return self.String[item[0]:item[1]]
        return self.String[item - 1] if 1 <= item < len(self.String) else None

    # yeah me neither bro
    def TryGetIndex(self, *args):
        raise NotImplementedError()


class StringLineIndex:
    def __init__(self, s: str):
        self.String = s

    def __getitem__(self, item):
        if isinstance(item, LingoNumber):
            item = item.IntValue
        if item <= 0:
            return self.String
        cacheData = LingoGlobal.GetCachedStringLineData(self.String)
        indices = cacheData.NewlineIndices
        idx = item - 1
        if idx > len(indices):
            return ""
        endIdx = len(self.String)
        if idx < len(indices):
            endIdx = indices[idx]
        startIdx = 0
        if idx > 0:
            startIdx = indices[idx - 1] + 1

        return self.String[startIdx:endIdx]


class LingoGlobal:
    def __init__(self, runtime: LingoRuntime):
        self._system: System | None = None
        self._key: Key | None = None
        self._mouse: Mouse | None = None
        self._movie: Movie | None = None
        self._global: Global | None = None
        self._player: Player | None = None
        self.LingoRuntime: LingoRuntime = runtime

        self.ScriptRuntime: LingoScriptRuntime | None = None

    BACKSPACE = "\x08"
    EMPTY = ""
    ENTER = "\x03"
    QUOTE = "\""
    RETURN = "\r"
    SPACE = " "
    VOID = None

    TRUE = LingoNumber(1)
    FALSE = LingoNumber(0)
    PI = LingoNumber(math.pi)
    StringLineCache: dict[str, StringLineData] = {}

    @staticmethod
    def GetCachedStringLineData(string: str):
        return LingoGlobal.StringLineCache.get(string)

    @staticmethod
    def CacheStringLineData(key: str):
        l = []
        for i in range(len(key)):
            char = key[i]
            if char == "\r":
                l.append(i)
        sld = StringLineData()
        sld.NewlineIndices = l

        return sld

    @staticmethod
    def thenumberoflines_helper(value: str):
        cacheData = LingoGlobal.GetCachedStringLineData(value)
        return len(cacheData.NewlineIndices) + 1

    @staticmethod
    def lineof_helper(idx: LingoNumber, collection: str):
        return LingoGlobal.linemember_helper(collection)[idx.IntValue]

    @staticmethod
    def charof_helper(idx: LingoNumber, string: str):
        iVal = idx.IntValue

        if iVal < 1:
            return string

        if iVal > len(string):
            return ""

        return str(string[iVal - 1])

    @staticmethod
    def charmember_helper(d: str): return StringCharIndex(d)

    @staticmethod
    def linemember_helper(d: str): return StringLineIndex(d)

    @staticmethod
    def lengthmember_helper(d): return len(d)

    def DoSliceString(self, string: str, start: int, end: int): raise NotImplementedError()

    @dispatch(int)
    def numtochar(self, num: int): return chr(num)

    @dispatch(LingoNumber)
    def numtochar(self, num: LingoNumber): return chr(num.IntValue)

    @staticmethod
    def abs(value: LingoNumber) -> LingoNumber:
        return LingoNumber.Abs(value)

    @staticmethod
    def sqrt(value: LingoNumber) -> LingoNumber:
        return LingoNumber.Sqrt(value)

    @staticmethod
    def contains(container: str, value: str) -> LingoNumber:
        return LingoNumber(1) if container.find(value) >= 0 else LingoNumber(0)

    @staticmethod
    def starts(container: str, value: str) -> LingoNumber:
        return LingoNumber(1) if container.startswith(value) else LingoNumber(0)

    @staticmethod
    @dispatch(Any, Any)
    def concat(a, b): return f"{a}{b}"

    @staticmethod
    @dispatch(str, str)
    def concat(a, b): return f"{a}{b}"

    @staticmethod
    @dispatch(Any, Any, Any)
    def concat(a, b, c): return f"{a}{b}{c}"

    @staticmethod
    @dispatch(str, str, str)
    def concat(a, b, c): return f"{a}{b}{c}"

    @staticmethod
    @dispatch(list)
    def concat(items): return "".join(items)

    @staticmethod
    @dispatch(Any, Any)
    def concat_space(a, b): return f"{a} {b}"

    @staticmethod
    @dispatch(str, str)
    def concat_space(a, b): return f"{a} {b}"

    @staticmethod
    @dispatch(Any, Any, Any)
    def concat_space(a, b, c): return f"{a} {b} {c}"

    @staticmethod
    @dispatch(str, str, str)
    def concat_space(a, b, c): return f"{a} {b}, {c}"

    @staticmethod
    @dispatch(list)
    def concat_space(a): return " ".join(a)

    def slice_helper(self, obj, start: LingoNumber, end: LingoNumber):
        try:
            return obj[start.IntValue:end.IntValue]
        except:
            raise NotImplementedError("fuckyoy")

    def new_castlib(self, type: str, lib):
        raise NotImplementedError()

    def new_script(self, type: str, l: LingoList):
        return self.LingoRuntime.CreateScript(type, l)

    @staticmethod
    def thenumberof_helper(obj):
        return len(obj)

    @staticmethod
    def itemof_helper(obj, collection):
        if isinstance(obj, LingoNumber):
            obj = obj.IntValue
        return collection[obj]

    @staticmethod
    def point(h: LingoNumber, v: LingoNumber): return LingoPoint(h, v)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber, LingoNumber, LingoNumber)
    def rect(l: LingoNumber, t: LingoNumber, r: LingoNumber, b: LingoNumber): return LingoRect(l, t, r, b)

    @staticmethod
    @dispatch(LingoPoint, LingoPoint)
    def rect(lt: LingoPoint, rb: LingoPoint): return LingoRect(lt, rb)

    @staticmethod
    def cos(d: LingoNumber) -> LingoNumber: return LingoNumber.Cos(d)

    @staticmethod
    def sin(d: LingoNumber) -> LingoNumber: return LingoNumber.Sin(d)

    @staticmethod
    def tan(d: LingoNumber) -> LingoNumber: return LingoNumber.Tan(d)

    @staticmethod
    def atan(d: LingoNumber) -> LingoNumber: return LingoNumber.Atan(d)

    @staticmethod
    def pow(base: LingoNumber, exp: LingoNumber) -> LingoNumber: return LingoNumber.Pow(base, exp)

    @staticmethod
    def symbol(s: str) -> LingoSymbol: return LingoSymbol(s)

    def put(self, d):
        print(d)

    def xtra(self, xtraNameOrNum):
        xtraname = str(xtraNameOrNum)
        xtraname = xtraname.lower()
        return {"fileio": FileIOXtra(), "imgxtra": ImgXtra()}[xtraname]

    def new(self, a):
        if isinstance(a, BaseXtra):
            return a.Duplicate()
        raise NotImplementedError("you stupid")

    def basetdisplay(self, w, h, idk3, idk, idk2):
        raise NotImplementedError("wtf is this^^^")

    def bascreeninfo(self, prop: str):
        raise NotImplementedError("help me")

    def getnthfilenameinfolder(self, folderPath: str, fileNumber: LingoNumber) -> str:
        idx = int(fileNumber) - 1
        entries = os.listdir(folderPath)
        return "" if idx >= len(entries) else os.path.join(folderPath, entries[idx])

    def script(self, a: str):
        return self.LingoRuntime.CreateScript(a, LingoList())
    
    @property
    def the_milliseconds(self):
        return self._system.milliseconds

    @property
    def the_moviepath(self):
        return self.the_moviePath

    @property
    def the_dirseparator(self):
        return self.the_dirSeparator

    def objectp(self, d): raise NotImplementedError("when would this end")

    @dispatch(Any, Any)
    def member(self, membernameornum, castnameornum=None):
        return self.LingoRuntime.GetCastMember(membernameornum, castnameornum)

    @dispatch(str)
    def member(self, name: str):
        return self.LingoRuntime.GetCastMember(name)

    @dispatch(LingoNumber, LingoNumber, LingoNumber)
    def color(self, r: LingoNumber, g: LingoNumber, b: LingoNumber):
        return LingoColor(min(r.IntValue, 255), min(g.IntValue, 255), min(b.IntValue, 255))

    @dispatch(LingoNumber)
    def color(self, palIdx: LingoNumber):
        return LingoColor.getitem(palIdx)

    @dispatch(LingoNumber, LingoNumber, LingoNumber)
    def image(self, w: LingoNumber, h: LingoNumber, bitDepth: LingoNumber):
        return LingoImage(w.IntValue, h.IntValue, bitDepth.IntValue)

    @dispatch(LingoNumber, LingoNumber, LingoSymbol)
    def image(self, w: LingoNumber, h: LingoNumber, Type: LingoSymbol):
        return LingoImage(w, h, Type)  # todo

    @dispatch(Any)
    def string(self, value): return str(value)

    @dispatch(LingoNumber)
    def string(self, value): return str(value)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_add(a: LingoNumber, b: LingoNumber): return a + b

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_sub(a: LingoNumber, b: LingoNumber): return a - b

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_mul(a: LingoNumber, b: LingoNumber): return a * b

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_div(a: LingoNumber, b: LingoNumber): return a / b

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_mod(a: LingoNumber, b: LingoNumber): return a % b

    @staticmethod
    @dispatch(LingoPoint, LingoPoint)
    def op_add(a: LingoPoint, b: LingoPoint): return a + b

    @staticmethod
    @dispatch(LingoPoint, LingoPoint)
    def op_sub(a: LingoPoint, b: LingoPoint): return a - b

    @staticmethod
    @dispatch(LingoPoint, LingoPoint)
    def op_mul(a: LingoPoint, b: LingoPoint): return a * b

    @staticmethod
    @dispatch(LingoPoint, LingoPoint)
    def op_div(a: LingoPoint, b: LingoPoint): return a / b

    @staticmethod
    @dispatch(LingoPoint, LingoNumber)
    def op_add(a: LingoPoint, b: LingoNumber): return a + b

    @staticmethod
    @dispatch(LingoPoint, LingoNumber)
    def op_sub(a: LingoPoint, b: LingoNumber): return a - b

    @staticmethod
    @dispatch(LingoPoint, LingoNumber)
    def op_mul(a: LingoPoint, b: LingoNumber): return a * b

    @staticmethod
    @dispatch(LingoPoint, LingoNumber)
    def op_div(a: LingoPoint, b: LingoNumber): return a / b

    @staticmethod
    @dispatch(LingoRect, LingoRect)
    def op_add(a: LingoRect, b: LingoRect): return a + b

    @staticmethod
    @dispatch(LingoRect, LingoRect)
    def op_sub(a: LingoRect, b: LingoRect): return a - b

    @staticmethod
    @dispatch(LingoRect, LingoRect)
    def op_mul(a: LingoRect, b: LingoRect): return a * b

    @staticmethod
    @dispatch(LingoRect, LingoRect)
    def op_div(a: LingoRect, b: LingoRect): return a / b

    @staticmethod
    @dispatch(Any, Any)
    def op_add(a, b):
        if isinstance(a, LingoNumber) and b is None:
            return a

        if a is None and isinstance(b, LingoNumber):
            return b

        if isinstance(a, type(b)) and type(b) in [LingoNumber, LingoPoint, LingoRect]:
            return a + b

        # lingovector bullshit
        return a + b

    @staticmethod
    @dispatch(Any, Any)
    def op_sub(a, b):
        if isinstance(a, LingoNumber) and b is None:
            return a

        if a is None and isinstance(b, LingoNumber):
            return LingoNumber(0) - b

        if isinstance(a, type(b)) and type(b) in [LingoNumber, LingoPoint, LingoRect]:
            return a - b

        # lingovector bullshit
        return a - b

    @staticmethod
    @dispatch(Any, Any)
    def op_mul(a, b):
        if isinstance(a, LingoNumber) and b is None:
            return LingoNumber(0)

        if a is None and isinstance(b, LingoNumber):
            return LingoNumber(0)

        if isinstance(a, type(b)) and type(b) in [LingoNumber, LingoPoint, LingoRect]:
            return a * b

        # lingovector bullshit
        return a * b

    @staticmethod
    @dispatch(Any, Any)
    def op_div(a, b):
        if isinstance(a, LingoNumber) and b is None:
            return a / LingoNumber(0)  # the chaos

        if a is None and isinstance(b, LingoNumber):
            return LingoNumber(0) / b

        if isinstance(a, type(b)) and type(b) in [LingoNumber, LingoPoint, LingoRect]:
            return a / b

        # lingovector bullshit
        return a / b

    @staticmethod
    @dispatch(Any, Any)
    def op_mod(a, b):
        if isinstance(a, LingoNumber) and b is None:
            return a % LingoNumber(0)  # the chaos

        if a is None and isinstance(b, LingoNumber):
            return LingoNumber(0) % b

        if isinstance(a, type(b)) and type(b) in [LingoNumber, LingoPoint, LingoRect]:
            return a % b

        # lingovector bullshit
        return a % b

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_eq_b(a: LingoNumber, b: LingoNumber):
        return a == b

    @staticmethod
    @dispatch(Any, Any)
    def op_eq_b(a: Any, b: Any):
        # some stuff i wouldn't care about
        if type(a) is not type(b):
            return False
        if isinstance(a, str) and isinstance(b, str):
            return a.lower() == b.lower()
        return a == b

    @staticmethod
    @dispatch(Any, Any)
    def op_eq(a: Any, b: Any) -> LingoNumber:
        return LingoNumber(1) if LingoGlobal.op_eq_b(a, b) else LingoNumber(0)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_eq(a: LingoNumber, b: LingoNumber) -> LingoNumber:
        return LingoNumber(1) if LingoGlobal.op_eq_b(a, b) else LingoNumber(0)

    @staticmethod
    @dispatch(Any, Any)
    def op_ne_b(a: Any, b: Any) -> bool:
        return not LingoGlobal.op_eq_b(a, b)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_ne_b(a: LingoNumber, b: LingoNumber) -> bool:
        return not LingoGlobal.op_eq_b(a, b)

    @staticmethod
    @dispatch(Any, Any)
    def op_ne(a: Any, b: Any) -> LingoNumber:
        return LingoNumber(1) if LingoGlobal.op_eq_b(a, b) else LingoNumber(0)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_ne(a: LingoNumber, b: LingoNumber) -> LingoNumber:
        return LingoNumber(1) if LingoGlobal.op_eq_b(a, b) else LingoNumber(0)

    @staticmethod
    @dispatch(Any, Any)
    def op_lt(a: Any, b: Any): return LingoNumber(1) if a < b else LingoNumber(0)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_lt(a: LingoNumber, b: LingoNumber): return LingoNumber(1) if a < b else LingoNumber(0)
    
    @staticmethod
    @dispatch(Any, Any)
    def op_le(a: Any, b: Any): return LingoNumber(1) if a >= b else LingoNumber(0)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_le(a: LingoNumber, b: LingoNumber): return LingoNumber(1) if a >= b else LingoNumber(0)
    
    @staticmethod
    @dispatch(Any, Any)
    def op_gt(a: Any, b: Any): return LingoNumber(1) if a > b else LingoNumber(0)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_gt(a: LingoNumber, b: LingoNumber): return LingoNumber(1) if a > b else LingoNumber(0)
    
    @staticmethod
    @dispatch(Any, Any)
    def op_ge(a: Any, b: Any): return LingoNumber(1) if a <= b else LingoNumber(0)

    @staticmethod
    @dispatch(LingoNumber, LingoNumber)
    def op_ge(a: LingoNumber, b: LingoNumber): return LingoNumber(1) if a <= b else LingoNumber(0)

    @staticmethod
    @dispatch(Any, Any)
    def op_and(a: Any, b: Any):
        bA = LingoGlobal.ToBool(a)
        bB = LingoGlobal.ToBool(b)
        return LingoNumber(1) if bA and bB else LingoNumber(0)

    @staticmethod
    @dispatch(Any, Any)
    def op_or(a: Any, b: Any):
        bA = LingoGlobal.ToBool(a)
        bB = LingoGlobal.ToBool(b)
        return LingoNumber(1) if bA or bB else LingoNumber(0)

    @staticmethod
    @dispatch(Any)
    def ToBool(a: Any):
        if isinstance(a, LingoNumber):
            return a.IntValue != 0
        return a is not None

    @staticmethod
    @dispatch(LingoNumber)
    def ToBool(a: LingoNumber):
        return a.DecimalValue != 0

    @property
    def the_platform(self):
        return "win"  # does he not know

    def sprite(self, *args): return LingoSprite()
    
    def sound(self, *args): return NotImplementedError("Please god")
    def call(self, *args): return NotImplementedError("Help me finish this")

    def str(self, a: Any):
        return str(a)
    
    @staticmethod
    def chars(string: str, first: LingoNumber, last: LingoNumber):
        if first == last:
            return str(string[first.IntValue - 1])
        return string[first.IntValue - 1:min(len(string), last.IntValue)]
    
    def alert(self, *args): return NotImplementedError("Help me finish this")

    def ilk(self, obj):
        val = ""
        if isinstance(obj, LingoNumber) and not obj.IsDecimal:
            val = "integer"
        elif isinstance(obj, LingoNumber) and obj.IsDecimal:
            val = "float"
        elif isinstance(obj, LingoList):
            val = "list"
        elif isinstance(obj, LingoPropertyList):
            val = "proplist"
        elif isinstance(obj, str):
            val = "string"
        elif isinstance(obj, LingoRect):
            val = "rect"
        elif isinstance(obj, LingoPoint):
            val = "point"
        elif isinstance(obj, LingoColor):
            val = "color"
        elif isinstance(obj, LingoSymbol):
            val = "symbol"
        elif isinstance(obj, LingoImage):
            val = "image"
        elif isinstance(obj, None):
            val = "void"
        else:
            raise NotImplementedError()

        return LingoSymbol(val)

    def createfile(self, d, f: str): return d.createfile(f)

    @property
    def MovieScriptInstance(self):
        return self.LingoRuntime.MovieScriptInstance

    @staticmethod
    def last_char(string: str):
        return string[-1]

    @staticmethod
    def stringp(string): return LingoNumber(1) if isinstance(string, str) else LingoNumber(0)

    def castlib(self, nameOrNum): raise NotImplementedError("THE LINGOGLOBAL IS REAL")

    def value(self, a: str):
        trimmed = a.strip()
        if trimmed == "":
            return LingoNumber(0)

        try:
            pass
        except:
            return None  # todo

    @property
    def the_dirSeparator(self):
        return os.path.sep
    @property
    def the_moviePath(self):
        return self.LingoRuntime.MovieBasePath

    def Init(self):
        self._system = System(self)
        self._key = Key()
        self._mouse = Mouse()
        self._movie = Movie(self)
        self._player = Player
        self._global = Global(self)
        self.ScriptRuntime = LingoScriptRuntime(self)

    def go(self, frame: LingoNumber):
        self._movie.go(frame)

    @property
    def the_frame(self):
        return self._movie.frame
    
    @property
    def the_randomSeed(self) -> LingoNumber:
        return LingoNumber(self.LingoRuntime.RngSeed)

    @the_randomSeed.setter
    def the_randomSeed(self, value: LingoNumber):
        self.LingoRuntime.RngSeed = value.IntValue

    def random(self, max: LingoNumber) -> LingoNumber:
        return LingoNumber(self.LingoRuntime.Random(max.IntValue))
