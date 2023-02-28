from time import sleep
from konsi_worker.src.celery_app import celery_app


@celery_app.task
def dummy_task(s: int = 5):
    print('starting dummy task')
    sleep(s)
    print('done')
    return s


@celery_app.task
def dummy_add(x: int, y: int) -> int:
    return x + y
