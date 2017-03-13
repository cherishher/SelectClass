# -*- coding: utf-8 -*-
# @Date    : 2016/5/22  16:57
# @Author  : 490949611@qq.com

import json
from sqlalchemy.orm.exc import NoResultFound
from ..db.Member import Member
from ..db.SelectMember import SelectMember
import traceback

import tornado.web

class ListHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get_current_user(self):
		return self.get_secure_cookie("user")

	def get(self):
		if not self.get_current_user():
			self.redirect("/login")
			return
		else:
			self.render('list.html')






