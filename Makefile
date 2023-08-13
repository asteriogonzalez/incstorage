.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := @python3 -c "$$BROWSER_PYSCRIPT"



# ----------------------------------------------------------
# Helpers
# ----------------------------------------------------------
.PHONY: help

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# ----------------------------------------------------------
# virtual env
# ----------------------------------------------------------
.PHONY: create-venv

create-venv: ## craeate virtual Environment
	virtualenv venv
	
# ----------------------------------------------------------
# Coding Helpers
# ----------------------------------------------------------

clean: clean-build clean-pyc clean-test docker-clean ## remove all build, test, coverage and Python artifacts

# ----------------------------------------------------------
# docker Setup
# ----------------------------------------------------------
.PHONY: docker-build docker-clean docker-run docker-test

docker-build: ## build and execute server in a docker container
	sudo docker compose build

docker-run: docker-build ## build and execute server in a docker container
	sudo docker compose up --build

docker-test: docker-build ## test server in a docker container
	sudo docker compose run --rm web-server python -m pytest

docker-clean: ## clean container
	sudo docker rm web-server


# ----------------------------------------------------------
# Test Helpers
# ----------------------------------------------------------
.PHONY: test test-parallel test-all clean-test ptw

test: ## run tests quickly with the default Python
	pytest

test-parallel: ## run parallel pytests with the default Python
	@python3 -n 5

test-all: ## run tests on every Python version with tox
	tox

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

ptw: ## pytest-watch
	ptw -- -s -n 2


# ----------------------------------------------------------
# Code Quality Helpers
# ----------------------------------------------------------
.PHONY: coverage lint lint/pylint lint/flake8 lint/black

coverage: ## check code coverage quickly with the default Python
	coverage run --source incstorage -m pytest	
	coverage run -a --source tests -m pytest

	# coverage combine
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

lint/pylint: ## pylint checker
	pylint incstorage tests

lint/flake8: ## check style with flake8
	flake8 incstorage tests
lint/black: ## check style with black
	black --check incstorage tests

lint: lint/pylint lint/flake8 lint/black ## check style

# ----------------------------------------------------------
# Documentation Helpers
# ----------------------------------------------------------
.PHONY: docs livehtml #servedocs

# ----------------------------------------------------------
# Sphinx Parameters
# ----------------------------------------------------------
# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = @python3 -m sphinx
SPHINXPROJ    = python-coding-challenge
SOURCEDIR     = docs
BUILDDIR      = docs/_build
AUTODIR       = docs/_autosummary
PORT          = 18086
IGNORE        = ".* *.log *.json $(AUTODIR) $(BUILDDIR)"

# seconds before opening the browser
AUTODELAY     = 0

# a sleep to avoid too much CPU use while typing documentation
# and the system is rebuilind too fast
AUTOOPS       = --pre-build "sleep 5"

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/incstorage.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ incstorage
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

livehtml:
	nice -n 20 sphinx-autobuild -b html $(ALLSPHINXOPTS) --open-browser --port $(PORT) --watch . --re-ignore "\.git/" $(SOURCEDIR) $(BUILDDIR)/html --ignore $(IGNORE) --delay $(AUTODELAY) $(AUTOOPS)

clean-doc: ## remove docs artifacts
	rm -fr docs/_build

# ----------------------------------------------------------
# Environment Setup
# ----------------------------------------------------------
.PHONY: develop-setup install-testing-requisites

develop-setup: install-testing-requisites ## install module as developer
	@python3 setup.py develop 

install-testing-requisites: ## install testing requisites
	@pip install -U -r requirements/base.txt
	@pip install -U -r requirements/testing.txt

# ----------------------------------------------------------
# Deployment Helpers
# ----------------------------------------------------------
.PHONY: release dist install clean-build clean-pyc

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	@python3 setup.py sdist
	@python3 setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	@python3 setup.py install

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

