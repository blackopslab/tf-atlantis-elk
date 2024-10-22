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


# TODO: dismiss
# def _load_env_file(envfile: str) -> None:
#     load_dotenv(envfile)


# def _unload_env_file(envfile: str) -> None:
#     env_vars = dotenv_values(envfile)
#     for key in env_vars.keys():
#         # KUBE_CONFIG_PATH is required by Atlantis/Terraform
#         if key != "KUBE_CONFIG_PATH":
#             os.environ.pop(key, None)


def _change_working_directory(path: str) -> None:
    os.chdir(path)


def _download_binary(url: str, output_path: str) -> None:
    if os.path.exists(output_path):
        print(f"{output_path} already exists!")
        return
    else:
        _run_command(f"wget {url} -O {output_path}")


#
# TODO: Error handling -> impossible to write e.g. directory drive permissions
#       Also see compliance logic TODO:189
def _unzip_binary(zip_path: str, extract_to: str) -> None:
    _run_command(f"unzip {zip_path} -d {extract_to}")


def _untar_binary(tar_path: str, extract_to: str) -> None:
    _run_command(f"tar -xvf {tar_path} -C {extract_to}")


def _match_and_extract(name: str, temp_path: str, install_path: str):

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


def _set_permissions(path: str, mode: str) -> None:
    _run_command(f"chmod {mode} {path}")


def _set_kube_config_path(conf_path: str) -> None:
    os.environ["KUBE_CONFIG_PATH"] = conf_path


# TODO: needs to be refactored to use .tfvars
# def _create_secret(secret_name: str, envfile: str) -> None:
#     _run_command(
#         f"kubectl create secret generic {secret_name} \
#             --from-env-file={envfile}"
#     )


# def _delete_secret(secret_name: str) -> None:
#     _run_command(f"kubectl delete secret {secret_name}")


def _run_terraform_init() -> None:
    _run_command("terraform init -var-file='variables.tfvars'")


def _run_terraform_plan() -> None:
    _run_command("terraform plan -var-file='variables.tfvars'")


def _run_terraform_apply() -> None:
    _run_command("terraform apply -auto-approve -var-file='variables.tfvars'")


def _run_terraform_destroy() -> None:
    _run_command("terraform destroy -auto-approve -var-file='variables.tfvars'")


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


def t_apply() -> str:

    # TODO: add error handling

    print("")
    print("Creating all Terraform resources...")

    _set_kube_config_path("~/.kube/config/")

    _change_working_directory("./terraform/")

    _run_terraform_apply()

    _change_working_directory("../")

    return "'terraform apply' completed successfully."


def t_destroy() -> str:

    # TODO: add error handling

    print("")
    print("Destroying all Terraform resources...")

    _set_kube_config_path("~/.kube/config/")

    _change_working_directory("./terraform/")

    _run_terraform_destroy()

    _change_working_directory("../")

    return "'terraform destroy' completed successfully."


def t_install() -> str:

    print("")
    print("1. POPULATING ENVIRONMENT...")

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
            # TODO: test nested exceptions when handling TODO:54
            _match_and_extract(name, temp_path, install_path)
            _set_permissions(install_path, permissions)

        except RuntimeError as e:
            print(f"Error downloading {name} binary: {e}")
            print(f"URL {url} does not respond!")

        except Exception as e:
            print(f"Unexpected error installing {name} binary: {e}")

    # TODO: compliance test

    try:
        print("")
        print("2. INSTALLING...")

        _set_kube_config_path("~/.kube/config/")

        _change_working_directory("./terraform/")

        _run_terraform_init()

        _run_terraform_plan()

        _run_terraform_apply()

        _change_working_directory("../")

    except Exception as e:
        return f"Error during installation: {e}"

    return "Installation completed successfully."
