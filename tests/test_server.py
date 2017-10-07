import hashlib
import json
from mock import Mock
from mock import ANY

from queue_functions import do_work
from server import handle_post

# The S3 URL-maker is the default.
# If you change the default in server.py, you'll need to change it here too
from uploaders.s3 import get_url

def faux_upload():
    return True

def faux_analyze(filepath):
    return True

def test_post():
    q = Mock()
    filename = 'afakefilename'
    files = {'file': [{'body':  b'a-fake-file-body', 'filename': filename}]}

    hash_object = hashlib.md5(filename.encode())
    audio_filename = hash_object.hexdigest() + "-" + filename
    analysis_filename = audio_filename + '.analysis.json'

    expected = {'analysis': get_url(analysis_filename), 'audio': get_url(audio_filename)}
    actual = json.loads(handle_post(q, files, faux_upload, faux_analyze))

    q.enqueue.assert_called_with(do_work, (ANY, audio_filename, analysis_filename, faux_upload, faux_analyze))
    assert expected == actual
