# Met Service

[![CircleCI](https://circleci.com/gh/sam-atkins/met-service/tree/main.svg?style=svg)](https://circleci.com/gh/sam-atkins/met-service/tree/main)
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Description

Meteorological API service.

## Development

Prerequisites:

* Python 3
* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)

```bash
# set up a virtual env
virtualenv -p python3.7 env

# activate the virtual env
source env/bin/activate

# install requirements
pip install -r requirements-dev.txt

# build the Lambda function for local dev
sam build --use-container
```

For local dev, add a file `.env.json` with contents:

```json
{
  "GetWeatherFunction": {
    "DARKSKY_API_KEY": "XXXXXXXXXXX"
  }
}
```

And add the Darksky api key to replace XXXXXXXXXXX.

To run locally:

```bash
# run API
sam local start-api -d 3000 --env-vars .env.json --profile {aws-profile}

# invoke function
sam local invoke GetWeatherFunction --event event.json --env-vars .env.json --profile {aws-profile}
```

More info in the [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli/blob/develop/docs/usage.md#invoke-functions-locally) docs.

## Tests

```bash
# make sure venv is activated
source env/bin/activate

# run tests
python -m pytest -vv
```

## Deploy

[Placeholder]

More info in the [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli/blob/develop/docs/deploying_serverless_applications.md) docs.
