"""Withdraw account schema module"""
from typing import List
from apiflask import Schema, fields
from apiflask.validators import OneOf

withdraw_messages: List[str] = ["success", "blocked account", "insufficient funds"]


class AccountWithdrawBase(Schema):
    """Schema Base AccountWithdraw"""


class AccountWithdrawIn(AccountWithdrawBase):
    """Schema Input AccountWithdraw"""

    valor = fields.Float(required=True)
    id_pessoa = fields.Integer(required=True)


class AccountWithdrawOut(AccountWithdrawBase):
    """Schema Output AccountWithdraw"""

    message = fields.String(validate=OneOf(withdraw_messages))
