# _*_ coding: utf-8 _*_

# 调试模式是否开启
DEBUG = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/test"

SQLALCHEMY_POOL_SIZE = 11 # 数据库连接池的大小

SQLALCHEMY_POOL_TIMEOUT = 10 # 默认是10

SQLALCHEMY_ECHO = True

SQLALCHEMY_POOL_RECYCLE = 3600 # 3600秒自动回收连接

# 参考：http://www.cnblogs.com/wf-skylark/p/9306326.html