"""FastAPI application launcher module.

This module is responsible for constructing the FastAPI application instance,
configuring middleware such as CORS based on application settings, and setting up
dependency injection for the entire application lifecycle.
"""

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from injector import Injector

from app.settings import Settings

def build_app(injector: Injector) -> FastAPI:
    """Builds and returns a FastAPI application configured with dependency injection.

    Args:
        injector (Injector): The Injector instance used for dependency injection.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    async def bind_injector_to_request(request: Request) -> None:
        """Attaches the injector to the request state for use in dependency injection."""
        request.state.injector = injector

    app = FastAPI(dependencies=[Depends(bind_injector_to_request)])

    # Apply CORS middleware if enabled in settings
    settings: Settings = injector.get(Settings)
    if settings.server.cors_allowed:
        app.add_middleware(CORSMiddleware, **settings.server.cors.model_dump())

    return app
