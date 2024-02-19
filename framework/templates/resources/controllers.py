"""Controller (request intermediate) class for this resource."""

from app.core.controllers import Controller
from app.core.exceptions import NotImplementedException
from app.core.requests import NullRequest, Req
from app.core.services import S
# from app.core.validations import
from app.typing import ID

# from .exceptions import
from .models.requests import POSTRequest, PUTRequest
from .models.responses import (DELETEResponse, GETALLResponse, GETResponse,
                               HealthResponse, OPTIONSResponse, POSTResponse,
                               PUTResponse)

# from .validators import
from .services import HealthService


class _Controller(Controller):
    """Controller for this resource."""
    async def post(self,
                   request_body: POSTRequest,
                   request: Req = NullRequest) -> POSTResponse:
        raise NotImplementedException

    async def get(self,
                  identifier: ID,
                  request: Req = NullRequest) -> GETResponse:
        raise NotImplementedException

    async def get_all(self,
                      request: Req = NullRequest) -> GETALLResponse:
        raise NotImplementedException

    async def put(self,
                  identifier: ID,
                  request_body: PUTRequest,
                  request: Req = NullRequest) -> PUTResponse:
        raise NotImplementedException

    async def delete(self,
                     identifier: ID,
                     request: Req = NullRequest) -> DELETEResponse:
        raise NotImplementedException

    async def options(self,
                      request: Req = NullRequest) -> OPTIONSResponse:
        raise NotImplementedException

    async def health(self,
                     request: Req = NullRequest) -> HealthResponse:
        service: S = HealthService(request)
        result = service.execute()
        return HealthResponse(detail=result)
