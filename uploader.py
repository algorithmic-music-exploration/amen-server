#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Uploaders to various cloud services
'''

import os
import boto3

from uploaders.s3_config import bucket_name
from uploaders.s3_secrets import secrets

def local_upload(filepath, filename):
    print("Local file at: " + filepath)
    pass

def s3_upload(filepath, filename):
    # We could maybe do idempotent stuff here, in terms of the bucket existing?
    # should we cache the creation of the client?
    # is this secrets management OK?

    aws_secrets = secrets()
    client = boto3.client(
        's3',
        aws_access_key_id=aws_secrets['aws_access_key_id'],
        aws_secret_access_key=aws_secrets['aws_secret_access_key'],
    )

    client.upload_file(filepath, bucket_name(), filename)
    os.remove(filepath)
