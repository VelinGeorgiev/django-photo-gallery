# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code/django_photo_gallery
COPY django_photo_gallery/requirements.txt /code/django_photo_gallery
RUN pip3 install -r requirements.txt
COPY . /code/

