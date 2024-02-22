"""Controller (request intermediary) for [Resource Name].

This module defines the controller class for [Resource Name], handling incoming
HTTP requests, executing the appropriate service layer logic, and returning
the corresponding HTTP responses.
"""

from app.base.controllers import Controller
from app.base.exceptions import NotImplementedException
from app.base.requests import NullRequest, Req
from app.base.services import S
from .validators import POSTValidator, GETValidator, GETALLValidator, OPTIONSValidator, PUTValidator, DELETEValidator
from app.base.validators import V
from app.typing import I

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
                   request: Req = NullRequest,
                   validator: V = POSTValidator) -> POSTResponse:
        raise NotImplementedException

    async def get(self,
                  identifier: I,
                  request: Req = NullRequest,
                  validator: V = GETValidator) -> GETResponse:
        raise NotImplementedException

    async def get_all(self,
                      request: Req = NullRequest,
                      validator: V = GETALLValidator) -> GETALLResponse:
        raise NotImplementedException

    async def put(self,
                  identifier: I,
                  request_body: PUTRequest,
                  request: Req = NullRequest,
                  validator: V = PUTValidator) -> PUTResponse:
        raise NotImplementedException

    async def delete(self,
                     identifier: I,
                     request: Req = NullRequest,
                     validator: V = DELETEValidator) -> DELETEResponse:
        raise NotImplementedException

    async def options(self,
                      request: Req = NullRequest,
                      validator: V = OPTIONSValidator) -> OPTIONSResponse:
        raise NotImplementedException

    async def health(self,
                     request: Req = NullRequest) -> HealthResponse:
        service: S = HealthService(request)
        result = service.execute()
        return HealthResponse(detail=result)
