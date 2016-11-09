# -*- coding: utf-8 -*-
# @Date    : 2016/5/24  19:45
# @Author  : 490949611@qq.com
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine


Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'
    studentnum = Column(String(64), nullable=False)
    name = Column(String(64),nullable=False)
    cardnum = Column(String(64), nullable=False)


if __name__ == '__main__':
	Base.metadata.create_all(engine)