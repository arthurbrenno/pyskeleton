"""Basic interface (contract) for all controllers in the application"""

from abc import ABC, abstractmethod
from typing import Type

from fastapi import Request, UploadFile

from app.base.exceptions import NotImplementedException
from app.base.validators import V
from app.typing import ID, M


class Controller(ABC):
    """Abstract base class for all controllers in the application.

    This class defines the contract that all controllers must follow, specifying
    methods for handling standard HTTP operations. Controllers derived from this
    class should implement these methods to manage their specific resources.

    Implementing classes must provide functionality for CRUD operations, along
    with any additional actions that are relevant to the resource they manage.
    """

    @abstractmethod
    async def post(self,
                   request_body: M | UploadFile,
                   request: Request,
                   validator_cls: Type[V]) -> M:
        """Handles POST requests to create a new resource.

        Args:
            request_body (M): The data used to create the resource.
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException

    @abstractmethod
    async def get(self,
                  identifier: ID,
                  request: Request) -> M:
        """Handles GET requests to retrieve a resource by its identifier.

        Args:
            identifier (ID): The unique identifier for the resource to retrieve.
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException

    @abstractmethod
    async def get_all(self,
                      request: Request) -> M:
        """Handles GET requests to retrieve all instances of the resource.

        Args:
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException

    @abstractmethod
    async def put(self,
                  identifier: ID,
                  request_body: M,
                  request: Request,
                  validator_cls: Type[V]) -> M:
        """Handles PUT requests to update a resource by its identifier.

        Args:
            identifier (ID): The unique identifier for the resource to update.
            request_body (M): The updated data for the resource.
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException

    @abstractmethod
    async def delete(self,
                     identifier: ID,
                     request: Request) -> M:
        """Handles DELETE requests to remove a resource by its identifier.

        Args:
            identifier (ID): The unique identifier for the resource to delete.
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException

    @abstractmethod
    async def options(self,
                      request: Request) -> M:
        """Handles OPTIONS requests, typically used to describe the communication options for the target resource.

        Args:
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException

    @abstractmethod
    async def health(self,
                     request: Request) -> M:
        """Performs a health check of the controller, useful for monitoring and uptime checks.

        Args:
            request (Req): Additional context or parameters for the request.

        Raises:
            NotImplementedException: If the method is not implemented by the derived class.
        """
        raise NotImplementedException
