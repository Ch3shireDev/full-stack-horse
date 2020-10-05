# FROM ubuntu:16.04
# RUN apt-get update -y && apt-get install -y python-pip python-dev

# FROM tiangolo/uwsgi-nginx-flask:python3.8

FROM python:alpine
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]