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

# We need this as a function so we can stub it out in tests
def make_audio(filepath):
    audio = Audio(filepath)
    return AudioAnalysis(filepath)

def do_work(args):
    filepath = args[0]
    audio_filename = args[1]
    analysis_filename = args[2]
    upload = args[3]
    analyze = args[4]

    remix_audio = analyze(filepath)
    f = NamedTemporaryFile(delete=False, mode='w')
    analysis_filepath = f.name
    json.dump(remix_audio.to_json(), f)
    f.close()

    upload(filepath, audio_filename)
    upload(analysis_filepath, analysis_filename)
