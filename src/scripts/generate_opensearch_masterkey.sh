#!/bin/bash

SECRET_NAME="os-masterkey"
NAMESPACE="monitoring"
COMMON_NAME="localhost"
DAYS_VALID=365

# Generate a private key
openssl genrsa -out tls.key 2048
openssl req -new -x509 -key tls.key -out tls.crt -days $DAYS_VALID -subj "/CN=$COMMON_NAME"
kubectl create secret tls $SECRET_NAME --cert=tls.crt --key=tls.key -n $NAMESPACE
rm tls.key tls.crt
