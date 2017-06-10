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

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers for CORS")
        self.set_header("Access-Control-Allow-Origin", "*")

    @gen.coroutine
    def get(self):
        self.write("Hello, world")

    @gen.coroutine
    def post(self):
        # We should clearly not create the Q here, but here we are
        q = Queue(connection=Redis())

        file_body = self.request.files['file'][0]['body']
        target_filename = self.request.files['file'][0]['filename']
        target_filename = re.sub(r'[^\w\.]', '', target_filename)
        hash_object = hashlib.md5(target_filename.encode())
        target_filename = hash_object.hexdigest() + "-" + target_filename

        # This target_filename needs to be the complete uploaded paths.  hmm
# somewhere in MainHandler we should config the uploader, maybe?
# but psobot thinks the queue should be a seperate container
# both containers could read the same config file
# we could make users duplicate code
# we could have the server return a middle-man URL, that the user then GETs, and that eventually points to the data
        # let's hard code it for now, and figure out the config later.

        audio_url= 'https://s3-us-west-2.amazonaws.com/amen-data/' + target_filename
        analysis_url= 'https://s3-us-west-2.amazonaws.com/amen-data/' + target_filename + '.analysis.json'

        f = NamedTemporaryFile(delete=False)
        filepath = f.name
        f.write(file_body)
        f.close()

        # put the file on the queue
        q.enqueue(do_work, (filepath, target_filename))

        # we'll also need to do some stuff here, around what we return, etc
        # we need to return a link to where to poll for analysis, etc
        res = {'audio': audio_url, 'analysis': analysis_url}
        self.write(json.dumps(res))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
