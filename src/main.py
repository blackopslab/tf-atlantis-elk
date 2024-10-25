import sys, click
from util.install import install_atlantis
from util.install import run_terraform_apply, run_terraform_destroy, run_terraform_init


@click.group()
def main():
    """Main entry point for the CLI tool."""
    click.echo("Welcome to the tf-atlantis-elk installation tool!")
    click.echo("Use 'python main.py <command> --help' for more information.")
    click.echo("")


@main.command()
def install():
    """Installs Atlantis from GitHub credentials provided by ./deploy/atlantis/terraform/variables.tfvars.

    Example:
        python main.py install
    """
    click.echo(install_atlantis())


@main.command()
def init():
    """Initlializas all Terraform resources in ./deploy/atlantis/terraform/

    Example:
        python main.py init
    """
    click.echo(run_terraform_init())


@main.command()
def apply():
    """Creates all Terraform resources in ./deploy/atlantis/terraform/

    Example:
        python main.py apply
    """
    click.echo(run_terraform_apply())


@main.command()
def destroy():
    """Destroys all Terraform resources in ./deploy/atlantis/terraform/

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
