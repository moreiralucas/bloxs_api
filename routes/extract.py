"""Extract Module"""
from app import app
from models import Transacao
from schemas import ExtractDepositOut

@app.get("/account/<int:account_id>/extract")
@app.output(ExtractDepositOut)
def extract_account(account_id):
    """Extract endpoint"""

    try:
        transacao: Transacao = Transacao.query.filter_by(
            id_conta=account_id,
        ).all()
    except Exception as error:
        return {
            "message": "Internal error"
        }, 500

    return transacao
    # TODO: Add list of transaction in return of schema
