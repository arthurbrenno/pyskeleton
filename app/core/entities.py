"""Base classes for all entities in the application."""

from typing import TypeVar

from abc import ABC
from dataclasses import dataclass

@dataclass
class Entity(ABC):
    """Base class for entities in the application

    Args:
        BaseModel(class): Superclass
    """

@dataclass
class NullEntity(Entity):
    """Null entity Base class

    Args:
        Entity (class): Superclass
    """



E = TypeVar('E', bound=Entity)
