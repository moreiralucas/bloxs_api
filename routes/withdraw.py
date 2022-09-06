"""Withdraw Module"""
from app import app
from models import Conta
from schemas import AccountWithdrawIn, AccountWithdrawOut



@app.post("/account/<int:account_id>/withdraw")
@app.input(AccountWithdrawIn)
@app.output(AccountWithdrawOut)
def withdraw(account_id, data):
    """With draw money"""

    account: Conta = Conta.query.filter_by(id_conta=account_id).first()
    result: str = account.withdraw_money(data["valor"])

    return {
        "message": result
    }
