"""Utils Module"""
from .database import init_database
from .initialization import create_app

__all__ = [
    "create_app",
    "init_database",
]
