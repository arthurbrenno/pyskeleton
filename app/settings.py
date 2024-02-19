"""Core settings for the application"""

from pydantic import BaseModel, Field

from app.config import config


class CorsSettings(BaseModel):
    """Settings for CORS (Cross-Origin Resource Sharing)"""

    allow_credentials: bool = Field(
        description="Indicates if cookies should be allowed by CORS",
        default=config.server.cors.allow_credentials,
    )
    allow_origins: list[str] = Field(
        description="Origins that should be allowed to make CO requests.",
        default=config.server.cors.allow_origins,
    )
    allow_origin_regex: list[str] | str = Field(
        description="Origins that should be permitted to make CORS.",
        default=config.server.cors.allow_origin_regex,
    )
    allow_methods: list[str] = Field(
        description="A list of HTTP methods that should be allowed for CORS.",
        default=config.server.cors.allow_methods
    )
    allow_headers: list[str] = Field(
        description="Request headers that should be supported for CORS.",
        default=config.server.cors.allow_headers,
    )


class ServerSettings(BaseModel):
    """Settings for the server"""

    port: int = Field(
        description="The port of the application.",
        default=config.server.port
    )
    host: str = Field(
        description="The host of the application.",
        default=config.server.host
    )
    reload: bool = Field(
        description="",
        default=config.server.reload
    )
    workers: int = Field(
        description="",
        default=config.server.workers
    )
    cors_allowed: bool = Field(
        description="Indicates if cors is allowed.",
        default=config.server.cors.allowed
    )
    cors: CorsSettings = Field(
        description="CORS settings.",
        default=CorsSettings()
    )


class Settings(BaseModel):
    """Settings for the application"""

    server: ServerSettings = Field(
        description="Server settings",
        default=ServerSettings()
    )


def settings() -> Settings:
    """Get the current settings for the application."""
    from app.di import global_injector  # pylint: disable=C0415
    return global_injector.get(Settings)
