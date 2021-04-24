# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 python3-opencv -y
RUN pip install -r requirements.txt

COPY . /code/