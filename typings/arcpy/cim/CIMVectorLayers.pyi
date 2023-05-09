"""
This type stub file was generated by pyright.
"""

from .CIMEnum import *
from .CIMExternal import *
from .CIMLayer import CIMBaseLayer, CIMSubLayerBase
from .CIMCore import CIMDefinition

class CIMActivity:
    """
    Represents activity.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAggregateVisualization:
    """
    Describes the appearance of aggregated features.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBindVariable:
    """
    Represents a bind variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBinningVisualization:
    """
    Describes the appearance and application behavior of polygon aggregation
    bins.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCondition:
    """
    Represents a condition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDataConnection:
    """
    Represents a data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDimensionShape:
    """
    Represents a dimension shape as used by a dimension feature.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDimensionStyle:
    """
    Represents an dimension style which defines dimension appearance.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDisplayFilter:
    """
    Represents a display filter used to restrict the display of features
    across scale ranges.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDisplayTable:
    """
    Represents a display table.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCDisplaySettings:
    """
    Represents generic ENC display settings.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplate:
    """
    Represents an editing template.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateRelationship:
    """
    Represents an editing template relationship.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateToolOptions:
    """
    Represents editing template tool options.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureExtrusion:
    """
    Represents feature extrusion.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureReduction:
    """
    Represents a technique for visually reducing large numbers of features
    in a map.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureSortInfo:
    """
    Contains information about the field name and sort order used to
    draw features.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureTrajectorySubLayer:
    """
    Represents the trajectory feature sublayer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFieldDescription:
    """
    Represents a field description.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloorAwareTableProperties:
    """
    Represents floor-aware properties for the layer/table used in floor
    filtering.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFolderConnection:
    """
    Represents a folder connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupEditingTemplatePart:
    """
    Represents a group editing template part.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHtmlPopupFormat:
    """
    Represents an HTML pop-up format.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerAction:
    """
    Represents a layer action.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerRange:
    """
    Represents a layer range.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaterializedViewProperties:
    """
    Properties relevant to query layers based on materialized views.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipatchFeatureTemplateModel:
    """
    Represents a multipatch feature template model.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPageDefinition:
    """
    Represents page definition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRange:
    """
    Represents a range.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRangeDefinition:
    """
    Represents a range definition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelateInfoBase:
    """
    Represents relate base.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52MarinerSettings:
    """
    Represents S-52 mariner settings object for controlling the drawing
    of ENC layers.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52TextGroupVisibilitySettings:
    """
    Represents S-52 text group settings.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52ViewingGroupSettings:
    """
    Represents S-52 viewing group properties object.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolIdentifier:
    """
    Represents a symbol identifier.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolLayerMasking:
    """
    Represents symbol layer masking.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeDataDefinition:
    """
    Represents a time data definition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeDimensionDefinition:
    """
    Represents a time dimension definition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeDisplayDefinition:
    """
    Represents a time display definition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeTableDefinition:
    """
    Represents a time table definition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnnotationSubLayer(CIMSubLayerBase):
    """
    Represents an annotation sublayer used to draw annotation feature
    classes subclasses.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBasicFeatureLayer(CIMBaseLayer):
    """
    Represents a basic feature layer, the base class for all layer
    types that draw feature classes as features.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBuildingDisciplineLayer(CIMBaseLayer):
    """
    Represents a building discipline layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBuildingLayer(CIMBaseLayer):
    """
    Represents a building composite layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCatalogDynamicGroupLayer(CIMBaseLayer):
    """
    Composite layer to hold all the dynamic content of a Catalog layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCLayer(CIMBaseLayer):
    """
    Represents an Electronic Navigational Charts (ENC) layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMParcelFabricLayer(CIMBaseLayer):
    """
    Represents a parcel fabric layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMParcelLayer(CIMBaseLayer):
    """
    Represents a parcel fabric layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandaloneTable(CIMDefinition):
    """
    Represents a standalone table.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTrajectoryLayer(CIMBaseLayer):
    """
    Represents a trajectory layer corresponding to a trajectory dataset.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVectorTileLayer(CIMBaseLayer):
    """
    Represents a VectorTile layer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAggregateField(CIMFieldDescription):
    """
    A field holding the result of an aggregation of multiple field
    values.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAggregationFeatureReduction(CIMFeatureReduction):
    """
    Represents a technique for visually reducing large numbers of features
    in a map by aggregating them.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnnotationLayer(CIMBasicFeatureLayer):
    """
    Represents an annotation layer used to draw annotation feature
    classes.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAttributeCondition(CIMCondition):
    """
    Represents an attribute condition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBasicRowTemplate(CIMEditingTemplate):
    """
    Represents a basic row template.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBinningFeatureReduction(CIMAggregationFeatureReduction):
    """
    Represents a technique for reducing features by aggregating them
    into polygon bins.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCatalogLayer(CIMBasicFeatureLayer):
    """
    Represents a layer which dynamically loads its sublayers according
    to scale and extent constraints.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClusteringFeatureReduction(CIMAggregationFeatureReduction):
    """
    Represents a technique for reducing features by aggregating them
    into point clusters.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDimensionLayer(CIMBasicFeatureLayer):
    """
    Represents an dimension layer used to draw dimension feature classes.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDiscreteVariable(CIMBindVariable):
    """
    Represents a single bind variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCDataConnection(CIMDataConnection):
    """
    Represents an ENC layer data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureDatasetDataConnection(CIMDataConnection):
    """
    Represents a feature dataset data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureTable(CIMDisplayTable):
    """
    Represents a feature table.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeoFeatureLayerBase(CIMBasicFeatureLayer):
    """
    Represents geographic feature layer base, a base class for geographic
    feature layers.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupEditingTemplate(CIMEditingTemplate):
    """
    Represents a group editing template.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHighlightActivity(CIMActivity):
    """
    Represents a highlight activity.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLocationCondition(CIMCondition):
    """
    Represents a location condition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipatchFeatureTemplate(CIMBasicRowTemplate):
    """
    Represents a multipatch feature template.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetCDFRasterDataConnection(CIMDataConnection):
    """
    Represents a NetCDF raster data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetCDFStandardDataConnection(CIMDataConnection):
    """
    Represents a NetCDF standard data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRangeVariable(CIMBindVariable):
    """
    Represents a range variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterTable(CIMDisplayTable):
    """
    Represents a raster table.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelQueryTableDataConnection(CIMDataConnection):
    """
    Represents a RelQuery table data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelateInfo(CIMRelateInfoBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRouteEventDataConnection(CIMDataConnection):
    """
    Represents a route event data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRowTemplate(CIMBasicRowTemplate):
    """
    Represents a row template.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52DisplaySettings(CIMENCDisplaySettings):
    """
    Represents S-52 display settings.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSqlQueryDataConnection(CIMDataConnection):
    """
    Represents a SQL query data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardDataConnection(CIMDataConnection):
    """
    Represents a standard data connection, the most common data connection
    type.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStreamServiceDataConnection(CIMDataConnection):
    """
    Represents a stream service data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubtypeGroupLayer(CIMBasicFeatureLayer):
    """
    Represents a subtype group layer that works with feature classes
    enabled with subtypes.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubtypeGroupLayerBase(CIMBasicFeatureLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSuppressActivity(CIMActivity):
    """
    Represents suppress activity.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableQueryNameDataConnection(CIMDataConnection):
    """
    Represents a table query name data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTemporalDataConnection(CIMDataConnection):
    """
    Represents a temporal data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTrackingServerDataConnection(CIMDataConnection):
    """
    Represents a tracking server data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVectorTileDataConnection(CIMDataConnection):
    """
    Represents a VectorTile layer data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWorkspaceConnection(CIMDataConnection):
    """
    Represents a workspace connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMXYEventDataConnection(CIMDataConnection):
    """
    Represents an XY event data connection.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureLayer(CIMGeoFeatureLayerBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometryLocationCondition(CIMLocationCondition):
    """
    Represents geometry location condition.
    """

    def __init__(self, *args, **Kwargs) -> None: ...
