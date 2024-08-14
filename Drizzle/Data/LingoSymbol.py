from __future__ import annotations


class LingoSymbol:
    def __init__(self, value: str):
        self.Value = value.lower()  # just to ensure that it will not be case sensetive

    def __str__(self):
        return f"#{self.Value}"

    def __hash__(self):
        return self.Value.__hash__()

    def __eq__(self, other: LingoSymbol):
        return self.Value == other.Value

    def __ne__(self, other: LingoSymbol):
        return self.Value != other.Value