"""Services (business rules || repository executors) of this resource"""
from fastapi import Request

# from app.core.repositories import AsyncRepository, Repository
from app.core.services import Service

# from app.typing import R


class HealthService(Service):
    """Service that indicates the health of this resource"""

    request: Request

    def __init__(self, request: Request) -> None:
        self.request = request

    def execute(self) -> dict:
        client = self.request.client
        host = self.request.headers.get("host", "Unknown Host")
        user_agent = self.request.headers.get("user-agent",
                                              "Unknown User Agent")

        return {
            "client": str(client),
            "host": host,
            "user_agent": user_agent,
        }
