"""Common types for the application"""

from typing import TypeVar

from pydantic import BaseModel


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
M = TypeVar("M", bound=BaseModel)
ID = TypeVar("ID", bound=str | int)

"""Generic type variables for use in the application."""
