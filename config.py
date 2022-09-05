"""Config Module"""
import os

from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)


class Config(object):
    """SQLAlchemy base config settings"""

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Settings
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """SQLAlchemy development config settings"""

    DEBUG = True
    ENVIRONMENT = "dev"
    FLASK_APP = "app"


class TestingConfig(Config):
    """SQLAlchemy test config settings"""

    database = "heroes-database-test"
    DEBUG = True
    TESTING = True
    ENVIRONMENT = "test"


class ProductionConfig(Config):
    """SQLAlchemy production config settings"""

    DEBUG = False
    TESTING = False
    ENVIRONMENT = "prod"
