#!/usr/bin/env python
#coding:utf-8

import os.path
import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.simple_httpclient
import tornado.httpclient
import tornado.httpserver
import tornado.options
import tornado.gen
from tornado.options import define, options
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.db.db import engine
from mod.login.handler import LoginHandler
from mod.select.handler import SelectHandler
from mod.publish.handler import PublishHandler
from mod.list.handler import ListHandler


define("port", default= 8000, help= "run on the given port", type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
		    (r"/login",LoginHandler),
			(r'/list',ListHandler),
			(r"/select",SelectHandler),
			(r"/publish",PublishHandler)
		]

		settings = dict (
			template_path= os.path.join(os.path.dirname(__file__), 'templates'),
			static_path= os.path.join(os.path.dirname(__file__), 'static'),
			cookie_secret="MAX90KLP8371B5AEAC5E64C6042415EF",
			debug= True,
			)
		tornado.web.Application.__init__(self,handlers,**settings)
		self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


if __name__ == "__main__":
	tornado.options.parse_command_line()
	Application().listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
