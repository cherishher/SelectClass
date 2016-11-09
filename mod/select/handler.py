# -*- coding: utf-8 -*-
# @Date    : 2016/5/22  16:57
# @Author  : 490949611@qq.com

import json
import traceback
import tornado.web

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
		'500':u'程序出错'
	}

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
				cardnum = self.get_argument("cardnum",default=None)
				classname = self.get_argument("classname",default=None)
				handle = self.get_argument("handle",default=None)#handle=0选课，1退课

				status = 1

				print cardnum,classname,handle
				retjson = {
					'code':200,
					'content':''
				}

				if not (cardnum and classname and handle):
					retjson['code'] = 400
				else:
					try:
						class_situation = self.db.query(Class).filter(Class.classname == classname).one()
						class_state = class_situation.state
						if class_state == 1:
							remain = class_situation.surplus
							if handle == '1':
								select = self.db.query(Select).filter(Select.cardnum == cardnum).one()
								self.db.delete(select)
								remain += 1
								class_situation.surplus = remain
								self.db.commit()
							# r = redis.Redis(host='localhost',port=6379,db=1)
							# if handle == "0":
							# 	r.set(cardnum,"1")
							# 	r.incr('remain')
							# remain = int(r.get("remain"))
							# remain = 20
							if remain <= 0:
								retjson['code'] = 403
							else:
								select = Select(cardnum = cardnum,classname = classname,state = 1)
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
				retjson['content'] = self.wrongcodeMap[retjson['code']]
				self.write(json.dumps(retjson))








