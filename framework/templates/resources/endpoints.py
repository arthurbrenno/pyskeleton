"""Endpoints related to this resource"""

from typing import Type

from fastapi import APIRouter, Depends, Request

from app.base.controllers import Controller
from app.base.validators import V
from app.base.value_objects import ID

from .dependecies import (get_controller, get_post_validator_cls,
                          get_put_validator_cls)
from .models.requests import POSTRequest, PUTRequest
from .models.responses import (DELETEResponse, GETALLResponse, GETResponse,
                               HealthResponse, OPTIONSResponse, POSTResponse,
                               PUTResponse)

router = APIRouter(prefix="/_")

@router.post("/")
async def create(request: Request,
                 body: POSTRequest,
                 controller: Controller = Depends(get_controller),
                 validator_cls: Type[V] = Depends(get_post_validator_cls)) -> POSTResponse:
    """Creates one entity of this resource"""
    return await controller.post(request_body=body,
                                 request=request,
                                 validator_cls=validator_cls)


@router.get("/health")
async def get_health(request: Request,
                     controller: Controller = Depends(get_controller)
                     ) -> HealthResponse:
    """Gets the health of this resource service"""
    return await controller.health(request=request)


@router.get("/{identifier}")
async def read(identifier: str,
               request: Request,
               controller: Controller = Depends(get_controller)
               ) -> GETResponse:
    """Gets one entity related to this resource"""
    return await controller.get(identifier=ID(identifier),
                                request=request)


@router.get("/")
async def read_all(request: Request,
                   controller: Controller = Depends(get_controller)
                   ) -> GETALLResponse:
    """Read all entities related of this resource"""
    return await controller.get_all(request=request)


@router.put("/{identifier}")
async def put(identifier: str,
              body: PUTRequest,
              request: Request,
              controller: Controller = Depends(get_controller),
              validator_cls: Type[V] = Depends(get_put_validator_cls)) -> PUTResponse:
    """Updates an entity of this resource"""
    return await controller.put(identifier=ID(identifier),
                                request_body=body,
                                request=request,
                                validator_cls=validator_cls)


@router.delete("/{identifier}")
async def delete(identifier: str,
                 request: Request,
                 controller: Controller = Depends(get_controller)
                 ) -> DELETEResponse:
    """Deletes one entity of this resource"""
    return await controller.delete(identifier=ID(identifier),
                                   request=request)


@router.options("/")
async def options(request: Request,
                  controller: Controller = Depends(get_controller)
                  ) -> OPTIONSResponse:
    """Gets the options of this resource"""
    return await controller.options(request=request)
