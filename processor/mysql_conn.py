# import pymysql
# from dbutils.pooled_db import PooledDB
#
# # class MysqlPool(object):
# #     """
# #     mysql connection client of pool
# #     """
# #     pool = PooledDB(creator=pymysql, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD,
# #                     db=MYSQL_DATABASE, maxconnections=10, cursorclass=pymysql.cursors.DictCursor)
# #
# #     def __enter__(self):
# #         self.conn = MysqlPool.pool.connection()
# #         self.cursor = self.conn.cursor()
# #         return self
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.cursor.close()
# #         self.conn.close()
#

import pymysql
from dbutils.pooled_db import PooledDB
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


class MysqlPool(object):

    def __init__(self, creator=pymysql, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD,
                 db=MYSQL_DATABASE, maxconnections=10, cursorclass=pymysql.cursors.DictCursor):
        self.POOL = PooledDB(
            creator=creator,
            maxconnections=maxconnections,  # 连接池的最大连接数
            maxcached=10,
            maxshared=10,
            blocking=True,
            setsession=[],
            host=host,
            port=port,
            user=user,
            password=password,
            database=db,
            charset='utf8',
            cursorclass=cursorclass
        )

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect(self):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        return conn, cursor

    def connect_close(self, conn, cursor):
        cursor.close()
        conn.close()

    def fetch_all(self, sql, args=None):
        conn, cursor = self.connect()
        if args is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, args=None)
        record_list = cursor.fetchall()
        return record_list

    def fetch_one(self, sql, args=None):
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        return result

    def insert(self, sql, args=None):
        conn, cursor = self.connect()
        row = cursor.execute(sql, args)
        conn.commit()
        self.connect_close(conn, cursor)
        return row


conn = MysqlPool()
if __name__ == '__main__':
    conn = MysqlPool()
    sql = 'select district,stationid from area_cn where district like %s or city like %s'
    ret = conn.fetch_one(sql, ('莒南', '莒南'))
    print(ret)
