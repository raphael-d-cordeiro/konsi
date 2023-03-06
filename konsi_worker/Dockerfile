FROM python:3.10.8-slim-buster

#Install
WORKDIR /konsi_worker

COPY ./requirements.txt /konsi_worker/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /konsi_worker/requirements.txt

COPY . .

# Run.
CMD \
  celery -A src.celery_worker worker -E --loglevel=INFO --concurrency=1 -Ofair