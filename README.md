# File Uploader

## Overview

This is a Python module to upload images and media files to AWS S3 and documents to Google Cloud Storage. 

## Installation

You can install the module using pip:

```bash
pip install .


## Usage

```
from file_uploader.uploader import FileUploader
from file_uploader.config import DEFAULT_S3_FILE_TYPES, DEFAULT_GCS_FILE_TYPES

uploader = FileUploader(
    s3_bucket_name='your-s3-bucket-name',
    gcs_bucket_name='your-gcs-bucket-name',
    s3_file_types=DEFAULT_S3_FILE_TYPES,
    gcs_file_types=DEFAULT_GCS_FILE_TYPES
)

uploader.upload_files('/path/to/your/directory')
```


### Running the Project

- Install the module: `pip install .`
- Run the module: Create an instance of `FileUploader` with the required configurations and call `upload_files()` with the directory path.
- Run tests: Use `pytest` to run the tests and ensure 85% code coverage.
