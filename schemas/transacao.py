"""Transaction schema module"""
from apiflask import Schema, fields


class TransactionBase(Schema):
    """Schema Base Transaction"""

    id_conta = fields.Integer()
    valor = fields.Float()
    data_transacao = fields.Date()


class TransactionIn(TransactionBase):
    """Schema Input Transaction"""


class TransactionOut(TransactionBase):
    """Schema Output Transaction"""

    id_transacao = fields.Integer()
