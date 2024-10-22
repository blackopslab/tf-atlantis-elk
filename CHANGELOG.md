# Changelog

All notable changes to this project will be documented in this file. See [commit-and-tag-version](https://github.com/absolute-version/commit-and-tag-version) for commit guidelines.

## [2.0.0-alpha.7](///compare/v2.0.0-alpha.6...v2.0.0-alpha.7) (2024-10-22)


### Features

* improve error handling and code organization in install.py 1729e7b

## [2.0.0-alpha.2](///compare/v2.0.0-alpha.1...v2.0.0-alpha.2) (2024-10-21)


### Features

* Enable permission and file checks in install.py cecb6c0
* **util:** add check_permissions_and_files.py and rules.json b842357

## [2.0.0-alpha.6](///compare/v2.0.0-alpha.5...v2.0.0-alpha.6) (2024-10-22)


### Bug Fixes

* **atlantis.yaml:** replace vars fix extra_args in plan and apply steps 6f6533a

## [2.0.0-alpha.5](///compare/v2.0.0-alpha.4...v2.0.0-alpha.5) (2024-10-22)


### Bug Fixes

* refactor environment variables handling ad0e50a

## [2.0.0-alpha.4](///compare/v2.0.0-alpha.3...v2.0.0-alpha.4) (2024-10-22)


### Features

* refactor CLI tool 5d2cd65

## [2.0.0-alpha.3](///compare/v2.0.0-alpha.1...v2.0.0-alpha.3) (2024-10-22)


### Features

* **atlantis.yaml:** integrate GitHub secrets into terraform apply command 07da846
* cloudflared conditional download 8d3faf1
* **helm/atlantis:** update orgAllowlist in values.yaml ebd31ca
* **helm/atlantis:** update repoConfig in values.yaml 8c87294
* refactor atlantis.yaml 08cdad5
* refactor terraform commands in install.py 96ef0a7


### Bug Fixes

* fix atlantis.yaml workflow 69d148f

## [2.0.0-alpha.2](///compare/v2.0.0-alpha.1...v2.0.0-alpha.2) (2024-10-22)


### Features

* **atlantis.yaml:** integrate GitHub secrets into terraform apply command 07da846
* cloudflared conditional download 8d3faf1
* **helm/atlantis:** update orgAllowlist in values.yaml ebd31ca
* **helm/atlantis:** update repoConfig in values.yaml 8c87294
* refactor atlantis.yaml 08cdad5
* refactor terraform commands in install.py 96ef0a7


### Bug Fixes

* fix atlantis.yaml workflow 69d148f

## [2.0.0-alpha.2](///compare/v2.0.0-alpha.1...v2.0.0-alpha.2) (2024-10-22)


### Features

* **atlantis.yaml:** integrate GitHub secrets into terraform apply command 07da846
* cloudflared conditional download 8d3faf1
* **helm/atlantis:** update orgAllowlist in values.yaml ebd31ca
* **helm/atlantis:** update repoConfig in values.yaml 8c87294
* refactor atlantis.yaml 08cdad5
* refactor terraform commands in install.py 96ef0a7


### Bug Fixes

* fix atlantis.yaml workflow 69d148f

## [1.2.0](///compare/v1.2.0-alpha.0...v1.2.0) (2024-10-17)


### Features

* Expose Atlantis service via Cloudflared and improve documentation fc365af

## 1.2.0-alpha.0 (2024-10-17)


### Features

* Add Atlantis Helm chart 82c73aa
* Add CLI tool for Atlantis installation 115447e
* Add Makefile with commands for project setup and management 3381d81
* add Terraform files b69415e
* Update README and add cluster diagram 598c025
