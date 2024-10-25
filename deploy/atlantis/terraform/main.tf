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
  lifecycle {
    prevent_destroy = true
    ignore_changes  = all
  }
}


resource "helm_release" "atlantis" {
  name       = "atlantis"
  repository = "https://runatlantis.github.io/helm-charts"
  chart      = "atlantis"
  namespace  = "atlantis"

  values = [file("${path.module}/../helm/values.yaml")]

  lifecycle {
    prevent_destroy = true
    ignore_changes  = all
  }

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
