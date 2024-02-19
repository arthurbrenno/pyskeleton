"""__main__"""

import uvicorn
from dotenv import load_dotenv

from app.main import app
from app.settings import Settings, settings

settings: Settings = settings()
load_dotenv()

uvicorn.run(app,
            host=settings.server.host,
            port=settings.server.port,
            workers=settings.server.workers)
