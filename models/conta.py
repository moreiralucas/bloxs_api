"""Conta Model Module"""
from datetime import datetime
from decimal import Decimal
from typing import Dict
from .base_mixin import BaseModelMixin, db

class Conta(db.Model, BaseModelMixin):
    """Conta Model class"""

    id_conta = db.Column("idConta", db.Integer, primary_key=True, autoincrement=True)
    id_pessoa = db.Column("idPessoa", db.Integer)
    saldo = db.Column("saldo", db.Numeric)
    limite_saque_diario = db.Column("limiteSaqueDiario", db.Numeric)
    flag_ativo = db.Column("flagAtivo", db.Boolean)
    tipo_conta = db.Column("tipoConta", db.Integer)
    data_criacao = db.Column("dataCriacao", db.Date)

    def save(self):
        """Override save method"""
        if self.id_conta is None:
            self.saldo = 0.0
            self.data_criacao = datetime.now()
        return super().save()

    def add_money(self, value: float, commit: bool = True):
        """Add money in this account"""
        self.saldo += Decimal(value)

        if commit:
            self.save()

    def withdraw_money(self, value: float, commit: bool = True) -> str:
        """withdraw money in this account"""
        result_index: str = "insufficient_funds"
        decimal_value: Decimal = Decimal(value)

        if not self.flag_ativo:
            result_index = "blocked_account"
        elif self.saldo < decimal_value:
            result_index = "success"
            self.saldo -= decimal_value

            if commit:
                self.save()

        result_dict: Dict[str, str] = {
            "success": "success",
            "blocked_account": "blocked account",
            "insufficient_funds": "insufficient funds"
        }

        return result_dict[result_index]

    def block(self, commit: bool = True):
        """Block this account"""
        self.flag_ativo = False

        if commit:
            self.save()
