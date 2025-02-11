from __future__ import annotations
import math
import sys


class LingoNumber:
    def __init__(self, value: int | float | None=None):
        if value is None:
            value = 0
        self.IsDecimal = isinstance(value, float)
        self._intValue = 0 if self.IsDecimal else value
        self._decimalValue = 0 if not self.IsDecimal else value

    @property
    def DecimalValue(self) -> float:
        return self._decimalValue if self.IsDecimal else self._intValue

    @property
    def IntValue(self) -> int:
        return round(self._decimalValue) if self.IsDecimal else self._intValue

    @property
    def integer(self):
        return LingoNumber(self.IntValue)

    @property
    def float(self):
        return LingoNumber(self.DecimalValue)


    def findpos(self, val):
        return -sys.maxsize * 2 - 1

    @staticmethod
    def Parse(text: str) -> LingoNumber:
        try:
            return LingoNumber(float(text))
        except:
            return LingoNumber()

    @staticmethod
    def Abs(number: LingoNumber):
        if number.IsDecimal:
            return LingoNumber(abs(number._decimalValue))
        return LingoNumber(abs(number._intValue))

    @staticmethod
    def Sqrt(dec: LingoNumber):
        return LingoNumber(math.sqrt(dec.DecimalValue))

    @staticmethod
    def Cos(dec: LingoNumber) -> LingoNumber:
        return LingoNumber(math.cos(dec.DecimalValue))

    @staticmethod
    def Sin(dec: LingoNumber) -> LingoNumber:
        return LingoNumber(math.sin(dec.DecimalValue))

    @staticmethod
    def Tan(dec: LingoNumber) -> LingoNumber:
        return LingoNumber(math.tan(dec.DecimalValue))

    @staticmethod
    def Atan(dec: LingoNumber) -> LingoNumber:
        return LingoNumber(math.atan(dec.DecimalValue))

    @staticmethod
    def Pow(base: LingoNumber, exp: LingoNumber) -> LingoNumber:
        return LingoNumber(math.pow(base.DecimalValue, exp.DecimalValue))

    def __str__(self) -> str:
        return str(self.DecimalValue) if self.IsDecimal else str(self.IntValue)

    def __neg__(self) -> LingoNumber:
        return LingoNumber(-self.DecimalValue if self.IsDecimal else -self.IntValue)

    def __pos__(self) -> LingoNumber:
        return LingoNumber(+self.DecimalValue if self.IsDecimal else +self.IntValue)

    def __add__(self, other: LingoNumber) -> LingoNumber:
        return LingoNumber((self.DecimalValue + other.DecimalValue) if self.IsDecimal and other.IsDecimal else (self.IntValue + other.IntValue))

    def __sub__(self, other: LingoNumber) -> LingoNumber:
        return LingoNumber((self.DecimalValue - other.DecimalValue) if self.IsDecimal and other.IsDecimal else (self.IntValue - other.IntValue))

    def __mul__(self, other: LingoNumber) -> LingoNumber:
        return LingoNumber((self.DecimalValue * other.DecimalValue) if self.IsDecimal and other.IsDecimal else (self.IntValue * other.IntValue))

    def __truediv__(self, other: LingoNumber) -> LingoNumber:
        return LingoNumber((self.DecimalValue / other.DecimalValue) if self.IsDecimal and other.IsDecimal else (self.IntValue / other.IntValue))

    def __mod__(self, other: LingoNumber) -> LingoNumber:
        return LingoNumber((self.DecimalValue % other.DecimalValue) if self.IsDecimal and other.IsDecimal else (self.IntValue % other.IntValue))

    def __int__(self) -> int:
        return self.IntValue

    def __float__(self) -> float:
        return self.DecimalValue

    def __eq__(self, other: LingoNumber) -> bool:
        return self.DecimalValue == other.DecimalValue

    def __ne__(self, other: LingoNumber) -> bool:
        return self.DecimalValue != other.DecimalValue

    def __hash__(self):
        return self.DecimalValue.__hash__()

    def __ge__(self, other: LingoNumber) -> bool:
        return self.DecimalValue >= other.DecimalValue

    def __lt__(self, other: LingoNumber) -> bool:
        return self.DecimalValue < other.DecimalValue

    def __gt__(self, other: LingoNumber) -> bool:
        return self.DecimalValue > other.DecimalValue

    def __le__(self, other: LingoNumber) -> bool:
        return self.DecimalValue <= other.DecimalValue

