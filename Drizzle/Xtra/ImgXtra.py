from Drizzle.Xtra.BaseXtra import BaseXtra
from Drizzle.Data.LingoPropertyList import LingoPropertyList


class ImgXtra(BaseXtra):
    def Duplicate(self):
        return ImgXtra()

    def ix_saveimage(self, props: LingoPropertyList) -> int:
        img = props["image"]
        filename = props["filename"]
        img.SaveAsPng(filename)
        return 1
