#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Functions that the queue can call
'''

import os
import json
from tempfile import NamedTemporaryFile
from amen.audio import Audio
from amen.utils import example_audio_file
from amen.echo_nest_converter import AudioAnalysis

from uploader import local_upload

def do_work(filepaths):
    filepath = filepaths[0]
    s3_filename = filepaths[1]
    audio = Audio(filepath)
    remix_audio = AudioAnalysis(audio)

    f = NamedTemporaryFile(delete=False, mode='w')
    analysis_filepath = f.name
    json.dump(remix_audio.to_json(), f)
    f.close()

    # post audio and analysis to S3
    local_upload(filepath)
    local_upload(analysis_filepath)
