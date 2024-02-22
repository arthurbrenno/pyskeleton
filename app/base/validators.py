"""Base request validator classes.

This module defines the abstract base and null object classes for request validation. Validators
are specialized services responsible for checking the correctness and completeness of incoming
requests against defined schemas or rules before processing them further in the application.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Optional
from pydantic import BaseModel
from app.base.exceptions import NotImplementedException
from app.base.services import Service

class RequestValidator(Service, ABC):
    """Abstract base class for synchronous request validators.

    Inherits from the `Service` base class and defines an interface for request validation
    operations. Validators are used to ensure that incoming requests meet the expected format
    and contain valid data before being processed by the application.

    Attributes:
        request (BaseModel): The request object to validate, defined using Pydantic models
                             for structured data validation.
    """

    def __init__(self, request: BaseModel) -> None:
        """Initializes the request validator with a request object.

        Args:
            request (BaseModel): The request object to be validated.
        """
        self.request = request

    @abstractmethod
    def execute(self) -> None:
        """Performs the validation logic on the provided request object.

        This method should implement the specific validation logic to verify
        the request's correctness and completeness. It should raise appropriate
        exceptions or errors if the validation fails.

        Raises:
            NotImplementedException: If the method is not implemented in a subclass.
        """
        raise NotImplementedException

class NullValidator(RequestValidator):
    """Null object implementation for the `RequestValidator` class.

    This class represents a no-op validator that can be used in contexts where
    validation is optional or not necessary. It effectively implements the Null Object
    design pattern for validators, providing default do-nothing behavior.
    """

    def __init__(self, request: Optional[BaseModel] = None) -> None:
        """Initializes the null validator, optionally with a request object.

        Args:
            request (Optional[BaseModel]): An optional request object, which is ignored
                                           in the null validator. Defaults to None.
        """
        super().__init__(request)

    def execute(self) -> None:
        """Overrides the validation execution method with a no-op implementation."""
        return None

V = TypeVar("V", bound=RequestValidator)
