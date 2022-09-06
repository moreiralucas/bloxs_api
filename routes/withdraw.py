"""Withdraw Module"""
from datetime import datetime
from app import app
from models import Conta, Transacao
from schemas import AccountWithdrawIn, AccountWithdrawOut



@app.post("/account/<int:account_id>/withdraw")
@app.input(AccountWithdrawIn)
@app.output(AccountWithdrawOut)
def withdraw(account_id, data):
    """With draw money"""
    status_code: int = 200

    try:
        account: Conta = Conta.query.filter_by(id_conta=account_id).first()
        result: str = account.withdraw_money(data["valor"])
        transacao: Transacao = Transacao(
            id_conta=account.id_conta,
            valor=data["valor"],
            data_transacao=datetime.now(),
        )
        transacao.save()
    except Exception as err:  # pylint: disable=broad-except
        result: str = "Internal error"
        status_code = 500

    return {
        "message": result
    }, status_code
