project_dir := $(patsubst %/,%,$(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
PATH := $(project_dir)/venv/bin:$(PATH)

all:

format:
	python -m black mingus mingus_examples tests

dev:
	pip install -e '.[fft,fluidsynth]' -r requirements-dev.in

install:
	pip install .

test: test-unit

test-unit:
	python -m unittest discover tests.unit

test-fluidsynth:
	python -m unittest tests.integration.test_fluidsynth

test-lilypond:
	python -m unittest tests.integration.test_lilypond

test-all: test test-fluidsynth test-lilypond

clean:
	rm -rf build/ dist/

build:
	python setup.py sdist bdist_wheel

sign-build: build
	(\
		cd dist; \
		rm -f *.asc; \
		for a in *.whl *.gz; do \
			gpg --armor --detach-sign "$$a"; \
		done)

upload:
	twine upload dist/*

tag:
	git tag -s $$(python setup.py --version)

release: clean build sign-build upload tag

.PHONY: format \
	dev install \
	test test-unit test-fluidsynth test-lilypond test-all \
	clean build \
	upload tag release
