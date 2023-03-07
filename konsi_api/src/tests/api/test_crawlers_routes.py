from fastapi.testclient import TestClient
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND
)


class TestCrawlersRoute:

    def test_post_crawler_route(self,
                                client: TestClient, fake_post: dict) -> None:

        response = client.post('/crawlers/', json=fake_post)
        assert response.status_code == HTTP_201_CREATED
        assert response.json is not None

    def test_get_crawler_results_without_data(self, client: TestClient,
                                              fake_task_id: dict) -> None:

        response = client.get('/crawlers/', params=fake_task_id)
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.json is not None
