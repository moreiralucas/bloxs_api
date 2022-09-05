"""Pessoa Model Module"""
from .base_mixin import BaseModelMixin, db


class Pessoa(BaseModelMixin):
    """Pessoa Model class"""

    id_pessoa = db.Column("idPessoa", db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column("nome", db.Text)
    cpf = db.Column("cpf", db.Text)
    data_nascimento = db.Column("dataNascimento", db.Date)
