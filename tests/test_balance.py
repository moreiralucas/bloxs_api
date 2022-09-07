"""Balance test Module"""
from werkzeug.test import TestResponse
from models import Conta


def test_get_balance(app, conta: Conta):
    """
    GIVEN a account id
    WHEN the '/account/<account_id>/balance' is requested (GET)
    THEN return the balance info
    """

    client = app.test_client()
    url: str = f"/account/{conta.id_conta}/balance"

    response: TestResponse = client.get(url)
    assert response.status_code == 200
    assert response.json["saldo"] == 0.0

    conta.add_money(50.0)

    response: TestResponse = client.get(url)
    assert response.status_code == 200
    assert response.json["saldo"] == 50.0
