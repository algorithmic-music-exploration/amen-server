#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Start of a server for uploading an analyzing audio with Amen
'''


import tornado.ioloop
import tornado.web

from tornado import gen

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.write("Hello, world")
    def post(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
