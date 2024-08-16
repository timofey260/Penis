from Drizzle.Data.LingoNumber import LingoNumber
from Drizzle.Data.LingoList import LingoList
from Drizzle.Data.LingoColor import LingoColor
from Drizzle.Data.LingoPoint import LingoPoint
from Drizzle.Data.LingoPropertyList import LingoPropertyList
from Drizzle.Data.LingoRect import LingoRect
from Drizzle.Data.LingoSymbol import LingoSymbol
from enum import Enum, auto

class ParsedKeywords(Enum):
    ListStart = auto()
    PropListStart = auto()
    ListEnd = auto()


class Parser:
    @staticmethod
    def Lexer(text: str):
        # lexer shit
        indent = []
        isstr = False
        isprop = False
        isnum = False
        count = -1
        lastchars = ""
        while count + 1 < len(text):
            count += 1
            char = text[count]
            if isstr:
                if char != "\"":
                    lastchars += char
                    continue
                indent.append(lastchars)
                isstr = False
                lastchars = ""
                continue
            elif isprop:
                if char != ":":
                    lastchars += char
                    continue
                indent.append(lastchars)
                isprop = False
                lastchars = ""
                continue
            elif isnum:
                if char in "-1234567890.":
                    lastchars += char
                    continue
                isfloat = "." in lastchars
                indent.append(LingoNumber(float(lastchars) if isfloat else int(lastchars)))
                isnum = False
                lastchars = ""

            if char == "[":
                if text[count + 1] == "#":
                    indent.append(ParsedKeywords.PropListStart)
                    continue
                indent.append(ParsedKeywords.ListStart)
            elif char == " " or char == ",":
                pass
            elif char == "]":
                indent.append(ParsedKeywords.ListEnd)
            elif char == "#":
                isprop = True
            elif char == "\"":
                isstr = True
            elif char in "-1234567890.":
                isnum = True
                lastchars += char
            elif text[count:count+5].lower() == "color":
                count += 6
                items, newcount = Parser.LexerSubLoop(text[count:])
                count += newcount
                indent.append(LingoColor(*items))
            elif text[count:count+5].lower() == "point":
                count += 6
                items, newcount = Parser.LexerSubLoop(text[count:])
                count += newcount
                indent.append(LingoPoint(*items))
            elif text[count:count+4].lower() == "rect":
                count += 5
                items, newcount = Parser.LexerSubLoop(text[count:])
                count += newcount
                indent.append(LingoRect(*items))
        return indent

    @staticmethod
    def LexerSubLoop(text):
        count = -1
        items = []
        isnum = False
        lastchars = ""
        while count + 1 < len(text):
            count += 1
            char = text[count]
            if isnum:
                if char in "-1234567890.":
                    lastchars += char
                    continue
                isfloat = "." in lastchars
                items.append(LingoNumber(float(lastchars) if isfloat else int(lastchars)))
                isnum = False
                lastchars = ""
            if char in "-1234567890.":
                isnum = True
                lastchars += char
            elif char == ")":
                count += 1
                break
        return items, count

    @staticmethod
    def ParseLexedList(parsed: list):
        elementslist = []
        i = -1
        while i + 1 < len(parsed):
            i += 1
            item = parsed[i]
            if not isinstance(item, Enum):
                elementslist.append(item)
                continue
            elif item == ParsedKeywords.ListStart:
                item, offset = Parser.ParseLexedList(parsed[i+1:])
                i += offset
                elementslist.append(item)
                continue
            elif item == ParsedKeywords.PropListStart:
                item, offset = Parser.ParseLexedPropList(parsed[i+1:])
                i += offset
                elementslist.append(item)
                continue
            elif item == ParsedKeywords.ListEnd:
                break
        return LingoList(*elementslist), i + 1

    @staticmethod
    def ParseLexedPropList(parsed: list):
        elementslist = []
        i = -1
        iskey = True
        while i + 1 < len(parsed):
            i += 1
            item = parsed[i]
            if not isinstance(item, Enum):
                if iskey:
                    iskey = False
                    elementslist.append(LingoSymbol(item))
                    continue
                else:
                    iskey = True
                elementslist.append(item)
                continue
            elif item == ParsedKeywords.ListStart:
                item, offset = Parser.ParseLexedList(parsed[i + 1:])
                i += offset
                elementslist.append(item)
                iskey = True
                continue
            elif item == ParsedKeywords.PropListStart:
                item, offset = Parser.ParseLexedPropList(parsed[i + 1:])
                i += offset
                elementslist.append(item)
                iskey = True
                continue
            elif item == ParsedKeywords.ListEnd:
                break
        return LingoPropertyList(*elementslist), i + 1

    @staticmethod
    def Parse(text: str):
        newtext = Parser.Lexer(text)
        if newtext[0] == ParsedKeywords.PropListStart:
            return Parser.ParseLexedPropList(newtext[1:])[0]
        elif newtext[0] == ParsedKeywords.ListStart:
            return Parser.ParseLexedList(newtext[1:])[0]
        else:
            return newtext[0]


