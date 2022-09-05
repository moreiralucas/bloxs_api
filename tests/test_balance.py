"""Balance test Module"""
from werkzeug.test import TestResponse
from models import Conta, Pessoa


def test_get_balance(app):
    """
    GIVEN a account id
    WHEN the '/account/<account_id>/balance' is requested (GET)
    THEN return the balance info
    """

    pessoa: Pessoa = Pessoa(
        nome = "Sicrano da Silva",
        cpf = "717777918073",
        data_nascimento = "1991-01-01",
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
    url = f'/account/{conta.id_conta}/balance'

    response: TestResponse = client.get(url)
    assert response.status_code == 200
    assert response.json["saldo"] == 0.0

    conta.add_money(50.0)

    response: TestResponse = client.get(url)
    assert response.status_code == 200
    assert response.json["saldo"] == 50.0
