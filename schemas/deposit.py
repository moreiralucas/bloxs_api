"""Balance schema module"""
from apiflask import Schema, fields


class AccountDeposit(Schema):
    """Schema Base AccountDeposit"""


class AccountDepositIn(AccountDeposit):
    """Schema Input AccountDeposit"""
    valor = fields.Float()


class AccountDepositOut(AccountDeposit):
    """Schema Output AccountDeposit"""
    message = fields.String()
