"""Block test Module"""
from typing import Dict
from werkzeug.test import TestResponse
from models import Conta, Pessoa


def test_block_account(app, conta: Conta):
    """
    GIVEN a account id
    WHEN the '/account/<account_id>/block' is requested (GET)
    THEN return the account block status
    """

    client = app.test_client()
    url: str = f'/account/{conta.id_conta}/block'

    response: TestResponse = client.post(url)
    assert response.status_code == 200
    assert response.json["flag_ativo"] is False

def test_dont_handle_withdraw(app, conta: Conta, pessoa: Pessoa):
    """
    GIVEN a block account and the account id
    WHEN the '/account/<account_id>/withdraw' is requested (POST)
    THEN return the unsuccessful status
    """

    client = app.test_client()
    url: str = f'/account/{conta.id_conta}/block'

    response: TestResponse = client.post(url)
    assert response.status_code == 200

    url: str = f'/account/{conta.id_conta}/withdraw'
    data: Dict = {
        "valor": 500.0,
        "id_pessoa": pessoa.id_pessoa,
    }

    response: TestResponse = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json["message"] == "blocked account"

def test_dont_handle_deposit(app, conta: Conta):
    """
    GIVEN a block account and the account id
    WHEN the '/account/<account_id>/deposit' is requested (POST)
    THEN return the unsuccessful status
    """

    client = app.test_client()
    url: str = f'/account/{conta.id_conta}/block'

    response: TestResponse = client.post(url)
    assert response.status_code == 200

    data: Dict = {
        "valor": 100.0
    }

    url: str = f'/account/{conta.id_conta}/deposit'
    response: TestResponse = client.put(url, json=data)
    assert response.status_code == 200
    assert response.json["message"] == "blocked account"
