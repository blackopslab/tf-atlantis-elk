### tf-atlantis-elk

### Goals

* Automate single-node deployment of Atlassian, with on-board resource monitoring and log collection

#### Internals / Edge cases

* Storage: persistent volumes?

#### Current Status
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

* Added Makefile ✅
* Added Atlantis Helm Chart ✅
* Added CLI tool to manage installation ✅

TODO:
* Expose cluster
* Automate cloudflared/ngrok 🔧
* Remove `helm` binary download -> Terraform Helm Provider 🔧

For details, see [[CHANGELOG.md]]

#### Future Improvements

* Add `terraform destroy` to CLI tool

See various inline `# TODO:` comments!

#### Building and Running

1. Create `atlantis/.env` from template
    ```bash
    cp env/.env.template env/.env
    ```
    and fill in secrets

2. Generate execution environment:
    ```bash
    make config
    ```
3. Deploy Atlantis on the cluster, using Terraform and the provided credentials:
    ```bash
    make install
    ```

#### Rollout

Run `make clean` to delete execution environment and terraform states. Does not yet run `terraform destroy`.

#### Versioning

This project uses [commit-and-tag-version](https://github.com/absolute-version/commit-and-tag-version) to generate an automated [[CHANGELOG.md]].
SSPlease use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) when pushing.

Commands:

* ```bash make alpha``` releases and tags sd alpha, used to test github actions
* ```bash make release```standard release and tag
