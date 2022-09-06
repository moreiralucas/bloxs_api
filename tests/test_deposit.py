"""Deposit test Module"""
from typing import Dict
from werkzeug.test import TestResponse
from models import Conta


def test_deposit_in_account(app, conta: Conta):
    """
    GIVEN a account instance
    WHEN the '/account/<account_id>/deposit' is requested (GET)
    THEN update an account instance with new deposit value
    """

    client = app.test_client()
    url: str = f'/account/{conta.id_conta}/deposit'

    data: Dict = {
        "valor": 100.0
    }

    response: TestResponse = client.put(url, json=data)
    assert response.status_code == 200
    assert response.json["message"] == "success"
