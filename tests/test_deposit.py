"""Deposti test Module"""
import json
from typing import Dict
from werkzeug.test import TestResponse
from models import Conta, Pessoa

def test_deposit_in_account(app):
    """
    GIVEN a account instance
    WHEN the '/account/<account_id>/deposit' is requested (GET)
    THEN update an account instance with new deposit value
    """
    pessoa: Pessoa = Pessoa(
        nome = "Sicrano da Silva",
        cpf = "717777918070",
        data_nascimento = "1992-01-01",
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
    url = f'/account/{conta.id_conta}/deposit'
    data: Dict = {
        "id_pessoa": pessoa.id_pessoa,
        "valor": 100.0
    }

    response: TestResponse = client.post(url, data)
    assert response.status_code == 200
