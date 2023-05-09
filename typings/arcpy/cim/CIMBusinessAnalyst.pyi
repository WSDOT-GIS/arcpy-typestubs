"""
This type stub file was generated by pyright.
"""

from .CIMEnum import *
from .CIMExternal import *
from .CIMDocument import CIMVersion

class CIMBAVariableListVariable:
    """
    Represents variable of at variable list.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelAttractivenessVariable:
    """
    Represents attractiveness variable used in Huff Model.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelDistanceParameters:
    """
    Distance properties of the Huff Model calibration item.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationProfile:
    """
      Business Analyst segmentation profile. Segmentation profile represents
      distribution
    /// of the market (e.g. people or households)
      between the segments of the segmentation system.
    /// For example,
      it could represent the distribution of the customer base between
      the segments.
    /// Segmentation profile can include the volumetric
      information in addition to the counts,
    /// e.g. it could also
      provide the distribution of the sales between segments.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTarget:
    """
        Business Analyst segmentation target. Target is a collection of
        market segments
    /// that are treated as a whole. A user might
        apply the same marketing strategy to
    /// all segments in a target,
        for example.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroup:
    """
    Business Analyst target group. Target group represents a collection
    of targets.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroupVisualizationProperties:
    """
    Visualization properties of Business Analyst Segmentation target
    group.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAVariableList(CIMVersion):
    """
    Represents Business Analyst variable list.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelCalibrationDocument(CIMVersion):
    """
    Represents a Huff Model calibration.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationProfileDocument(CIMVersion):
    """
    Represents a document used for saving segmentation profile.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroupDocument(CIMVersion):
    """
    Represents a document used for saving target group.
    """

    def __init__(self, *args, **Kwargs) -> None: ...
