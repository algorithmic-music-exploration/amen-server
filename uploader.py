
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Uploaders to various cloud services
'''

import os

def local_upload(filepath):
    print("Local file at: " + filepath)
    pass

def s3_upload(filepath, destination):
    pass
    os.remove(filepath)
