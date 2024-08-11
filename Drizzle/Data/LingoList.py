from __future__ import annotations
from Drizzle.Data.LingoNumber import LingoNumber
from multipledispatch import dispatch
from typing import Any

class LingoList:

    @dispatch()
    def __init__(self):
        self.List = []

    @dispatch(int)
    def __init__(self, capacity: int):
        self.List = []

    @dispatch(list)
    def __init__(self, items: list):
        self.List = items

    def __len__(self):
        return len(self.List)

    def __getitem__(self, item):
        return self.List[int(item)]

    def __setitem__(self, key, value):
        self.List[int(key)] = value

    def getpos(self, value):
        return self.List.index(value)

    def findpos(self):
        return None

    def add(self, value):
        self.List.append(value)

    def Add(self, value):
        self.List.append(value)

    def append(self, value):
        self.List.append(value)

    @dispatch(int)
    def deleteat(self, index: int):
        try:
            self.List.pop(index)
        except:
            print("Fuckyoy")

    @dispatch(LingoNumber)
    def deleteat(self, index: LingoNumber): self.deleteat(index.IntValue)

    @dispatch(int, Any)
    def addat(self, number: int, value): self.List.insert(number - 1, value)

    @dispatch(LingoNumber, Any)
    def addat(self, number: LingoNumber, value): self.addat(number.IntValue, value)

    def deleteone(self, value): self.List.remove(value)

    def duplicate(self): return LingoList(list(map(lambda x: LingoList.DuplicateIfList(x), self.List)))

    def sort(self): self.List.sort(key=self.compare)

    @staticmethod
    def DuplicateIfList(obj): return obj.duplicate() if isinstance(obj, LingoList) else obj

    def __add__(self, other):
        if isinstance(other, LingoList):
            return LingoList(list(map(lambda x, y: x + y, self.List, other.List)))
        self.List = list(map(lambda x: x + other, self.List))

    def __sub__(self, other):
        if isinstance(other, LingoList):
            return LingoList(list(map(lambda x, y: x - y, self.List, other.List)))
        self.List = list(map(lambda x: x - other, self.List))

    def __mul__(self, other):
        if isinstance(other, LingoList):
            return LingoList(list(map(lambda x, y: x * y, self.List, other.List)))
        self.List = list(map(lambda x: x * other, self.List))

    def __truediv__(self, other):
        if isinstance(other, LingoList):
            return LingoList(list(map(lambda x, y: x / y, self.List, other.List)))
        self.List = list(map(lambda x: x / other, self.List))

    def __eq__(self, other):
        return self.List == other.List

    def __ne__(self, other):
        return self.List != other.List

    def __str__(self):
        return print(self.List)

    def compare(self, x):
        if isinstance(x, LingoNumber):
            return x.DecimalValue
        return x

