"""Core generic exceptions for the application.

This module defines custom exceptions for the application, extending FastAPI's HTTPException.
These exceptions include specific cases like internal server errors and not implemented errors,
allowing for consistent error handling and response formatting throughout the application.
"""

from typing import Any, Dict

from fastapi import HTTPException, status


class InternalServerError(HTTPException):
    """Exception for internal server errors (500).

    This exception should be raised when an unexpected condition was encountered and no more
    specific exception is suitable. It results in an HTTP 500 response being returned to the client.
    """
    def __init__(self,
                 status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
                 detail: Any = "An internal server error occurred. We're working on it.",
                 headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)

class GenericException(HTTPException):
    """A generic exception for HTTP errors.

    This exception can be used to raise any HTTP error by specifying a status code and detail.
    It provides flexibility in handling various error conditions with custom messages.
    """
    def __init__(self,
                 status_code: int,
                 detail: Any,
                 headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)

class NotImplementedException(HTTPException):
    """Exception for not implemented features (501).

    This exception indicates that the requested method or operation is not implemented.
    It should be used to signal unimplemented functionality, resulting in an HTTP 501 response.
    """
    def __init__(self,
                 status_code: int = status.HTTP_501_NOT_IMPLEMENTED,
                 detail: Any = "This feature is not implemented yet.",
                 headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)
