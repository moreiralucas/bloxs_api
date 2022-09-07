"""Block Account Module"""

from app import app
from schemas import AccountBlockOut
from models import Conta
from utils import internal_server_error, success_response


@app.post("/account/<int:account_id>/block")
@app.output(AccountBlockOut)
def block_account(account_id):
    """Block an account from a given account_id"""

    try:
        account: Conta = Conta.query.get_or_404(account_id)
        account.block()
    except Exception as error:  # pylint: disable=broad-except
        internal_server_error(error)

    return success_response({"flag_ativo": account.flag_ativo})
