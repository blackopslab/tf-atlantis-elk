import sys, click
from util.install import install_atlantis
from util.install import run_terraform_apply
from util.install import run_terraform_destroy


@click.group()
def main():
    """Main entry point for the CLI tool."""
    click.echo("Welcome to the tf-atlantis-elk installation tool!")
    click.echo("Use 'python main.py <command> --help' for more information.")
    click.echo("")


@main.command()
def install(verbose):
    """Installs Atlantis from GitHub credentials provided by terraform/variables.tfvars.

    Example:
        python main.py install
    """
    click.echo(install_atlantis())


@main.command()
def apply(verbose):
    """Creates all Terraform resources in ./terraform/

    Example:
        python main.py apply
    """
    click.echo(run_terraform_apply())


@main.command()
def destroy(verbose):
    """Destroys all Terraform resources in ./terraform/

    Example:
        python main.py destroy
    """
    click.echo(run_terraform_destroy())


@main.command()
def version():
    """Shows the version of this CLI tool.

    Example:
        python main.py version
    """
    click.echo("tf-atlantis-cli version: 4.0.0")


if __name__ == "__main__":
    # show help if no args
    if len(sys.argv) == 1:
        click.echo("No command provided. Use one of the following:")
        click.echo("  install             Full installation script.")
        click.echo("  apply               Apply Terraform manifests.")
        click.echo("  destroy             Destroy Terraform manifests.")
        click.echo("  version             Show the version of the CLI tool.")
        click.echo("\nFor more information, run 'python main.py <command> --help'.")
    else:
        main()
