variable "github_user" {
  description = "GitHub username for Atlantis"
  type        = string
#  default     = "${lookup(var.env_vars, "GITHUB_USER", "")}"
}

variable "github_token" {
  description = "GitHub token for Atlantis"
  type        = string
#  default     = "${lookup(var.env_vars, "GITHUB_TOKEN", "")}"
}

variable "github_secret" {
  description = "Webhook secret for GitHub"
  type        = string
#  default     = "${lookup(var.env_vars, "GITHUB_SECRET", "")}"
}
