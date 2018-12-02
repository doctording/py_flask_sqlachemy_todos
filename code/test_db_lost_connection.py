# -*- coding:utf-8 -*-
import pymysql
import time


class Database(object):

    def __init__(self):
        self.dbhost = '127.0.0.1'
        self.port = 3306
        self.dbuser = 'root'
        self.dbpass = ''
        self.dbname = 'test'
        # DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host=self.dbhost,
                                port=self.port,
                                user=self.dbuser,
                                password=self.dbpass,
                                database=self.dbname)

    def close(self):
        try:
            self.conn.close()
        except:
            raise ValueError('conn close exception')

    # def query(self, sql):
    #     if self.db:
    #         cursor = self.db.cursor()
    #         cursor.execute(sql)
    #     else:
    #         raise ValueError('DB not connected')


def handle_query():
    db = Database()
    db.connect()
    # 可以睡眠超过`wait_timeout`
    print("sleep 6 seconds") 
    time.sleep(6)
    cur = db.conn.cursor()
    sql = "select id, sno, name from t_user"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)
    cur.close()

    db.close()

if __name__ == '__main__':
    handle_query()
