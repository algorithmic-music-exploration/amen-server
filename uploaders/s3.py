#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
S3 uploader
'''

import os
import boto3

BUCKET_NAME = 'amen-data'
BUCKET_REGION = 'us-west-2'

def bucket_name():
    return BUCKET_NAME

def bucket_region():
    return BUCKET_REGION

def get_url(filename):
    """"
    Generate the cloud URL for a given filename

    Parameters
    ----------
    filename : str

    Returns
    ------
    str
    """
    return 'https://s3-{}-amazonaws.com/{}/{}'.format(BUCKET_REGION, BUCKET_NAME, filename)

def upload(filepath, filename):
    """
    Upload a file to the configured bucket, with the given filename, and then remove the local file.

    Parameters
    ---------
    filepath : str
        The local filepath of the file.

    filename: str
        The name of the file on the server.
    """
    # This terrible import workaround is for travis testing.
    # A long-term fix might be to make a test uploader that has no secrets?
    from .s3_secrets import secrets
    aws_secrets = secrets()
    client = boto3.client(
        's3',
        aws_access_key_id=aws_secrets['aws_access_key_id'],
        aws_secret_access_key=aws_secrets['aws_secret_access_key'],
    )

    client.upload_file(filepath, bucket_name(), filename)
    os.remove(filepath)
