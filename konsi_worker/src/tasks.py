from typing import Dict, Any

from konsi_worker.src.consumer import celery_app
from services import crawler


@celery_app.task(bind=True)
def run_crawler(self, body_request: Dict[str, Any]) -> int:

    username = body_request['username']
    password = body_request['password']
    document = body_request['document']

    response = crawler.get_data(username, password, document)

    return
