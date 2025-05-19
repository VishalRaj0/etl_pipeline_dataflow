variable "service_account" {
  type = string
  description = "GCP service account."
  sensitive = true
}

variable "owner_email" {
  type = string
  description = "GCP account owner email."
  sensitive = true
}

variable "sa_credentials_file_path" {
  type = string
  description = "File path of service account credentials."
  sensitive = true
}

variable "project_id" {
  type = string
  description = "Project ID for dataflow job to be deployed in."
}

