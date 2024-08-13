from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Data.LingoNumber import LingoNumber
import os


class EditorRuntimeHelpers:
    @staticmethod
    def RunStartup(runtime: LingoRuntime):
        startup = runtime.CreateScript("startUp")
        startup.exitframe()

    @staticmethod
    def RunLoadLevel(runtime: LingoRuntime, filePath: str):
        withoutExt = os.path.split(filePath)
        runtime.CreateScript("loadLevel").loadlevel(withoutExt, LingoNumber(1))

    # something that we don't need
