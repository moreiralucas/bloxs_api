"""Configuration Test Module"""
import pytest

from app import app as application
from models.base_mixin import db


@pytest.fixture
def app():
    """Create database"""

    with application.app_context():
        db.create_all()

        yield application
        db.session.remove()
        db.drop_all()
