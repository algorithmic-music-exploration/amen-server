#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Start of a server for uploading an analyzing audio with Amen
'''
import re
import hashlib

from tempfile import NamedTemporaryFile
from redis import Redis
from rq import Queue
import tornado.ioloop
import tornado.web
from tornado import gen

from queue_functions import do_work

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.write("Hello, world")

    @gen.coroutine
    def post(self):
        # We should clearly not create the Q here, but here we are
        q = Queue(connection=Redis())

        file_body = self.request.files['file'][0]['body']
        s3_filename = self.request.files['file'][0]['filename']
        s3_filename = re.sub(r'[^\w\.]', '', s3_filename)
        hash_object = hashlib.md5(s3_filename.encode())
        s3_filename = hash_object.hexdigest() + s3_filename

        f = NamedTemporaryFile(delete=False)
        filepath = f.name
        f.write(file_body)
        f.close()

        # put the file on the queue
        q.enqueue(do_work, (filepath, s3_filename))

        # we'll also need to do some stuff here, around what we return, etc
        # we need to return a link to where to poll for analysis, etc
        self.write("Async done, file write may or may not be done.  Poll the following URL to see: " + s3_filename)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
