from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Data.LingoRect import LingoRect, LingoPoint, LingoNumber
from Drizzle.Data.LingoSymbol import LingoSymbol
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoColor import LingoColor
from Drizzle.Data.LingoImage import LingoImage, ImageType
from Drizzle.Data.LingoSprite import LingoSprite
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from Drizzle.Xtra.ImgXtra import ImgXtra, BaseXtra
from Drizzle.Xtra.FileIOXtra import FileIOXtra
from Drizzle.LingoScriptRuntime import LingoScriptRuntime
import math
import os
from multipledispatch import dispatch


class Global:
    def __init__(self, glob: LingoGlobal):
        self._global = glob

    def clearglobals(self):
        movieScript = self._global.MovieScriptInstance
        from Drizzle.MovieScript import MovieScript
        MovieScript.gLoadedName: ... = None
        MovieScript.INT_EXIT: str = None
        MovieScript.INT_EXRD: str = None
        MovieScript.DRInternalList: LingoList = None
        MovieScript.DRFirstTileCat: LingoNumber = None
        MovieScript.DRLastMatCat: LingoNumber = None
        MovieScript.RandomMetals_allowed: LingoList = None
        MovieScript.RandomMetals_grabTiles: LingoList = None
        MovieScript.ChaoticStone2_needed: LingoList = None
        MovieScript.DRRandomMetal_needed: LingoList = None
        MovieScript.SmallMachines_grabTiles: LingoList = None
        MovieScript.SmallMachines_forbidden: LingoList = None
        MovieScript.RandomMachines_forbidden: LingoList = None
        MovieScript.RandomMachines_grabTiles: LingoList = None
        MovieScript.RandomMachines2_forbidden: LingoList = None
        MovieScript.RandomMachines2_grabTiles: LingoList = None
        MovieScript.gLOprops: ... = None
        MovieScript.gCameraProps: ... = None
        MovieScript.gLightEProps: ... = None
        MovieScript.gLEProps: ... = None
        MovieScript.gEnvEditorProps: ... = None
        MovieScript.gLevel: ... = None
        MovieScript.gSkyColor: ... = None
        MovieScript.gTEprops: ... = None
        MovieScript.gLastImported: str = None
        MovieScript.tileSetIndex: LingoList = None
        MovieScript.gTiles: LingoList = None
        MovieScript.gTinySignsDrawn: LingoNumber = None
        MovieScript.gRenderCameraTilePos: LingoPoint = None
        MovieScript.gRenderCameraPixelPos: LingoPoint = None
        MovieScript.gRenderTrashProps: LingoList = None
        MovieScript.gMegaTrash: ... = None
        MovieScript.gDRMatFixes: LingoNumber = None
        MovieScript.gDRInvI: LingoNumber = None
        MovieScript.gRRSpreadsMore: LingoNumber = None
        MovieScript.gShortcuts: ... = None
        MovieScript.gEEprops: ... = None
        MovieScript.gAnyDecals: LingoNumber = None
        MovieScript.gTrashPropOptions: LingoList = None
        MovieScript.gProps: LingoList = None
        MovieScript.templeStoneCorners: ... = None
        MovieScript.DRLastMatImp: ... = None
        MovieScript.DRLastSlpImp: ... = None
        MovieScript.DRLastFlrImP: ... = None
        MovieScript.DRLastTexImp: ... = None
        MovieScript.DRCustomMatList: ... = None
        MovieScript.DRLastTL: ... = None
        MovieScript.r: LingoNumber = None
        MovieScript.solidMtrx: LingoList = None
        MovieScript.effectIn3D: LingoNumber = None
        MovieScript.gLASTDRAWWASFULLANDMINI: ... = None
        MovieScript.ropeModel: ... = None
        MovieScript.gCurrentRenderCamera: LingoNumber = None
        MovieScript.gPEprops: ... = None
        MovieScript.gSaveProps: LingoList = None
        MovieScript.newSize: ... = None
        MovieScript.extraBufferTiles: ... = None
        MovieScript.gEffects: LingoList = None
        MovieScript.lstSpace: ... = None
        MovieScript.gDirectionKeys: ... = None
        MovieScript.showControls: ... = None
        MovieScript.gEnvEditButtons: ... = None
        MovieScript.gLastEnvEditButtons: ... = None
        MovieScript.c: LingoNumber = None
        MovieScript.pal: ... = None
        MovieScript.pal2: ... = None
        MovieScript.gPalette: ... = None
        MovieScript.gEffectPaletteA: ... = None
        MovieScript.gEffectPaletteB: ... = None
        MovieScript.gFogColor: ... = None
        MovieScript.keepLooping: LingoNumber = None
        MovieScript.gCustomColor: ... = None
        MovieScript.dptsL: LingoList = None
        MovieScript.fogDptsL: LingoList = None
        MovieScript.gGradientImages: ... = None
        MovieScript.gDecalColors: LingoList = None
        MovieScript.levelName: ... = None
        MovieScript.gFullRender: ... = None
        MovieScript.gViewRender: LingoNumber = None
        MovieScript.gMassRenderL: ... = None
        MovieScript.gBlurOptions: ... = None
        MovieScript.gEditLizard: ... = None
        MovieScript.gPrioCam: ... = None
        MovieScript.snapToGrid: ... = None
        MovieScript.preciseSnap: ... = None
        MovieScript.stg: ... = None
        MovieScript.ps: ... = None
        MovieScript.lvlPropOutput: ... = None
        MovieScript.hideHelpClick: ... = None
        MovieScript.massRenderSelectL: ... = None
        MovieScript.gSEprops: ... = None
        MovieScript.geverysecond: ... = None
        MovieScript.firstFrame: ... = None
        MovieScript.glgtimgQuad: LingoList = None
        MovieScript.projects: ... = None
        MovieScript.ldPrps: ... = None
        MovieScript.gLOADPATH: ... = None
        MovieScript.TEdraw: ... = None
        MovieScript.gPEblink: ... = None
        MovieScript.gPEcounter: ... = None
        MovieScript.peScrollPos: ... = None
        MovieScript.peSavedRotat: ... = None
        MovieScript.peSavedFlip: ... = None
        MovieScript.peFreeQuad: ... = None
        MovieScript.peMousePos: ... = None
        MovieScript.lastPeMouse: ... = None
        MovieScript.mouseStill: ... = None
        MovieScript.propSettings: ... = None
        MovieScript.editSettingsProp: ... = None
        MovieScript.peSavedStretch: ... = None
        MovieScript.settingsPropType: ... = None
        MovieScript.gPEcolors: ... = None
        MovieScript.closestProp: LingoNumber = None
        MovieScript.longPropPlacePos: ... = None
        MovieScript.settingCursor: ... = None
        MovieScript.loadedPropPreviews: ... = None
        MovieScript.grimeActive: LingoNumber = None
        MovieScript.grimeOnGradients: LingoNumber = None
        MovieScript.bkgFix: LingoNumber = None
        MovieScript.vertRepeater: LingoNumber = None
        MovieScript.colr: LingoColor = None
        MovieScript.colrDetail: ... = None
        MovieScript.colrInd: ... = None
        MovieScript.gdLayer: str = None
        MovieScript.gdDetailLayer: ... = None
        MovieScript.gdIndLayer: ... = None
        MovieScript.gEffectProps: ... = None
        MovieScript.effectSeed: LingoNumber = None
        MovieScript.lrSup: ... = None
        MovieScript.chOp: ... = None
        MovieScript.fatOp: ... = None
        MovieScript.gradAf: ... = None
        MovieScript.gRotOp: ... = None
        MovieScript.slimeFxt: LingoNumber = None
        MovieScript.DRWhite: ... = None
        MovieScript.DRPxl: ... = None
        MovieScript.DRPxlRect: ... = None
        MovieScript.colrIntensity: ... = None
        MovieScript.fruitDensity: ... = None
        MovieScript.leafDensity: ... = None
        MovieScript.daddyCorruptionHoles: LingoList = None
        MovieScript.q: LingoNumber = None
        MovieScript.tm: LingoNumber = None
        MovieScript.pos: LingoPoint = None
        MovieScript.mvL: ... = None
        MovieScript.gLastImportedImage: LingoImage = None
        MovieScript.afterEffects: LingoNumber = None
        MovieScript.gCurrentlyRenderingTrash: LingoNumber = None
        MovieScript.gESoftProp: LingoNumber = None
        MovieScript.softProp: ... = None
        MovieScript.propsToRender: LingoList = None
        MovieScript.lG: ... = None
        MovieScript.wireBunchSav: LingoList = None
        MovieScript.firstCamRepeat: ... = None
        MovieScript.lightRects: ... = None
        MovieScript.gImgXtra: ... = None
        MovieScript.specialRectPoint: ... = None


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


