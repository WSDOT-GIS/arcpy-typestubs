"""
This type stub file was generated by pyright.
"""

from enum import IntEnum
from arcgisscripting import na as cna

"""Module for working with Origin Destination Cost Matrix Solver."""
__all__ = [
    "OriginDestinationCostMatrixInputDataType",
    "OriginDestinationCostMatrixOutputDataType",
    "OriginDestinationCostMatrix",
]

class OriginDestinationCostMatrixInputDataType(IntEnum):
    """Enumeration for feature class names used by the Origin Destination Cost Matrix solver to store inputs."""

    Origins = ...
    Destinations = ...
    PointBarriers = ...
    LineBarriers = ...
    PolygonBarriers = ...

class OriginDestinationCostMatrixOutputDataType(IntEnum):
    """Enumeration for feature class names used by the Origin Destination Cost Matrix solver to store outputs."""

    Origins = ...
    Destinations = ...
    Lines = ...

class OriginDestinationCostMatrix(cna.OriginDestinationCostMatrix):
    """Perform origin destination cost matrix analysis.

    # An example showing how to perform origin destination cost matrix analysis using inputs from feature classes.
    import arcpy
    import arcpy._na as nax

    nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
    nd_layer_name = "Routing_ND"
    input_origins = "C:/data/io.gdb/Origins"
    input_destinations = "C:/data/io.gdb/Destinations"
    output_lines = "C:/data/io.gdb/ODCostMatrixLines"

    arcpy.CheckOutExtension("network")
    arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
    nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
    travel_mode = nd_travel_modes["Driving Time"]
    odcm = nax.OriginDestinationCostMatrix(nd_layer_name)
    odcm.travelMode = travel_mode
    odcm.defaultImpedanceCutoff = 15
    odcm.defaultDestinationCount = 5
    odcm.lineShapeType = nax.LineShapeType.NoLine
    odcm.load(nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins)
    odcm.load(nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations)
    result = odcm.solve()
    if result.solveSucceeded:
        result.export(nax.OriginDestinationCostMatrixOutputDataType.Lines, output_lines)
    else:
        print("Solved failed")
        print(result.solverMessages())

    """

    __slots__ = ...
    def __init__(self, in_network) -> None:
        """Create an origin destination cost matrix solver object based on the input network dataset.

        Args:
                in_network: A string representing the full catalog path to the network dataset, a network dataset
                            layer object, a string representing the name of a network dataset layer, or a portal URL
                            for a network analysis service. For best performance pass a network dataset layer object
                            or a network dataset layer name.

        Returns:
                No value.

        Raises:
                ValueError if the in_network does not exist or cannot be opened or if you are not signed in to the
                portal.

        """
        ...
