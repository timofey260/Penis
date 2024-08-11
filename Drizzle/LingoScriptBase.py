from Drizzle.LingoScriptRuntimeBase import LingoScriptRuntimeBase
from Drizzle.MovieScript import MovieScript
from Drizzle.LingoGlobal import LingoGlobal
from multipledispatch import dispatch
from typing import Any


class LingoScriptBase(LingoScriptRuntimeBase):
    def __init__(self):
        self._movieScript: MovieScript | None = None
        self._global: LingoGlobal | None = None

    @dispatch(Any, LingoGlobal)
    def Init(self, movieScript: MovieScript, glob: LingoGlobal):
        self._movieScript = movieScript
        self._global = glob
