#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Functions that the queue can call
'''

import os
import shutil

def do_work(filepath):
    print("This is the filename in the queue")
    shutil.move(filepath, '/Users/thor/Desktop')
    return
