resource "google_storage_bucket" "dataflow_bucket" {
  location = "US"
  name     = "dataflow-apache-python"
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
  force_destroy = true
}

resource "google_storage_bucket_object" "csv_obj" {
  bucket = google_storage_bucket.dataflow_bucket.id
  name   = "1000_ml_jobs_us.csv"
  source = "../1000_ml_jobs_us.csv"
}

resource "google_bigquery_dataset" "test_dataset" {
  dataset_id = "dataflow_job_dataset"
  location = "northamerica-northeast1"
  description = "This dataset's tables will be used for data insertion by dataflow jobs."

  access {
    role           = "OWNER"
    user_by_email  = var.service_account
  }
  access {
    role = "OWNER"
    user_by_email = var.owner_email
  }
  access {
    role = "READER"
    domain = "hashicorp.com"
  }
}

resource "google_bigquery_table" "jobs_table" {
  dataset_id = google_bigquery_dataset.test_dataset.dataset_id
  table_id   = "1000_jobs"
}
