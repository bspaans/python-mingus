Contributor Guide
=================

Project Conventions
-------------------

* **Source code formatting:** use [black][]. A recipe for running it is provided in the Makefile: just `make format`.


Development setup
-----------------

* Set up a Python virtual environment with `python -m venv venv` at the root of this project.
* Run `make dev` to install the project in editable mode and install dependencies.

```shell
$ python -m venv venv
$ make dev
```

The Makefile is already configured to use Python from the virtual environment `venv`; for running other commands, activate it using `source venv/bin/activate`.


[black]: https://black.readthedocs.io/en/stable/
