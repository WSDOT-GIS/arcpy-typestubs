"""
This type stub file was generated by pyright.
"""

from enum import IntEnum
from arcgisscripting import na as cna

"""Module for working with Vehicle Routing Problem Solver."""
__all__ = [
    "VehicleRoutingProblemInputDataType",
    "VehicleRoutingProblemOutputDataType",
    "VehicleRoutingProblemInputDataType2",
    "VehicleRoutingProblemOutputDataType2",
    "VehicleRoutingProblemSchemaVersion",
    "VehicleRoutingProblem",
]

class VehicleRoutingProblemInputDataType(IntEnum):
    """Enumeration for feature class names used by the Vehicle Routing Problem solver to store inputs."""

    Orders = ...
    Depots = ...
    Routes = ...
    Breaks = ...
    RouteZones = ...
    RouteRenewals = ...
    OrderPairs = ...
    PointBarriers = ...
    LineBarriers = ...
    PolygonBarriers = ...

class VehicleRoutingProblemInputDataType2(IntEnum):
    """Enumeration for feature class names used by the Vehicle Routing Problem solver version 2 to store inputs."""

    Orders = ...
    Depots = ...
    Routes = ...
    Breaks = ...
    RouteZones = ...
    RouteRenewals = ...
    OrderPairs = ...
    PointBarriers = ...
    LineBarriers = ...
    PolygonBarriers = ...
    OrderSpecialties = ...
    RouteSpecialties = ...

class VehicleRoutingProblemOutputDataType(IntEnum):
    """Enumeration for feature class names used by the Vehicle Routing Problem solver to store outputs."""

    UnassignedStops = ...
    Stops = ...
    Routes = ...
    Directions = ...

class VehicleRoutingProblemOutputDataType2(IntEnum):
    """Enumeration for feature class names used by the Vehicle Routing Problem solver version 2 to store outputs."""

    Orders = ...
    Depots = ...
    DepotVisits = ...
    Breaks = ...
    Routes = ...
    DirectionPoints = ...
    DirectionLines = ...

class VehicleRoutingProblemSchemaVersion(IntEnum):
    """Enumeration for feature class names used by the Vehicle Routing Problem solver to store outputs."""

    One = ...
    Two = ...

class VehicleRoutingProblem(cna.VehicleRoutingProblem):
    """Perform vehicle routing problem analysis.

    # An example showing how to perform vehicle routing problem analysis using inputs from feature classes and tables.
    import arcpy
    import arcpy._na as nax

    nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
    nd_layer_name = "Routing_ND"
    input_orders = "C:/data/io.gdb/Orders"
    input_depots = "C:/data/io.gdb/Depots"
    input_routes = "C:/data/io.gdb/Vehicles"
    output_stops = "C:/data/io.gdb/AssignedStops"
    output_routes = "C:/data/io.gdb/Routes"
    output_directions = "C:/data/io.gdb/Directions"
    unassigned_stops = "C:/data/io.gdb/UnassignedStops"

    arcpy.CheckOutExtension("network")
    arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
    nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
    travel_mode = nd_travel_modes["Driving Time"]
    vrp = nax.VehicleRoutingProblem(nds)
    vrp.travelMode = travel_mode
    vrp.distanceUnits = nax.DistanceUnits.Miles
    vrp.routeShapeType = nax.RouteShapeType.StraightLine
    vrp.returnDirections = True
    vrp.populateStopShapes = True
    vrp.load(nax.VehicleRoutingProblemInputDataType.Orders, input_orders)
    vrp.load(nax.VehicleRoutingProblemInputDataType.Depots, input_depots)
    vrp.load(nax.VehicleRoutingProblemInputDataType.Routes, input_routes)
    result = vrp.solve()
    if result.solveSucceeded:
        result.export(nax.VehicleRoutingProblemOutputDataType.Stops, output_stops)
        result.export(nax.VehicleRoutingProblemOutputDataType.Routes, output_routes)
        result.export(nax.VehicleRoutingProblemOutputDataType.Directions, output_directions)
        if result.isPartialSolution:
            print("Some of the orders were not assigned.")
            result.export(nax.VehicleRoutingProblemOutputDataType.UnassignedStops, unassigned_stops)
    else:
        print("Solved failed")
        print(result.solverMessages())

    """

    __slots__ = ...
    def __init__(self, in_network, version=...) -> None:
        """Create a vehicle routing problem solver object based on the input network dataset.

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
