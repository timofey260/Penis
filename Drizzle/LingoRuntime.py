from __future__ import annotations
from Drizzle.LingoGlobal import LingoGlobal
from Drizzle.Data.Stopwatch import Stopwatch
from multipledispatch import dispatch


class RngState:
    def __init__(self):
        self.Seed = 0
        self.Init = 0


class LingoRuntime:
    def __init__(self):
        self.Stopwatch = Stopwatch()
        self.KeysDown: set[int] = set()
        self.Global = LingoGlobal(self)
        self._rngState = RngState()
        self.RngSeed = 0

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
