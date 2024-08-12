from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Drizzle.LingoGlobal import LingoGlobal


class LingoScriptRuntimeBase(ABC):
    @abstractmethod
    def Init(self, movieScript, glob: LingoGlobal):
        pass
