"""Balance Module"""
from app import app
from schemas import AccountBalanceOut
from models import Conta
from utils import internal_server_error, success_response


@app.get("/account/<int:account_id>/balance")
@app.output(AccountBalanceOut)
def retrieve_balance(account_id):
    """Retrieve balance account"""

    try:
        account: Conta = Conta.query.get_or_404(account_id)
    except Exception as error:
        return internal_server_error(error)

    return success_response(account)
