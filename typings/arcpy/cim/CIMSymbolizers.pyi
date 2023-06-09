"""
This type stub file was generated by pyright.
"""

from .CIMEnum import *
from .CIMExternal import *

class CIMBivariateFieldInfo:
    """
    Contains a collection of properties that describe a bivariate attribute
    field.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClassBreak:
    """
    Represents a class break.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExpressionInfo:
    """
    Represents the properties required for authoring an Arcade expression.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPrimitiveOverride:
    """
    Represents a primitive override.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProportionalPieSizeOptions:
    """
    Represents proportional pie size options.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRenderer:
    """
    Represents a renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRendererAuthoringInfo:
    """
    Represents additional authoring properties used by a renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRuleSymbolLayerNames:
    """
    Represents rule symbol layer names.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScaleDependentSizeVariation:
    """
    Represents the scale dependent size variations for a symbol reference.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStringMap:
    """
    Represents a string map of key value pairs.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolReference:
    """
    Represents a symbol reference.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolizationRule:
    """
    Represents a symbolization rule.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValue:
    """
    Represents a unique value.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueClass:
    """
    Represents a unique value class.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueGroup:
    """
    Represents a unique value group.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUnitSymbolization:
    """
    Represents unit symbolization.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariable:
    """
    Represents a visual variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariableAuthoringInfo:
    """
    Represents visual variable metadata used for authoring.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariableInfo:
    """
    Represents visual variable info.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariableLevel:
    """
    Represents a level-of-detail for a multilevel visual variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartRenderer(CIMRenderer):
    """
    Represents chart renderer which contains properties common to all
    symbolizers that depict some feature value as a chart drawn on
    top of the feature itself.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClassBreaksRendererBase(CIMRenderer):
    """
    The base class for class breaks renderer types.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorVisualVariable(CIMVisualVariable):
    """
    Represents a color visual variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDictionaryRenderer(CIMRenderer):
    """
    Represents a dictionary renderer where symbols are drawn from a
    symbol dictionary.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDotDensityRenderer(CIMRenderer):
    """
    Represents a dot density renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHeatMapRenderer(CIMRenderer):
    """
    Represents a heat map renderer.
      /// The Heat Map Renderer draws point features as a continuous
    /// color gradient representing the density of the points. The
    resulting /// density surface represents the physical proximity
    between points, /// optionally weighted by a specified attribute
    value. The displayed /// raster surface is dynamic and morphs according
    to the zoom level /// and updates if the source point features
    are edited.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultilevelVisualVariable(CIMVisualVariable):
    """
    Represents a visual variable with different levels-of-detail, each
    with its own minimum and maximum data values. Used for binning
    layers.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProportionalRenderer(CIMRenderer):
    """
    Represents a proportional renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRepresentationRenderer(CIMRenderer):
    """
    Represents a representation renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRotationVisualVariable(CIMVisualVariable):
    """
    Represents a rotation visual variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRuleRenderer(CIMRenderer):
    """
    Represents a rule renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSimpleRenderer(CIMRenderer):
    """
    Represents a simple renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSizeVisualVariable(CIMVisualVariable):
    """
    Represents a size visual variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTransparencyVisualVariable(CIMVisualVariable):
    """
    Represents a transparency visual variable.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueRenderer(CIMRenderer):
    """
    Represents a unique value renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueRendererAuthoringInfo(CIMRendererAuthoringInfo):
    """
    Represents additional authoring properties used by a unique value
    renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBivariateRendererAuthoringInfo(CIMUniqueValueRendererAuthoringInfo):
    """
    Represents additional authoring properties used by a bivariate
    choropleth renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClassBreaksRenderer(CIMClassBreaksRendererBase):
    """
    Represents a class break renderer.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultilevelColorVisualVariable(CIMMultilevelVisualVariable):
    """
    Represents a color visual variable with different levels-of-detail.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultilevelSizeVisualVariable(CIMMultilevelVisualVariable):
    """
    Represents a size visual variable with different levels-of-detail.
    """

    def __init__(self, *args, **Kwargs) -> None: ...
