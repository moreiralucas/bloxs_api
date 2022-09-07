"""Account schema module"""
from apiflask import Schema, fields


class AccountBase(Schema):
    """Schema Base Account"""

    id_pessoa = fields.Integer()
    limite_saque_diario = fields.Float()
    flag_ativo = fields.Boolean()
    tipo_conta = fields.Integer()


class AccountIn(AccountBase):
    """Schema Input Account"""


class AccountOut(AccountBase):
    """Schema Output Account"""

    id_conta = fields.Integer()
    saldo = fields.Float()
    data_criacao = fields.Date()
