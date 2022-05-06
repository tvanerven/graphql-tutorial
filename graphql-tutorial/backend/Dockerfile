FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk upgrade

WORKDIR backend

COPY scripts /scripts/
COPY project_backend ./

RUN pip install -U pip

COPY requirements.txt ./

RUN pip install -r requirements.txt