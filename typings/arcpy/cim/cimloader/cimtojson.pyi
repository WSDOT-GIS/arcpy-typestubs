"""
This type stub file was generated by pyright.
"""

from json import JSONEncoder

__all__ = ["CimJsonEncoder"]

def GetDateTimeAsInt(dt): ...

pointAttribs = ...

def GetPointAttribs(obj): ...

class CimJsonEncoder(JSONEncoder):
    def default(self, o): ...
