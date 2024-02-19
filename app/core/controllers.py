"""Basic interface (contract) for all controllers in the application"""

from abc import ABC, abstractmethod
from typing import Any

from app.core.exceptions import NotImplementedException
from app.core.requests import NullRequest, Req
from app.core.services import S
from app.typing import ID, M


class Controller(ABC):
    """Base class for all controllers.

    Args:
        `ABC` (class): Abstract Base Class

    Raises:
        `NotImplementedError`: post method not implemented
        `NotImplementedError`: get method not implemented
        `NotImplementedError`: get_all method not implemented
        `NotImplementedError`: put method not implemented
        `NotImplementedError`: delete method not implemented
        `NotImplementedError`: options method not implemented
        `NotImplementedError`: health method not implemented
    """
    @abstractmethod
    async def post(self,
                   request_body: M,
                   request: Req = NullRequest) -> M:
        """Post method for the controller."""
        raise NotImplementedException

    @abstractmethod
    async def get(self,
                  identifier: ID,
                  request: Req = NullRequest) -> M:
        """Get method for the controller."""
        raise NotImplementedException

    @abstractmethod
    async def get_all(self,
                      request: Req = NullRequest) -> M:
        """Get all method for the controller."""
        raise NotImplementedException

    @abstractmethod
    async def put(self,
                  identifier: ID,
                  request_body: M,
                  request: Req = NullRequest) -> M:
        """Put method for the controller."""
        raise NotImplementedException

    @abstractmethod
    async def delete(self,
                     identifier: ID,
                     request: Req = NullRequest) -> M:
        """Delete method for the controller."""
        raise NotImplementedException

    @abstractmethod
    async def options(self,
                      request: Req = NullRequest) -> M:
        """Options method for the controller."""
        raise NotImplementedException

    @abstractmethod
    async def health(self,
                     request: Req = NullRequest) -> M:
        """Health method for the controller."""
        raise NotImplementedException
