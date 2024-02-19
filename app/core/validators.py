"""Base request validator classes."""

from abc import ABC, abstractmethod
from typing import TypeVar

# from overrides import override
from pydantic import BaseModel

from app.core.exceptions import NotImplementedException
from app.core.services import Service


class RequestValidator(Service, ABC):
    """Validates a request syncronously"""

    request: BaseModel

    @abstractmethod
    def __init__(self, request: BaseModel) -> None:
        self.request = request

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedException


class NullValidator(RequestValidator):
    """Null object for validator class"""

    request: None

    def __init__(self, request: BaseModel = None) -> None:
        super().__init__(request)

    def execute(self) -> None:
        return None

V = TypeVar("V", bound=RequestValidator | NullValidator)
