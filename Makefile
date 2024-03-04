.PHONY: run install better uncache clean venv res

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

# Extract the second word from the argument list, which is the resource name
res:=$(wordlist 2,2,$(MAKECMDGOALS))

# If the resource name is not provided, prompt the user
ifndef res
res:
	@echo "Please specify the resource name. Example: make res NAME"
else
res:
	poetry run api create res $(res)
endif

# Ensure make passes the argument to res rule
%:
	@: