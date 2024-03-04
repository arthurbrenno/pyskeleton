"""Controller (request intermediary) for [Resource Name].

This module defines the controller class for [Resource Name], handling incoming
HTTP requests, executing the appropriate service layer logic, and returning
the corresponding HTTP responses.
"""

from typing import Type

from fastapi import Request, UploadFile

from app.base.controllers import Controller
from app.base.exceptions import NotImplementedException
from app.base.services import S
from app.typing import I

from .models.requests import POSTRequest, PUTRequest
from .models.responses import (DELETEResponse, GETALLResponse, GETResponse,
                               HealthResponse, OPTIONSResponse, POSTResponse,
                               PUTResponse)
from .services import HealthService
from .validators import POSTValidator, PUTValidator


class _Controller(Controller):
    """Controller for this resource."""
    async def post(self,
                   request_body: POSTRequest | UploadFile,
                   request: Request,
                   validator_cls: POSTValidator = POSTValidator) -> POSTResponse:
        validator_cls(request_body).execute()
        raise NotImplementedException

    async def get(self,
                  identifier: I,
                  request: Request) -> GETResponse:
        raise NotImplementedException

    async def get_all(self,
                      request: Request) -> GETALLResponse:
        raise NotImplementedException

    async def put(self,
                  identifier: I,
                  request_body: PUTRequest,
                  request: Request,
                  validator_cls: PUTRequest = PUTValidator) -> PUTResponse:
        validator_cls(request_body).execute()
        raise NotImplementedException


    async def delete(self,
                     identifier: I,
                     request: Request) -> DELETEResponse:
        raise NotImplementedException


    async def options(self,
                      request: Request) -> OPTIONSResponse:
        raise NotImplementedException


    async def health(self,
                     request: Request) -> HealthResponse:
        service: S = HealthService(request)
        result = service.execute()
        return HealthResponse(detail=result)
