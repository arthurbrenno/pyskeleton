"""Abstract repository interface for [Resource Name].

This module defines an abstract repository interface for [Resource Name], extending
the generic Repository interface to include [Resource Name]-specific data access
operations. It encapsulates the abstract methods that must be implemented by any
concrete repository class for [Resource Name], ensuring consistency and adherence
to the domain-driven design principles.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from app.base.entities import E  # Ensure E is replaced with the actual entity class for this resource
from app.base.exceptions import NotImplementedException
from app.base.repositories import Repository
from app.typing import I

class ResourceRepository(Repository[E], ABC):
    """Abstract repository interface for [Resource Name] entities.
    
    Provides an abstract base for [Resource Name]-specific repository operations,
    extending the generic CRUD operations defined in the base Repository interface.
    """

    @abstractmethod
    def create(self, entity: E) -> E:
        """Creates and returns a new [Resource Name] entity."""
        raise NotImplementedException

    @abstractmethod
    def read(self, identifier: I) -> Optional[E]:
        """Retrieves a [Resource Name] entity by its identifier, if found."""
        raise NotImplementedException

    @abstractmethod
    def read_all(self) -> List[E]:
        """Retrieves all [Resource Name] entities."""
        raise NotImplementedException

    @abstractmethod
    def update(self, identifier: I, entity: E) -> E:
        """Updates and returns an existing [Resource Name] entity."""
        raise NotImplementedException

    @abstractmethod
    def delete(self, identifier: I) -> None:
        """Deletes a [Resource Name] entity by its identifier."""
        raise NotImplementedException
