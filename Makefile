SHELL := /bin/bash
.PHONY: help config install expose clean prune apply destroy force_rollout finalize_namespaces format alpha release

help:
	@echo "Makefile Commands:"
	@echo "  config               - Set up the virtual environment."
	@echo "  install              - Install the required Python packages."
	@echo "  expose               - Exposes to the internet using cloudflared"
	@echo "  clean                - Remove binary files."
	@echo "  prune                - Prune downloaded and temporary files"
	@echo "  apply                - Applie all Terraform manifests."
	@echo "  destroy              - Destroy all Terraform resources."
	@echo "  force_rollout        - Destroys namespaces manually."
	@echo "  finalize_namespaces  - Destroys namespaces stuck in terminating state"
	@echo "  format               - Format Terraform files."
	@echo "  alpha                - Generate changelog and create an alpha tag."
	@echo "  release              - Generate changelog and create a release tag."

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
		echo ""; \
	fi
	@echo ""

expose:
	@sudo sysctl -w net.core.rmem_max=7500000
	@sudo sysctl -w net.core.wmem_max=7500000
	@./bin/cloudflared tunnel --url http://localhost:32141

clean: destroy prune

prune:
	@echo "Pruning files..."
#	@rm -rf bin/*
	@rm -rf tmp/*
	@rm -rf .venv
	@rm -rf terraform/.terraform*
	@rm -rf terraform/*.tfstate*
	@echo ""

apply:
	@if ! [ -d .venv ]; then \
		echo "No virtual environment in .venv. Please run `make config`."; \
	else \
		echo "Activating the virtual environment..."; \
		source .venv/bin/activate; \
		python3 src/main.py apply "env/.env" --verbose; \
		echo ""; \
	fi
	@echo ""

destroy:
	@if ! [ -d .venv ]; then \
		echo "No virtual environment in .venv. Please run `make config`."; \
	else \
		echo "Activating the virtual environment..."; \
		source .venv/bin/activate; \
		python3 src/main.py destroy "env/.env" --verbose; \
		echo ""; \
	fi
	@echo ""

force_rollout:
	@bash src/scripts/force_rollout.sh

finalize_namespaces:
	@bash src/scripts/force_rollout.sh

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
