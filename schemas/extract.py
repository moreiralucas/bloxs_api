"""Extract schema module"""
from apiflask import Schema, fields


class ExtractDeposit(Schema):
    """Schema Base ExtractDeposit"""


class ExtractDepositIn(ExtractDeposit):
    """Schema Input ExtractDeposit"""

    valor = fields.Float()


class ExtractDepositOut(ExtractDeposit):
    """Schema Output ExtractDeposit"""

    id_transacao = fields.Integer()
    id_conta = fields.Integer()
    valor = fields.Float()
    data_transacao = fields.Date()
