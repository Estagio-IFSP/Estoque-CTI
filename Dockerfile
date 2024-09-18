# syntax = docker/dockerfile:1.4

FROM docker.io/library/python:3.12-alpine as builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
