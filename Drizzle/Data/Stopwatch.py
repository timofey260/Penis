import time


class Stopwatch:
    def __init__(self):
        self.time: float = 0

    def Start(self):
        self.time = time.time()

    @property
    def ElapsedMilliseconds(self):
        return time.time() - self.time
