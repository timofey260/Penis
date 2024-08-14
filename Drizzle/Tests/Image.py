import unittest
from Drizzle.Data.LingoImage import ImageType, LingoColor, LingoImage, LingoRect, LingoPoint, LingoNumber, LingoList, LingoPropertyList


class ImageTest(unittest.TestCase):
    def test_something(self):
        img = LingoImage(20, 20, 33)
        img2 = LingoImage(100, 100, 33)
        img.fill(LingoColor(255, 255, 255))
        img.setpixel(0, 0, LingoColor(255, 255, 0))
        img.setpixel(2, 2, LingoColor(255, 255, 0))
        self.assertEqual(img.getpixel(0, 0), LingoColor(255, 255, 0))
        self.assertEqual(img.getpixel(0, 1), LingoColor(255, 255, 255))
        img2.fill(LingoColor(0, 255, 0))
        img2.copypixels(img, LingoList(LingoPoint(0, 0), LingoPoint(2, 0), LingoPoint(2, 2), LingoPoint(0, 2)),
                        LingoRect(LingoNumber(0), LingoNumber(0), img.width, img.height), LingoPropertyList())
        img.SaveAsPng("shit.png")
        img2.SaveAsPng("shit2.png")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
