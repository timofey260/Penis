from __future__ import annotations
from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Data.LingoRect import LingoRect, LingoPoint, LingoNumber
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoList import LingoList
from Drizzle.Xtra.ImgXtra import ImgXtra, BaseXtra
from Drizzle.Xtra.FileIOXtra import FileIOXtra
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


class LingoGlobal:
    def __init__(self, runtime: LingoRuntime):
        self._system: System | None = None
        self._key: Key | None = None
        self._mouse: Mouse | None = None
        self._movie: Movie | None = None
        self._global: Global | None = None
        self._player: Player | None = None
        self.LingoRuntime: LingoRuntime = runtime

        self.BACKSPACE = "\x08"
        self.EMPTY = ""
        self.ENTER = "\x03"
        self.QUOTE = "\""
        self.RETURN = "\r"
        self.SPACE = " "
        self.VOID = None

    TRUE = LingoNumber(1)
    FALSE = LingoNumber(0)
    PI = LingoNumber(math.pi)

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
    @dispatch(list[Any])
    def concat(items): return "".join(items)

    @staticmethod
    @dispatch(list[str])
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
    @dispatch(list[Any])
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

    @dispatch()
    def member(self, membernameornum, castnameornum=None):
        return self.LingoRuntime.GetCastMember(membernameornum, castnameornum)

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
