import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("ivankmk/thousand-ml-jobs-in-usa")
print("Path to dataset files:", path)

os.rename(f"{path}/1000_ml_jobs_us.csv", f"{os.getcwd()}/1000_ml_jobs_us.csv") # moves the csv file into the project directory
