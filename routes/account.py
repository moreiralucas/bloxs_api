"""Account Module"""
from app import app
from models import Conta
from schemas import AccountIn, AccountOut

@app.post("/account")
@app.input(AccountIn)
@app.output(AccountOut, status_code=201)
def create_account(data):
    """Create account"""
    status_code: int = 200

    try:

        account: Conta = Conta(**data)
        account.save()
    except Exception as err:  # pylint: disable=broad-except
        result: str = "Internal error"
        status_code = 500

    return account, status_code
