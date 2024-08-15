from Drizzle.LingoRuntime import LingoRuntime
from Drizzle.Data.Assembly import Assembly
from Drizzle.Misc.EditorRuntimeHelpers import EditorRuntimeHelpers


if __name__ == '__main__':
    asm = Assembly()
    runtime = LingoRuntime(asm)
    runtime.Init()
    EditorRuntimeHelpers.RunStartup(runtime)
    filename = ""
    # EditorRuntimeHelpers.RunLoadLevel(runtime, filename)

