terraform {
  cloud {
    organization = "vdistefano-studio"
    workspaces {
      name = "tf-atlantis-elk"
    }
  }
}
resource "kubernetes_namespace" "atlantis" {
  metadata {
    name = "atlantis"
  }
}

# resource "kubernetes_namespace" "monitoring" {
#   metadata {
#     name = "monitoring"
#   }
# }

resource "helm_release" "atlantis" {
  name       = "atlantis"
  repository = "https://runatlantis.github.io/helm-charts"
  chart      = "atlantis"
  namespace  = "atlantis"

  values = [file("${path.module}/../helm/values.yaml")]

  set {
    name  = "github.user"
    value = var.github_user
  }

  set {
    name  = "github.token"
    value = var.github_token
  }

  set {
    name  = "github.secret"
    value = var.github_secret
  }

  set {
    name  = "environmentRaw[0].value"
    value = var.hcp_token
  }
}

# resource "helm_release" "opensearch" {
#   name       = "opensearch"
#   repository = "https://charts.bitnami.com/bitnami"
#   chart      = "opensearch"
#   namespace  = "monitoring"

#   values = [file("${path.module}/../helm/opensearch/values.yaml")]
# }
