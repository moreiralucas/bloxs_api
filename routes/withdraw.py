"""Withdraw Module"""
from datetime import datetime
from app import app
from models import Conta, Transacao
from schemas import AccountWithdrawIn, AccountWithdrawOut
from utils import internal_server_error, success_response


@app.post("/account/<int:account_id>/withdraw")
@app.input(AccountWithdrawIn)
@app.output(AccountWithdrawOut)
def withdraw(account_id, data):
    """With draw money"""

    try:
        account: Conta = Conta.query.filter_by(id_conta=account_id).first()
        result: str = account.withdraw_money(data["valor"])
        transacao: Transacao = Transacao(
            id_conta=account.id_conta,
            valor=(-data["valor"]),
            data_transacao=datetime.now(),
        )
        transacao.save()
    except Exception as error:  # pylint: disable=broad-except
        return internal_server_error(error)

    return success_response({"message": result})
