# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
# FROM python:alpine
FROM lambci/lambda:build-python3.7

LABEL Name=met-service Version=0.0.1
EXPOSE 5000

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements-test.txt
