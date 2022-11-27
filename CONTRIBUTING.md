
**You need PYTHON3!**

This instructions are for linux base systems. (Linux, MacOS, BSD, etc.)

## Setting up your own virtual environment

Run `make virtualenv` to create a virtual environment.
then activate it with `source .venv/bin/activate`.

## Install the project in develop mode

Run `make install` to install the project in develop mode.

## Run the tests to ensure everything is working

Run `make test` to run the tests.
Ensure code coverage report shows `100%` coverage, add tests to your PR.

## Format the code

Run `make fmt` to format the code.

## Run the linter

Run `make lint` to run the linter.

## Build the docs locally

Run `make docs` to build the docs.

Ensure your new changes are documented.


## Makefile utilities

This project comes with a `Makefile` that contains a number of useful utility.

```bash 
❯ make
Usage: make <target>

Targets:
help:             ## Show the help.
install:          ## Install the project in dev mode.
fmt:              ## Format code using black & isort.
lint:             ## Run pep8, black, mypy linters.
test: lint        ## Run tests and generate coverage report.
watch:            ## Run tests on every change.
clean:            ## Clean unused files.
virtualenv:       ## Create a virtual environment.
docs:             ## Build the documentation.
```
