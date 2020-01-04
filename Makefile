project_dir := $(patsubst %/,%,$(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
PATH := $(project_dir)/venv/bin:$(PATH)

all:

format:
	python -m black mingus mingus_examples unittest

dev:
	pip install -e '.[fft,fluidsynth]' -r requirements-dev.in

install:
	pip install .

test:
	(cd unittest; python run_tests.py)

test-fluidsynth:
	(cd unittest; python run_fluidsynth_tests.py)

test-lilypond:
	(cd unittest; python run_lilypond_tests.py)

test-all: test test-fluidsynth test-lilypond

clean:
	rm -rf build/ dist/

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

tag:
	git tag $$(python setup.py --version)

release: clean build upload tag

.PHONY: format \
	dev install \
	test test-fluidsynth test-lilypond test-all \
	clean build \
	upload tag release