class AppearanceOptions:
    def __init__(self):
        self.border = None


class Window:
    def __init__(self, glob: LingoGlobal):
        self.appearanceoptions = AppearanceOptions()
        self.resizable = LingoNumber()
        self.rect = LingoRect(LingoNumber(0))
        self.sizestate = LingoSymbol("normal")


class Movie:
    def __init__(self, glob: LingoGlobal):
        self._global = glob
        self.window = Window(glob)
        self.frame = 0
        self.lock = LingoNumber(0)
    @property
    def path(self):
        return self._global.the_moviePath

    @property
    def stage(self):
        raise NotImplementedError()

    @property
    def exitlock(self):
        return self.lock

    @exitlock.setter
    def exitlock(self, value):
        self.lock = value

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
        return LingoGlobal.StringLineCache.get(string, LingoGlobal.CacheStringLineData(string))

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
        return LingoNumber(len(cacheData.NewlineIndices) + 1)

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
    def lengthmember_helper(d): return LingoNumber(len(d))

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
    def concat(*items): return "".join([str(i) for i in items])

    @staticmethod
    def concat_space(*a): return " ".join([str(i) for i in a])

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

    def member(self, membernameornum, castnameornum=None):
        return self.LingoRuntime.GetCastMember(membernameornum, castnameornum)

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
        return LingoImage(w.IntValue, h.IntValue, ImageType[Type.Value])

    def string(self, value): return str(value)

    @staticmethod
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
    def op_eq_b(a, b):
        # some stuff i wouldn't care about
        if type(a) is not type(b):
            return False
        if isinstance(a, str) and isinstance(b, str):
            return a.lower() == b.lower()
        return a == b

    @staticmethod
    def op_eq(a, b) -> LingoNumber:
        return LingoNumber(1) if LingoGlobal.op_eq_b(a, b) else LingoNumber(0)

    @staticmethod
    def op_ne_b(a, b) -> bool:
        return not LingoGlobal.op_eq_b(a, b)

    @staticmethod
    def op_ne(a, b) -> LingoNumber:
        return LingoNumber(1) if LingoGlobal.op_eq_b(a, b) else LingoNumber(0)

    @staticmethod
    def op_lt(a, b): return LingoNumber(1) if a < b else LingoNumber(0)
    
    @staticmethod
    def op_le(a, b): return LingoNumber(1) if a >= b else LingoNumber(0)
    
    @staticmethod
    def op_gt(a, b): return LingoNumber(1) if a > b else LingoNumber(0)
    
    @staticmethod
    def op_ge(a, b): return LingoNumber(1) if a <= b else LingoNumber(0)

    @staticmethod
    def op_and(a, b):
        bA = LingoGlobal.ToBool(a)
        bB = LingoGlobal.ToBool(b)
        return LingoNumber(1) if bA and bB else LingoNumber(0)

    @staticmethod
    def op_or(a, b):
        bA = LingoGlobal.ToBool(a)
        bB = LingoGlobal.ToBool(b)
        return LingoNumber(1) if bA or bB else LingoNumber(0)

    @staticmethod
    def ToBool(a):
        if isinstance(a, LingoNumber):
            return a.DecimalValue != 0
        return a is not None

    @property
    def the_platform(self):
        return "win"  # does he not know

    def sprite(self, *args): return LingoSprite()
    
    def sound(self, *args): return NotImplementedError("Please god")

    def call(self, *args): return NotImplementedError("Help me finish this")

    def str(self, a): return str(a)

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
        elif obj is None:
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
