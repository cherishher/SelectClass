# -*- coding: utf-8 -*-
# @Date    : 2016/11/5  11:34
# @Author  : 490949611@qq.com
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine


Base = declarative_base()

class Select(Base):
    __tablename__ = 'select'
    id = Column(Integer, primary_key=True)
    cardnum = Column(String(128), nullable=False)
    classname = Column(String(64),nullable=False)
    phonenum = Column(String(64),nullable=False)
    state = Column(String(64), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)