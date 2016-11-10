# -*- coding: utf-8 -*-
# @Date    : 2016/5/22  16:57
# @Author  : 490949611@qq.com

import json
from sqlalchemy.orm.exc import NoResultFound
from ..db.Member import Member
from ..db.SelectMember import SelectMember
import traceback

import tornado.web

class LoginHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get(self):
		self.render('demo.html')

	def post(self):
		#验证用户身份
		retjson={
				'code':200,
				'text':u"登录成功"
				}

		cardnum = self.get_argument('cardnum',default=None)
		studentnum = self.get_argument('studentnum',default=None)
		college = self.get_argument('college',default=None)
		phonenum = self.get_argument('phonenum',default=None)

		print(cardnum)
		try:
			member = self.db.query(Member).filter(Member.cardnum == cardnum).one()
			self.set_secure_cookie("user",cardnum)
			newSelectMember = SelectMember(cardnum = cardnum,studentnum = studentnum,college = college,phonenum = phonenum)
			self.db.add(newSelectMember)
			self.db.commit()
		except NoResultFound:
			retjson['code'] = 401
			retjson['text'] = u'一卡通或学号错误'
		except Exception,e:
			self.db.rollback()
			traceback.print_exc()
			retjson['code'] = 500
			retjson['text'] = u'系统故障'
		self.write(json.dumps(retjson,ensure_ascii=False,indent=2))







