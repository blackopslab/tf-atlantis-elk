#!/bin/bash

# Variables
NAMESPACE="atlantis"
SERVICE_ACCOUNT="atlantis"

# Check if the namespace exists
if ! kubectl get namespace "$NAMESPACE" >/dev/null 2>&1; then
  echo "Namespace '$NAMESPACE' does not exist."
  exit 1
fi

# Check if the service account exists
if ! kubectl get serviceaccount "$SERVICE_ACCOUNT" -n "$NAMESPACE" >/dev/null 2>&1; then
  echo "Service account '$SERVICE_ACCOUNT' does not exist in namespace '$NAMESPACE'."
  exit 1
fi

# Check the role bindings for the service account
echo "Checking RoleBindings for service account '$SERVICE_ACCOUNT' in namespace '$NAMESPACE':"
ROLE_BINDINGS=$(kubectl get rolebindings -n "$NAMESPACE" -o json 2>/dev/null)
if [ $? -eq 0 ]; then
  ROLE_BINDING_NAMES=$(echo "$ROLE_BINDINGS" | jq -r --arg SA "$SERVICE_ACCOUNT" '.items[] | select(.subjects[].name == $SA) | .metadata.name')

  if [ -z "$ROLE_BINDING_NAMES" ]; then
    echo "No RoleBindings found for service account '$SERVICE_ACCOUNT'."
  else
    for ROLE in $ROLE_BINDING_NAMES; do
      echo "RoleBinding found: $ROLE"
      kubectl describe rolebinding "$ROLE" -n "$NAMESPACE"
    done
  fi
else
  echo "Failed to retrieve RoleBindings."
fi

# Check the cluster role bindings
echo "Checking ClusterRoleBindings for service account '$SERVICE_ACCOUNT':"
CLUSTER_ROLE_BINDINGS=$(kubectl get clusterrolebindings -o json 2>/dev/null)
if [ $? -eq 0 ]; then
  CLUSTER_ROLE_BINDING_NAMES=$(echo "$CLUSTER_ROLE_BINDINGS" | jq -r --arg SA "$SERVICE_ACCOUNT" '.items[] | select(.subjects[].name == $SA and .subjects[].namespace == "'$NAMESPACE'") | .metadata.name')

  if [ -z "$CLUSTER_ROLE_BINDING_NAMES" ]; then
    echo "No ClusterRoleBindings found for service account '$SERVICE_ACCOUNT'."
  else
    for ROLE in $CLUSTER_ROLE_BINDING_NAMES; do
      echo "ClusterRoleBinding found: $ROLE"
      kubectl describe clusterrolebinding "$ROLE"
    done
  fi
else
  echo "Failed to retrieve ClusterRoleBindings."
fi

echo "Check completed."
