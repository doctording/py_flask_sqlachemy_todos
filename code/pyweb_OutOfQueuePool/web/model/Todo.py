# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class Todo(Base):
    __tablename__ = 't_todo'

    id = Column(Integer, primary_key=True)
    sno = Column(String(255))
    task = Column(Text)
    finish = Column(Integer)
    createtime = Column(DateTime)

    def __init__(self, sno, task, finish, createtime):
        self.sno = sno
        self.task = task
        self.finish = finish
        self.createtime = createtime

    # def __repr__(self):
    #     return '<Todo %r>' % self.id

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.sno)
