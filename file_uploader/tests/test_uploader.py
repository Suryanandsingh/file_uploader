import pytest
from unittest.mock import patch, MagicMock
from file_uploader.uploader import FileUploader

@pytest.fixture
def uploader():
    return FileUploader(
        s3_bucket_name="test-s3-bucket",
        gcs_bucket_name="test-gcs-bucket",
        s3_file_types=['jpg', 'png', 'mp3'],
        gcs_file_types=['doc', 'pdf']
    )

@patch('file_uploader.uploader.boto3.client')
@patch('file_uploader.uploader.storage.Client')
def test_upload_to_s3(mock_gcs_client, mock_s3_client, uploader):
    mock_s3_client_instance = mock_s3_client.return_value
    uploader._upload_to_s3('/path/to/file.jpg', 'file.jpg')
    mock_s3_client_instance.upload_file.assert_called_once_with('/path/to/file.jpg', 'test-s3-bucket', 'file.jpg')

@patch('file_uploader.uploader.boto3.client')
@patch('file_uploader.uploader.storage.Client')
def test_upload_to_gcs(mock_gcs_client, mock_s3_client, uploader):
    mock_gcs_bucket = MagicMock()
    mock_gcs_blob = MagicMock()
    mock_gcs_client.return_value.bucket.return_value = mock_gcs_bucket
    mock_gcs_bucket.blob.return_value = mock_gcs_blob

    uploader._upload_to_gcs('/path/to/file.doc', 'file.doc')
    mock_gcs_blob.upload_from_filename.assert_called_once_with('/path/to/file.doc')
