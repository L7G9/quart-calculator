HERE = $(shell pwd)
VENV = .
VIRTUALENV = virtualenv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python

INSTALL = $(BIN)/pip install --no-deps

all: build

$(PYTHON):
	$(VIRTUALENV) $(VTENV_OPTS) $(VENV)

build: $(PYTHON)
	$(PYTHON) setup.py develop

run:
	QUART_APP=calculator_service bin/quart run
