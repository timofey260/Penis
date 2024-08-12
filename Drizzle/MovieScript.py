from Drizzle.LingoGlobal import LingoGlobal
from Drizzle.LingoScriptBase import LingoScriptBase
from Drizzle.LingoRuntime import LingoRuntime
from multipledispatch import dispatch


class MovieScript(LingoScriptBase):
    @dispatch(LingoGlobal)
    def Init(self, glob: LingoGlobal):
        super().Init(self, glob)


class MovieScriptExt:
    @staticmethod
    def MovieScript(runtime: LingoRuntime):
        return runtime.MovieScriptInstance
