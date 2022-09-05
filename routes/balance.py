"""Balance Module"""
from app import app
from schemas import AccountBalanceOut
from models import Conta


@app.get("/account/<int:account_id>/balance")
@app.output(AccountBalanceOut)
def retrieve_balance(account_id):
    """Retrieve balance account"""

    account: Conta = Conta.query.get_or_404(account_id)
    return account
