SHELL := /bin/bash
.PHONY: help config install expose clean format alpha release

help:
	@echo "Makefile Commands:"
	@echo "  config   - Set up the virtual environment."
	@echo "  install  - Install the required Python packages."
	@echo "  expose   - Exposes to the internet using cloudflared"
	@echo "  clean    - Remove binary files."
	@echo "  format   - Format Terraform files."
	@echo "  alpha    - Generate changelog and create an alpha tag."
	@echo "  release  - Generate changelog and create a release tag."

all: clean config install

config:
	@echo "0. CREATING ENVIRONMENT"
	@if [ -d .venv ]; then \
		echo "A virtual environment already exists in .venv. Please double-check."; \
	else \
		echo "Setting up the virtual environment..."; \
		python3 -m venv .venv; \
		echo "Activating the virtual environment..."; \
		source .venv/bin/activate; \
		echo "Installing required packages..."; \
		pip3 install -r src/requirements.txt --require-virtualenv --no-input; \
	fi
	@echo ""

install:
	@if ! [ -d .venv ]; then \
		echo "No virtual environment in .venv. Please run `make config`."; \
	else \
		echo "Activating the virtual environment..."; \
		source .venv/bin/activate; \
		echo ""; \
		echo "Installing Atlantis..."; \
		python3 src/main.py install "env/.env" --verbose; \
		echo "";
	fi
	@echo ""

expose:
	@./bin/cloudflared tunnel --url http://localhost:32141

clean:
	@echo "Cleaning up..."
	@rm -rf bin/*
	@rm -rf tmp/*
	@rm -rf .venv
	@rm -rf terraform/.terraform*
	@rm -rf terraform/*.tfstate*
	@echo ""

format:
	@echo "Formatting Terraform files..."
	@terraform fmt
	@echo ""

alpha:
	@echo "Generating changelog and tag..."
	@commit-and-tag-version --prerelease alpha

release:
	@echo "Generating changelog and tag..."
	@commit-and-tag-version
