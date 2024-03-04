"""Concrete repository implementations for [Resource Name]."""

from typing import List, Optional

from app.base.entities import E
from app.base.exceptions import NotImplementedException
# from .abstract import
from app.typing import I


class _Repository(...):
    """Concrete implementation of the Repository for [Resource Name]."""

    def create(self, entity: E) -> E:
        # Implementation for creating an entity in the database
        raise NotImplementedException

    def read(self, identifier: I) -> Optional[E]:
        # Implementation for reading an entity by its identifier
        raise NotImplementedException

    def read_all(self) -> List[E]:
        # Implementation for reading all entities
        raise NotImplementedException

    def update(self, identifier: I, entity: E) -> E:
        # Implementation for updating an entity
        raise NotImplementedException

    def delete(self, identifier: I) -> None:
        # Implementation for deleting an entity
        raise NotImplementedException

# Implement AsyncRepository similarly if asynchronous operations are needed.
