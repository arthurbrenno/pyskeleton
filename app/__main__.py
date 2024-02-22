"""Application entry point when run directly by module.

This module initializes and runs the FastAPI application using Uvicorn as the ASGI server.
It loads application settings from environment variables and applies these settings
to configure the server, such as host, port, and number of workers.
"""

import uvicorn
from dotenv import load_dotenv

from app.main import app
from app.settings import Settings, settings

app_settings: Settings = settings()

if __name__ == '__main__':
    uvicorn.run(app,
                host=app_settings.server.host,
                port=app_settings.server.port,
                workers=app_settings.server.workers)
