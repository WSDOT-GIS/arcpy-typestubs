from typing import Literal

"""
See https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm

| Data type                          | datatype keyword              | Description                                                                                                                                                                                                                                  |
| ---------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Address Locator                    | DEAddressLocator              | A dataset used for geocoding that stores the address attributes, associated indexes, and rules that define the process for translating nonspatial descriptions of places to spatial data.                                                    |
| Analysis Cell Size                 | analysis_cell_size            | The cell size used by raster tools.                                                                                                                                                                                                          |
| Any Value                          | GPType                        | A data type that accepts any value.                                                                                                                                                                                                          |
| ArcMap Document                    | DEMapDocument                 | A file that contains one map, its layout, and its associated layers, tables, charts, and reports.                                                                                                                                            |
| Areal Unit                         | GPArealUnit                   | An areal unit type and value, such as square meter or acre.                                                                                                                                                                                  |
| Boolean                            | GPBoolean                     | A Boolean value.                                                                                                                                                                                                                             |
| CAD Drawing Dataset                | DECadDrawingDataset           | A vector data source mixed with feature types and symbology. The dataset is not usable for feature class-based queries or analysis.                                                                                                          |
| Calculator Expression              | GPCalculatorExpression        | A calculator expression.                                                                                                                                                                                                                     |
| Catalog Layer                      | GPCatalogLayer                | A collection of references to different data types. The data types can be from different locations and are managed and visualized dynamically as layers based on location, time, and other attributes.                                       |
| Catalog Root                       | DECatalogRoot                 | The top-level node in the Catalog tree.                                                                                                                                                                                                      |
| Cell Size                          | GPSACellSize                  | The cell size used by the ArcGIS Spatial Analyst extension.                                                                                                                                                                                  |
| Cell Size XY                       | GPCellSizeXY                  | Defines the two sides of a raster cell.                                                                                                                                                                                                      |
| Composite Layer                    | GPCompositeLayer              | A reference to several children layers, including symbology and rendering properties.                                                                                                                                                        |
| Compression                        | GPSAGDBEnvCompression         | Specifies the type of compression used for a raster.                                                                                                                                                                                         |
| Coordinate System                  | GPCoordinateSystem            | A reference framework, such as the UTM system consisting of a set of points, lines, or surfaces, and a set of rules used to define the positions of points in two- and three-dimensional space.                                              |
| Coordinate Systems Folder          | DESpatialReferencesFolder     | A folder on disk storing coordinate systems.                                                                                                                                                                                                 |
| Coverage                           | DECoverage                    | A coverage dataset, a proprietary data model for storing geographic features as points, arcs, and polygons with associated feature attribute tables.                                                                                         |
| Coverage Feature Class             | DECoverageFeatureClasses      | A coverage feature class, such as point, arc, node, route, route system, section, polygon, and region.                                                                                                                                       |
| Data Element                       | DEType                        | A dataset visible in ArcCatalog.                                                                                                                                                                                                             |
| Data File                          | GPDataFile                    | A data file.                                                                                                                                                                                                                                 |
| Database Connections               | DERemoteDatabaseFolder        | The database connection folder in ArcCatalog.                                                                                                                                                                                                |
| Dataset                            | DEDatasetType                 | A collection of related data, usually grouped or stored together.                                                                                                                                                                            |
| Date                               | GPDate                        | A date value.                                                                                                                                                                                                                                |
| dBASE Table                        | DEDbaseTable                  | Attribute data stored in dBASE format.                                                                                                                                                                                                       |
| Decimate                           | GP3DADecimate                 | Specifies a subset of nodes of a TIN to create a generalized version of that TIN.                                                                                                                                                            |
| Diagram Layer                      | GPDiagramLayer                | A diagram layer.                                                                                                                                                                                                                             |
| Disk Connection                    | DEDiskConnection              | An access path to a data storage device.                                                                                                                                                                                                     |
| Double                             | GPDouble                      | Any floating-point number stored as a double precision, 64-bit value.                                                                                                                                                                        |
| Encrypted String                   | GPEncryptedString             | Encrypted string for passwords.                                                                                                                                                                                                              |
| Envelope                           | GPEnvelope                    | The coordinate pairs that define the minimum bounding rectangle in which the data source falls.                                                                                                                                              |
| Evaluation Scale                   | GPEvaluationScale             | The scale value range and increment value applied to inputs in a weighted overlay operation.                                                                                                                                                 |
| Extent                             | GPExtent                      | Specifies the coordinate pairs that define the minimum bounding rectangle (x-minimum, y-minimum and x-maximum, y-maximum) of a data source. All coordinates for the data source fall in this boundary.                                       |
| Extract Values                     | GPSAExtractValues             | An extract values parameter.                                                                                                                                                                                                                 |
| Feature Class                      | DEFeatureClass                | A collection of spatial data with the same shape type: point, multipoint, polyline, and polygon.                                                                                                                                             |
| Feature Dataset                    | DEFeatureDataset              | A collection of feature classes that share a common geographic area and the same spatial reference system.                                                                                                                                   |
| Feature Layer                      | GPFeatureLayer                | A reference to a feature class, including symbology and rendering properties.                                                                                                                                                                |
| Feature Set                        | GPFeatureRecordSetLayer       | Interactive features that draw the features when the tool is run.                                                                                                                                                                            |
| Field                              | Field                         | A column in a table that stores the values for a single attribute.                                                                                                                                                                           |
| Field Info                         | GPFieldInfo                   | The details about a field in a field map.                                                                                                                                                                                                    |
| Field Mappings                     | GPFieldMapping                | A collection of fields in one or more input tables.                                                                                                                                                                                          |
| File                               | DEFile                        | A file on disk.                                                                                                                                                                                                                              |
| Folder                             | DEFolder                      | Specifies a location on disk where data is stored.                                                                                                                                                                                           |
| Formulated Raster                  | GPRasterFormulated            | A raster surface whose cell values are represented by a formula or constant.                                                                                                                                                                 |
| Fuzzy function                     | GPSAFuzzyFunction             | Specifies the algorithm used in fuzzification of an input raster.                                                                                                                                                                            |
| Geodataset                         | DEGeodatasetType              | A collection of data with a common theme in a geodatabase.                                                                                                                                                                                   |
| GeoDataServer                      | DEGeoDataServer               | A coarse-grained object that references a geodatabase.                                                                                                                                                                                       |
| Geometric Network                  | DEGeometricNetwork            | A linear network represented by topologically connected edge and junction features. Feature connectivity is based on their geometric coincidence.                                                                                            |
| Geostatistical Layer               | GPGALayer                     | A reference to a geostatistical data source, including symbology and rendering properties.                                                                                                                                                   |
| Geostatistical Search Neighborhood | GPGASearchNeighborhood        | Defines the searching neighborhood parameters for a geostatistical layer.                                                                                                                                                                    |
| Geostatistical Value Table         | GPGAValueTable                | A collection of data sources and fields that define a geostatistical layer.                                                                                                                                                                  |
| GlobeServer                        | DEGlobeServer                 | A Globe server.                                                                                                                                                                                                                              |
| GPServer                           | DEGPServer                    | A geoprocessing server.                                                                                                                                                                                                                      |
| Graph                              | GPGraph                       | A graph.                                                                                                                                                                                                                                     |
| Graph Data Table                   | GPGraphDataTable              | A graph data table.                                                                                                                                                                                                                          |
| Group Layer                        | GPGroupLayer                  | A collection of layers that appear and act as a single layer. Group layers make it easier to organize a map, assign advanced drawing order options, and share layers for use in other maps.                                                  |
| Horizontal Factor                  | GPSAHorizontalFactor          | The relationship between the horizontal cost factor and the horizontal relative moving angle.                                                                                                                                                |
| Image Service                      | DEImageServer                 | An image service.                                                                                                                                                                                                                            |
| Index                              | Index                         | A data structure used to speed the search for records in geographic datasets and databases.                                                                                                                                                  |
| INFO Expression                    | GPINFOExpression              | A syntax for defining and manipulating data in an INFO table.                                                                                                                                                                                |
| INFO Item                          | GPArcInfoItem                 | An item in an INFO table.                                                                                                                                                                                                                    |
| INFO Table                         | DEArcInfoTable                | A table in an INFO database.                                                                                                                                                                                                                 |
| Internet Tiled Layer               | GPInternetTiledLayer          | An internet tiled layer.                                                                                                                                                                                                                     |
| KML Layer                          | GPKMLLayer                    | A KML layer.                                                                                                                                                                                                                                 |
| LAS Dataset                        | DELasDataset                  | A LAS dataset stores reference to one or more LAS files on disk as well as to additional surface features. A LAS file is a binary file that stores airborne lidar data.                                                                      |
| LAS Dataset Layer                  | GPLasDatasetLayer             | A layer that references a LAS dataset on disk. This layer can apply filters on lidar files and surface constraints referenced by a LAS dataset.                                                                                              |
| Layer                              | GPLayer                       | A reference to a data source, such as a shapefile, coverage, geodatabase feature class, or raster, including symbology and rendering properties.                                                                                             |
| Layer File                         | DELayer                       | A layer file stores a layer definition, including symbology and rendering properties.                                                                                                                                                        |
| Line                               | GPLine                        | A shape, straight or curved, defined by a connected series of unique x,y-coordinate pairs.                                                                                                                                                   |
| Linear Unit                        | GPLinearUnit                  | A linear unit type and value such as meter or feet.                                                                                                                                                                                          |
| Long                               | GPLong                        | An integer number value.                                                                                                                                                                                                                     |
| M Domain                           | GPMDomain                     | A range of lowest and highest possible value for m-coordinates.                                                                                                                                                                              |
| Map                                | GPMap                         | An ArcGIS Pro map.                                                                                                                                                                                                                           |
| MapServer                          | DEMapServer                   | A map server.                                                                                                                                                                                                                                |
| Map Server Layer                   | GPMapServerLayer              | A map server layer.                                                                                                                                                                                                                          |
| Mosaic Dataset                     | DEMosaicDataset               | A collection of raster and image data that allows you to store, view, and query the data. It is a data model in the geodatabase used to manage a collection of raster datasets (images) stored as a catalog and viewed as a mosaicked image. |
| Mosaic Layer                       | GPMosaicLayer                 | A layer that references a mosaic dataset.                                                                                                                                                                                                    |
| Neighborhood                       | GPSANeighborhood              | The shape of the area around each cell used to calculate statistics.                                                                                                                                                                         |
| Network Analyst Class FieldMap     | NAClassFieldMap               | Mapping between location properties in a Network Analyst layer (such as stops, facilities, and incidents) and a point feature class.                                                                                                         |
| Network Analyst Hierarchy Settings | GPNAHierarchySettings         | A hierarchy attribute that divides hierarchy values of a network dataset into three groups using two integers. The first integer sets the ending value of the first group; the second number sets the beginning value of the third group.    |
| Network Analyst Layer              | GPNALayer                     | A special group layer used to express and solve network routing problems. Each sublayer held in memory in a Network Analyst layer represents some aspect of the routing problem and the routing solution.                                    |
| Network Data Source                | GPNetworkDataSource           | A network data source can be a local dataset specified either using its catalog path or a layer from a map, or it can be a URL to a portal.                                                                                                  |
| Network Dataset                    | DENetworkDataset              | A collection of topologically connected network elements (edges, junctions, and turns), derived from network sources and associated with a collection of network attributes.                                                                 |
| Network Dataset Layer              | GPNetworkDatasetLayer         | A reference to a network dataset, including symbology and rendering properties.                                                                                                                                                              |
| Network Travel Mode                | NetworkTravelMode             | A dictionary of travel mode objects.                                                                                                                                                                                                         |
| Parcel Fabric For ArcMap           | DECadastralFabric             | A parcel fabric is a dataset for the storage, maintenance, and editing of a continuous surface of connected parcels or parcel network.                                                                                                       |
| Parcel Fabric Layer                | GPCadastralFabricLayer        | A layer referencing a parcel fabric on disk. This layer works as a group layer organizing a set of related layers under a single layer.                                                                                                      |
| Point                              | GPPoint                       | A pair of x,y-coordinates.                                                                                                                                                                                                                   |
| Polygon                            | GPPolygon                     | A connected sequence of x,y-coordinate pairs, where the first and last coordinate pair are the same.                                                                                                                                         |
| Projection File                    | DEPrjFile                     | A file storing coordinate system information for spatial data.                                                                                                                                                                               |
| Pyramid                            | GPSAGDBEnvPyramid             | Specifies whether pyramids are built.                                                                                                                                                                                                        |
| Radius                             | GPSARadius                    | Specifies which surrounding points are used for interpolation.                                                                                                                                                                               |
| Random Number Generator            | GPRandomNumberGenerator       | Specifies the seed and the generator to use when creating random values.                                                                                                                                                                     |
| Raster Band                        | DERasterBand                  | A layer in a raster dataset.                                                                                                                                                                                                                 |
| Raster Calculator Expression       | GPRasterCalculatorExpression  | A raster calculator expression.                                                                                                                                                                                                              |
| Raster Catalog                     | DERasterCatalog               | A collection of raster datasets defined in a table. Each table record defines an individual raster dataset in the catalog.                                                                                                                   |
| Raster Catalog Layer               | GPRasterCatalogLayer          | A reference to a raster catalog, including symbology and rendering properties.                                                                                                                                                               |
| Raster Data Layer                  | GPRasterDataLayer             | A raster data layer.                                                                                                                                                                                                                         |
| Raster Dataset                     | DERasterDataset               | A single dataset built from one or more rasters.                                                                                                                                                                                             |
| Raster Layer                       | GPRasterLayer                 | A reference to a raster, including symbology and rendering properties.                                                                                                                                                                       |
| Raster Statistics                  | GPSAGDBEnvStatistics          | Specifies whether raster statistics build.                                                                                                                                                                                                   |
| Raster Type                        | GPRasterBuilder               | Raster data is added to a mosaic dataset by specifying a raster type. The raster type identifies metadata, such as georeferencing, acquisition date, and sensor type, with a raster format.                                                  |
| Record Set                         | GPRecordSet                   | Interactive table; type in the table values when the tool is run.                                                                                                                                                                            |
| Relationship Class                 | DERelationshipClass           | The details about the relationship between objects in the geodatabase.                                                                                                                                                                       |
| Remap                              | GPSARemap                     | A table that defines how raster cell values are reclassified.                                                                                                                                                                                |
| Route Measure Event Properties     | GPRouteMeasureEventProperties | Specifies the fields on a table that describe events measured by a linear reference route system.                                                                                                                                            |
| Scene Service Layer                | GPSceneServiceLayer           | A scene service layer.                                                                                                                                                                                                                       |
| Schematic Dataset                  | DESchematicDataset            | A schematic dataset contains a collection of schematic diagram templates and schematic feature classes that share the same application domain, for example, water or electrical.                                                             |
| Schematic Diagram                  | DESchematicDiagram            | A schematic diagram.                                                                                                                                                                                                                         |
| Schematic Diagram Class            | DESchematicDiagramClass       | A schematic diagram class.                                                                                                                                                                                                                   |
| Schematic Folder                   | DESchematicFolder             | A schematic folder.                                                                                                                                                                                                                          |
| Schematic Layer                    | GPSchematicLayer              | A schematic layer is a composite layer composed of feature layers based on the schematic feature classes associated with the template on which the schematic diagram is based.                                                               |
| SemiVariogram                      | GPSASemiVariogram             | Specifies the distance and direction representing two locations used to quantify autocorrelation.                                                                                                                                            |
| ServerConnection                   | DEServerConnection            | A server connection.                                                                                                                                                                                                                         |
| Shapefile                          | DEShapeFile                   | Spatial data in a shapefile format.                                                                                                                                                                                                          |
| Spatial Reference                  | GPSpatialReference            | The coordinate system used to store a spatial dataset, including the spatial domain.                                                                                                                                                         |
| SQL Expression                     | GPSQLExpression               | A syntax for defining and manipulating data from a relational database.                                                                                                                                                                      |
| String                             | GPString                      | A text value.                                                                                                                                                                                                                                |
| String Hidden                      | GPStringHidden                | A string that is masked by \* characters.Note:The text is not encrypted when used in scripting.                                                                                                                                              |
| Table                              | DETable                       | Tabular data.                                                                                                                                                                                                                                |
| Table View                         | GPTableView                   | A representation of tabular data for viewing and editing purposes, stored in memory or on disk.                                                                                                                                              |
| Terrain Layer                      | GPTerrainLayer                | A reference to a terrain, including symbology and rendering properties. It’s used to draw a terrain.                                                                                                                                         |
| Text File                          | DETextfile                    | A text file.                                                                                                                                                                                                                                 |
| Tile Size                          | GPSAGDBEnvTileSize            | Specifies the width and the height of data stored in block.                                                                                                                                                                                  |
| Time configuration                 | GPSATimeConfiguration         | Specifies the time periods used for calculating solar radiation at specific locations.                                                                                                                                                       |
| Time Unit                          | GPTimeUnit                    | A time unit type and value such as minutes or hours.                                                                                                                                                                                         |
| TIN                                | DETin                         | A vector data structure that partitions geographic space into contiguous, nonoverlapping triangles. The vertices of each triangle are sample data points with x-, y-, and z-values.                                                          |
| Tin Layer                          | GPTinLayer                    | A reference to a TIN, including topological relationships, symbology, and rendering properties.                                                                                                                                              |
| Tool                               | DETool                        | A geoprocessing tool.                                                                                                                                                                                                                        |
| Toolbox                            | DEToolbox                     | A geoprocessing toolbox.                                                                                                                                                                                                                     |
| Topo Features                      | GPSATopoFeatures              | Features that are input to the interpolation.                                                                                                                                                                                                |
| Topology                           | DETopology                    | A topology that defines and enforces data integrity rules for spatial data.                                                                                                                                                                  |
| Topology Layer                     | GPTopologyLayer               | A reference to a topology, including symbology and rendering properties.                                                                                                                                                                     |
| Transformation Function            | GPSATransformationFunction    | A Spatial Analyst transformation function.                                                                                                                                                                                                   |
| Trajectory Layer                   | GPTrajectoryLayer             | A layer that references a trajectory dataset.                                                                                                                                                                                                |
| Utility Network                    | DEUtilityNetwork              | A utility network.                                                                                                                                                                                                                           |
| Utility Network Layer              | GPUtilityNetworkLayer         | A utility network layer.                                                                                                                                                                                                                     |
| Value Table                        | GPValueTable                  | A collection of columns of values.                                                                                                                                                                                                           |
| Variant                            | GPVariant                     | A data value that can contain any basic type: Boolean, date, double, long, and string.                                                                                                                                                       |
| Vector Tile Layer                  | GPVectorLayer                 | A vector tile layer.                                                                                                                                                                                                                         |
| Vertical Factor                    | GPSAVerticalFactor            | Specifies the relationship between the vertical cost factor and the vertical, relative moving angle.                                                                                                                                         |
| VPF Coverage                       | DEVPFCoverage                 | Spatial data stored in Vector Product Format.                                                                                                                                                                                                |
| VPF Table                          | DEVPFTable                    | Attribute data stored in Vector Product Format.                                                                                                                                                                                              |
| WCS Coverage                       | DEWCSCoverage                 | Web Coverage Service (WCS) is an open specification for sharing raster datasets on the web.                                                                                                                                                  |
| Weighted Overlay Table             | GPSAWeightedOverlayTable      | A table with data to combine multiple rasters by applying a common measurement scale of values to each raster, weighing each according to its importance.                                                                                    |
| Weighted Sum                       | GPSAWeightedSum               | Specifies data for overlaying several rasters, each multiplied by their given weight and summed.                                                                                                                                             |
| WMS Map                            | DEWMSMap                      | A WMS map.                                                                                                                                                                                                                                   |
| Workspace                          | DEWorkspace                   | A container such as a geodatabase or folder.                                                                                                                                                                                                 |
| XY Domain                          | GPXYDomain                    | A range of lowest and highest possible values for x,y-coordinates.                                                                                                                                                                           |
| Z Domain                           | GPZDomain                     | A range of lowest and highest possible values for z-coordinates.                                                                                                                                                                             |
"""
ParameterDataType = (
    Literal["DEAddressLocator"]
    | Literal["analysis_cell_size"]
    | Literal["GPType"]
    | Literal["DEMapDocument"]
    | Literal["GPArealUnit"]
    | Literal["GPBoolean"]
    | Literal["DECadDrawingDataset"]
    | Literal["GPCalculatorExpression"]
    | Literal["GPCatalogLayer"]
    | Literal["DECatalogRoot"]
    | Literal["GPSACellSize"]
    | Literal["GPCellSizeXY"]
    | Literal["GPCompositeLayer"]
    | Literal["GPSAGDBEnvCompression"]
    | Literal["GPCoordinateSystem"]
    | Literal["DESpatialReferencesFolder"]
    | Literal["DECoverage"]
    | Literal["DECoverageFeatureClasses"]
    | Literal["DEType"]
    | Literal["GPDataFile"]
    | Literal["DERemoteDatabaseFolder"]
    | Literal["DEDatasetType"]
    | Literal["GPDate"]
    | Literal["DEDbaseTable"]
    | Literal["GP3DADecimate"]
    | Literal["GPDiagramLayer"]
    | Literal["DEDiskConnection"]
    | Literal["GPDouble"]
    | Literal["GPEncryptedString"]
    | Literal["GPEnvelope"]
    | Literal["GPEvaluationScale"]
    | Literal["GPExtent"]
    | Literal["GPSAExtractValues"]
    | Literal["DEFeatureClass"]
    | Literal["DEFeatureDataset"]
    | Literal["GPFeatureLayer"]
    | Literal["GPFeatureRecordSetLayer"]
    | Literal["Field"]
    | Literal["GPFieldInfo"]
    | Literal["GPFieldMapping"]
    | Literal["DEFile"]
    | Literal["DEFolder"]
    | Literal["GPRasterFormulated"]
    | Literal["GPSAFuzzyFunction"]
    | Literal["DEGeodatasetType"]
    | Literal["DEGeoDataServer"]
    | Literal["DEGeometricNetwork"]
    | Literal["GPGALayer"]
    | Literal["GPGASearchNeighborhood"]
    | Literal["GPGAValueTable"]
    | Literal["DEGlobeServer"]
    | Literal["DEGPServer"]
    | Literal["GPGraph"]
    | Literal["GPGraphDataTable"]
    | Literal["GPGroupLayer"]
    | Literal["GPSAHorizontalFactor"]
    | Literal["DEImageServer"]
    | Literal["Index"]
    | Literal["GPINFOExpression"]
    | Literal["GPArcInfoItem"]
    | Literal["DEArcInfoTable"]
    | Literal["GPInternetTiledLayer"]
    | Literal["GPKMLLayer"]
    | Literal["DELasDataset"]
    | Literal["GPLasDatasetLayer"]
    | Literal["GPLayer"]
    | Literal["DELayer"]
    | Literal["GPLine"]
    | Literal["GPLinearUnit"]
    | Literal["GPLong"]
    | Literal["GPMDomain"]
    | Literal["GPMap"]
    | Literal["DEMapServer"]
    | Literal["GPMapServerLayer"]
    | Literal["DEMosaicDataset"]
    | Literal["GPMosaicLayer"]
    | Literal["GPSANeighborhood"]
    | Literal["NAClassFieldMap"]
    | Literal["GPNAHierarchySettings"]
    | Literal["GPNALayer"]
    | Literal["GPNetworkDataSource"]
    | Literal["DENetworkDataset"]
    | Literal["GPNetworkDatasetLayer"]
    | Literal["NetworkTravelMode"]
    | Literal["DECadastralFabric"]
    | Literal["GPCadastralFabricLayer"]
    | Literal["GPPoint"]
    | Literal["GPPolygon"]
    | Literal["DEPrjFile"]
    | Literal["GPSAGDBEnvPyramid"]
    | Literal["GPSARadius"]
    | Literal["GPRandomNumberGenerator"]
    | Literal["DERasterBand"]
    | Literal["GPRasterCalculatorExpression"]
    | Literal["DERasterCatalog"]
    | Literal["GPRasterCatalogLayer"]
    | Literal["GPRasterDataLayer"]
    | Literal["DERasterDataset"]
    | Literal["GPRasterLayer"]
    | Literal["GPSAGDBEnvStatistics"]
    | Literal["GPRasterBuilder"]
    | Literal["GPRecordSet"]
    | Literal["DERelationshipClass"]
    | Literal["GPSARemap"]
    | Literal["GPRouteMeasureEventProperties"]
    | Literal["GPSceneServiceLayer"]
    | Literal["DESchematicDataset"]
    | Literal["DESchematicDiagram"]
    | Literal["DESchematicDiagramClass"]
    | Literal["DESchematicFolder"]
    | Literal["GPSchematicLayer"]
    | Literal["GPSASemiVariogram"]
    | Literal["DEServerConnection"]
    | Literal["DEShapeFile"]
    | Literal["GPSpatialReference"]
    | Literal["GPSQLExpression"]
    | Literal["GPString"]
    | Literal["GPStringHidden"]
    | Literal["DETable"]
    | Literal["GPTableView"]
    | Literal["GPTerrainLayer"]
    | Literal["DETextfile"]
    | Literal["GPSAGDBEnvTileSize"]
    | Literal["GPSATimeConfiguration"]
    | Literal["GPTimeUnit"]
    | Literal["DETin"]
    | Literal["GPTinLayer"]
    | Literal["DETool"]
    | Literal["DEToolbox"]
    | Literal["GPSATopoFeatures"]
    | Literal["DETopology"]
    | Literal["GPTopologyLayer"]
    | Literal["GPSATransformationFunction"]
    | Literal["GPTrajectoryLayer"]
    | Literal[" DEUtilityNetwork"]
    | Literal["GPUtilityNetworkLayer"]
    | Literal["GPValueTable"]
    | Literal["GPVariant"]
    | Literal["GPVectorLayer"]
    | Literal["GPSAVerticalFactor"]
    | Literal["DEVPFCoverage"]
    | Literal["DEVPFTable"]
    | Literal["DEWCSCoverage"]
    | Literal["GPSAWeightedOverlayTable"]
    | Literal["GPSAWeightedSum"]
    | Literal["DEWMSMap"]
    | Literal["DEWorkspace"]
    | Literal["GPXYDomain"]
    | Literal["GPZDomain"]
)
