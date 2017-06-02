#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Uploaders to various cloud services
'''

import os
import boto

from s3_config.py import bucket_name
from s3_secrets.py import secrets

def local_upload(filepath):
    print("Local file at: " + filepath)
    pass

def s3_upload(filepath):
    ## Unsure if this works, but it looks sane?  Where do we configure secrets?

    # This requires that we have the bucket before hand.  Would be nice to make it idempotent.
    # how do we set bucket policies?  Need to look at how infinite juke does it
    # maybe we need an "s3_configure" that runs when we boot the server,
    # or we ask users to run it beforehand, if they're S3 users?
    # s3_configure would create the bucket, & set policies including auto-deletion and security.
    # let's make an secrets.py = s3_secrets, gcp_secrets, etc

    s3_connection = boto.connect_s3()
    bucket = s3_connection.get_bucket(bucket_name())
    key = boto.s3.key.Key(bucket, filepath)
    with open(filepath) as f:
        key.send_file(f)
    os.remove(filepath)
