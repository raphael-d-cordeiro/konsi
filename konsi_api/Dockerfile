FROM python:3.10.8-slim-buster

#Install
WORKDIR /konsi
COPY . .
RUN pip3 install -r requirements.txt

# Run.
EXPOSE 8000
CMD ["python", "konsi/konsi_api/src/main.py"]