from src.services import crawler


class TestCrawlerFunction:

    def test_crawler_get_data_function(self, fake_kwargs: dict) -> None:

        response = crawler.get_data(**fake_kwargs)
        assert response is not None
