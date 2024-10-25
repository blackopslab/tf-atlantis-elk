import os, subprocess, shlex
from typing import List, Tuple


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
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory {path} not found.")
        raise
    except NotADirectoryError:
        print(f"{path} is not a directory.")
        raise
    except PermissionError:
        print(f"Permission denied to access {path}.")
        raise


def _download_binary(url: str, output_path: str) -> None:
    try:
        if os.path.exists(output_path):
            print(f"{output_path} already exists!")
            return
        else:
            _run_command(f"wget {url} -O {output_path}")
    except OSError:
        print(f"Error downloading {url} to {output_path}")
        raise


def _unzip_binary(zip_path: str, extract_to: str) -> None:
    try:
        _run_command(f"unzip {zip_path} -d {extract_to}")
    except OSError:
        _set_permissions(extract_to, "755")
        try:
            _run_command(f"unzip {zip_path} -d {extract_to}")
        except OSError as e:
            print(f"Failed to unzip {zip_path} again after setting permissions.")
            raise e


def _untar_binary(tar_path: str, extract_to: str) -> None:
    try:
        _run_command(f"tar -xvf {tar_path} -C {extract_to}")
    except OSError:
        _set_permissions(extract_to, "755")
        try:
            _run_command(f"tar -xvf {tar_path} -C {extract_to}")
        except OSError as e:
            print(f"Failed to untar {tar_path} again after setting permissions.")
            raise e  # Re-raise the exception to propagate the error


def _match_and_extract(name: str, temp_path: str, install_path: str):
    try:
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
    except OSError:
        print(f"Error extracting {name} binary.")
        raise


def _install_binaries(binaries):
    for name, url, temp_path, install_path, permissions in binaries:
        try:
            print(f"Downloading {name} binary...")
            _download_binary(url, temp_path)
            _match_and_extract(name, temp_path, install_path)
            _set_permissions(install_path, permissions)

        except RuntimeError as e:
            print(f"Error downloading {name} binary: {e}")
            print(f"URL {url} does not respond!")

        except Exception as e:
            print(f"Unexpected error installing {name} binary: {e}")


def _set_permissions(path: str, mode: str) -> None:
    _run_command(f"chmod {mode} {path}")


def _set_kube_config_path(conf_path: str) -> None:
    os.environ["KUBE_CONFIG_PATH"] = conf_path


def _run_terraform_init() -> None:
    _run_command("terraform init")


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


def _terraform_operation(operation: str) -> str:
    try:
        print(f"\n{operation.capitalize()} all Terraform resources...")
        _set_kube_config_path("~/.kube/config/")
        _change_working_directory("./terraform/")

        if operation == "apply":
            _run_terraform_apply()
        elif operation == "destroy":
            _run_terraform_destroy()

        _change_working_directory("../")
        return f"'terraform {operation}' completed successfully."

    except Exception as e:
        return f"Error during 'terraform {operation}': {e}"


def t_apply() -> str:
    return _terraform_operation("apply")


def t_destroy() -> str:
    return _terraform_operation("destroy")


def t_install() -> str:
    print("\n1. POPULATING ENVIRONMENT...")

    BINARIES = _map_binaries()

    try:
        print("Generating required directory tree...")
        os.makedirs("./bin", exist_ok=True)
        os.makedirs("./tmp", exist_ok=True)

    except OSError as e:
        print(f"Error creating required directories: {e}")
        return "Installation failed due to directory creation error."

    _install_binaries(BINARIES)

    try:
        print("\n2. INSTALLING...")
        _set_kube_config_path("~/.kube/config/")
        _change_working_directory("./terraform/")
        _run_terraform_init()
        _run_terraform_plan()
        _run_terraform_apply()
        _change_working_directory("../")

    except Exception as e:
        return f"Error during installation: {e}"

    return "Installation completed successfully."
