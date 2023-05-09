import re
from json import dumps
from logging import getLogger
from typing import Any, NamedTuple, Optional

from arcpy import Filter, GetParameterInfo, ListToolboxes, ListTools, Parameter

_LOGGER = getLogger()


class ToolTuple(NamedTuple):
    full_name: str
    tool_name: str
    toolbox_alias: str


class ToolParameterTuple(NamedTuple):
    full_name: str
    tool_name: str
    toolbox_alias: str
    parameter: Parameter


class ToolboxNameTuple(NamedTuple):
    name: str
    alias: str


class PropertyNameValueTuple(NamedTuple):
    name: str
    value: Optional[str]


class ToolInfoTuple(NamedTuple):
    toolbox_name: str
    toolbox_alias: str
    full_tool_name: str
    tool_name: str
    tool_properties: list[PropertyNameValueTuple]


def parse_toolbox_into_name_and_alias(toolbox_name: str):
    """Splits a toolbox name in `Toolbox Full Name(alias)` format
    into a tuple of the name and the alias.

    Args:
        toolbox_name (str): The name of a toolbox returned from arcpy.ListToolboxes()

    Raises:
        ValueError: Raised when the toolbox_name is not in the expected format.

    Returns:
        ToolboxNameTuple: Returns a tuple containing the name and
        alias of the toolbox, respectively.
    """
    name_re = re.compile(r"^(?P<name>.+)\((?P<alias>.+)\)$")
    match = name_re.match(toolbox_name)
    if not match:
        raise ValueError(f'"{toolbox_name}" does not match\t{name_re}')
    return ToolboxNameTuple(*match.groups())


def list_toolboxes(wild_card: Optional[str] = None):
    """A generator function that calls arcpy.ListToolboxes and then
    yields each item in the returned array as a tuple of name and alias
    pairs.

    Args:
        wild_card (Optional[str], optional): Same as used with the arcpy.ListToolboxes function. Defaults to None.

    Yields:
        Yields tuples of name and alias pairs.
    """
    return (parse_toolbox_into_name_and_alias(t) for t in ListToolboxes(wild_card))


def get_tb_alias_from_tool_name(name: str):
    """Parses a tool's name, as returned by arcpy.ListTools, into
    a tuple of the full name, tool name portion, and the alias of
    the toolbox that contains the tool.

    Args:
        name: The name of a tool as returned by arcpy.ListTools,

    Raises:
        ValueError: Raised if input string is not in the expected format

    Returns:
        A tuple consisting of the following:

        - The input string
        - The tool name portion
        - The toolbox alias portion
    """
    logger = _LOGGER.getChild(get_tb_alias_from_tool_name.__name__)
    # Matches the underscore that separates the alias part of the name from the rest.
    tool_name_re = re.compile(r"(?P<tool>.+)_(?P<alias>.+)$", re.IGNORECASE)

    match = tool_name_re.match(name)

    if not match:
        raise ValueError(f"{name} does not match {tool_name_re}")

    parts: tuple[str, str] = match.groups()

    if len(parts) != 2:
        logger.warning(
            f'Expected "{name}" to be able to be split into tool name and toolbox alias. Actual result was "{parts}"'
        )

    tool_name, toolbox_alias = parts

    return ToolTuple(name, tool_name, toolbox_alias)


def enumerate_tool_info(wild_card: Optional[str] = None):
    class ToolboxTuple(NamedTuple):
        name: str
        alias: str
        tools: list[str]

    toolboxes = (
        ToolboxTuple(name, alias, ListTools(f"*_{alias}"))
        for (name, alias) in list_toolboxes(wild_card=wild_card)
    )

    for toolbox_name, toolbox_alias, tools in toolboxes:
        for full_tool_name, tool_name, _ in (
            get_tb_alias_from_tool_name(t) for t in tools
        ):
            parameters = (
                (p, get_parameter_properties(p))
                for p in GetParameterInfo(full_tool_name)
            )
            for _, p_props in parameters:
                yield ToolInfoTuple(
                    toolbox_name, toolbox_alias, full_tool_name, tool_name, [*p_props]
                )


def get_parameter_properties(parameter: Parameter):
    logger = _LOGGER.getChild(get_parameter_properties.__name__)

    class PropertyTuple(NamedTuple):
        name: str
        definition: Optional[Any]

    # Get all the properties of a Parameter object
    properties = (
        pt
        for pt in (
            PropertyTuple(d, getattr(Parameter, d, None))
            for d in dir(Parameter)
            # Filter out "private" properties
            if not d.startswith("_")
        )
        if pt.definition is not None and type(pt.definition) == property
    )

    def format_filter(filter: Filter):
        out_dict = {"list": filter.list, "type": filter.type}
        return dumps(out_dict)

    for name, _ in properties:
        logger.debug(f"Parameter property: {parameter.name}: {name}")
        value = None
        try:
            value = getattr(parameter, name)
        except AttributeError as a_ex:
            logger.exception(a_ex)
            continue
        except RuntimeError as r_ex:
            logger.exception(r_ex)
            continue
        else:
            if isinstance(value, Filter):
                yield PropertyNameValueTuple(name, format_filter(value))
            else:
                yield PropertyNameValueTuple(name, value)
