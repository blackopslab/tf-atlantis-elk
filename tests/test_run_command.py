import pytest
from src.util.install import _run_command


def test_run_command_success():
    print("Running test_run_command_success")  # Debug statement
    assert _run_command("echo 'success'").strip() == "success"


def test_run_command_failure():
    with pytest.raises(RuntimeError, match="Command 'bad_command' failed"):
        _run_command("bad_command")
