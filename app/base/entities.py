"""Base classes for all entities in the application."""

from abc import ABC
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, TypeVar

from app.base.value_objects import ID, NullID


@dataclass
class Entity(ABC):
    """Abstract base class for all entities in the application.

    Entities are foundational data objects with an optional identifier and creation timestamp,
    accommodating new entities that have not yet been persisted.

    Attributes:
        _id (Optional[ID]): The unique identifier for the entity. None for new entities.
        created_at (Optional[datetime]): The timestamp of when the
        entity was created. None for new entities.
    """
    _id: ID = NullID
    created_at: Optional[datetime] = None


    def mark_as_persisted(self, _id: ID, created_at: Optional[datetime] = None):
        """Updates the entity's identifier and creation timestamp upon persistence.

        Args:
            _id (ID): The unique identifier assigned upon persistence.
            created_at (Optional[datetime]): The creation timestamp, defaults to
            the current UTC time if not provided.
        """
        self._id = _id
        if created_at is None:
            self.created_at = datetime.now(timezone.utc)
        else:
            self.created_at = created_at


@dataclass
class NullEntity(Entity):
    """Implementation of the null object pattern for entities.

    Represents a null or "empty" state for an entity, useful for avoiding null checks
    and providing a default, non-operative entity object.
    """
    id: ID = NullID
    created_at: datetime = None


E = TypeVar('E', bound=Entity)
