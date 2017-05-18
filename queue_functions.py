#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Functions that the queue can call
'''

import os
import json
from amen.audio import Audio
from amen.utils import example_audio_file
from amen.echo_nest_converter import AudioAnalysis

def do_work(filepath):
    audio = Audio(filepath)
    remix_audio = AudioAnalysis(audio)
    analysis_filepath = '/Users/thor/Desktop/test.json'
    with open(analysis_filepath, 'w') as f:
        json.dump(remix_audio.to_json(), f)
    os.remove(filepath)

    return
