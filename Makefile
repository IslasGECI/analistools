mutation:
	mutmut run \
		--paths-to-mutate bootstraping_tools \
		--paths-to-mutate cli_paths \
		--paths-to-mutate geci_plots

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