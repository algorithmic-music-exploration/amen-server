#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions that the queue can call.
"""

import os
import json
from tempfile import NamedTemporaryFile
from amen.audio import Audio
from amen.utils import example_audio_file
from amen.echo_nest_converter import AudioAnalysis

def make_audio(filepath):
    """
    Helper function to generate the Echo Nest style AudioAnalysis object, for easier testing.

    Parameters
    ---------
    filepath : str
        Path to the local file to be analyzed.

    Returns
    ------
    AudioAnalysis
    """
    audio = Audio(filepath)
    return AudioAnalysis(filepath)

def do_work(args):
    """
    Main queue function that:
        - Analyzes the local audio file.
        - Uploads the audio file to the cloud server
        - Uploads the analysis file to the cloud server

    Parameters
    ---------
    args : List
        `args` is a wrapper for five arguments:
            - `filepath` is the path to the local audio file.
            - `audio_filename` is the name that the audio file will be uploaded as.
            - `analysis_filename` is the name that the analysis file will be uploaded as.
            - `upload` is a function that does the uploading to the given cloud server.
            - `analyze` is a function that analyzes the audio and returns the analysis.
    """
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
