from __future__ import annotations
import os.path
import re
from Drizzle.LingoParentScript import LingoParentScript
from Drizzle.LingoBehaviorScript import LingoBehaviorScript
from Drizzle.LingoScriptRuntimeBase import LingoScriptRuntimeBase
from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.LingoCastLib import LingoCastLib
from Drizzle.Cast.CastMember import CastMember, CastMemberType
from Drizzle.LingoGlobal import LingoGlobal
from Drizzle.Data.Stopwatch import Stopwatch
from Drizzle.Data.LingoList import LingoList
from multipledispatch import dispatch
from Drizzle.Data.Stopwatch import Stopwatch
from Drizzle.Data.Assembly import Assembly
from copy import deepcopy

AssemblyLocation = os.path.dirname(os.path.dirname(__file__))


class RngState:
    def __init__(self):
        self.Seed = 0
        self.Init = 0


class LingoRuntime:
    @dispatch(Assembly)
    def __init__(self, assembly: Assembly):
        self._assembly = assembly
        self.Global = LingoGlobal(self)
        self.__init__()

    @dispatch()
    def __init__(self):
        from Drizzle.MovieScript import MovieScript
        path = os.path.join(AssemblyLocation, "Data")
        self.MovieBasePath = path
        self.CastPath = os.path.join(self.MovieBasePath, "Cast")

        self.Stopwatch = Stopwatch()
        self.KeysDown: set[int] = set()
        self._rngState = RngState()
        self.RngSeed = 0
        self.MovieBasePath = ""
        self.MovieScriptInstance: MovieScript | None = None
        self._behaviorScripts: dict[str, type] = {}
        self._parentScripts: dict[str, type] = {}

        self._castLibNames: dict[str, LingoCastLib] = {}
        self._castLibs: list[LingoCastLib] = []  # 8
        self._castMemberNameIndex: dict[str, CastMember] = {}
        self._castMemberNameIndexDirty = False

    @dispatch(str)
    def GetCastLib(self, castName: str):
        return self._castLibNames[castName]

    def GetCastMember(self, nameOrNum, cast=None):
        if isinstance(nameOrNum, str):
            found = self.GetCastMemberAnyCast(nameOrNum)

            if found is None:
                print("failed to find the thing")

            return found
        if isinstance(cast, str):
            found = self._castLibNames[cast].GetMember(nameOrNum)
        elif isinstance(cast, int):
            found = self._castLibs[cast - 1].GetMember(nameOrNum)
        elif isinstance(cast, LingoNumber):
            found = self._castLibs[cast.IntValue - 1].GetMember(nameOrNum)
        elif cast is None:
            found = self.GetCastMemberAnyCast(nameOrNum)
        else:
            raise AttributeError("Invalid")

        if found is None:
            print("failed to find the thing")

        return found

    def GetCastMemberAnyCast(self, nameOrNum):
        if isinstance(nameOrNum, str):
            if self._castMemberNameIndexDirty:
                self.UpdateMemberNameIndex()

            mem = self._castMemberNameIndex.get(nameOrNum)
            if mem is not None:
                return mem

        for castLib in self._castLibs:
            mem = castLib.GetMember(nameOrNum)
            if mem is not None:
                return mem

        return None

    def LoadCast(self):
        count = 0
        def DoWork(s: str):
            nonlocal count
            member = self.LoadSingleCastMember(s)
            if member is not None:
                # self.InterLocked.Increment(count)
                count += 1
                # todo
        print("loading Cast")

        self.InitCastLibs()
        sw = Stopwatch.StartNew()

        files = os.listdir(self.CastPath)

        if self.LoadCastParallel() and False:
            pass
        else:
            for s in files:
                DoWork(s)  # todo

        print(f"Loaded {count} cast members in {sw.Elapsed}")

        self.GetCastMember("pxl").image.IsPxl = True

    def InitCastLibs(self):
        i = 0
        def InitLib(name: str, offset: int):
            nonlocal i
            castLib = LingoCastLib(self, name, offset)
            self._castLibNames[name] = castLib
            self._castLibs.append(castLib)
            i += 1
        InitLib("Internal", 0)
        InitLib("customMems", 131072)
        InitLib("soundCast", 196608)
        InitLib("levelEditor", 262144)
        InitLib("exportBitmaps", 327689)
        InitLib("Drought", 393216)
        InitLib("Dry Editor", 458752)
        InitLib("MSC", 524288)

    def LoadSingleCastMember(self, file: str):
        _, fileName = os.path.split(file)
        match = re.match(self.CastPathRegex(), fileName)
        if match is None:
            print(f"Unable to parse {fileName}")
            return None

        cast = match.group(1)
        number = int(match.group(2))
        ext = match.group(4)
        name: str = None

        if match.group(3) != "":
            name = match.group(3)

        member = self.GetCastMember(number, cast)
        member.ImportFile(file, ext, name)

        if member.Type == CastMemberType.Empty:
            print(f"Warning: unrecognized cast member type {file}")

        return member

    def UpdateMemberNameIndex(self):
        self._castMemberNameIndex.clear()

        for castLib in self._castLibs:
            for i in range(castLib.NumMembers):
                member = castLib.GetMember(i)
                if member is None or member.name is None:
                    continue

                if not member.name in list(self._castMemberNameIndex.keys()):
                    self._castMemberNameIndex[member.name] = member

        self._castMemberNameIndexDirty = False

    def NameIndexDirty(self):
        self._castMemberNameIndexDirty = True

    @staticmethod
    def InitRng(state: RngState):
        state.Seed = 1
        state.Init = 0xA3000000

    @staticmethod
    def RandomDerive(param: int):
        var1 = int((param << 0xd ^ param) - int(param >> 0x15))
        var2 = ((var1 * var1 * 0x3d73 + 0xc0ae5) * var1 + 0xd208dd0d & 0x7fffffff) + var1
        return int((var2 * 0x2000 ^ var2) - int(var2 >> 0x15))

    @dispatch(int)
    def Random(self, clamp: int):
        return self.Random(self._rngState, clamp)

    @staticmethod
    @dispatch(RngState, int)
    def Random(state: RngState, clamp: int):
        if state.Seed == 0:
            LingoRuntime.InitRng(state)

        if (state.Seed & 1) == 0:
            state.Seed = int(state.Seed >> 1)
        else:
            state.Seed = int(state.Seed >> 1 ^ state.Init)

        var1 = LingoRuntime.RandomDerive(int(state.Seed * 0x47))

        if clamp > 0:
            var1 = int((var1 & 0x7FFFFFFF) % clamp)

        return var1 + 1

    @property
    def RngSeed(self) -> int:
        return self._rngState.Seed

    @RngSeed.setter
    def RngSeed(self, value: int):
        self.InitRng(self._rngState)
        self._rngState.Seed = value

    @staticmethod
    def LoadCastParallel():
        return True

    @staticmethod
    def CastPathRegex():
        return r"([^_]+)_(\d+)_(.+)?\.([a-z]*)"

    def Init(self):
        print("May pebbles help me if this code wouldn't run")
        self.InitNoCast()
        self.LoadCast()

    def InitNoCast(self):
        self.Stopwatch.Start()
        self.Global.Init()
        self.InitScript()

    def InitScript(self):
        from Drizzle.MovieScript import MovieScript
        movieScriptType: type = None
        parentScripts: list[type] = []
        behaviorScripts: list[type] = []

        for tp in self._assembly.GetTypes():
            tp: type
            if tp == MovieScript:
                movieScriptType = tp
            if tp.__base__ == LingoParentScript:
                parentScripts.append(type)
            if tp.__base__ == LingoBehaviorScript:
                behaviorScripts.append(tp)

        if movieScriptType is None:
            print("No Movie Script")
            raise Exception(":(")

        self.MovieScriptInstance: MovieScript = movieScriptType()
        self.MovieScriptInstance.Init(self.Global)

        for scriptType in behaviorScripts:
            self._behaviorScripts[scriptType.__name__] = scriptType

        for scriptType in parentScripts:
            self._behaviorScripts[scriptType.__name__] = scriptType

        print(f"Instantiated movie script {movieScriptType}")
        print(f"found {len(parentScripts)} parent and {len(behaviorScripts)} behavior scripts")

    def InstantiateBehaviorScript(self, name: str):
        return self.InstantiateScriptType(self._behaviorScripts[name])

    def InstantiateParentScript(self, name: str):
        return self.InstantiateScriptType(self._parentScripts[name])

    def InstantiateScriptType(self, Type: type):
        instance: LingoScriptRuntimeBase = Type()
        instance.Init(self.MovieScriptInstance, self.Global)
        return instance

    @dispatch(str, LingoList)
    def CreateScript(self, Type: str, l: LingoList = LingoList()):
        scriptType = self._parentScripts.get(Type, None)
        if scriptType is None:
            scriptType = self._behaviorScripts.get(Type, None)
            if scriptType is None:
                raise AttributeError("bullshit")

        instance = self.InstantiateScriptType(scriptType)
        # newMethod = instance.new()
        return instance

    @dispatch(type, LingoList)
    def CreateScript(self, Type: type, l: LingoList = LingoList()):
        instance = self.InstantiateScriptType(Type)
        # newMethod = instance.new()
        return instance

    def GetFilePath(self, relPath: str):
        fullPath = os.path.join(self.MovieBasePath, relPath)
        if os.path.exists(fullPath):
            return fullPath

        dir = os.path.dirname(fullPath)  # todo
        if dir == "" or not os.path.exists(dir):
            return fullPath

        _, origFileName = os.path.split(fullPath)
        for dirFile in os.listdir(dir):
            if dirFile.lower() == origFileName:
                return os.path.join(dir, dirFile)

        return fullPath

    def Clone(self):
        print("Cloning Runtime")
        newRuntime = LingoRuntime(self._assembly)
        newRuntime.InitNoCast()
        self.CloneCast(self, newRuntime)
        self.CloneGlobals(self, newRuntime)

        return newRuntime

    def CloneCast(self, src: LingoRuntime, dst: LingoRuntime):
        print("Cloning Cast")
        dst.InitCastLibs()
        dst._castMemberNameIndexDirty = True

        for srcLib, dstLib in zip(src._castLibs, dst._castLibs):

            for j in range(srcLib.NumMembers):
                srcMem = srcLib.GetMember(j)
                dstMem = dstLib.GetMember(j)
                if srcMem is None or dstMem is None:
                    continue
                dstMem.CloneFrom(srcMem)

    def CloneGlobals(self, src: LingoRuntime, dst: LingoRuntime):
        print("cloning Globals")
        srcMovieScript = src.MovieScriptInstance
        dstMovieScript = dst.MovieScriptInstance
        dstMovieScript._global = deepcopy(srcMovieScript._global)

    def DeepClone(self):
        raise NotImplementedError("welp")
