#!/bin/bash

### FINALIZES GIVEN KUBERNETES NAMESPACE WHEN STUCK IN TERMINATING STATE ###
finalize_namespace() {
    local namespace="$1"

    # Check if a namespace was provided
    if [ -z "$namespace" ]; then
        echo "Error: Please provide a namespace!"
        return 1
    fi

    # Start kubectl proxy in the background
    kubectl proxy &
    local proxy_pid=$!

    # Give the proxy some time to start
    sleep 2

    # Create a temporary JSON file with modified finalizers
    kubectl get namespace "$namespace" -o json | jq '.spec.finalizers = []' > temp.json

    # Send a PUT request to finalize the namespace
    curl -k -H "Content-Type: application/json" -X PUT --data-binary @temp.json \
        "127.0.0.1:8001/api/v1/namespaces/$namespace/finalize"

    # Clean up the temporary file
    rm -f temp.json

    # Kill the kubectl proxy process
    kill "$proxy_pid"
}

# Check for input and call the function
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <namespace>"
    exit 1
fi

finalize_namespace "$1"

unset -f finalize_namespace
