# -*- coding: utf-8 -*-
# @Date    : 2016/5/22  16:57
# @Author  : 490949611@qq.com

import json
import traceback
import tornado.web
from sqlalchemy.orm.exc import NoResultFound
import time

import redis
from ..db.Select import Select
from ..db.Class import Class

class SelectHandler(tornado.web.RequestHandler):

	wrongcodeMap={
		'200':u'选课成功',
		'400':u'账户信息不匹配',
		'401':u'缺少必要参数',
		'402':u'课程状态异常',
		'403':u'人满为患，选课失败',
		'404':u'不能重复选课',
		'500':u'程序出错'
	}

	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get_current_user(self):
		return self.get_secure_cookie("user")

	def get(self):
		if int(time.time())<1478827860:
			self.write(u"请等待开始")
		else:
			if not self.get_current_user():
				self.redirect("/login")
				return
			else:
				try:
					student = self.db.query(Select).filter(Select.cardnum == self.get_current_user()).one()
					course = self.db.query(Class).filter(Class.id == 1).one()
					self.render('quit.html',data = course)
				except NoResultFound:
					course = self.db.query(Class).filter(Class.id == 1).one()
					self.render('select.html',data = course)
				except Exception,e:
					self.write(str(e))
	def post(self):
		if not self.get_current_user:
			self.redirect("/login")
			return
		else:
				selecttime = self.get_argument('selecttime',default=None)
				classname = self.get_argument("classname",default=None)
				handle = self.get_argument("handle",default=None)#handle=0选课，1退课
				status = 1

				retjson = {
					'code':200,
					'text':''
				}

				if not (selecttime and classname and handle):
					retjson['code'] = 400
				else:
					try:
						class_situation = self.db.query(Class).filter(Class.classname == classname).one()
						class_state = class_situation.state
						if class_state == 1:
							remain = class_situation.surplus
							if handle == '1':
								select = self.db.query(Select).filter(Select.cardnum == self.get_current_user()).one()
								self.db.delete(select)
								remain += 1
								class_situation.surplus = remain
								self.db.commit()
							else:
								if remain <= 0:
									retjson['code'] = 403
								else:
									try:
										ifselect = self.db.query(Select).filter(Select.cardnum == self.get_current_user()).one()
										retjson['code'] = 404
									except NoResultFound:
										select = Select(cardnum = self.get_current_user(),selecttime = selecttime,classname = classname,state = 1)
										self.db.add(select)
										# r.lpush("select",json.dumps(data))
										# r.decr('remain')
										remain -= 1
										class_situation.surplus = remain
										# retjson['content'] = remain
										self.db.commit()

							#
							# if status == 1:
							# 	select
						else:
							retjson['code'] = 402
					except Exception,e:
						self.db.rollback()
						traceback.print_exc()
				retjson['text'] = self.wrongcodeMap[str(retjson['code'])]
				self.write(json.dumps(retjson,ensure_ascii=False,indent=2))








