# -*- coding: utf-8 -*-
# @Date    : 2016/11/5  11:15
# @Author  : 490949611@qq.com
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine


Base = declarative_base()

class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    classname = Column(String(128), nullable=False)
    capacity = Column(Integer,nullable=False)
    surplus = Column(Integer, nullable=False)
    state = Column(Integer,nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)