from multipledispatch import dispatch


class LingoPropertyList:
    @dispatch()
    def __init__(self, count):
        self.Dict = {}

    @dispatch(dict)
    def __init__(self, d: dict):
        self.Dict = d
