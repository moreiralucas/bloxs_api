"""Block Account Module"""

from app import app
from schemas import AccountBlockOut
from models import Conta

@app.post("/account/<int:account_id>/block")
@app.output(AccountBlockOut)
def block_account(account_id):
    """Block an account from a given account_id"""

    try:
        account: Conta = Conta.query.get_or_404(account_id)
        account.block()
    except Exception as err:  # pylint: disable=broad-except
        return {
            "message": "Internal error"
        }, 500

    return {
        "flag_ativo" :account.flag_ativo,
    }, 200
