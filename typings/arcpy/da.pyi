"""
Data Access Module
"""

from typing import Any, Generator, NamedTuple, Optional, Sequence, Callable
from typing_extensions import Literal, Self
import numpy
import pyarrow
from . import Field, SpatialReference

# from arcgisscripting import da

# "Data Access Module"
# __all__ = [item for item in dir(da) if notitem.startswith("_")]

SpecialFieldName = Literal[
    "SHAPE@XY",
    "SHAPE@XYZ",
    "SHAPE@TRUECENTROID",
    "SHAPE@X",
    "SHAPE@Y",
    "SHAPE@Z",
    "SHAPE@M",
    "SHAPE@JSON",
    "SHAPE@WKB",
    "SHAPE@WKT",
    "SHAPE@",
    "SHAPE@AREA",
    "SHAPE@LENGTH",
    "CREATED@",
    "CREATOR@",
    "EDITED@",
    "EDITOR@",
    "GLOBALID@",
    "OID@",
    "SUBTYPE@",
]

class FieldDescriptionTuple(NamedTuple):
    Field_Name: str
    Field_Type: str
    Field_Alias: str | None = None
    Field_Length: int | None = None
    IsNullable: bool = True
    Default_Value: Any = None

class ShapeFieldDefinitionTuple(NamedTuple):
    geometry_type: str
    spatial_reference: int | str | SpatialReference | None = None
    has_z: bool = False
    has_m: bool = False

class CreateTableResult(NamedTuple):
    path: str
    field_names: list[str]

class SqlClause(NamedTuple):
    prefix: Literal["DISTINCT", "TOP"] | None
    postfix: Literal["ORDER BY", "GROUP BY"] | None

def CreateTable(
    path: str,
    fields: numpy.record[numpy.dtype] | Sequence[Field] | FieldDescriptionTuple,
    shape: str | ShapeFieldDefinitionTuple,
    configuration: str | None = None,
) -> CreateTableResult:
    """CreateTable(path, fields=None, shape=None, configuration=None)

       creates Table or FeatureClass.

    INPUTS:
      path (String): full path to new table
      fields: define new fields
         1. numpy.dtype() records
         2. sequence of arcpy.arcobjects.arcobjects.Field, the same as da.Describe()['fields']
         3. sequence of field descriptions (Field Name, Field Type, Field Alias=None, Field Length=None, IsNullable=True, Default Value = None), the same as arcpy.management.AddFields
      shape:
        define Shape field. Geometry type (String) or a tuple of (geometry_type, spatial_reference=None, has_z=False, has_m=False)
        Spacial Reference can be: WKID, string, or arcpy.SpatialReference()
      configuration {String}:
        the configuration keyword applies to enterprise geodatabase

    OUTPUTS:
      tuple of path and list of added field names. Field names can be corrected and differ from the input
    """  # noqa: E501
    ...

class __Cursor__:
    def __init__(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type, exc_value: Any, traceback: Any) -> bool: ...

class InsertCursor(__Cursor__):
    def __init__(
        self,
        in_table: str,
        field_names: str | Sequence[str | SpecialFieldName | Literal["*"]],
        where_clause: str | None = None,
        explode_to_points: bool = False,
        sql_clause: SqlClause = SqlClause(None, None),
        datum_transformation: str | None = None,
        explicit: bool | Sequence[bool] = False,
    ) -> None: ...
    def insertRow(self, row: Sequence[Any] | Sequence[Sequence[Any]]) -> int: ...

class UpdateCursor(__Cursor__):
    def __init__(
        self,
        in_table: str,
        field_names: str | Sequence[str | SpecialFieldName | Literal["*"]],
        where_clause: str | None = None,
        explode_to_points: bool = False,
        sql_clause: SqlClause = SqlClause(None, None),
        datum_transformation: str | None = None,
        explicit: bool | Sequence[bool] = False,
    ) -> None: ...

class SearchCursor(__Cursor__):
    def __init__(
        self,
        in_table: str,
        field_names: str | Sequence[str | SpecialFieldName | Literal["*"]],
        where_clause: str | None = None,
        spatial_reference: SpatialReference | str | None = None,
        explode_to_points: bool = False,
        sql_clause: SqlClause = SqlClause(None, None),
        datum_transformation: str | None = None,
    ) -> None: ...

# Classes

class ContingentFieldValue: ...
class ContingentValue: ...
class DatabaseSequence: ...
class Domain: ...
class Editor: ...
class Replica: ...
class SyncReplica: ...
class Version: ...

# Functions

def Describe(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ExtendTable(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def FeatureClassToNumPyArray(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListContingentValues(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListDatabaseSequences(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListDomains(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListFieldConflictFilters(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListReplicas(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListSubtypes(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def ListVersions(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any: ...
def NumPyArrayToFeatureClass(
    in_array: numpy.ndarray,
    out_table: str,
    shape_fields: Sequence[str],
    spatial_reference: Optional[SpatialReference | str] = None,
) -> Any:
    """Converts a NumPy structured array to a point feature class.
    Discussion

    If a field name from the input array is invalid for the output format, it will be
    validated. All invalid characters in the input field name are replaced with an
    underscore (_) in the output field name. Field name restrictions depend on the
    specific database used.

    NumPyArrayToFeatureClass will not overwrite an existing feature class, even if the
    overwriteOutput environment is set to True.

    NumPy is a fundamental package for scientific computing in Python, including support
    for a powerful N-dimensional array object. For more information, see
    [Working with NumPy in ArcGIS](https://pro.arcgis.com/en/pro-app/3.1/arcpy/get-started/working-with-numpy-in-arcgis.htm).
    """
    ...

def NumPyArrayToTable(*args: Sequence[Any], **kwargs: dict[str, Any]) -> Any:
    ...

def TableToArrowTable(
    in_table: str, field_names: str = "", where_clause: str = ""
) -> pyarrow.Table:  # type: ignore
    """Converts a table or feature class to an Apache Arrow table.

    Apache Arrow is a standard cross-platform in-memory representation of columnar data
    used to efficiently transport data between analytics systems for big data.
    For more information, see working with
    [Apache Arrow in ArcGIS](https://pro.arcgis.com/en/pro-app/3.1/arcpy/get-started/working-with-arrow-in-arcgis.htm).
    """

def TableToNumPyArray(
    *args: Sequence[Any], **kwargs: dict[str, Any]
) -> numpy.ndarray:
    ...

def Walk(
    top: str,
    topdown: bool = True,
    onerror: Callable[[OSError], Any] | None = None,
    followlinks: bool = False,
    datatype: str | Sequence[str] | None = None,
    type: str | None = None,
) -> Generator[tuple[str, list[str], list[str]], None, None]: ...
