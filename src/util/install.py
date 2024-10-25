import os, subprocess, shlex
from typing import List, Tuple


# Run any command as a subprocess
def _run_command(command: str) -> str:
    try:
        cmd = shlex.split(command)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return output.decode("utf-8")

    except subprocess.CalledProcessError as called_process_error:
        raise RuntimeError(
            f"Command '{command}' failed with error: {called_process_error.output.decode('utf-8')}"
        )


def _change_working_directory(path: str) -> None:
    """
    Changes the current working directory to the specified path.
    TODO: deal with permission_error
    """

    try:
        os.chdir(path)
        print(f"Current working directory: {os.getcwd()}")

    except FileNotFoundError as file_not_found_error:
        print(f"Directory {path} not found.")
        raise file_not_found_error

    except NotADirectoryError as not_a_directory_error:
        print(f"{path} is not a directory.")
        raise not_a_directory_error

    except PermissionError as permission_error:
        raise RuntimeError(f"Permission denied to access {path}: {permission_error}")


def _create_directory(path: str) -> None:
    """
    Creates a directory at the specified path if it doesn't already exist.
    TODO: deal with permission_error
    """
    try:
        os.makedirs(path, exist_ok=True)

    except PermissionError as permission_error:
        raise RuntimeError(f"Failed to create required directories: {permission_error}")


def _download_binary(url: str, output_path: str) -> None:
    """
    Downloads a binary from the specified URL and saves it to the output path.
    """
    try:
        if os.path.exists(output_path):
            print(f"{output_path} already exists!")
            return
        else:
            _run_command(f"wget {url} -O {output_path}")

    except OSError as download_error:
        raise RuntimeError(
            f"Error downloading {url} to {output_path}: {download_error}"
        )


def _unzip_binary(zip_path: str, extract_to: str) -> None:
    """
    Unzips a zip file to the specified directory.
    """
    try:
        _run_command(f"unzip {zip_path} -d {extract_to}")

    except PermissionError:
        _set_permissions(extract_to, "755")

        try:
            _run_command(f"unzip {zip_path} -d {extract_to}")

        except OSError as e:
            raise RuntimeError(
                f"Failed to unzip {zip_path} again after setting permissions: {e}"
            )


def _untar_binary(tar_path: str, extract_to: str) -> None:
    """
    Untars a tar.gz file to the specified directory.
    """
    try:
        _run_command(f"tar -xvf {tar_path} -C {extract_to}")

    except PermissionError:
        _set_permissions(extract_to, "755")

        try:
            _run_command(f"tar -xvf {tar_path} -C {extract_to}")

        except OSError as e:
            raise RuntimeError(
                f"Failed to untar {tar_path} again after setting permissions: {e}"
            )


def _match_and_extract(name: str, temp_path: str, install_path: str) -> None:
    """
    Matches the file extension of the downloaded binary and extracts it to the specified directory.
    """
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

    except OSError as e:
        raise RuntimeError(f"Failed to extract {name} binary: {e}")


def _map_binaries() -> List[Tuple[str, str, str, str, str]]:
    """
    Returns a list of tuples containing the name, URL, temporary path, installation path, and permissions for each binary.
    """
    return [
        (
            "Cloudflared",
            "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64",
            "./bin/cloudflared",
            "./bin/cloudflared",
            "750",
        ),
    ]


def _install_binaries(binaries) -> None:
    """
    Iterates over a list of binaries, downloads them, extracts them, and sets permissions.
    """
    for name, url, temp_path, install_path, permissions in binaries:
        try:
            print(f"Downloading {name} binary...")
            _download_binary(url, temp_path)
            _match_and_extract(name, temp_path, install_path)
            _set_permissions(install_path, permissions)

        except RuntimeError as e:
            print(f"Error downloading {name} binary.")
            print(f"URL {url} does not respond!")
            raise e

        except Exception as e:
            print(f"Unexpected error installing {name} binary.")
            raise e


def _set_permissions(path: str, mode: str) -> None:
    """
    Sets the permissions of a file or directory to the specified mode.
    TODO: deal with no_sudo_error
    """
    try:
        _run_command(f"chmod {mode} {path}")

    except PermissionError as no_sudo_error:
        raise RuntimeError(
            f"Failed to set permissions for {path}: {no_sudo_error}. Do you have sudo permissions?"
        )


def _set_kube_config_path(conf_path: str) -> None:
    os.environ["KUBE_CONFIG_PATH"] = conf_path


def run_terraform_init() -> None:
    _run_command("terraform init")


def run_terraform_plan() -> None:
    _run_command("terraform plan -var-file='variables.tfvars'")


def run_terraform_apply() -> None:
    _run_command("terraform apply -auto-approve -var-file='variables.tfvars'")


def run_terraform_destroy() -> None:
    _run_command("terraform destroy -auto-approve -var-file='variables.tfvars'")


def _populate_environment() -> None:
    print("\n1. POPULATING ENVIRONMENT...")
    BINARIES = _map_binaries()
    try:
        print("Generating required directory tree...")
        _create_directory("./bin")
        _create_directory("./tmp")
        _install_binaries(BINARIES)

    except Exception as e:
        raise e


def install_atlantis() -> str:
    try:
        _populate_environment()

        print("\n2. INSTALLING...")

        _set_kube_config_path("~/.kube/config/")

        _change_working_directory("./deploy/atlantis/terraform/")

        run_terraform_init()
        run_terraform_plan()
        run_terraform_apply()

        _change_working_directory("../../../")

    except Exception as e:
        return f"Error during installation: {e}"

    return "Installation completed successfully."
