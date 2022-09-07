"""Withdraw test Module"""
from typing import Dict
from werkzeug.test import TestResponse
from models import Conta, Pessoa


def test_withdraw_account(app):
    """
    GIVEN a account id and a value
    WHEN the '/account/<account_id>/deposit' is requested (GET)
        and the account has founds
    THEN decrement account value
    """

    pessoa: Pessoa = Pessoa(
        nome="Sicrano da Silva",
        cpf="715579180470",
        data_nascimento="1992-01-02",
    )
    pessoa.save()

    conta: Conta = Conta(
        id_pessoa=pessoa.id_pessoa,
        limite_saque_diario=1000.00,
        flag_ativo=True,
        tipo_conta=1,
    )
    conta.save()
    conta.add_money(800.0)

    client = app.test_client()
    url: str = f"/account/{conta.id_conta}/withdraw"
    data: Dict = {"id_pessoa": pessoa.id_pessoa, "valor": 500.0}

    response: TestResponse = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json["message"] == "success"

    client = app.test_client()
    url: str = f"/account/{conta.id_conta}/withdraw"
    data: Dict = {"id_pessoa": pessoa.id_pessoa, "valor": 500.0}

    response: TestResponse = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json["message"] == "insufficient funds"
