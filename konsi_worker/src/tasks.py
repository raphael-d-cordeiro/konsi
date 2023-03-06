from typing import Dict, Any

from konsi_worker.src.celery_worker import celery_app
from konsi_worker.src.services import crawler
from konsi_worker.src.core import DBConnection
from konsi_worker.src.models import CrawlerModel


@celery_app.task(bind=True)
def run_crawler(self, body_request: Dict[str, Any]) -> int:

    username = body_request['username']
    password = body_request['password']
    document = body_request['document']

    response = crawler.get_data(username, password, document)

    with DBConnection() as db_connection:
        try:
            new_crawler_response = CrawlerModel(
                task_id=self.request.id,
                document=document,
                crawler_data=response
            )
            db_connection.session.add(new_crawler_response)
            db_connection.session.commit()
        except Exception:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    return
