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
sam build

# alternatively, build using Docker container (had to use on some occasions to manage
# install of python dependencies)
sam build --use-container
```

For local dev, add a file `.env.json` with contents:

```json
{
  "GetWeatherFunction": {
    "DARKSKY_API_KEY": "XXXXXXXXXXX",
    "stage": "local"
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

[AWS SAM CLI](https://github.com/awslabs/aws-sam-cli/blob/develop/docs/deploying_serverless_applications.md) docs.

### Build Artifacts

Ensure build artifacts are available /  up-to-date.

```bash
sam build --use-container

# output
Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml
```

### Package Artifacts

Confirm path to `template.yml` and update `s3-bucket-name`. If not using default AWS profile, replace `aws-profile` with the actual profile name. If using default AWS profile, this line can be removed.

```bash
sam package \
    --template-file .aws-sam/build/template.yaml \
    --output-template-file serverless-output.yaml \
    --s3-bucket s3-bucket-name \
    --profile aws-profile
```

### Deploy Package

Update `new-stack-name` and `aws-profile`.

```bash
sam deploy \
    --template-file serverless-output.yaml \
    --stack-name new-stack-name \
    --capabilities CAPABILITY_IAM \
    --profile aws-profile
```
