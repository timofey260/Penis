from __future__ import annotations
from Drizzle.Xtra.BaseXtra import BaseXtra
from Drizzle.Data.LingoNumber import LingoNumber
from multipledispatch import dispatch
from io import TextIOWrapper
import os


class FileIOXtra(BaseXtra):
    def __init__(self):
        self._file: TextIOWrapper | None = None

    @dispatch(str)
    def openfile(self, filePath: str):
        self.openfile(filePath, LingoNumber(0))

    @dispatch(str, LingoNumber)
    def openfile(self, filePath: str, mode: LingoNumber):
        openmode = ["r+", "r", "a"][mode.IntValue]
        self._file = open(filePath, openmode)

    def Duplicate(self):
        return FileIOXtra()

    def readfile(self):
        if self._file is None:
            raise FileNotFoundError("nuh uh")
        return self._file.read()

    def createfile(self, path):
        with open(path, "w"):
            pass

    def closefile(self):
        self._file.close()
        self._file = None

    def delete(self):
        if self._file is None:
            raise FileNotFoundError("theres no fucking file")
        name = self._file.name
        self._file.close()
        os.remove(name)

    def writestr(self, text: str):
        if self._file is None:
            raise FileNotFoundError("theres no fucking file")
        self._file.write(text)

    def writereturn(self, type):
        if self._file is None:
            raise FileNotFoundError("theres no fucking file")
        self._file.write("\r\n")
