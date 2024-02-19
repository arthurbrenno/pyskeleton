"""Request representations for this resource."""
from pydantic import BaseModel

# from pydantic import Field, validator


class POSTRequest(BaseModel):
    """Represents a POST request to this specific resource"""


class PUTRequest(BaseModel):
    """Represents a PUT request to this specific resource"""
