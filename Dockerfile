FROM lambci/lambda:build-python3.7

LABEL Name=met-service Version=0.0.1
EXPOSE 5000

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements-test.txt
