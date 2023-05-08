"""
This type stub file was generated by pyright.
"""

from .CIMEnum import *
from .CIMExternal import *


class CIMBinaryReference:
    """
      Represents a binary reference in a document.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMColorReplacementRule:
    """
      Represents a color replacement rule.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMGISProject:
    """
      Represents a project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMModuleSettings:
    """
      Represents module settings in the project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMProjectItem:
    """
      Represents an item in the project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMProjectThumbnailOptions:
    """
      A collection of options governing project thumbnail generation.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollection:
    """
      A statistical data collection is used by the Business Analyst to 
      organize and present data that can be aggregated by the enrich 
      functionality. This is not the storage of the data, it is metadata 
      about the data that describes how data will be aggregated by Business 
      Analyst. Currently, data can be calculated by defining what data 
      collections and analysis variables are needed in the output for 
      a given input features.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionCalculator:
    """
      Base class for statistical data collection calculator.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionField:
    """
      Represents a field of a statistical data collection that matches 
      to existing field in referenced feature dataset.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionInputAreaProperty:
    """
      Represents the property used to calculate the geodesic area of 
      the input feature.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionInputProperty:
    """
      Represents a property of an input feature.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionStandardVariable:
    """
      Represents a field of a statistical data collection that matches 
      to an existing variable in referenced feature dataset.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMVersion:
    """
      Represents a version object used for representing the saved version.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMView:
    """
      Represents a view in the project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMBookmarkDocument(CIMVersion):
    """
      Represents a bookmark document which is the document type used 
      for saving .bkmx files.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMColorReplacementDocument(CIMVersion):
    """
      Represents list of color replacement rules.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMDocumentInfo(CIMVersion):
    """
      Represents high level information for a document.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMGenericView(CIMView):
    """
      Represents a generic view.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMLayerDocument(CIMVersion):
    """
      Represents a layer document which is the document type used for 
      saving .lyrx files.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMLayoutDocument(CIMVersion):
    """
      Represents a layout document which is the document type used for 
      saving .pagx files.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMMapDocument(CIMVersion):
    """
      Represents a map document which is the document type used for saving 
      .mapx files.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMMapView(CIMView):
    """
      Represents a map view in the project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionDocument(CIMVersion):
    """
      Represents a document used for saving statistical data collections.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionFeatureLayerCalculator(CIMStatisticalDataCollectionCalculator):
    """
      Statistical data collection calculator based on a feature layer.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionInputPropertiesCalculator(CIMStatisticalDataCollectionCalculator):
    """
      Statistical Data Collection calculator for accessing properties 
      of input features, e.g. Area of polygonal input.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionScriptCalculator(CIMStatisticalDataCollectionCalculator):
    """
      Statistical data collection calculator based on a scripts that 
      use fields from other calculators.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMStatisticalDataCollectionStandardDataCalculator(CIMStatisticalDataCollectionCalculator):
    """
      Statistical data collection calculator based on a standard local 
      data.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMTableView(CIMView):
    """
      Represents a table view in the project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMExternalTableView(CIMTableView):
    """
      Represents an external table view.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMMapTableView(CIMTableView):
    """
      Represents a map table view in the project.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


