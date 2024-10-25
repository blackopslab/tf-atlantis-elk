terraform {
  cloud {
    organization = "vdistefano-studio"
    workspaces {
      name = "tf-atlantis-elk"
    }
  }
}
resource "kubernetes_namespace" "monitoring" {
  metadata {
    name = "monitoring"
  }
}

resource "helm_release" "opensearch" {
  name       = "opensearch"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "opensearch"
  namespace  = "monitoring"

  values = [file("${path.module}/../helm/values.yaml")]
}
