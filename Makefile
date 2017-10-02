.PHONY: help deps lint test

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  lint        check style with flake8"
	@echo "  test        run all your tests using pytest"
	@echo
	@echo "Remember to activate your environment with: env/bin/activate"

env:
	python3 -m venv env && \
	source env/bin/activate && \
	make deps

deps:
	pip install --upgrade pip
	pip install -r requirements.txt

lint: env
	flake8-3 --exclude=env .

test: env
	source env/bin/activate && \
	pytest tests

