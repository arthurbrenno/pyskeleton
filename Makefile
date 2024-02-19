run:
	poetry run python -m app

install:
	poetry install --with dev

better:
	poetry run flake8

uncache:
	find app framework -type d -name "__pycache__" -exec rm -rf {} +

clean:
	rm -rf .venv

venv:
	poetry shell
