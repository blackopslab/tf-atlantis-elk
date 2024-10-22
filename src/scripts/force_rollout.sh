#!/bin/bash
helm uninstall opensearch -n monitoring &&
helm uninstall atlantis -n atlantis &&
kubectl delete pvc --all -n monitoring &
kubectl delete pvc --all -n atlantis &
kubectl get pv -A
echo ""
kubectl get pvc -A
echo ""
kubectl delete ns monitoring &
kubectl delete ns atlantis &
echo ""
kubectl get ns
