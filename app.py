"""Start Flask Module"""
from apiflask import APIFlask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models.base_mixin import db
from utils import create_app, init_database

app: APIFlask = create_app(db)
migrate = init_database(app, db)

import routes.account
import routes.balance
import routes.block
import routes.deposit
import routes.extract
import routes.withdraw

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
