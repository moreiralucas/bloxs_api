"""Utils Module"""
from .initialization import create_app
from .database import init_database

__all__ = [
    "create_app",
    "init_database",
]
