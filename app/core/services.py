"""Base service clases for all services in the application"""

import abc
from typing import Any, Optional, TypeVar


class Service(abc.ABC):
    """Syncronous service base class.

    Args:
        abc (ABC): Abstract class

    Raises:
        NotImplementedError: If the subclass
        doesn't implement the execute method.
    """

    @abc.abstractmethod
    def execute(self) -> Optional[Any]:
        """Method that will be executed syncronously.

        Raises:
            NotImplementedError: Method was not implemented by subclass.
        """
        raise NotImplementedError


S = TypeVar("S", bound=Service)
