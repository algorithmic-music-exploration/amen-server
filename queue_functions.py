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

from uploader import s3_upload as upload

def do_work(filepaths):
    filepath = filepaths[0]
    s3_filename = filepaths[1]
    audio = Audio(filepath)
    remix_audio = AudioAnalysis(audio)

    f = NamedTemporaryFile(delete=False, mode='w')
    analysis_filepath = f.name
    analysis_s3_filename = s3_filename + '.analysis.json'
    json.dump(remix_audio.to_json(), f)
    f.close()

    upload(filepath, s3_filename)
    upload(analysis_filepath, analysis_s3_filename)
