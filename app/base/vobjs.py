"""Value objects module.

This module defines value objects used across the application. Value objects are immutable
objects that are distinguished only by the values of their attributes. They do not have
a unique identity and are used to describe aspects of the domain with no conceptual identity.

Examples include objects representing amounts of money, quantities, or, as defined here,
identifiers that do not by themselves confer a distinct identity.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class ID:
    """A value object representing an identifier within the application.

    The ID class is used across the domain as a way to uniquely identify entities
    or other objects without embedding identity semantics within the value object itself.
    It encapsulates either a string or an integer value, allowing for flexibility in
    identifier schemes (e.g., UUIDs, numeric IDs, etc.).

    Attributes:
        val (str | int): The value of the identifier, which can be a string or an integer.
    """
    val: str | int
