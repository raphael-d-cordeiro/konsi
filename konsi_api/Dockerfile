FROM python:3.10.8-slim-buster

#Install
WORKDIR /konsi_api

COPY ./requirements.txt /konsi_api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /konsi_api/requirements.txt

COPY . .

# Run.
EXPOSE 8000
CMD ["python", "src/main.py"]