
## 项目简介

python flask+mysql搭建的一个web项目，主要是一个记录个人待办事项的系统。基于此项目重点理解几个关于Sqlacmhey，MySQL的问题

---

## 知识点,遇到的问题

* flask框架简单使用 + Python 基础

* Sqlachemy,Flask-Sqlachemy

* [MySQL自身状态的认识](https://blog.csdn.net/qq_26437925/article/details/83782403)

* [数据库连接池和Sqlachemy](./db_pool.md)

* 几个数据库报错问题 => [重点理解分析](./code/README.md)

1. TimeoutError: QueuePool limit of size 5 overflow 0 reached, connection timed out, timeout 30

2. too many connections

3. Lost Connection to MySQL server

## 主要开发环境要求

* python 2.7

* flask, sqlalchemy(数据库rom)

* mysql （见test.sql文件）

## 功能说明

### 粗版

1. 用户直接登录，未加注册功能

2. 能够显示一个登录用户的所有待办事项

3. 能够添加待办事项，但是不能修改

### 加强

* 登录，注册功能

* 数据修改功能

* 界面美观


## 运行截图

![](./imgs/todologin.png)


![](./imgs/login.png)

![](./imgs/logout.png)


## 参考

* Flask框架的学习指南之制作简单blog系统

作者： 茁壮的小草

地址： https://www.cnblogs.com/mysql-dba/p/6066861.html

* Flask-SQLAlchemy

http://flask-sqlalchemy.pocoo.org/2.3/


* 四个好看的CSS样式表格

作者：nightelve

地址：http://blog.csdn.net/nightelve/article/details/7957726/

* 思路来源

https://github.com/lalor/todolist


# Todo
