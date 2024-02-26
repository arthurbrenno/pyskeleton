"""Base interfaces for all repositories in the application.

Defines abstract base classes for synchronous and asynchronous repositories, facilitating
data access and manipulation across various storage mechanisms. These base classes ensure
a consistent interface for CRUD operations, supporting a clean architecture and
separation of concerns within the application.
"""

from abc import ABC, abstractmethod
from typing import Any, Generic, List, TypeVar, Union

from app.base.entities import E
from app.base.exceptions import NotImplementedException
from app.typing import I


class AsyncRepository(ABC, Generic[E]):
    """Abstract base class for asynchronous repositories.

    Provides a generic interface for asynchronous CRUD operations and other data access
    logic, ensuring consistency and reusability across different parts of the application.
    """

    @abstractmethod
    async def create(self, entity: E) -> Any:
        """Asynchronously creates a new entity in the repository."""
        raise NotImplementedException

    @abstractmethod
    async def read(self, identifier: I) -> E:
        """Asynchronously retrieves an entity by its identifier from the repository."""
        raise NotImplementedException

    @abstractmethod
    async def read_all(self) -> List[E]:
        """Asynchronously retrieves all entities from the repository."""
        raise NotImplementedException

    @abstractmethod
    async def update(self, identifier: I, entity: E) -> Any:
        """Asynchronously updates an existing entity in the repository."""
        raise NotImplementedException

    @abstractmethod
    async def delete(self, identifier: I) -> Any:
        """Asynchronously removes an entity from the repository."""
        raise NotImplementedException

class Repository(ABC, Generic[E]):
    """Abstract base class for synchronous repositories.

    Defines the standard CRUD operations and additional data access methods for managing entities,
    ensuring a consistent interface for data access across the application.
    """

    @abstractmethod
    def create(self, entity: E) -> Any:
        """Creates a new entity in the repository."""
        raise NotImplementedException

    @abstractmethod
    def read(self, identifier: I) -> E:
        """Retrieves an entity by its identifier from the repository."""
        raise NotImplementedException

    @abstractmethod
    def read_all(self) -> List[E]:
        """Retrieves all entities from the repository."""
        raise NotImplementedException

    @abstractmethod
    def update(self, identifier: I, entity: E) -> Any:
        """Updates an existing entity in the repository."""
        raise NotImplementedException

    @abstractmethod
    def delete(self, identifier: I) -> Any:
        """Removes an entity from the repository."""
        raise NotImplementedException

class NullRepository(Repository[E]):
    """Implementation of the Null Object pattern for repositories.

    A non-operative repository used for testing or as a default implementation,
    where no action is taken on method calls.
    """

    def create(self, entity: E) -> None:
        return None

    def read(self, identifier: I) -> None:
        return None

    def read_all(self) -> List[E]:
        return []

    def update(self, identifier: I, entity: E) -> None:
        return None

    def delete(self, identifier: I) -> None:
        return None

R = TypeVar("R", bound=Union[AsyncRepository, Repository, NullRepository])
