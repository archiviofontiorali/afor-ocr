PYTHON_VERSION=3

PACKAGE=ocr
SHELL=/bin/bash
VENV=.venv

PIP=$(VENV)/bin/pip3

bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)


.PHONY: bootstrap
bootstrap: venv develop

	
.PHONY: clean
clean:
	@echo "$(boid)Clean up old virtualenv and cache$(sgr0)"
	rm -rf $(VENV) $(PACKAGE).egg-info .pytest_cache

.PHONY: venv
venv: clean
	@echo "$(bold)Create virtualenv$(sgr0)"	
	virtualenv -p /usr/bin/python$(PYTHON_VERSION) $(VENV)
	$(PIP) install --upgrade pip setuptools

.PHONY: develop
develop:
	@echo "$(bold)Install and update develop requirements$(sgr0)"
	$(PIP) install --upgrade .[develop]
	$(PIP) install --upgrade .[testing]
	$(PIP) install --upgrade .[demo]
	$(PIP) install -e .	

.PHONY: demo
demo:
	@$(VENV)/bin/panel serve --dev --show demo

.PHONY: test
test: 
	$(VENV)/bin/python -m pytest -p no:warnings

.PHONY: requirements.txt
requirements.txt:
	@echo "$(bold)Freeze dependencies$(sgr0)"
	$(PIP) freeze > $@