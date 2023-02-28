from celery import Celery


celery_app = Celery(
    "konsi_worker",
    broker='amqp://admin:123@localhost:5672//',
    include=['konsi_worker.src.tasks']
)

celery_app.conf.timezone = 'America/Sao_Paulo'
celery_app.conf.result_backend = 'amqp://admin:123@localhost:5672//'
