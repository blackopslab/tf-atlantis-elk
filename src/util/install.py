import os, subprocess, shlex
from typing import List, Tuple
from dotenv import load_dotenv, dotenv_values

# from util.check_permissions_and_files import check_permissions_and_files

### MAP COMMANDS ###

# Run any command as a subprocess
def _run_command(command: str) -> str:
    try:
        cmd = shlex.split(command)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Command '{command}' failed with error: {e.output.decode('utf-8')}"
        )


def _change_working_directory(path: str) -> None:
    os.chdir(path)


def _download_binary(url: str, output_path: str) -> None:
    _run_command(f"wget {url} -O {output_path}")


def _unzip_binary(zip_path: str, extract_to: str) -> None:
    _run_command(f"unzip {zip_path} -d {extract_to}")


def _untar_binary(tar_path: str, extract_to: str) -> None:
    _run_command(f"tar -xvf {tar_path} -C {extract_to}")


def _set_permissions(path: str, mode: str) -> None:
    _run_command(f"chmod {mode} {path}")


def _load_env_file(envfile: str) -> None:
    load_dotenv(envfile)


def _unload_env_file(envfile: str) -> None:
    env_vars = dotenv_values(envfile)
    for key in env_vars.keys():
        # KUBE_CONFIG_PATH is required by Atlantis/Terraform
        if key != "KUBE_CONFIG_PATH":
            os.environ.pop(key, None)


def _create_secret(secret_name: str, envfile: str) -> None:
    _run_command(
        f"kubectl create secret generic {secret_name} \
            --from-env-file={envfile}"
    )


def _delete_secret(secret_name: str) -> None:
    _run_command(f"kubectl delete secret {secret_name}")


def _run_terraform_init() -> None:
    _run_command(
        "terraform init \
                -var 'github_user='{os.environ['GITHUB_USER']}'' \
                -var 'github_token='{os.environ['GITHUB_TOKEN']}'' \
                -var 'github_secret='{os.environ['GITHUB_SECRET']}''"
    )


def _run_terraform_plan() -> None:
    _run_command(
        f"terraform plan \
                -var 'github_user={os.environ['GITHUB_USER']}' \
                -var 'github_token={os.environ['GITHUB_TOKEN']}' \
                -var 'github_secret={os.environ['GITHUB_SECRET']}'"
    )


def _run_terraform_apply() -> None:
    _run_command(
        f"terraform apply -auto-approve\
                -var 'github_user={os.environ['GITHUB_USER']}' \
                -var 'github_token={os.environ['GITHUB_TOKEN']}' \
                -var 'github_secret={os.environ['GITHUB_SECRET']}'"
    )


def _run_terraform_destroy() -> None:
    _run_command(
        f"terraform destroy -auto-approve\
                -var 'github_user={os.environ['GITHUB_USER']}' \
                -var 'github_token={os.environ['GITHUB_TOKEN']}' \
                -var 'github_secret={os.environ['GITHUB_SECRET']}'"
    )


### MAP DEPENDENCIES ###


def _map_binaries() -> List[Tuple[str, str, str, str, str]]:
    return [
        (
            "Cloudflared",
            "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64",
            "./bin/cloudflared",
            "./bin/cloudflared",
            "750",
        ),
    ]


def apply(envfile: str) -> str:

    print("")
    print("Creating all Terraform resources...")

    _load_env_file(envfile)

    _change_working_directory("./terraform/")

    _run_terraform_apply()

    _create_secret("atlantis-github-secrets", envfile)
    # TODO: isolate secret name in env/.env

    _change_working_directory("../")

    _unload_env_file(envfile)

    return "'terraform apply' completed successfully."


def destroy(envfile: str) -> str:

    print("")
    print("Destroying all Terraform resources...")

    _load_env_file(envfile)

    _change_working_directory("./terraform/")

    _run_terraform_destroy()

    _change_working_directory("../")

    _unload_env_file(envfile)

    return "'terraform destroy' completed successfully."


### INSTALLATION SCRIPT ###


def install(envfile: str) -> str:

    # PRE-TASKS

    print("")
    print("1. POPULATING ENVIRONMENT...")

    # TODO flag to skip download

    BINARIES = _map_binaries()

    # Ensure working directories have not been deleted
    print("Generating required directory tree...")
    try:
        os.makedirs("./bin", exist_ok=True)
        os.makedirs("./tmp", exist_ok=True)

    except OSError as e:
        print(f"Error creating required directories: {e}")
        return "Installation failed due to directory creation error."

    # Download, extract and install binaries
    for name, url, temp_path, install_path, permissions in BINARIES:
        try:
            print(f"Downloading {name} binary...")
            _download_binary(url, temp_path)
            _, file_extension = os.path.splitext(temp_path)

            match file_extension:
                case ".gz":
                    print(f"Extracting {name} binary from tar.gz...")
                    _untar_binary(temp_path, install_path)
                case ".zip":
                    print(f"Extracting {name} binary from zip...")
                    _unzip_binary(temp_path, install_path)
                case "":
                    print(f"No extension for {name}. Skipping extraction.")
                case _:
                    print(f"Unknown file type for {name}.")

            _set_permissions(install_path, permissions)

        except RuntimeError as e:
            print(f"Error downloading {name} binary: {e}")
            print(f"URL {url} does not respond!")

        except Exception as e:
            print(f"Unexpected error installing {name} binary: {e}")

    # TODO: fix compliance test
    # print("")
    # print("Running compliance tests...")
    # check_permissions_and_files("src/util/rules.json")

    try:
        print("")
        print("2. INSTALLING...")

        _load_env_file(envfile)

        _change_working_directory("./terraform/")

        _run_terraform_init()

        _run_terraform_plan()

        _run_terraform_apply()

        _unload_env_file(envfile)

        _change_working_directory("../")

        _create_secret("atlantis-github-secrets", envfile)
        # TODO: isolate secret name in env/.env

    except Exception as e:
        return f"Error during installation: {e}"

    return "Installation completed successfully."
