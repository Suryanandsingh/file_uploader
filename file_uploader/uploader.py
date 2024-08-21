import os
import boto3
from google.cloud import storage
from pathlib import Path

class FileUploader:
    def __init__(self, s3_bucket_name, gcs_bucket_name, s3_file_types, gcs_file_types):
        self.s3_client = boto3.client('s3')
        self.gcs_client = storage.Client()
        self.s3_bucket_name = s3_bucket_name
        self.gcs_bucket_name = gcs_bucket_name
        self.s3_file_types = s3_file_types
        self.gcs_file_types = gcs_file_types

    def upload_files(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = file.split('.')[-1].lower()
                if file_extension in self.s3_file_types:
                    self._upload_to_s3(file_path, file)
                elif file_extension in self.gcs_file_types:
                    self._upload_to_gcs(file_path, file)

    def _upload_to_s3(self, file_path, file_name):
        print(f"Uploading {file_name} to S3 bucket {self.s3_bucket_name}...")
        self.s3_client.upload_file(file_path, self.s3_bucket_name, file_name)
        print(f"Uploaded {file_name} to S3.")

    def _upload_to_gcs(self, file_path, file_name):
        print(f"Uploading {file_name} to Google Cloud Storage bucket {self.gcs_bucket_name}...")
        bucket = self.gcs_client.bucket(self.gcs_bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_name} to Google Cloud Storage.")
