"""Base module for holding core Request concepts."""

from typing import TypeVar

from fastapi import Request


class NullRequest(Request):
    """A null request that can be used for mocking."""



Req = TypeVar("Req", bound=Request | NullRequest)
