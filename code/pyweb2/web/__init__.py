# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

# 配置文件
import config


app = Flask(__name__)

# 加载配置文件内容
app.config.from_object(config)
'''
dbhost = '127.0.0.1:3306'
dbuser = 'root'
dbpass = '123456'
dbname = 'test'
DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
'''

"""
create_engine 会返回一个数据库引擎，echo 参数为 True 时，会显示每条执行的 SQL 语句，生产环境下可关闭
"""
engine = create_engine('mysql://root:@127.0.0.1:3306/test',
                        max_overflow = 20,  # 超过连接池大小外最多创建的连接
                        pool_size = 50,  # 连接池大小
                        pool_timeout = 30,  # 池中没有线程最多等待的时间，否则报错
                        pool_recycle = -1,  # 多久之后对线程池中的线程进行一次连接的回收（重置）—— -1 永不回收
                        echo=True)

# engine = create_engine('mysql://root:@127.0.0.1:3306/test',poolclass=NullPool,echo=True)

"""
sessionmaker() 会生成一个数据库会话类。
这个类的实例可以当成一个数据库连接，它同时还记录了一些查询的数据，并决定什么时候执行 SQL 语句。
"""
DB_Session = sessionmaker(bind=engine)

from web.controller import manage