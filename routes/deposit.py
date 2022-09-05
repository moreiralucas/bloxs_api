"""Deposit Module"""
from app import app
from models import Conta
from schemas import AccountDepositIn, AccountDepositOut


@app.put("/account/<int:account_id>/deposit")
@app.input(AccountDepositIn)
@app.output(AccountDepositOut)
def deposit_account(account_id, data):
    """Deposit money in a given account"""

    account: Conta = Conta.query.filter_by(id_conta=account_id).first()
    account.add_money(data["valor"])

    return account
