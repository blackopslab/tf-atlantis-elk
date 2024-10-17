### tf-atlantis-elk

### Goals

* Automate single-node deployment of Atlassian, with on-board resource monitoring and log collection

#### Internals

* Storage: Atlantis recommends persistent volume for plan/deploy consistency -> local sc vs. rook/ceph

#### Current Status

* Added Makefile ✅
* Added Atlantis Helm Chart ✅
* Added CLI tool to manage installation ✅

TODO:
* Automating cloudflared/ngrok 🔧

For details, see [[CHANGELOG.md]]

#### Future Improvements

* See various inline `TODO` comments!

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

#### Versioning

This project uses [commit-and-tag-version](https://github.com/absolute-version/commit-and-tag-version) to generate an automated [[CHANGELOG.md]].
SSPlease use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) when pushing.

Commands:

* ```bash make alpha``` releases and tags sd alpha, used to test github actions
* ```bash make release```standard release and tag
