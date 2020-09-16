VENV=.venv
PACKAGE=ocr

.PHONY: clean
clean:
	rm -rf $(VENV) $(PACKAGE).egg-info

.PHONY: venv
venv: clean
	virtualenv $(VENV)

.PHONY: bootstrap
bootstrap: venv
	$(VENV)/bin/pip3 install --upgrade pip
	$(VENV)/bin/pip3 install -U -r requirements.txt
	$(VENV)/bin/pip3 install -e .

.PHONY: bootstrap-dev
bootstrap-dev: bootstrap
	$(VENV)/bin/pip3 install pytest

.PHONY: test
test:
	@$(VENV)/bin/pytest tests
