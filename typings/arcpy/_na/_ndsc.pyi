"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from typing import Iterable, Union
from enum import IntEnum

class Attribute:
    """The unique identifier of a network attribute within a network dataset."""

    ...

class NetworkTimeUsage(IntEnum):
    """Enumeration for time usage types."""

    Unused = ...
    BeforeTraversal = ...
    AfterTraversal = ...

class AttributeUsage(IntEnum):
    """Enumeration for network attribute usage types."""

    Cost = ...
    Descriptor = ...
    Restriction = ...
    Hierarchy = ...

class AttributeParameterUsage(IntEnum):
    """Enumeration for network attribute parameter usage types."""

    General = ...
    Restriction = ...

class AttributeParameter:
    """A parameter associated with a network attribute."""

    @property
    def name(self) -> str:
        """The attribute parameter name."""
        ...
    @property
    def value(self) -> Union[float, int, str, bool, None]:
        """The attribute parameter value."""
        ...
    @property
    def usage(self) -> AttributeParameterUsage:
        """The attribute parameter usage."""
        ...

class NetworkElement:
    """A network element of the network dataset."""

    @property
    def isJunction(self) -> bool:
        """Indicates if the network element is a junction."""
        ...
    @property
    def isTurn(self) -> bool:
        """Indicates if the network element is a turn."""
        ...
    @property
    def isEdge(self) -> bool:
        """Indicates if the network element is an edge."""
        ...

class Edge(NetworkElement):
    """An edge."""

    @property
    def isAlong(self) -> bool:
        """Indicates if the direction of the edge is along the source feature."""
        ...
    @property
    def isAgainst(self) -> bool:
        """Indicates if the direction of the edge is against the source feature."""
        ...
    @property
    def opposite(self) -> Edge:
        """The edge that is the opposite direction of the current edge."""
        ...

class Junction(NetworkElement):
    """A junction."""

    ...

class Turn(NetworkElement):
    """A turn."""

    ...

class NetworkQuery:
    """Provides access to the properties, attributes, attribute values, and elements of a network dataset."""

    @property
    def networkName(self) -> str:
        """The name of the network."""
        ...
    @property
    def sourceNames(self) -> Iterable[str]:
        """The names of the sources referenced by the network."""
        ...
    def attribute(self, attribute_name: str) -> Attribute | None:
        """Return an attribute of the specified attribute name.

        If the attribute name is not found, None will be returned.

        Args:
            attribute_name (str): Name of the network attribute.

        Returns:
            Attribute:  An attribute object.
        """
        ...
    def attributeUsage(self, attribute: Attribute) -> AttributeUsage:
        """Return usage type of the specified attribute.

        Args:
            attribute (Attribute): Attribute id as an attribute object.

        Returns:
            AttributeUsage: An attribute usage enum.
        """
        ...
    def attributeParameters(self, attribute: Attribute) -> Iterable[AttributeParameter]:
        """Return the parameters of the specified attribute.

        Args:
            attribute (Attribute): Attribute id as an attribute object.

        Returns:
            Iterable[AttributeParameter]: Iterable of attribute parameters.
        """
        ...
    def fromJunction(self, edge: Edge) -> Junction:
        """Return the 'from' junctions for the specified edge."""
        ...
    def toJunction(self, edge: Edge) -> Junction:
        """Return the 'to' junctions for the specified edge."""
        ...
    def atJunction(self, turn: Turn) -> Junction:
        """Return the junction that connects first and second edges of the turn.

        Args:
            turn (Turn): Turn to get junction for.

        Returns:
            Junction: Junction that connects first and second edges of the turn.
        """
        ...
    def turns(self, junction: Junction) -> Iterable[Turn]:
        """Return the turns for the specified junction where the junction connects the first and second edges of each turn.

        Args:
            junction (Junction): Junction to get turns for.

        Returns:
            Iterable[Turn]: Iterable of turns.
        """
        ...
    def edges(self, element: Junction | Turn) -> Iterable[Edge]:
        """Return the edges that are connected to the specified element.

        Args:
            element (Junction | Turn): Element to get edges for.

        Returns:
            Iterable[Edge]: Iterable of edges.
        """
        ...
    def edgePositions(self, edge: Edge) -> tuple[float, float]:
        """Return the 'from' and 'to' positions along the source feature for the specified edge.

        This uses the digitization direction of the source feature.
        The values are in the range of 0.0 to 1.0

        Args:
            edge (Edge): Edge to get positions for.

        Returns:
            tuple[float, float]: Tuple containing the 'from' and 'to' position values.
        """
        ...
    def edgeAzimuths(self, edge: Edge) -> tuple[float, float]:
        """Return the 'from' and 'to' azimuths for the specified edge.

        Args:
            edge (Edge): Edge to get azimuths for.

        Returns:
            tuple[float, float]: Tuple containing the 'from' and 'to' azimuths values.
        """
        ...
    def sourceInfo(self, element: Junction | Edge | Turn) -> tuple[int, int]:
        """Return source information for the specified network element.

        Args:
            element (Junction | Edge | Turn): Element to get source information for.

        Returns:
            tuple[int, int]: Tuple of network source id and network source object id.
        """
        ...
    def attributeValue(
        self,
        element: Junction | Edge | Turn,
        attribute: Attribute,
        time_usage: NetworkTimeUsage = ...,
        local_time: datetime | None = ...,
    ) -> Union[int, float, bool]:
        """Attribute value for a specified element, with optional time.

        Args:
            element (Junction | Edge | Turn): Element to get the attribute value for.
            attribute (Attribute): The attribute to get the value for.
            time_usage (NetworkTimeUsage, optional): The time usage type. Defaults to NetworkTimeUsage.Unused.
            local_time (datetime | None, optional): The time to get the attribute value for. Defaults to None.

        Returns:
            Union[int, float, bool]: The attribute value for a specified element at a given time.
        """
        ...

