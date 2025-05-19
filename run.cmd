python insertion_into_bigquery.py ^
--job_name=dataflow-job-1 ^
--project=<project_id> ^
--region=northamerica-northeast1 ^
--runner=DataflowRunner ^
--staging_location=gs://dataflow-apache-python/test ^
--temp_location=gs://dataflow-apache-python/test ^
--input=gs://dataflow-apache-python/1000_ml_jobs_us.csv ^
--output=<project_id>:dataflow_job_dataset.1000_jobs
