FROM python:3.10.12-alpine3.18

WORKDIR /opt/application

RUN apk update && apk upgrade

RUN apk add --no-cache sqlite

RUN /usr/bin/sqlite3 /db/test.db

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./config ./config

COPY models ./models

COPY routes ./routes

COPY schemas ./schemas

COPY services ./services

COPY utils ./utils

COPY app.py ./app.py

EXPOSE 8000

CMD python -m uvicorn app:app --host 0.0.0.0 --port 8000