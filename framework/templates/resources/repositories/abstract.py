"""Abstract repository --related to this resource -- to depend from."""

from abc import ABC, abstractmethod
from typing import Any, List, Union

from app.core.entities import E
from app.core.exceptions import NotImplementedException
from app.core.repositories import Repository


class _Repository(Repository[E], ABC):
    @abstractmethod
    def create(self,
               entity: ...,
               **kwargs: object) -> ...:
        raise NotImplementedException

    @abstractmethod
    def read(self,
             identifier: int,
             **kwargs: object) -> ...:
        raise NotImplementedException

    @abstractmethod
    def read_all(self,
                 **kwargs: object) -> ...:
        raise NotImplementedException

    @abstractmethod
    def update(self,
               identifier: Union[str, int],
               entity: ...,
               **kwargs: object) -> ...:
        raise NotImplementedException

    @abstractmethod
    def delete(self,
               identifier: Union[str, int],
               **kwargs: object) -> ...:
        raise NotImplementedException
