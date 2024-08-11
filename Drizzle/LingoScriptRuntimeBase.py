from abc import ABC, abstractmethod
from Drizzle.LingoGlobal import LingoGlobal


class LingoScriptRuntimeBase(ABC):
    @abstractmethod
    def Init(self, movieScript, glob: LingoGlobal):
        pass
