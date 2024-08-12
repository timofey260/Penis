from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Cast.CastMember import CastMember
from Drizzle.Data.LingoNumber import LingoNumber
from multipledispatch import dispatch
from typing import Any


class LingoCastLib:
    def __init__(self, runtime: LingoRuntime, name: str, offset: int):
        self.name = name
        self._runtime = runtime
        self.Offset = offset
        self._cast: list[CastMember] = []
        self._nameIndexDirty = False
        self._names: dict[str, int] = {}
        for i in range(0, 1000):
            self._cast.append(CastMember(runtime, self, i + 1 + offset, name))
            
    @property
    def NumMembers(self):
        return len(self._cast)

    @property
    def member(self):
        raise NotImplementedError("damn")

    @dispatch(Any)
    def GetMember(self, nameOrNum):
        if isinstance(nameOrNum, str):
            if self._nameIndexDirty:
                self.UpdateNameIndex()

            if self._names.get(nameOrNum, False):
                return self._cast[self._names.get(nameOrNum)]
        if isinstance(nameOrNum, int):
            numMember = self.GetMember(int(nameOrNum))
            if numMember is not None:
                return numMember
        if isinstance(nameOrNum, LingoNumber):
            numMember = self.GetMember(nameOrNum.IntValue)
            if numMember is not None:
                return numMember
        return None

    @dispatch(int)
    def GetMember(self, num: int):
        if 0 < num <= len(self._cast):
            return self._cast[num - 1]
        idx = num - self.Offset
        if 0 < idx < len(self._cast):
            return self._cast[idx - 1]
        return None

    def NameIndexDirty(self):
        self._nameIndexDirty = True
        self._runtime.NameIndexDirty()

    def UpdateNameIndex(self):
        self._names.clear()

        for i in range(len(self._cast)):
            member = self._cast[i]
            if member.name is not None:
                self._names[member.name] = i

        self._nameIndexDirty = False
