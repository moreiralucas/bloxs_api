"""Extract Module"""
from app import app
from models import Transacao
from schemas import ExtractDepositOut
from utils import internal_server_error, success_response


@app.get("/account/<int:account_id>/extract")
@app.output(ExtractDepositOut(many=True))
def extract_account(account_id):
    """Extract endpoint"""

    try:
        transacao: Transacao = Transacao.query.filter_by(
            id_conta=account_id,
        ).all()
    except Exception as error:
        return internal_server_error(error)

    return success_response(transacao)
    # TODO: Add list of transaction in return of schema
