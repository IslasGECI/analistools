mutation:
	mutmut run --paths-to-mutate bootstraping_tools

.PHONY: clean install mutation tests

install:
	pip install --editable .

tests: install
	pytest --verbose

clean:
	rm --recursive --force test/__pycache__
	rm --recursive --force bootstraping_tools/__pycache__
	rm --recursive --force bootstraping_tools.egg-info
	rm --force .mutmut-cache