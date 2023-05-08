"""
This type stub file was generated by pyright.
"""

from .CIMEnum import *
from .CIMExternal import *
from .CIMVectorLayers import CIMDataConnection, CIMGeoFeatureLayerBase
from .CIMCore import CIMDefinition
from .CIMLayer import CIMBaseLayer


class CIMKnowledgeGraphDataLoadingConfiguration:
    """
      Represents a Knowledge Graph Data Loading Configuration.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphDataLoadingEntity:
    """
      Represents a Knowledge Graph Data Loading Entity.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphDataLoadingRelationship:
    """
      Represents a Knowledge Graph Data Loading Relationship.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphLinkChartCentralityConfiguration:
    """
      Represents the Centrality computation options in a Knowledge Graph 
      Link Chart.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphLinkChartProperties:
    """
      Represents a Knowledge Graph Link Chart Properties object.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphProperty:
    """
      Represents a Knowledge Graph Data Loading Property used for entities 
      and relationships.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphPropertyValue:
    """
      Base (indicator) class for all CIMKnowledgeGraphXXXPropertyValue.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphQueryDefinition:
    """
      Represents a Knowledge Graph Query Definition.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphSearchDefinition:
    """
      Represents a Knowledge Graph Search Definition.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphSearchFilterSetting:
    """
      Represents a Knowledge Graph Search Filter Setting.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeLinkChartLayout:
    """
      Represents a Knowledge Link Chart Layout Info object.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphDataConnection(CIMDataConnection):
    """
      Represents a Knowledge Graph data connection.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphInvestigation(CIMDefinition):
    """
      Represents a Knowledge Graph Investigation.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphLayer(CIMBaseLayer):
    """
      Provides access to properties of a Knowledge Graph layer.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphTableDataConnection(CIMDataConnection):
    """
      Represents a Knowledge Graph data connection.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMLinkChartFeatureLayer(CIMGeoFeatureLayerBase):
    """
      Represents a Link Chart Feature Layer.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphCoordinatePropertyValue(CIMKnowledgeGraphPropertyValue):
    """
      Represents a coordinate property value.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphFieldPropertyValue(CIMKnowledgeGraphPropertyValue):
    """
      Represents a property value from a specific import field.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphFixedPropertyValue(CIMKnowledgeGraphPropertyValue):
    """
      Represents a fixed string property value.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphNonspatialProperty(CIMKnowledgeGraphProperty):
    """
      Represents a Knowledge Graph Data Loading Property used by entities 
      and relationships.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


class CIMKnowledgeGraphSpatialProperty(CIMKnowledgeGraphProperty):
    """
      Represents a Spatial Knowledge Graph Data Loading Property used 
      for entities. This
  /// class is expected to be used only when 
      the Type of property is esriFieldTypeGeometry.
    """
    def __init__(self, *args, **Kwargs) -> None:
        ...
    


