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
	test test-fluidsynth test-lilypond test-all \
	clean build \
	upload tag release
