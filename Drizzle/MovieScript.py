from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Drizzle.LingoGlobal import LingoGlobal
from Drizzle.LingoScriptBase import LingoScriptBase
from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Data.LruCache import LruCache
from multipledispatch import dispatch


class MovieScript(LingoScriptBase):
    @dispatch(LingoGlobal)
    def Init(self, glob: LingoGlobal):
        super().Init(self, glob)

    def __init__(self):
        self._imageCache = LruCache(64)

    def cacheloadimage(self, fileName: str):
        return self._imageCache.Get(fileName, self, lambda state, fileName: state.CacheLoadImageLoad(fileName))

    def CacheLoadImageLoad(self, fileName: str):
        member = self._global.member("previewImprt")
        member.importfileinto(fileName)
        member.name = "previewImprt"
        return member.image


class MovieScriptExt:
    @staticmethod
    def MovieScript(runtime: LingoRuntime):
        return runtime.MovieScriptInstance
