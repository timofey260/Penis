from __future__ import annotations
import time


class Stopwatch:
    def __init__(self):
        self.time: float = 0

    def Start(self):
        self.time = time.time()

    @property
    def ElapsedMilliseconds(self):
        return time.time() - self.time

    @property
    def Elapsed(self):
        return time.ctime(self.ElapsedMilliseconds)

    @staticmethod
    def StartNew():
        n = Stopwatch()
        n.Start()
        return n
