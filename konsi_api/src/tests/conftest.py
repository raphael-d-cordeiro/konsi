from typing import Generator, Any

import pytest

from fastapi.testclient import TestClient
from faker import Faker
from fastapi import FastAPI

from main import app as app_client

fake = Faker('pt_BR')

# Create a new application for testing


@pytest.fixture
def app() -> FastAPI:

    return app_client

# Make requests in our tests


@pytest.fixture(scope="function")
def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope='function')
def fake_post() -> dict:
    username = fake.user_name()

    return {
        'document': fake.cpf(),
        'username': username,
        'password': username,
    }


@pytest.fixture(scope='function')
def fake_task_id() -> dict:
    return {
        "task_id": fake.uuid4(),
        "crawler_filter_result": "BENEFITS_NUMBERS_ONLY"}
