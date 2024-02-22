"""Common types for the application"""

from typing import TypeVar
from app.base.vobjs import ID
from pydantic import BaseModel


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
M = TypeVar("M", bound=BaseModel)
I = TypeVar("I", bound=ID)

"""Generic type variables for use in the application."""
