"""Base response classes for this resource."""

from typing import Dict

from pydantic import BaseModel, Field


class POSTResponse(BaseModel):
    """Represents a response for a POST request."""


class GETResponse(BaseModel):
    """Represents a response for a GET request."""


class GETALLResponse(BaseModel):
    """Represents a response for a GET_ALL request."""


class PUTResponse(BaseModel):
    """Represents a response for a PUT request."""


class DELETEResponse(BaseModel):
    """Represents a response for a DELETE request."""


class OPTIONSResponse(BaseModel):
    """Represents a response for an OPTIONS request."""


class HealthResponse(BaseModel):
    """Represents a response for a GET _/v1/_/health request."""

    healthy: bool = Field(
        description="Indicates if the resource is healthy.",
        default=True
    )
    detail: Dict = Field(
        description="Extra details",
        default={}
    )
