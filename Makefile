mutation:
	mutmut run --paths-to-mutate bootstraping_tools

.PHONY: install mutation tests

install:
	pip install --editable .

tests: install
	pytest --verbose