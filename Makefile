
install:
	sudo python setup.py install

clean:
	sudo rm -rf build/ dist/

register:
	python setup.py register

upload:
	python setup.py sdist upload

tag:
	git tag $$(python setup.py --version)

release: clean register upload tag
