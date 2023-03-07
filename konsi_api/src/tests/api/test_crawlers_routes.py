import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
)

# decorate all tests with @pytest.mark.asyncio
pytestmark = pytest.mark.asyncio


class TestCrawlersRoute:
    @pytest.mark.parametrize(
        'end_point',
        ['/api/v1/crawlers/']
    )
    async def test_post_route_exists(
        self, app: FastAPI, client: AsyncClient, end_point: str
    ) -> None:
        response = await client.post(app.url_path_for('/crawlers/'), json={})
        assert response.status_code != HTTP_404_NOT_FOUND

    async def test_get_route_exists(
        self, app: FastAPI, client: AsyncClient, end_point: str
    ) -> None:
        response = await client.get(app.url_path_for('/crawlers/'), json={})
        assert response.status_code != HTTP_404_NOT_FOUND

    async def test_post_crawlers(
            self, app: FastAPI, client: AsyncClient, fake_post: dict
    ) -> None:
        response = await client.post(
            app.url_path_for('crawlers'), json=fake_post
        )
        assert response.status_code == HTTP_201_CREATED
        assert response.json() is not None

        fake_post['task_id'] = response.json()['task_id']

    async def test_get_crawlers(
            self, app: FastAPI, client: AsyncClient, fake_post: dict
    ) -> None:
        task_id = fake_post['task_id']
        header = {"task_id": task_id}

        response = await client.get(
            app.url_path_for('crawlers'), headers=header
        )

        assert response.status_code == HTTP_200_OK
        assert response.json() is not None
