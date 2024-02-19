"""Fastapi app launcher module"""

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from injector import Injector

from app.settings import Settings


def build_app(injector: Injector):
    """Build the entire FastAPI application.

    Args:
        injector (Injector): _description_
    """
    async def bind_injector_to_request(request: Request) -> None:
        request.state.injector = injector

    app = FastAPI(dependencies=[Depends(bind_injector_to_request)])

    settings = injector.get(Settings)
    if settings.server.cors_allowed:
        cors_config = settings.server.cors.model_dump()
        app.add_middleware(CORSMiddleware, **cors_config)

    return app
