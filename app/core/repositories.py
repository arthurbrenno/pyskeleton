"""Base interfaces for all repositories in the application."""

from abc import ABC, abstractmethod
from typing import Any, Generic, List, TypeVar, Union

from app.core.entities import E
from app.core.exceptions import NotImplementedException


class AsyncRepository(ABC, Generic[E]):
    """Base repository class for all repositories"""

    @abstractmethod
    async def create(self,
                     entity: E,
                     **kwargs: object) -> Any:
        """Creates an entity inside the repository asynchronously.

        Args:
            entity (E): The entity to be created

        Raises:
            NotImplementedError: Method not implemented by subclass

        Returns:
            Any: Can return implementation-defined objects.
        """
        raise NotImplementedException

    @abstractmethod
    async def read(self,
                   identifier: Union[int, str],
                   **kwargs: object) -> E:
        """Reads one entity from the repository

        Args:
            identifier (int): The entity id to be read

        Raises:
            NotImplementedError: Method not implemented

        Returns:
            Entity: The entity being read
        """
        raise NotImplementedException

    @abstractmethod
    async def read_all(self,
                       **kwargs: object) -> List[E]:
        """Reads all entities from the repository asynchronously.

        Args:
            kwargs (object): external parameters

        Raises:
            NotImplementedError: Method not implemented.

        Returns:
            T: _description_
        """
        raise NotImplementedException

    @abstractmethod
    async def update(self,
                     identifier: Union[str, int],
                     entity: E,
                     **kwargs: object) -> Any:
        """Updates one entity inside the repository asynchronously.

        Args:
            id (Union[str, int]): The entity id to be updated
            entity (E): The data to be updated

        Raises:
            NotImplementedError: If the method
            was called and the subclass didn't implement it.

        Returns: Optional[Union[bool, Any]]: Can return
        either a boolean indicating success or Any for
        implementation-defined returns.
        """
        raise NotImplementedException

    @abstractmethod
    async def delete(self,
                     identifier: Union[str, int],
                     **kwargs: object) -> Any:
        """Deletes an entity from the repository asynchronously.

        Args:
            identifier: The entity id to be deleted.

        Raises:
            NotImplementedError: If the method was
            called and the subclass didn't implement it.

        Returns: Union[bool, Any]: Most implementations will
        only return a boolean, but implementations can define
        their own return types.9
        """
        raise NotImplementedException


class Repository(ABC, Generic[E]):
    """Base repository class for all repositories"""

    @abstractmethod
    def create(self,
               entity: E,
               **kwargs: object) -> Any:
        """Creates an entity inside the repository.

        Args:
            entity (E): The entity to be created

        Raises:
            NotImplementedError: Method not implemented by subclass

        Returns:
            Any: Can return implementation-defined objects.
        """
        raise NotImplementedException

    @abstractmethod
    def read(self,
             identifier: int,
             **kwargs: object) -> E:
        """Reads one entity from the repository

        Args:
            identifier (int): The entity id to be read

        Raises:
            NotImplementedError: _description_

        Returns:
            Entity: The entity being read
        """
        raise NotImplementedException

    @abstractmethod
    def read_all(self,
                 **kwargs: object) -> List[E]:
        """Reads all entities from the repository.

        Args:
            kwargs (object): external parameters

        Raises:
            NotImplementedError: Method not implemented.

        Returns:
            T: _description_
        """
        raise NotImplementedException

    @abstractmethod
    def update(self,
               identifier: Union[str, int],
               entity: E,
               **kwargs: object) -> Any:
        """Updates one entity inside the repository.

        Args:
            identifier(Union[str, int]): The entity id to be updated
            entity (E): The data to be updated

        Raises:
            NotImplementedError: If the method was called and
            the subclass didn't implement it.

        Returns:
            Optional[Union[bool, Any]]: Can return either a boolean
            indicating success or Any for implementation-defined returns.
        """
        raise NotImplementedException

    @abstractmethod
    def delete(self,
               identifier: Union[str, int],
               **kwargs: object) -> Any:
        """Deletes an entity from the repository.

        Args:
            identifier: The entity id to be deleted.

        Raises:
            NotImplementedError: If the method was called
            and the subclass didn't implement it.

        Returns:
            Union[bool, Any]: Most implementations will
            only return a boolean, but implementations
            can define their own return types.
        """
        raise NotImplementedException


class NullRepository(Repository[E]):
    """A null repository that does nothing"""

    def create(self,
               entity: E,
               **kwargs: object) -> Any:
        return None

    def read(self,
             identifier: int,
             **kwargs: object) -> E:
        return None

    def read_all(self,
                 **kwargs: object) -> List[E]:
        return []

    def update(self,
               identifier: Union[str, int],
               entity: E,
               **kwargs: object) -> Any:
        return None

    def delete(self,
               identifier: Union[str, int],
               **kwargs: object) -> Any:
        return None


R = TypeVar("R", bound=AsyncRepository | Repository | NullRepository)
