# tf-atlantis-elk

## Goals

* Automated single-node deployment of Atlantis, with on-board resource monitoring and log collection

### 📋 Current Status

* Added RBAC management to CLI Tool
* Working Atlantis Deployments
* Atlantis up /w remote state
* Cluster exposed to the internet
* Added cloudflare quick tunnel
* Added Makefile & Atlantis Helm Chart
* Added CLI tool to manage installation

For details, see [CHANGELOG.md](CHANGELOG.md)

### ⚒️ WIP

### 🪲 Known Bugs


### 🧑‍🏭 Future Improvements

* Add CLI tool logging instead of print statements
* Add CLI tool tests
* Cloudflared
    * Automate execution and remind user to copy-paste to github webhook
    * Wrap into a crd

See various inline `# TODO:` comments!

## 🫡 Requirements

* Any Kubernetes distro with a `kubectl` interface (e.g. k3s, minikube, Docker Desktop on WSL2 etc.)
* `terraform`
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
Note: `make all` consists of `make clean | config | install`. See Makefile.


4. Exclude Atlantis from Terraform tracking
   ```bash
    cd deploy/atlantis/terraform
    src/scripts/untrack_atlantis_terraform.sh
   ```

5. Add RBAC roles for Atlantis
   ```
   kubectl apply -f
   ```


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
