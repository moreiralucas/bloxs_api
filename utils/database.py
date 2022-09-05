"""Database Utils Module"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import ENVIRONMENT


def init_database(app: Flask, database: SQLAlchemy):
    """Create all models of database"""
    if ENVIRONMENT != "test":
        with app.app_context():
            database.create_all()

            migrate = Migrate(app, database)

            return migrate
