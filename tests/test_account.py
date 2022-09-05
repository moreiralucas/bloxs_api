"""Account test Module"""
from typing import Dict
from datetime import datetime
from werkzeug.test import TestResponse
from models import Pessoa, Conta


def test_create_account(app):
    """
    GIVEN a account data
    WHEN the '/account' is requested (POST)
    THEN create and return an account instance
    """

    instance: Pessoa = Pessoa()
    instance.nome = "Fulano de Tal"
    instance.cpf = "71530918073"
    instance.data_nascimento = "1990-01-01"
    instance.save()

    client = app.test_client()
    url = '/account'
    data: Dict = {
        "id_pessoa": instance.id_pessoa,
        "limite_saque_diario": "1000.00",
        "flag_ativo": True,
        "tipo_conta": "1"
    }

    today: str = datetime.now().strftime("%Y-%m-%d")
    response: TestResponse = client.post(url, json=data)
    assert response.status_code == 201
    assert response.json["limite_saque_diario"] == 1000.0
    assert response.json["saldo"] == 0.0
    assert response.json["id_pessoa"] == instance.id_pessoa
    assert response.json["data_criacao"] == today
