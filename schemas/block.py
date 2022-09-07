"""Block Account schema module"""
from apiflask import Schema, fields


class AccountBlock(Schema):
    """Schema Base AccountBlock"""


class AccountBlockIn(AccountBlock):
    """Schema Input AccountBlock"""


class AccountBlockOut(AccountBlock):
    """Schema Output AccountBlock"""

    flag_ativo = fields.Boolean()
    message = fields.String()
