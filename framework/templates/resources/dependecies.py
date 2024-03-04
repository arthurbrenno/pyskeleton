"""Dependencies for this resource"""

from typing import Type

from app.base.controllers import Controller
from app.base.validators import NullValidator
from app.typing import V

# from .controllers import


def get_controller() -> Controller:
    """Gets this resource controller"""
    return ...


def get_post_validator_cls() -> Type[V]:
    """Gets the POST request validator for this resource, if there's any"""
    return NullValidator


def get_put_validator_cls() -> Type[V]:
    """Gets the PUT request validator for this resource, if there's any"""
    return NullValidator
