"""Entrypoint for the application"""

from app.di import global_injector
from app.launcher import build_app

app = build_app(global_injector)
