FROM python:3.11

WORKDIR /event

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./event ./
COPY ./requirements.txt ./
COPY ./gunicorn_start ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r ./requirements.txt --no-cache-dir

RUN python3 manage.py collectstatic --noinput