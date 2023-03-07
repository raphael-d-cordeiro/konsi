import asyncio
from typing import Generator

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from starlette.testclient import TestClient
from faker import Faker
from fastapi import FastAPI
from httpx import AsyncClient

from main import app as app_client

fake = Faker('pt_BR')


@pytest.fixture(scope='session')
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# Create a new application for testing


@pytest.fixture
def app() -> FastAPI:

    return app_client

# Make requests in our tests


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url='http://testserver',
            headers={'Content-Type': 'application/json'},
        ) as client:
            yield client


@pytest.fixture(scope='session')
def fake_post() -> dict:
    username = fake.user_name()

    return {
        'document': fake.cpf(),
        'username': username,
        'password': username,
    }
