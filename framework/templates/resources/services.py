"""Services (business rules or repository executors) for [Resource Name]."""

from fastapi import Request
from app.base.services import Service

class HealthService(Service):
    """Service that indicates the health of [Resource Name] resource.

    This service gathers and returns information about the request and client,
    useful for health checks and monitoring the status of the resource.
    """

    def __init__(self, request: Request) -> None:
        """Initializes the service with the incoming HTTP request.

        Args:
            request (Request): The incoming HTTP request.
        """
        self.request = request

    def execute(self) -> dict:
        """Executes the service logic to collect health-related information.

        Returns:
            dict: A dictionary containing client, host, and user agent information.
        """
        client = self.request.client.host
        host = self.request.headers.get("host", "Unknown Host")
        user_agent = self.request.headers.get("user-agent", "Unknown User Agent")

        return {
            "client_ip": client,
            "host": host,
            "user_agent": user_agent,
        }
