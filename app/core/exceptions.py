"""Core generic exceptions for the applications."""

from typing import Any, Dict

from fastapi import HTTPException, status


class InternalServerError(HTTPException):
    """Internal server error exception.

    Args:
        HTTPException (class): Superclass.
    """
    def __init__(self,
                 status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
                 detail: Any = "That's our fault. \
                 An internal server error happened.",
                 headers: Dict[str, str] | None = None) -> None:
        """Constructor

        Args:
            status_code (int, optional):
            The status code of the response.
            Defaults to status.HTTP_500_INTERNAL_SERVER_ERROR.

            detail (Any, optional):
            The detail (reason) of the response.
            Defaults to "That's our fault. An internal server error happened.".

            headers (Dict[str, str] | None, optional):
            Custom headers of the response. Defaults to None.
        """
        super().__init__(status_code, detail, headers)


class GenericException(HTTPException):
    """Internal server error exception.

    Args:
        HTTPException (class): Superclass.
    """
    def __init__(self,
                 status_code: int,
                 detail: Any,
                 headers: Dict[str, str] | None = None) -> None:
        """Constructor

        Args:
            status_code (int): The status code of the response.
            detail (Any): The detail (reason) of the response.

            headers (Dict[str, str] | None, optional):
            Custom headers of the response. Defaults to None.
        """
        super().__init__(status_code, detail, headers)


class NotImplementedException(HTTPException):
    """Generic exception for not implemented elements"""

    def __init__(self,
                 status_code: int = status.HTTP_501_NOT_IMPLEMENTED,
                 detail: Any = "This method was not implemented yet",
                 headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)
