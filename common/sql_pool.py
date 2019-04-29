import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

from config import MYSQL_CONFIG
from common.err_func import MysqlError
from common.log_print import logger


class MysqlPool(object):
    __pool = None

    def __init__(self, config):
        self._conn = MysqlPool.__getConn(config)
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn(config):
        if MysqlPool.__pool is None:
            __pool = PooledDB(pymysql, mincached=1, maxcached=20, cursorclass=DictCursor, **config)

        return __pool.connection()

    def get_one(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)

        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False

        return result

    def get_all(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)

        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False

        return result

    def get_many(self, sql, num, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)

        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False

        return result

    def insert(self, sql, param=None):
        try:
            count = self._query(sql, param)
        except MysqlError as e:
            raise MysqlError()

        return count

    def update(self, sql, param=None):
        try:
            count = self._query(sql, param)
        except MysqlError as e:
            raise MysqlError()

        return count

    def delete(self, sql, param=None):
        try:
            count = self._query(sql, param)
        except MysqlError as e:
            raise MysqlError()

        return count

    def _query(self, sql, param):
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
        except MysqlError as e:
            logger.error('[ERROR] SQL语句执行失败: %s', sql)
            raise MysqlError()

        return count

    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')

        self._cursor.close()
        self._conn.close()


if __name__ == '__main__':
    select_sql = 'select * from users'

    mysql = MysqlPool(MYSQL_CONFIG)
    print(mysql.get_all(select_sql))

    mysql.dispose()
