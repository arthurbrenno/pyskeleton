"""Entities related to the [Resource Name] resource.

This module defines the domain models (entities) for the [Resource Name] resource,
extending the base Entity classes to include resource-specific fields
and behavior. Use data classes for simple data-holding structures
that map closely to database records.
"""

from dataclasses import dataclass

from app.base.entities import Entity, NullEntity

# Uncomment the following line if you're using Pydantic for validation
# from pydantic.dataclasses import dataclass


@dataclass
class _(Entity):
    """Represents a _ entity in the [Resource Name] domain.

    Extend this class to define properties and behaviors of [Resource Name]'s entities.
    
    Attributes:
        ...
    """


@dataclass
class _(NullEntity):
    """A null object pattern implementation for [Resource Name] entities.

    Use this class to represent a null or default state of [Resource Name] entities,
    providing a non-null default object that adheres to the Entity interface.
    """
