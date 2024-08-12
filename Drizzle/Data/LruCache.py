from typing import Any, Callable
from dataclasses import dataclass
from multipledispatch import dispatch


@dataclass
class CacheEntry:
    Value: Any
    Key: Any
    Fresher: int
    Drier: int
    Valid: bool


class LruCache:
    def __init__(self, size: int):
        self._cacheEntries: dict[Any, int] = {}
        self._cache: list[CacheEntry | None] = [None for _ in range(size)]
        self._freshest: int = 0
        self._driest: int = 0

        self.Clear()

    @dispatch(Any, Callable)
    def Get(self, key, load):
        return self.Get(key, load, lambda func, key: func(key))

    @dispatch(Any, Any, Callable)
    def Get(self, key, state, load: Callable):
        CacheIdx = self._cacheEntries.get(key)
        if CacheIdx is not None:
            cacheEntry = self._cache[CacheIdx]
            if CacheIdx != self._freshest:
                if cacheEntry.Drier != -1:
                    self._cache[cacheEntry.Drier].Fresher = cacheEntry.Fresher
                if CacheIdx == self._driest:
                    self._driest = cacheEntry.Fresher

                self._cache[cacheEntry.Fresher].Drier = cacheEntry.Drier
                self._cache[self._freshest].Fresher = CacheIdx
                cacheEntry.Drier = self._freshest
                self._freshest = CacheIdx
                cacheEntry.Fresher = -1
            return cacheEntry.Value

        value = load(state, key)

        newIdx = self._driest

        newEntry = self._cache[newIdx]
        if newEntry is not None and newEntry.Valid:
            del self._cacheEntries[key]
            self._cache[newEntry.Fresher].Drier = -1

        self._driest = newEntry.Fresher
        self._cache[self._driest].Drier = -1

        self._cacheEntries[key] = newIdx
        newEntry.Fresher = -1
        newEntry.Drier = self._freshest
        newEntry.Value = value
        newEntry.Key = key
        newEntry.Valid = True

        self._cache[self._freshest].Fresher = newIdx
        self._freshest = newIdx
        return value

    def Clear(self):
        self._cacheEntries.clear()

        self._freshest = len(self._cache) - 1
        self._driest = 0

        for i in range(len(self._cache)):
            self._cache[i] = CacheEntry("", "", i + 1, i - 1, False)
