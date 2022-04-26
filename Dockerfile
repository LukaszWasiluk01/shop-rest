# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python3 -m venv /opt/venv
WORKDIR /code
COPY requirements.txt /code/
RUN  . /opt/venv/bin/activate && pip install -r requirements.txt
COPY . /code/