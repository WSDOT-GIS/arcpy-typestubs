"""
This type stub file was generated by pyright.
"""

from arcgisscripting import da

"Data Access Module"
__all__ = [item for item in dir(da) if notitem.startswith('_')]
def CreateTable(path, fields=..., shape=..., configuration=...): # -> tuple[Unknown, Unknown]:
    """CreateTable(path, fields=None, shape=None, configuration=None)

       creates Table or FeatureClass.

    INPUTS:
      path (String): full path to new table
      fields: define new fields
         1. numpy.dtype() records
         2. sequance of arcpy.arcobjects.arcobjects.Field, the same as da.Describe()['fields']
         3. sequance of field descriptions (Field Name, Field Type, Field Alias=None, Field Length=None, IsNullable=True, Default Value = None), the same as arcpy.management.AddFields
      shape:
        define Shape field. Geometry type (String) or a tuple of (geometry_type, spacialreference=None, has_z=False, has_m=False)
        Spacial Reference can be: WKID, string, or arcpy.SpatialReference()
      configuration {String}:
        the configuration keyword applies to enterprise geodatabase

    OUTPUTS:
      tuple of path and list of added field names. Field names can be corrected and differ from the input
    """
    ...

