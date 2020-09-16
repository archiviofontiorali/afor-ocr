VENV=.venv
PACKAGE=ocr

.PHONY: clean
clean:
	@echo "════ Clean up old virtualenv and cache ════" 
	rm -rf $(VENV) $(PACKAGE).egg-info

.PHONY: venv
venv: clean
	@echo "════ Create virtualenv ════" 	
	virtualenv -p /usr/bin/python3 $(VENV)
	$(VENV)/bin/pip3 install --upgrade pip

.PHONY: bootstrap
bootstrap: venv
	@echo "════ Install dependencies and package ════"
	$(VENV)/bin/pip3 install -U --prefer-binary --use-feature=2020-resolver -r requirements.txt
	$(VENV)/bin/pip3 install -e .

.PHONY: bootstrap-dev
bootstrap-dev: bootstrap
	@echo "════ Install dev utilities ════"
	$(VENV)/bin/pip3 install pytest

.PHONY: test
test:
	@$(VENV)/bin/pytest tests
