"""Start Flask Module"""
from apiflask import APIFlask
from models import db
from utils import create_app, init_database
from flask_cors import CORS

app: APIFlask = create_app(db)
CORS(app)
migrate = init_database(app, db)

# pylint: disable=wrong-import-position,unused-import
import routes.account
import routes.balance
import routes.block
import routes.deposit
import routes.extract
import routes.withdraw

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
