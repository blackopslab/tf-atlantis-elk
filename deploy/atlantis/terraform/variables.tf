variable "github_user" {
  description = "GitHub username for Atlantis"
  type        = string
  sensitive   = true
}

variable "github_token" {
  description = "GitHub token for Atlantis"
  type        = string
  sensitive   = true
}

variable "github_secret" {
  description = "Webhook secret for GitHub"
  type        = string
  sensitive   = true
}

variable "hcp_token" {
  description = "Terraform Cloud token"
  type        = string
  sensitive   = true
}
