"""
This type stub file was generated by pyright.
"""

from bapy import *

"""
Contains the implementation of the Business Analyst dataset discovery methods
"""
__all__ = ["ListDatasets", "ListVariables", "ListGeographyLevels"]
def get_out_field_name(ge_field_name): # -> str:
    ...

class CountryInfo:
    def __init__(self, name=..., iso2=..., iso3=...) -> None:
        ...
    


class Dataset:
    def __init__(self, id, countryName, countryIso2, countryIso3, vintage, directory=..., installDirectory=..., networkDatasetPath=..., hasMoe=...) -> None:
        ...
    


class Variable:
    def __init__(self, data_collection, name, alias, units, vintage, percentbase, averagebase) -> None:
        ...
    


class GeographyLevel:
    def __init__(self, levelID, levelName, isWholeCountry, layerID, idField, nameField, stateNameField, stateAbbrevField, displayName, singularName, pluralName, adminLevel) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class StandardGeography:
    def __init__(self, id, name) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


def ListDatasets(): # -> Generator[Dataset, Any, None]:
    ...

def ListVariables(dataset, include_derivatives=...): # -> Generator[Variable, Any, None]:
    ...

def ListGeographyLevels(dataset): # -> Generator[GeographyLevel, Any, None]:
    ...

def ListStandardGeographies(dataset, level=..., query=..., sublevel=..., subquery=...): # -> Generator[StandardGeography, Any, None]:
    ...

