FROM python:3.10-alpine

RUN apk update && \
    apk upgrade

WORKDIR backend

COPY scripts /scripts/
COPY project_backend ./

RUN pip install -U pip

COPY requirements.txt ./

RUN pip install -r requirements.txt