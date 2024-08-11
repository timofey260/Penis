from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoList import LingoList
from multipledispatch import dispatch


class LingoPropertyList:
    @dispatch()
    def __init__(self, count):
        self.Dict = {}

    @dispatch(dict)
    def __init__(self, d: dict):
        self.Dict = d

    def __getitem__(self, item):
        # if isinstance(item, LingoNumber):
        #     item = item.IntValue
        return self.Dict[item]

    def __setitem__(self, key, value):
        self.Dict[key] = value

    def duplicate(self): return LingoPropertyList({k: v for k, v in self.Dict.items() if LingoList.DuplicateIfList(v)})

    def addprop(self, key, value):
        self.__setitem__(key, value)

    def findpos(self, value):
        return self.Dict[value] if value in self.Dict.keys() else None

    def __str__(self):
        return print([f"{k}: {v}" for k, v in self.Dict.items()])
