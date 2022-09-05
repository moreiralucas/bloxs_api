"""Withdraw account schema module"""
from apiflask import Schema, fields


class AccountWithdrawBase(Schema):
    """Schema Base AccountWithdraw"""

class AccountWithdrawIn(AccountWithdrawBase):
    """Schema Input AccountWithdraw"""
    valor = fields.Float()


class AccountWithdrawOut(AccountWithdrawBase):
    """Schema Output AccountWithdraw"""
    message = fields.String()
