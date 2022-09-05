"""Start Flask Module"""
from apiflask import APIFlask
from models import db, Pessoa, Conta, Transacao
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
