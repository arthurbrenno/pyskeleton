"""Base service classes for all services in the application.

This module defines an abstract base class for synchronous services, ensuring a consistent interface
across all service implementations. Services are responsible for encapsulating the core business logic
of the application, providing a clear separation between the application's interface (controllers)
and its core operational logic (services).

Each service should implement the `execute` method, which contains the logic to be performed. This
approach allows for a modular, maintainable, and testable architecture, where services can be
independently developed, tested, and reused across the application.
"""

import abc
from typing import Any, Optional, TypeVar


class Service(abc.ABC):
    """Abstract base class for synchronous services within the application.

    Services extending this class must implement the `execute` method, defining the specific
    operations to be carried out by the service. The `execute` method encapsulates the service's
    main functionality and is designed to be invoked by the application's controllers or other services.

    Raises:
        NotImplementedError: If a subclass does not implement the `execute` method.
    """

    @abc.abstractmethod
    def execute(self) -> Optional[Any]:
        """Performs the service's main operations.

        This method should contain the primary business logic for the service. It may
        return a result or `None` if there is no result to return.

        Returns:
            Optional[Any]: The result of the service execution, if applicable.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError

# Type variable for generic service types, bound to the Service base class
S = TypeVar("S", bound=Service)
