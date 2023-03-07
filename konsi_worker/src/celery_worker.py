import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

_AMPQ_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
_AMPQ_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
_AMPQ_HOST = os.environ.get('RABBITMQ_DEFAULT_HOST')
_REDIS_HOST = os.environ.get('REDIS_HOST')

celery_app = Celery(
    "konsi_api",
    broker=f'amqp://{_AMPQ_USER}:{_AMPQ_PASS}@{_AMPQ_HOST}:5672//',
    result_backend=f'redis://{_REDIS_HOST}:6379/0',
    include=['src.tasks']
)

celery_app.conf.timezone = 'America/Sao_Paulo'
