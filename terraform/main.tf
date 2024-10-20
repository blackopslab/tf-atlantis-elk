provider "kubernetes" {
  config_path   = "~/.kube/config"
  config_context = ""
}

resource "kubernetes_namespace" "atlantis" {
  metadata {
    name = "atlantis"
  }
}

resource "kubernetes_namespace" "monitoring" {
  metadata {
    name = "monitoring"
  }
}

resource "helm_release" "atlantis" {
  name       = "atlantis"
  repository = "https://runatlantis.github.io/helm-charts"
  chart      = "atlantis"
  namespace  = "atlantis"

  values = [file("${path.module}/../helm/atlantis/values.yaml")]

resource "helm_release" "opensearch" {
  name       = "atlantis"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "opensearch:1.3.11"
  namespace  = "monitoring"

  values = [file("${path.module}/../helm/opensearch/values.yaml")]

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
}

# # Null resource to run cloudflared command
# resource "null_resource" "cloudflared_tunnel" {
#   provisioner "local-exec" {
#     command = "../bin/cloudflared tunnel --url http://localhost:34141"
#   }

#   triggers = {
#     always_run = "${timestamp()}"
#   }
#}
