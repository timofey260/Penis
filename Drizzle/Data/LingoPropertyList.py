from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoList import LingoList
from multipledispatch import dispatch


class LingoPropertyList:
    def __init__(self, *args):
        if len(args) == 1:
            self.Dict = {}
            return
        self.Dict = {k: v for k, v in zip(args[0::2], args[1::2])}

    def __len__(self):
        return len(self.Dict)

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
        return "[" + ", ".join([f"{k}: {v}" for k, v in self.Dict.items()]) + "]"
