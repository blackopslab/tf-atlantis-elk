import os, sys, stat, glob, json


def _open_json_file(path: str) -> dict:
    """Opens and loads a JSON file."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[FAIL] JSON file not found: {path}")
        sys.exit(127)
    except json.JSONDecodeError as e:
        print(f"[FAIL] Error decoding JSON from file: {path}. Error: {e}")
        sys.exit(128)


def check_permissions_and_files(rules_file):
    """Checks file permissions and presence based on rules defined in a JSON file."""

    failed = False

    try:
        rules = _open_json_file(rules_file)
        print(f"[PASS] {rules_file} found and loaded")

    except SystemExit as e:
        print(f"[FAIL] {rules_file} cannot be loaded")
        failed = True
        sys.cod

    for rule in rules:

        path_regex = rule["path_regex"]
        required_permissions = rule["file_permissions"]

        if path_regex is None or required_permissions is None:
            print(f"[FAIL] Missing path_regex or file_permissions in rule.")
            failed = True
            continue  # skip to next rule

        seen_files = glob.glob(path_regex)

    for filepath in seen_files:
        try:
            if not os.path.exists(filepath):
                print(f"[FAIL] File not found: {filepath}")
                failed = True
                continue  # skip to next file

            file_permissions = stat.S_IMODE(os.stat(filepath).st_mode)

            if file_permissions != required_permissions:
                print(f"[FAIL] Incorrect file permissions: {filepath}")
                failed = True

        except Exception as e:
            print(f"[FAIL] An error occurred while checking {filepath}: {e}")
            failed = True

    return failed
