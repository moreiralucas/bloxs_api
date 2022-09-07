"""Extract test Module"""
from decimal import Decimal
from typing import Dict
from werkzeug.test import TestResponse
from models import Conta, Pessoa


def test_get_extract(app, conta: Conta, pessoa: Pessoa):
    """
    GIVEN a account id
    WHEN the '/account/<account_id>/extract' is requested (GET)
    THEN return the extract info
    """

    client = app.test_client()
    url_extract: str = f"/account/{conta.id_conta}/extract"

    response: TestResponse = client.get(url_extract)
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Add money in account
    url: str = f"/account/{conta.id_conta}/deposit"
    data: Dict = {"valor": 100.0}
    response: TestResponse = client.put(url, json=data)
    assert response.status_code == 200

    # Withdraw money
    url: str = f"/account/{conta.id_conta}/withdraw"
    data: Dict = {"id_pessoa": pessoa.id_pessoa, "valor": 50.0}
    response: TestResponse = client.post(url, json=data)
    assert response.status_code == 200

    response: TestResponse = client.get(url_extract)
    assert response.status_code == 200
    assert isinstance(response.json, list)

    assert len([x for x in response.json if x["valor"] == -50.0]) == 1
    assert len([x for x in response.json if x["valor"] == 100.0]) == 1
    conta_obj: Conta = Conta.query.filter_by(id_conta=conta.id_conta).first()
    assert conta_obj.saldo == Decimal(50)
