# Makefile

install:
	uv sync


package-install:
	uv tool install dist/*.whl


build:
	uv build