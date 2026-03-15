# Makefile

install:
	uv sync


package-install:
	uv tool install dist/*.whl


build:
	uv build


lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml