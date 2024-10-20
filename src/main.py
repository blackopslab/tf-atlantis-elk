import sys, click
from util.install import install as env_install


@click.group()
def main():
    """Main entry point for the CLI tool."""
    click.echo("Welcome to the tf-atlantis-elk installation tool!")
    click.echo("Use 'python main.py <command> --help' for more information.")
    click.echo("")


@main.command()
@click.argument("envfile")
@click.option("--verbose", "-v", is_flag=True, help="Prints installation output.")
def install(envfile, verbose):
    """Installs Atlantis from GitHub credentials provided by envfile.

    envfile: Path to the .env file (e.g., env/.env)

    Required file content:

    GITHUB_USER=""
    GITHUB_TOKEN=""
    GITHUB_SECRET=""

    Example:
        python main.py install .env --verbose
    """
    match verbose:
        case True:
            click.echo("Verbose mode is enabled.")
            click.echo(f"Using .env file: {envfile}")
            click.echo(env_install(envfile))

        case False:
            click.echo("Verbose mode is disabled.")
            env_install(envfile)


@main.command()
@click.argument("envfile")
@click.option("--verbose", "-v", is_flag=True, help="Prints 'terraform apply' output.")
def apply(envfile, verbose):
    """Applies all Terraform manifests in ./terraform/

    envfile: Path to the .env file (e.g., env/.env)

    Required file content:

    GITHUB_USER=""
    GITHUB_TOKEN=""
    GITHUB_SECRET=""

    Example:
        python main.py apply .env --verbose
    """
    match verbose:
        case True:
            click.echo("Verbose mode is enabled.")
            click.echo(f"Using .env file: {envfile}")
            click.echo(env_install(envfile))

        case False:
            click.echo("Verbose mode is disabled.")
            env_install(envfile)


@main.command()
def version():
    """Shows the version of this CLI tool.

    Example:
        python main.py version
    """
    click.echo("tf-atlantis-cli version: 2.0.1")


if __name__ == "__main__":
    # show help if no args
    if len(sys.argv) == 1:
        click.echo("No command provided. Use one of the following:")
        click.echo(
            "  install <envfile>   Install packages from the specified requirements file."
        )
        click.echo("  version             Show the version of the CLI tool.")
        click.echo("\nFor more information, run 'python main.py <command> --help'.")
    else:
        main()
