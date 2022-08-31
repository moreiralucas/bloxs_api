"""Conta Model Module"""
from .base_mixin import BaseModelMixin, db

class Conta(BaseModelMixin):
    """Conta Model class"""
    id_conta  = db.Column("idConta", db.Integer, primary_key=True, autoincrement=True)
    id_pessoa  = db.Column("idPessoa", db.Integer)
    saldo  = db.Column("saldo", db.Numeric)
    limite_saque_diario = db.Column("limiteSaqueDiario", db.Numeric)
    flag_ativo = db.Column("flagAtivo", db.Boolean)
    tipo_conta  = db.Column("tipoConta", db.Integer)
    data_criacao  = db.Column("dataCriacao", db.Date)
