# -*- coding: utf-8 -*-
# @Date    : 2016/5/22  16:57
# @Author  : 490949611@qq.com

import json
from sqlalchemy.orm.exc import NoResultFound
from ..db.Class import Class
import traceback
import tornado.web

from config import *

class PublishHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def current_user(self):
		return self.get_secure_cookie("user")

	def get(self):
		self.render('select.html')

	def post(self):
		if not self.current_user:
			self.redirect("/login")
			return
		else:
			classname = self.get_argument("classname",default=None)
			capacity = self.get_argument("capacity",default=None)
			retjson = {
				'code':200,
				'content':u'添加成功！'
			}

			if not (classname and capacity):
				retjson['code'] = 400
				retjson['content'] = u'缺乏必须的参数'
			else:
				try:
					newClass = Class(classname=classname,capacity=capacity,surplus=capacity,state=1)
					self.db.add(newClass)
					self.db.commit()
				except Exception,e:
					self.db.rollback()
					traceback.print_exc()

			self.write(json.dumps(retjson))








