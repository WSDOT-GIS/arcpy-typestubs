"""
This type stub file was generated by pyright.
"""

"""
Module containing utilities used by the other modules.
"""
UNEVALUATED_RASTER_FUNCTION_SIGNAL = ...

class StateSwapper:
    SingleRasterResult = ...
    NoSingleRasterResult = ...
    def __init__(self, outputCategory=...) -> None: ...
    def __call__(self, wrapper): ...

class ParameterErrors:
    """Contains a list of localized mock GP tool validation error message strings"""

    def __init__(self) -> None: ...
    def add_id_message(self, severity: str, message_id: int, *args) -> None:
        """Add one message based on geoprocessing message ID and optional arguments"""
        ...
    def combine(self) -> str:
        """Returns one multiline string containing all of the stored messages"""
        ...
    def create_id_message(self, severity: str, message_id: int, *args) -> str:
        """Creates one localized message string based on geoprocessing message ID and optional arguments"""
        ...

def compoundParameterToString(parameter, cls):  # -> LiteralString | str:
    """
    Convert parameter if it is a compound parameter object, otherwise do
    nothing.

    parameter -- Parameter to a function.
    cls -- Compound parameter class or base class of compound parameter class
           family.
    """
    ...

def multiValueCompoundParameterToString(
    parameter, cls
):  # -> LiteralString | str | list[Unknown]:
    """
    Convert parameter if it is a single compound parameter object or a list of
    compund parameter objects, otherwise do nothing.

    parameter -- Parameter to a function.
    cls -- Compound parameter class or base class of compound parameter class
           family.
    """
    ...

def isNumerical(object):  # -> bool:
    """
    Return whether object is an instance of one of Python's built-in numeric
    types.

    object -- Object to test.
    """
    ...

def flattenLists(iterable):  # -> list[Unknown]:
    """
    Flatten nested list elements in the iterable passed in, non-recursively.

    Return a list.
    """
    ...

def argumentValueEqualsString(argument, string): ...
def useDefaultArgumentValue(argument): ...
