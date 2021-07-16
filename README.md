# python-starter

## Prerequisites
* install pipenv (E.g. `brew install pipenv`).
* install pre-commit (E.g. `brew install pre-commit`).

## Useful Commands

`pipenv run pytest` - runs the tests

`pipenv run coverage run -m pytest && pipenv run coverage report` - runs the tests + coverage

`pipenv run black .` - runs black.

`pipenv run flake8 .` - runs flake8.

`pipenv run isort .` - runs isort.

## Pre-commit Hooks

To enable pre-commit hooks run the following command:

```
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

The pre-commit hook will enforce isort, black and flake8 before every commit and run pytest + coverage before every push.

## Flask (web application)

Flask web application can be executed by running: `pipenv run flask run`

### Prometheus

Prometheus client is available through Flask: `http://127.0.0.1:5000/metrics/`