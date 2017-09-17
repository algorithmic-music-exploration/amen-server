import hashlib
import json
from unittest.mock import Mock
from unittest.mock import ANY

from queue_functions import do_work
from server import handle_post
from uploaders.s3 import get_url
from uploaders.s3 import upload

def test_post():
    q = Mock()
    filename = 'afakefilename'
    files = {'file': [{'body':  b'a-fake-file-body', 'filename': filename}]}

    hash_object = hashlib.md5(filename.encode())
    audio_filename = hash_object.hexdigest() + "-" + filename
    analysis_filename = audio_filename + '.analysis.json'

    expected = {'analysis': get_url(analysis_filename), 'audio': get_url(audio_filename)}
    actual = json.reads(handle_post(q, files, get_url, upload))

    q.enqueue.assert_called_with(do_work, (ANY, audio_filename, analysis_filename, upload))
    assert expected == actual
