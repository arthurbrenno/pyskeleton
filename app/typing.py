"""Common types for the application"""

from typing import TypeVar

from pydantic import BaseModel

from app.base.value_objects import ID, NullID

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
M = TypeVar("M", bound=BaseModel)
I = TypeVar("I", bound=ID)

"""Generic type variables for use in the application."""
