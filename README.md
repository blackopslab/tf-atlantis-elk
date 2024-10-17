# tf-atlantis-elk

## Goals

* Automated single-node deployment of Atlantis, with on-board resource monitoring and log collection

### 📋 Current Status
```bash
.
├── assets
│   └── cluster.drawio
├── bin
├── CHANGELOG.md
├── env
│   └── .env.template
├── .gitignore
├── helm
│   └── atlantis
│       └── values.yaml
├── LICENSE.md
├── Makefile
├── .pre-commit-config.yaml
├── README.md
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── util
│       └── install.py
├── terraform
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
└── tmp
```

* Cluster exposed to the internet 🎉
* Added cloudflare quick tunnel ✅
* Added Makefile & Atlantis Helm Chart ✅
* Added CLI tool to manage installation ✅

For details, see [[CHANGELOG.md]]

### 🧑‍🏭 Future Improvements

* `terraform destroy` -> not working correctly. Add graceful rollout with fix or workaround
* Expose cluster via https instead of http i.e. manage letsencrypt

See various inline `# TODO:` comments!

## 🛠️ Building and Running

1. Please create `atlantis/.env` from template
    ```bash
    cp env/.env.template env/.env
    ```
    and fill in all fields appropriately.

2. Generate execution environment:
    ```bash
    make config
    ```

3. Deploy Atlantis on the cluster, using Terraform and the credentials from `env/.env`:
    ```bash
    make install
    ```
or just run

```bash
make all # -> runs clean, config, install
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

### Clean

The above `make all` includes `make clean` which will reset your local repo and python environment. `make clean` can also be run manually.

### Rollout

`make clean` will prune the workspace, but will **not** rollback the Helm deployment. To rollout the Atlantis deployment, please run:

1. ```bash
    helm delete atlantis
    ```
2. ```bash
    kubectl delete --force ns atlantis
    ```
3. Namespace deletion tends to hang at the `Terminating` phase. To quickly kill the process, you can run the following finalizer script:
    ```bash
    src/scripts/finalize_namespace.sh
    ```
   Please check that all related resources, especially `pvs` and `pvcs` have been successfully terminated. Please force delete manually where needed.

4. Run `make clean` to delete execution environment and terraform states.

## Versioning

This project uses [commit-and-tag-version](https://github.com/absolute-version/commit-and-tag-version) to generate an automated [[CHANGELOG.md]].
SSPlease use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) when pushing.

Commands:

* ```bash
    make alpha # -> releases and tags as alpha, used to test github actions
    ```

* ```bash
    make release # -> standard release and tag
    ```
