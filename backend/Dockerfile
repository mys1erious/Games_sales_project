FROM python:3.9.12-alpine

ENV PYTHONBUFFERED 1
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

WORKDIR /games_sales_project/backend

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
