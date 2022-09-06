"""Balance Module"""
from datetime import datetime
from app import app
from schemas import AccountBalanceOut
from models import Transacao, Conta


@app.get("/account/<int:account_id>/balance")
@app.output(AccountBalanceOut)
def retrieve_balance(account_id):
    """Retrieve balance account"""

    try:
        account: Conta = Conta.query.get_or_404(account_id)
    except Exception as error:
        return {
            "message": "Internal error"
        }, 500

    return account, 200
