"""Account test Module"""
import json
from typing import Dict
from werkzeug.test import TestResponse
from models import Pessoa


def test_create_account(app):
    """
    GIVEN a account data
    WHEN the '/account' is requested (POST)
    THEN create and return an account instance
    """

    instance: Pessoa = Pessoa(**{
        "nome": "Fulano de Tal",
        "cpf": "71530918073",
        "data_nascimento": "01/01/1990"
    })
    instance.save()

    client = app.test_client()
    url = '/account'
    data: Dict = {
        "id_pessoa": instance.id_pessoa,
        "limite_saque_diario": "1000.00",
        "flag_ativo": True,
        "tipo_conta": "1"
    }

    response: TestResponse = client.post(url, data)
    assert response.status_code == 200

    response_json: Dict = json.loads(response.data.decode('utf-8'))
    assert isinstance(response_json, dict)
