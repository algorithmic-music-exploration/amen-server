#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Start of a server for uploading an analyzing audio with Amen
'''

import re
import json
import hashlib

from tempfile import NamedTemporaryFile
from redis import Redis
from rq import Queue
import tornado.ioloop
import tornado.web
from tornado import gen

from queue_functions import do_work
from queue_functions import make_audio

# Change this to the uploader of your choice!
from uploaders.s3 import get_url
from uploaders.s3 import upload

def handle_post(q, files, make_url, upload_function, analysis_function):
    file_body = files['file'][0]['body']
    target_filename = files['file'][0]['filename']
    target_filename = re.sub(r'[^\w\.]', '', target_filename)

    hash_object = hashlib.md5(target_filename.encode())
    audio_filename = hash_object.hexdigest() + "-" + target_filename
    analysis_filename = audio_filename + '.analysis.json'
    audio_url = get_url(audio_filename)
    analysis_url = get_url(analysis_filename)

    f = NamedTemporaryFile(delete=False)
    filepath = f.name
    f.write(file_body)
    f.close()

    q.enqueue(do_work, (filepath, audio_filename, analysis_filename, upload_function, analysis_function))
    res = {'audio': audio_url, 'analysis': analysis_url}
    return json.dumps(res)

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    @gen.coroutine
    def get(self):
        self.write("Hello, world")

    @gen.coroutine
    def post(self):
        # We should clearly not create the Q here, but here we are
        q = Queue(connection=Redis())
        res = handle_post(q, self.request.files, get_url, upload, make_audio)
        self.write(res)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
