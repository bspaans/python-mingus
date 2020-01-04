
format:
	python -m black mingus mingus_examples unittest

install:
	python setup.py install

test:
	(cd unittest; python run_tests.py)

test-fluidsynth:
	(cd unittest; python run_fluidsynth_tests.py)

test-lilypond:
	(cd unittest; python run_lilypond_tests.py)

test-all: test test-fluidsynth test-lilypond

clean:
	rm -rf build/ dist/

register:
	python setup.py register

upload:
	python setup.py sdist upload

tag:
	git tag $$(python setup.py --version)

release: clean register upload tag
