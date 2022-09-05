"""Database Utils Module"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import ENVIRONMENT


def init_database(app: Flask, database: SQLAlchemy):
    """Create all models of database"""
    if ENVIRONMENT != "test":
        with app.app_context():
            migrate = Migrate()
            from models import Pessoa, Conta, Transacao
            migrate.init_app(app, database)

            return migrate
