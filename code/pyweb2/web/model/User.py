# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer,Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True)
    sno = Column(String(255), unique=True)
    password = Column(String(255))

    # def __init__(self, sno, password):
    #     self.sno = sno
    #     self.password = password

    # def __repr__(self):
    #     return '<User %r>' % self.sno
