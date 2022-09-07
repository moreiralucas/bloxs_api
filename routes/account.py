"""Account Module"""
from app import app
from models import Conta
from schemas import AccountIn, AccountOut
from utils import internal_server_error, success_response


@app.post("/account")
@app.input(AccountIn)
@app.output(AccountOut)
def create_account(data):
    """Create account"""

    try:

        account: Conta = Conta(**data)
        account.save()
    except Exception as error:  # pylint: disable=broad-except
        return internal_server_error(error)

    return success_response(account, status_code=201)
