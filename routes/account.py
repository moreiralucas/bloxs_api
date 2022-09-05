"""Account Module"""
from app import app
from models import Conta
from schemas import AccountIn, AccountOut

@app.post("/account")
@app.input(AccountIn)
@app.output(AccountOut, status_code=201)
def create_account(data):
    """Create account"""

    account: Conta = Conta(**data)
    account.save()

    return account
