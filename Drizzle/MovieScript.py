from Drizzle.LingoGlobal import LingoGlobal
from Drizzle.LingoScriptBase import LingoScriptBase
from multipledispatch import dispatch


class MovieScript(LingoScriptBase):
    @dispatch(LingoGlobal)
    def Init(self, glob: LingoGlobal):
        super().Init(self, glob)