class AttributeEvaluator:
    """Base class for network attribute custom evaluator."""

    def __init__(
        self, attribute_name: str, specific_sources: list[str] | None = ...
    ) -> None:
        """Initialize of attribute evaluator object.

        If specific sources is not set then the custom evaluator will apply to all sources.

        Args:
            attribute_name (str): Name of the network attribute.
            specific_sources (list[str] | None, optional): List of specific network source names. Defaults to None.
        """
        ...
    @property
    def attributeName(self) -> str:
        """The network attribute name that the custom evaluator applies to."""
        ...
    @property
    def attribute(self) -> Attribute:
        """The network attribute that the custom evaluator applies to."""
        ...
    @property
    def sourceNames(self) -> list[str]:
        """The list of network source names that the custom evaluator applies to."""
        ...
    @property
    def networkQuery(self) -> NetworkQuery:
        """The network query object for the network the attribute evaluator is attached to.

        Returns:
            NetworkQuery: NetworkQuery object or None if the evaluator was not attached yet.
        """
        ...
    @property
    def attached(self) -> bool:
        """Indicates if the evaluator is attached to a network.

        Returns:
            bool: True if the evaluator is correctly attached to the network dataset.
        """
        ...
    def attach(self, network_query: NetworkQuery) -> bool:
        """Used to verify that the attribute evaluator can be applied to the network.

        Validation of attributes and resources can be done in this method.
        Invoked when the custom evaluator is attached to the network dataset.
        Can be invoked multiple times depending upon the number of threads accessing the network.

        Args:
            network_query (NetworkQuery): Network query instance for current network dataset.

        Returns:
            bool: True if the network has the specified attribute.
        """
        ...
    def refresh(self) -> None:
        """Used to for state management of the attribute evaluator.

        This method can be use to refresh the evaluator's state, such as resources can be read,
        internal caches can be refreshed, etc.
        Invoked on just prior to each a solve being executed.
        """
        ...
    def edgeValue(self, edge: Edge) -> Union[int, float, bool]:
        """Used to set the final evaluated attribute value for an edge.

        Custom logic can be applied in this method to determine the final attribute value.
        Invoked at the end of solver's evaluation of the edge.

        Args:
            edge (Edge): Edge being evaluated.

        Returns:
            Union[int, float, bool]: Returns the attribute value back to the solver.
        """
        ...
    def edgeValueAtTime(
        self, edge: Edge, time: datetime, time_usage: NetworkTimeUsage
    ) -> Union[int, float, bool]:
        """Used to set the final evaluated attribute value for an edge, when time is used.

        Custom logic can be applied in this method to determine the final attribute value.
        Invoked at the end of solver's evaluation of the edge, when time has
        been used (for evaluators that support time).

        Args:
            edge (Edge): Edge being evaluated.
            time (datetime): Time the edge would be encountered along the route.
            time_usage (NetworkTimeUsage): Time usage type.

        Returns:
            Union[int, float, bool]: Returns the attribute value back to the solver.
        """
        ...
    def junctionValue(self, junction: Junction) -> Union[int, float, bool]:
        """Used to set the final evaluated attribute value for a junction.

        Custom logic can be applied in this method to determine the final attribute value.
        Invoked at the end of solver's evaluation of the junction.

        Args:
            junction (Junction): Junction being evaluated.

        Returns:
            Union[int, float, bool]: Returns the attribute value back to the solver.
        """
        ...
    def junctionValueAtTime(
        self, junction: Junction, time: datetime, time_usage: NetworkTimeUsage
    ) -> Union[int, float, bool]:
        """Used to set the final evaluated attribute value for a junction, when time is used.

        Custom logic can be applied in this method to determine the final attribute value.
        Invoked at the end of solver's evaluation of the junction, when time has
        been used (for evaluators that support time).

        Args:
            junction (Junction): Junction being evaluated.
            time (datetime): Time the junction would be encountered along the route.
            time_usage (NetworkTimeUsage): Time usage type.

        Returns:
            Union[int, float, bool]: Returns the attribute value back to the solver.
        """
        ...
    def turnValue(self, turn: Turn) -> Union[int, float, bool]:
        """Used to set the final evaluated attribute value for a turn.

        Custom logic can be applied in this method to determine the final attribute value.
        Invoked at the end of solver's evaluation of the turn.

        Args:
            turn (Turn): Turn being evaluated.

        Returns:
            Union[int, float, bool]: Returns the attribute value back to the solver.
        """
        ...
    def turnValueAtTime(
        self, turn: Turn, time: datetime, time_usage: NetworkTimeUsage
    ) -> Union[int, float, bool]:
        """Used to set the final evaluated attribute value for a turn, when time is used.

         Custom logic can be applied in this method to determine the final attribute value.
         Invoked at the end of solver's evaluation of the turn, when time has
         been used (for evaluators that support time).

        Args:
            turn (Turn): Turn being evaluated.
            time (datetime): Time the turn would be encountered along the route.
            time_usage (NetworkTimeUsage): Time usage type.

        Returns:
            Union[int, float, bool]: Returns the attribute value back to the solver.
        """
        ...
