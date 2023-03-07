import pytest
from faker import Faker

fake = Faker('pt_BR')

# Create a new application for testing


@pytest.fixture(scope='function')
def fake_kwargs() -> dict:

    return {
        'document': fake.cpf(),
        'username': 'testekonsi',
        'password': 'testekonsi',
    }
