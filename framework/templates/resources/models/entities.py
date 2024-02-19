"""The entities related to this resource"""

from dataclasses import dataclass

from pydantic import Field

from app.core.entities import Entity, NullEntity


@dataclass
class _(Entity):
    ...


@dataclass
class _(NullEntity):
    ...
