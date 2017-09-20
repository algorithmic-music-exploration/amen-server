import os
from mock import Mock
from mock import ANY

from amen.audio import Audio
from queue_functions import do_work
from queue_functions import make_audio
from server import handle_post
from uploaders.s3 import get_url

class MockAnalysis():
    def to_json(self):
        return True


def faux_analysis(filepath):
    return MockAnalysis()

def test_do_work():
    faux_data = MockAnalysis()
    faux_upload = Mock()
    faux_analyze = Mock(return_value=faux_data)

    filepath = "faux/filepath.wav"
    audio_filename = "filepath.wav"
    analysis_filename = "filepath.analysis.json"

    do_work([filepath, "filepath.wav", "filepath.analysis.json", faux_upload, faux_analyze])

    faux_analyze.assert_called_with(filepath)
    faux_upload.assert_any_call(ANY, analysis_filename)
    faux_upload.assert_any_call(filepath, audio_filename)
