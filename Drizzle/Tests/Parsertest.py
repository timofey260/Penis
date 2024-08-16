import unittest
from Drizzle.Misc.Parser import Parser


class ParserTest(unittest.TestCase):
    def test_something(self):
        print(Parser.Parse("[[[0, [1]], [0, [1]]], [#tiles: point(10, 15), #props: point(14, -10), #colors: color(10, 10, 10)]]").__str__())
        print(Parser.Parse("[0, 1, color(1, 2, 3), [10, 15, 20], [2, 3, 4]").__str__())
        # print(Parser.LexerSubLoop("(0, 1, 2, 3)"))
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
