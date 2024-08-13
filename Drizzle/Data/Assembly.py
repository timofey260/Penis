import os
import re

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Translated")


class Assembly:
    def GetTypes(self) -> list[type]:
        files = os.listdir(path)
        types = []
        for file in files:
            name = re.match(r"((Behavior_|Parent_)(\w+))\.py", file)
            if file == "__pycache__":
                continue
            exec(f"from Drizzle.Translated.{name.group(1)} import {name.group(3)}")
            exec(f"types.append({name.group(3)})")
        from Drizzle.MovieScript import MovieScript
        types.append(MovieScript)
        return types


if __name__ == '__main__':
    asm = Assembly()
    print(asm.GetTypes())
