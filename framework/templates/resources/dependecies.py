"""Dependencies for this resource"""

from app.base.controllers import Controller
from app.base.validators import NullValidator
from app.typing import V

# from .controllers import


def get_controller() -> Controller:
    """Gets this resource controller"""
    return ...


# .##.....##....###....##.......####.########.....###....########..#######..########...######.
# .##.....##...##.##...##........##..##.....##...##.##......##....##.....##.##.....##.##....##
# .##.....##..##...##..##........##..##.....##..##...##.....##....##.....##.##.....##.##......
# .##.....##.##.....##.##........##..##.....##.##.....##....##....##.....##.########...######.
# ..##...##..#########.##........##..##.....##.#########....##....##.....##.##...##.........##
# ...##.##...##.....##.##........##..##.....##.##.....##....##....##.....##.##....##..##....##
# ....###....##.....##.########.####.########..##.....##....##.....#######..##.....##..######.

def get_post_validator() -> V:
    """Gets the POST request validator for this resource, if there's any"""
    return NullValidator


def get_read_validator() -> V:
    """Gets the GET request validator for this resource, if there's any"""
    return NullValidator


def get_read_all_validator() -> V:
    """Gets the GET ALLrequest validator for this resource, if there's any"""
    return NullValidator


def get_put_validator() -> V:
    """Gets the PUT request validator for this resource, if there's any"""
    return NullValidator


def get_delete_validator() -> V:
    """Gets the DELETE request validator for this resource, if there's any"""
    return NullValidator


def get_options_validator() -> V:
    """Gets the OPTIONS request validator for this resource, if there's any"""
    return NullValidator
