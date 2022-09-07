"""Populate database"""
from utils import create_app
from models import Pessoa
from models import db

def insert_dummy_data():
    """Insert dummy data"""

    app = create_app(db)
    with app.app_context():

        pessoa_obj: Pessoa = Pessoa(
            nome="Lucas Moreira",
            cpf="50434222038",
            data_nascimento="1994-01-01",
        )
        pessoa_obj.save()
