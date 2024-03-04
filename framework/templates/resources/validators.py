"""Request | Resource validators for this resource"""

from typing import Union

from app.base.repositories import AsyncRepository, NullRepository, Repository
from app.base.validators import RequestValidator

from .models.requests import POSTRequest, PUTRequest


class POSTValidator(RequestValidator):
    """Validates a POST request for this resource"""
    request: POSTRequest
    repository: Union[Repository, AsyncRepository]


    def __init__(self,
                 request: POSTRequest,
                 repository: Union[Repository, AsyncRepository] = NullRepository) -> None:
        super().__init__(request, repository)


    def execute(self) -> None:
        return None


class PUTValidator(RequestValidator):
    """Validates a PUT request for this resource"""

    def __init__(self,
                 request: PUTRequest,
                 repository: Union[Repository, AsyncRepository] = NullRepository) -> None:
        super().__init__(request, repository)

    def execute(self) -> None:
        return None
