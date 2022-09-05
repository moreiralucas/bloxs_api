"""Block test Module"""
from typing import Dict
from werkzeug.test import TestResponse
from models import Conta, Pessoa


def test_block_account(app):
    """
    GIVEN a account id
    WHEN the '/account/<account_id>/block' is requested (GET)
    THEN return the account block status
    """

    pessoa: Pessoa = Pessoa(
        nome = "Fulano de Tal",
        cpf = "71966618077",
        data_nascimento = "1988-01-01",
    )
    pessoa.save()

    conta: Conta = Conta(
        id_pessoa=pessoa.id_pessoa,
        limite_saque_diario=1000.00,
        flag_ativo=True,
        tipo_conta=1
    )
    conta.save()

    client = app.test_client()
    url = f'/account/{conta.id_conta}/block'

    response: TestResponse = client.post(url)
    assert response.status_code == 200
    assert response.json["flag_ativo"] is False

def test_dont_handle_withdraw(app, conta, pessoa):
    """
    GIVEN a block account and the account id
    WHEN the '/account/<account_id>/block' is requested (POST)
    THEN return the unsuccessful status
    """

    client = app.test_client()
    url = f'/account/{conta.id_conta}/block'

    response: TestResponse = client.post(url)
    assert response.status_code == 200

    url = f'/account/{conta.id_conta}/withdraw'
    data: Dict = {
        "id_pessoa": pessoa.id_pessoa,
        "valor": 500.0
    }

    response: TestResponse = client.post(url, data)
    assert response.status_code == 200
    assert response.json["message"] == "blocked account"
