"""
This type stub file was generated by pyright.
"""

from .CIMEnum import *
from .CIMExternal import *

class CIMColor:
    """
    Supports colors in the CIM model by providing low level access
    to properties common amongst all color types.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorRamp:
    """
    Supports color ramp schemes in the CIM model by providing low level
    access to properties common amongst all color ramp types.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorSpace:
    """
    Supports colors spaces by providing a common base type for all
    color spaces.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCMYKColor(CIMColor):
    """
    Represents a color in the CMYK color model.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMContinuousColorRamp(CIMColorRamp):
    """
    Supports continuous color ramp schemes by providing low level access
    to properties common amongst all continuous color ramp types.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFixedColorRamp(CIMColorRamp):
    """
    Represents a color scheme composed of discrete colors.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGrayColor(CIMColor):
    """
    Represents a grayscale color defined by lightness.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHSLColor(CIMColor):
    """
    Represents a color defined by hue, saturation, and lightness.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHSVColor(CIMColor):
    """
    Represents a color defined by hue, saturation, and brightness (value).
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMICCColorSpace(CIMColorSpace):
    """
    Represents a color space defined by an International Color Consortium
    (ICC) color profile.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLABColor(CIMColor):
    """
    Represents a color defined in the LAB color space.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinearContinuousColorRamp(CIMContinuousColorRamp):
    """
    Represents a linear continuous color ramp scheme.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipartColorRamp(CIMColorRamp):
    """
    Represents a multipart color ramp scheme.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPolarContinuousColorRamp(CIMContinuousColorRamp):
    """
    Represents a polar continuous color ramp scheme.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRGBColor(CIMColor):
    """
    Represents a color in the RGB color model.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRandomHSVColorRamp(CIMColorRamp):
    """
    Represents a random HSV color ramp scheme.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSpotColor(CIMColor):
    """
    Represents a spot color.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSpotColorSpace(CIMColorSpace):
    """
    Represents a color space for spot colors.
    """

    def __init__(self, *args, **Kwargs) -> None: ...

class CIMXYZColor(CIMColor):
    """
    Represents a color in the XYZ color model.
    """

    def __init__(self, *args, **Kwargs) -> None: ...
