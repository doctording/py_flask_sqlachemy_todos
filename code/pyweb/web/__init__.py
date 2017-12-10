# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

# #环境变量，指向配置文件setting的路径#创建数据库对象
db = SQLAlchemy(app)

from web.controller import manage