# Changelog

All notable changes to this project will be documented in this file. See [commit-and-tag-version](https://github.com/absolute-version/commit-and-tag-version) for commit guidelines.

## [3.3.2](///compare/v3.3.1...v3.3.2) (2024-10-29)


### Features

* Add pytest configuration and requirements c2d8f57
* **docs:** update Work in Progress and Future Improvements sections 42cf39b
* **scripts:** update force_rollout.sh to uninstall Prometheus 370808f
* **tests:** tests/test_run_command.py 069feea

## [3.3.1](///compare/v3.3.1-alpha.0...v3.3.1) (2024-10-27)

## [3.3.1-alpha.0](///compare/v3.3.0...v3.3.1-alpha.0) (2024-10-27)

## [3.4.0](///compare/v3.3.0...v3.4.0) (2024-10-27)


### Features

* **opensearch.yaml:** enable OpenSearch Dashboards deployment bc40d63

## [3.3.0](///compare/v3.2.0...v3.3.0) (2024-10-27)


### Features

* install monitoring tools 21191df
* **terraform:** add cloud configuration to main.tf 5f10f50
* update atlantisUrl in helm values 93caf53
* update project name and prometheus chart in terraform config b5f84f3

## [3.2.0](///compare/v3.1.0...v3.2.0) (2024-10-25)


### Bug Fixes

* correct function call in install.py 2da5f0d

## [3.1.0](///compare/v3.1.0-beta.0...v3.1.0) (2024-10-25)


### Features

* Remove file permission and presence check utility 1dce123

## [3.1.0-beta.0](///compare/v3.1.0-alpha.0...v3.1.0-beta.0) (2024-10-25)

### Features

* refactor: Update Terraform commands and refactor Python scripts
*

## [3.1.0-alpha.0](///compare/v3.0.0...v3.1.0-alpha.0) (2024-10-25)


### Features

* **monitoring:** add values.yaml for prometheus helm chart d010d83
* Refactor opensearch to elk 724364a

## [3.0.0-alpha.2](///compare/v3.0.0-alpha.1...v3.0.0-alpha.2) (2024-10-25)


### Features

* Add untrack_atlantis_terraform.sh script a618e4e

## [3.0.0-alpha.1](///compare/v3.0.0-alpha.0...v3.0.0-alpha.1) (2024-10-25)


### Features

* **atlantis.yaml:** change opensearch directory path fa3bb91
* Update lifecycle rules in Atlantis Terraform configuration a098f47

## [3.0.0-alpha.0](///compare/v2.0.0-beta.8...v3.0.0-alpha.0) (2024-10-25)


### ⚠ BREAKING CHANGES

* relocate Atlantis and OpenSearch Helm and Terraform files

* relocate Atlantis and OpenSearch Helm and Terraform files f658253


### Features

* **opensearch:** add terraform configuration for opensearch deployment c1ef044
* Refactor terraform and cleanup scripts 0ccc01b

## [2.0.0-beta.8](///compare/v2.0.0-beta.7...v2.0.0-beta.8) (2024-10-25)


### Features

* **atlantis.yaml:** hide output in workflows 99bf575

## [2.0.0-beta.7](///compare/v2.0.0-beta.6...v2.0.0-beta.7) (2024-10-24)


### ⚠ BREAKING CHANGES

* Update Atlantis RBAC and add sensitive outputs in Terraform

### Features

* Update Atlantis RBAC and add sensitive outputs in Terraform 4649a0d

## [2.0.0-beta.6](///compare/v2.0.0-beta.5...v2.0.0-beta.6) (2024-10-24)


### ⚠ BREAKING CHANGES

* **terraform:** add sensitive attribute to variables

### Features

* **terraform:** add sensitive attribute to variables 188ecb6

## [2.0.0-beta.5](///compare/v2.0.0-beta.4...v2.0.0-beta.5) (2024-10-23)


### Features

* Add Atlantis RBAC and permission check script a472709

## [2.0.0-beta.4](///compare/v2.0.0-beta.3...v2.0.0-beta.4) (2024-10-23)


### Features

* **atlantis.yaml:** add hcp_token to extra_args in init, plan and apply steps dc87eef

## [2.0.0-beta.3](///compare/v2.0.0-beta.2...v2.0.0-beta.3) (2024-10-23)


### Bug Fixes

* **atlantis.yaml:** remove lock=false 2f972af

## [2.0.0-beta.2](///compare/v2.0.0-beta.1...v2.0.0-beta.2) (2024-10-23)


### Bug Fixes

* **atlantis.yaml:** remove wrong keys 1762909

## [2.0.0-beta.1](///compare/v2.0.0-beta.0...v2.0.0-beta.1) (2024-10-23)


### Features

* add Terraform Cloud login and disable lock in Terraform commands cafaf48
* **terraform:** add cloud configuration and HCP_TOKEN to helm_release 10ead01


### Bug Fixes

* add missing variables.tfvars.template 3a18236

## [2.0.0-beta.0](///compare/v2.0.0-alpha.18...v2.0.0-beta.0) (2024-10-23)


### ⚠ BREAKING CHANGES

* **Atlantis:** update orgAllowlist in values.yaml

### Features

* **Makefile:** add beta release and update minor and release commands da0c5bb


### Bug Fixes

* **Atlantis:** update orgAllowlist in values.yaml 4927b3c

## [2.0.0-alpha.18](///compare/v2.0.0-alpha.17...v2.0.0-alpha.18) (2024-10-23)


### Bug Fixes

* restore new project configuration 404ebcd

## [2.0.0-alpha.17](///compare/v2.0.0-alpha.16...v2.0.0-alpha.17) (2024-10-23)


### Bug Fixes

* Update atlantis and terraform configurations e332b33

## [2.0.0-alpha.16](///compare/v2.0.0-alpha.12...v2.0.0-alpha.16) (2024-10-23)


### Features

* **atlantis.yaml:** change workspace from default to custom 55d9476
* **atlantis.yaml:** update workflow and workspace configuration 28f7181

## [2.0.0-alpha.13](///compare/v2.0.0-alpha.12...v2.0.0-alpha.13) (2024-10-23)

## [2.0.0-alpha.12](///compare/v2.0.0-alpha.11...v2.0.0-alpha.12) (2024-10-23)


### Bug Fixes

* refactor atlantis.yaml 1b8c012

## [2.0.0-alpha.11](///compare/v2.0.0-alpha.10...v2.0.0-alpha.11) (2024-10-23)


### Bug Fixes

* fix atlantis workflow 40db816

## [2.0.0-alpha.10](///compare/v2.0.0-alpha.9...v2.0.0-alpha.10) (2024-10-23)


### Bug Fixes

* fix atlantis workflow 3289486

## [2.0.0-alpha.9](///compare/v2.0.0-alpha.8...v2.0.0-alpha.9) (2024-10-23)


### Features

* **atlantis.yaml:** update project configuration and workflow 9c9ade6

## [2.0.0-alpha.8](///compare/v2.0.0-alpha.7...v2.0.0-alpha.8) (2024-10-23)


### Features

* **atlantis.yaml:** update configuration settings and workflow steps 720b5dd

## [2.0.0-alpha.7](///compare/v2.0.0-alpha.6...v2.0.0-alpha.7) (2024-10-22)


### Features

* improve error handling and code organization in install.py 1729e7b


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
