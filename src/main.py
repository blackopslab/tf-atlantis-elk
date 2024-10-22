import sys, click
from util.install import t_install as env_install
from util.install import t_apply as env_apply
from util.install import t_destroy as env_destroy


@click.group()
def main():
    """Main entry point for the CLI tool."""
    click.echo("Welcome to the tf-atlantis-elk installation tool!")
    click.echo("Use 'python main.py <command> --help' for more information.")
    click.echo("")


@main.command()
@click.option("--verbose", "-v", is_flag=True, help="Prints installation output.")
def install(verbose):
    """Installs Atlantis from GitHub credentials provided by terraform/variables.tfvars.

    Example:
        python main.py install --verbose
    """
    match verbose:
        case True:
            click.echo("Verbose mode is enabled.")
            click.echo(env_install())

        case False:
            click.echo("Verbose mode is disabled.")
            env_install()


@main.command()
@click.option("--verbose", "-v", is_flag=True, help="Prints 'terraform apply' output.")
def apply(verbose):
    """Creates all Terraform resources in ./terraform/

    Example:
        python main.py apply --verbose
    """
    match verbose:
        case True:
            click.echo("Verbose mode is enabled.")
            click.echo(env_apply())

        case False:
            click.echo("Verbose mode is disabled.")
            env_apply()


@main.command()
@click.option(
    "--verbose", "-v", is_flag=True, help="Prints 'terraform destroy' output."
)
def destroy(verbose):
    """Destroys all Terraform resources in ./terraform/

    Example:
        python main.py destroy --verbose
    """
    match verbose:
        case True:
            click.echo("Verbose mode is enabled.")
            click.echo(env_destroy())

        case False:
            click.echo("Verbose mode is disabled.")
            env_destroy()


@main.command()
def version():
    """Shows the version of this CLI tool.

    Example:
        python main.py version
    """
    click.echo("tf-atlantis-cli version: 3.0.0")


if __name__ == "__main__":
    # show help if no args
    if len(sys.argv) == 1:
        click.echo("No command provided. Use one of the following:")
        click.echo("  version             Show the version of the CLI tool.")
        click.echo("\nFor more information, run 'python main.py <command> --help'.")
    else:
        main()
