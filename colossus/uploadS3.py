"""

Function for uploading file to AWS s3 bucket.
Required fields -> file_name, bucket, object_name

"""

import os
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return True
