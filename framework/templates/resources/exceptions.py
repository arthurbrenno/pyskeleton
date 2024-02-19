"""Base exceptions related to this resource"""

from typing import Any, Dict

from fastapi import HTTPException, status


class _Exception(HTTPException):
    def __init__(self,
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 detail: Any = None,
                 headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)
