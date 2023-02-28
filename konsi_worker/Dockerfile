FROM python:3.10.8-slim-buster

WORKDIR /konsi_worker
RUN mkdir -p konsi_worker/src
COPY src/ konsi_worker/src
COPY .env.debug .env
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Run.
CMD \
  celery -A konsi_worker.src.celery_app worker -E --loglevel=INFO --concurrency=1 -Ofair