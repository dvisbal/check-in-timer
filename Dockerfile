# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /check-in-timer

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
