"""
This type stub file was generated by pyright.
"""

from arcpy.geoprocessing._base import gptooldoc

""""""
__all__ = ["QuickExport", "QuickImport"]
__alias__ = ...

@gptooldoc("QuickExport_interop", None)
def QuickExport(
    Input=..., Output=...
):  # -> conversion | int | float | complex | basestring | list[Unknown] | tuple[Unknown, ...] | dict[Unknown, Unknown]:
    """QuickExport_interop(Input;Input..., Output)

       Converts one or more input feature classes or feature layers into any
       format supported by the ArcGIS Data Interoperability extension.

    INPUTS:
     Input (Feature Layer):
         The feature layers or feature classes that will be exported from ArcGIS

    OUTPUTS:
     Output (Interop Destination Dataset):
         The format and dataset to which the data will be exported.If the
         destination is a file with a well-known file extension, it can be
         given as-is. For instance, "c:\\data\\roads.gml".If the destination
         is not a file, or the file has an unknown extension, the format
         can be given as part of the argument, separated by a comma. For
         instance,"MIF,c:\\data\\". The names for supported formats can be
         found in the formats gallery, by opening up this tool in dialog
         mode and clicking the browse button.Additional format-specific
         parameters can be added after the dataset, separated by a comma.
         However, the syntax can be complex, so if this is required it is
         easiest to run the tool using its dialog  and copy the Python syntax
         from the Results window."""
    ...

@gptooldoc("QuickImport_interop", None)
def QuickImport(
    Input=..., Output=...
):  # -> conversion | int | float | complex | basestring | list[Unknown] | tuple[Unknown, ...] | dict[Unknown, Unknown]:
    """QuickImport_interop(Input, Output)

       Converts data in any format supported by the ArcGIS Data Interoperability
       extension into feature classes.The output is stored in a geodatabase. The
       geodatabase can then be used directly
       or further post-processing can be performed.

    INPUTS:
     Input (Interop Source Dataset):
         The data to be imported. The syntax can take multiple forms:

         * If the source data is a file with a well-known file extension, it
         can be given as-is. For instance, "c:\\data\\roads.mif".

         * If the source data is not a file, or the file has an unknown extension,
         the format can be given as part of the argument, separated by a comma.
         For instance, "MIF,c:\\data\\roads.mif". The names for supported formats
         can be found in the Formats Gallery, by opening this tool in dialog
         mode and clicking the browse button.

         * Wildcards can be used to read in large datasets. For instance,
         "MIF,c:\\data\\roads*.*".

         * The * character matches any series of characters for all files in
         the current directory. For instance, c:\\data\\roads*.mif will match
         c:\\data\\roads.mif, c:\\data\\roads5.mif, and c:\\data\\roads-updated.mif.

         * The ** characters match any subdirectories, recursively. For instance,
         c:\\data\\**\\*.mif will match c:\\data\\roads.mif,
         c:\\data\\canada\\rivers.mif, and c:\\data\\canada\\alberta\\edmonton.mif.


         * Additional format-specific parameters can be added after the dataset,
         separated by a comma. However, the syntax can be complex, so if this
         is required it is easiest to run the tool using its dialog  and copy
         the Python syntax from the Results window.

    OUTPUTS:
     Output (Workspace):
         The output file or personal geodatabase."""
    ...
