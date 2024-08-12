from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from LingoGlobal import LingoGlobal
# idk what this is but i hope not something important


class LingoScriptRuntime:
    def __init__(self, glob: LingoGlobal):
        self.Global = glob
        self._getMemberBinders = {}
        self._binaryOperationBinders = {}

    def GetGetMemberBinder(self, memberName: str):
        value = self._getMemberBinders.get(memberName, None)
        if value is not None:
            self._getMemberBinders[memberName] = value = None

        return value

    def GetBinaryOperationBinder(self, Type):
        value = self._binaryOperationBinders.get(Type, None)
        if value is not None:
            self._binaryOperationBinders[Type] = value = None
        return value