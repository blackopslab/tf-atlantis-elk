# tf-atlantis-elk

## Goals

* Automated single-node deployment of Atlantis, with on-board resource monitoring and log collection

### 📋 Current Status

* Added streamlined CLI Tool logging
* Added Prometheus manifests
* Configured custom Atlantis workflow
* Added RBAC management to CLI Tool
* Automated Atlantis deployment

For details, see [CHANGELOG.md](CHANGELOG.md)

### ⚒️ WIP

* Writing unit tests for CLI tool

### 🪲 Known Bugs

* [Issue 58: src/scripts/force_rollout.sh deletes ALL pvc resources from the cluster](https://github.com/blackopslab/tf-atlantis-elk/issues/58)

### 🧑‍🏭 Future Improvements

* Cloudflared quick url wrapper (crd?) and CLI Tool integration

See various inline `# TODO:` comments!

## 🫡 Requirements

* Any Kubernetes distro with a `kubectl` interface
    * Tested on `k3s` and `Docker Desktop (WSL2)`
* `terraform`
* A HashiCorp cloud account for remote Terraform state
* `helm`
* `python3`
* `pip3`
* `click`
* `jq`

## 🛠️ Building and Running

1. Please create `deploy/atlantis/terraform/variables.tfvars` from template
    ```bash
    cp deploy/atlantis/terraform/variables.tfvars.template deploy/atlantis/terraform/variables.tfvars
    ```
    and fill in all fields appropriately.

2. Deploy Atlantis

```bash
make all # -> runs clean, config, install
```

4. Exclude Atlantis from Terraform tracking
   ```bash
    cd deploy/atlantis/terraform
    src/scripts/untrack_atlantis_terraform.sh
   ```
   thus preventing it to manage its own resources, while still being able to deploy from a single repo.


### Expose

```bash
make expose
```
should return a *quick url* with public access to the Atlantis entry point, e.g.
```bash
+--------------------------------------------------------------------------------------------+
|  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
|  https://carolina-victorian-shows-bahamas.trycloudflare.com                                |
+--------------------------------------------------------------------------------------------+
```

⚠️ Please ensure that your firewall rules allow inbound traffic to local port `32141`! ⚠️

### Destroy / Apply

`make apply` and `make destroy` will automate the respective Terraform commands.

### Clean

`make clean` runs `make prune` on top of `make destroy`.
Warning: `make clean` will destroy all Terraform resources and reset your local repo and python environment.

### Rollout

Just run `make all` on top of the running cluster to wipe it and deploy all resources from scratch.

Info: During tests `make all` performed well most of the time, but namespace deletion tended to hang at the `Terminating` phase.
To quickly kill the process, you can run the following finalizer script:

    ```bash
    make force_rollout.sh
    src/scripts/finalize_namespace.sh
    ```
   Warning: all unmanaged namespace resources that are still running will become orphans. See the output of `src/scripts/finalize_namespace.sh`
   Please check that especially `pvs` and `pvcs` have been successfully terminated. Please force delete manually where needed.


## Versioning

This project uses [commit-and-tag-version](https://github.com/absolute-version/commit-and-tag-version) to generate an automated [CHANGELOG.md](CHANGELOG.md).
Please use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) when pushing.

Commands:

* ```bash
    make alpha # -> releases and tags as alpha, used to test github actions
    ```


* ```bash
    make beta # -> releases and tags as beta
    ```

* ```bash
    make minor # -> releases and tags as minor
    ```

* ```bash
    make release # -> standard release and tag
    ```
