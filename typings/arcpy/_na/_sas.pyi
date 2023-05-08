"""
This type stub file was generated by pyright.
"""

from enum import IntEnum
from arcgisscripting import na as cna

"""Module for working with Service Area Solver."""
__all__ = ["ServiceAreaInputDataType", "ServiceAreaOutputDataType", "ServiceAreaPolygonCutoffGeometry", "ServiceAreaOverlapGeometry", "ServiceAreaPolygonDetail", "ServiceAreaOutputType", "ServiceArea"]
class ServiceAreaInputDataType(IntEnum):
    """Enumeration for feature class names used by the Service Area solver to store inputs."""
    Facilities = ...
    PointBarriers = ...
    LineBarriers = ...
    PolygonBarriers = ...


class ServiceAreaOutputDataType(IntEnum):
    """Enumeration for feature class names used by the Service Area solver to store outputs."""
    Facilities = ...
    Lines = ...
    Polygons = ...


class ServiceAreaPolygonCutoffGeometry(IntEnum):
    """Enumeration for supported polygon cutoff geometry types."""
    Disks = ...
    Rings = ...


class ServiceAreaOverlapGeometry(IntEnum):
    """Enumeration for the behavior of service-area output from multiple facilities in relation to one another."""
    Split = ...
    Overlap = ...
    Dissolve = ...


class ServiceAreaPolygonDetail(IntEnum):
    """Enumeration for supported polygon detail options."""
    Generalized = ...
    Standard = ...
    High = ...


class ServiceAreaOutputType(IntEnum):
    """Enumeration for the type of output to be generated."""
    Polygons = ...
    Lines = ...
    PolygonsAndLines = ...


class ServiceArea(cna.ServiceArea):
    """Perform route analysis.

    # An example showing how to perform service area analysis using a feature class for input facilities.
    import arcpy
    import arcpy._na as nax

    nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
    nd_layer_name = "Routing_ND"
    input_facilities = "C:/data/io.gdb/Facilities"
    output_polygons = "C:/data/io.gdb/ServiceAreaPolygons"

    arcpy.CheckOutExtension("network")
    arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
    nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
    travel_mode = nd_travel_modes["Driving Time"]
    service_area = nax.ServiceArea(nd_layer_name)
    service_area.defaultImpedanceCutoffs = [5, 10, 15]
    service_area.travelMode = travel_mode
    service_area.geometryAtOverlap = nax.ServiceAreaOverlapGeometry.Split
    service_area.load(nax.ServiceAreaInputDataType.Facilities, input_facilities)
    result = service_area.solve()
    if result.solveSucceeded:
        result.export(nax.ServiceAreaOutputDataType.Polygons, output_polygons)
    else:
        print("Solved failed")
        print(result.solverMessages())

    """
    __slots__ = ...
    def __init__(self, in_network) -> None:
        """Create a service area solver object based on the input network dataset.

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
    


