"""Balance schema module"""
from apiflask import Schema, fields


class AccountBalance(Schema):
    """Schema Base AccountBalance"""


class AccountBalanceIn(AccountBalance):
    """Schema Input AccountBalance"""


class AccountBalanceOut(AccountBalance):
    """Schema Output AccountBalance"""
    saldo = fields.Float()
