.PHONY: up down test lint

up:
    tilt up

down:
    tilt down

test:
    poetry run pytest

lint:
    poetry run black .
    poetry run isort .
    poetry run flake8 .
