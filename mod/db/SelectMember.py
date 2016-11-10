# -*- coding: utf-8 -*-
# @Date    : 2016/11/10  21:32
# @Author  : 490949611@qq.com
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine


Base = declarative_base()

class SelectMember(Base):
    __tablename__ = 'selectMember'
    id = Column(Integer, primary_key=True)
    studentnum = Column(String(64), nullable=False)
    college = Column(String(64),nullable=False)
    cardnum = Column(String(64), nullable=False)
    phonenum = Column(String(64), nullable=False)


if __name__ == '__main__':
	Base.metadata.create_all(engine)