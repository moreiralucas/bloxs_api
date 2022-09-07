"""Configuration Test Module"""
import pytest

from app import app as application
from models.base_mixin import db
from models import Pessoa, Conta


@pytest.fixture
def app():
    """Create database"""

    with application.app_context():
        db.create_all()

        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture
def pessoa():
    """Create Pessoa Model"""
    pessoa_obj: Pessoa = Pessoa(
        nome="Fulano de Tal",
        cpf="71966618077",
        data_nascimento="1988-01-01",
    )
    pessoa_obj.save()

    return pessoa_obj


@pytest.fixture
def conta(pessoa):  # pylint: disable=redefined-outer-name
    """Create Conta Model"""

    conta_obj: Conta = Conta(
        id_pessoa=pessoa.id_pessoa,
        limite_saque_diario=1000.00,
        flag_ativo=True,
        tipo_conta=1,
    )
    conta_obj.save()

    return conta_obj
