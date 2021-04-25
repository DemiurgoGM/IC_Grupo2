# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && apt-get install python3-opencv -y
RUN pip install -r requirements.txt &&  pip install pymupdf

COPY . /code/