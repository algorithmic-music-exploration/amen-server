import os
from mock import Mock
from mock import patch

import boto3

from uploaders.s3 import bucket_name
from uploaders.s3 import get_url
from uploaders.s3 import upload

def test_get_url():
    filename = "faux-filename"
    assert get_url(filename) == "https://s3-us-west-2-amazonaws.com/amen-data/{}".format(filename)

def test_upload():
    c = Mock()
    def make_fake_client(service, aws_access_key_id='test', aws_secret_access_key='test'):
        return c

    filename = "faux-filename"
    filepath = "faux/path/to/{}".format(filename)
    bucket = bucket_name()
    boto3.client = make_fake_client
    upload(filepath, filename)
    c.upload_file.assert_called_once_with(filepath, bucket, filename)
