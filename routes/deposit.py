"""Deposit Module"""
from datetime import datetime
from app import app
from models import Conta, Transacao
from schemas import AccountDepositIn, AccountDepositOut
from utils import internal_server_error, success_response


@app.put("/account/<int:account_id>/deposit")
@app.input(AccountDepositIn)
@app.output(AccountDepositOut)
def deposit_account(account_id, data):
    """Deposit money in a given account"""

    try:
        account: Conta = Conta.query.filter_by(id_conta=account_id).first()
        result: str = account.add_money(data["valor"])
        transacao: Transacao = Transacao(
            id_conta=account.id_conta,
            valor=data["valor"],
            data_transacao=datetime.now(),
        )
        transacao.save()
    except Exception as error:  # pylint: disable=broad-except
        return internal_server_error(error)

    return success_response({"message": result})
