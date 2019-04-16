# Met Service

[![CircleCI](https://circleci.com/gh/sam-atkins/met-service/tree/main.svg?style=svg)](https://circleci.com/gh/sam-atkins/met-service/tree/main)
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Description

Meteorological API service.

## Development

### Install

```bash
docker-compose up --build
```

The Docker build uses these requirements files:

* `requirements.txt` -> required by the API, installed as part of the Docker build
* `requirements-test.txt` -> used for testing, installed as part of the Docker build

#### Dev requirements

For local dev, the requirements in `requirements-dev.txt` can optionally be installed in a virtual env.

```bash
virtualenv -p python3.7 env

source env/bin/activate

pip install -r requirements-dev.txt
```

### Tests

```bash
# run test container
docker-compose run --entrypoint="" met-service-test  /bin/bash

# run tests
pytest -vv
```

## Deploy

```bash
serverless deploy

# deploy using a specific AWS profile
serverless deploy --aws-profile {AWS_Profile_Name}
```
