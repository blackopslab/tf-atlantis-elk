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
	@echo "Activating the virtual environment..."
	. .venv/bin/activate
	@echo ""
	@echo "TF-ATLANTIS-ELK CLI Tool"
	@python3 src/main.py install "env/.env" --verbose
	@echo ""

expose:
	@./bin/cloudflared tunnel --url http://localhost:32141

clean:

	@echo "Cleaning up..."
	@helm list -n atlantis -q | while read -r release; do \
  	namespace=$$(helm list --all-namespaces -o json | jq -r ".[] | select(.name == \"$release\") | .namespace"); \
  	if [ -n "$$namespace" ]; then \
    	helm uninstall "$$release" --namespace "$$namespace"; \
  	fi; \
	done
	@kubectl delete ns atlantis &
	@kubectl delete ns monitoring &
	@bash src/scripts/finalize_namespace.sh monitoring
	@bash src/scripts/finalize_namespace.sh atlantis
	@rm -rf bin/*
	@rm -rf tmp/*
	@rm -rf .venv
	@rm -rf terraform/.terraform*
	@rm -rf terraform/*.tfstate*
	@rm -rf *.tfstate*
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
