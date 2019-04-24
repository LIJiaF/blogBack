import pymysql
import queue
import threading
from pymysql.cursors import DictCursor

from config import mysqlConfig
from common.err_func import MysqlError


class MysqlPool(object):
    def __init__(self, **config):
        self.config = config
        self.min_conn = config.get('min_conn', 2)
        self.max_conn = config.get('max_conn', 10)
        self.pool = queue.Queue(self.max_conn)

    def __connection(self):
        return pymysql.connect(**self.config)

    def get_conn(self):
        if not self.pool.empty():
            return self.pool.get()
        self.create_conn()
        return self.pool.get()

    def create_conn(self):
        self.pool.put(self.__connection())

    def close_conn(self, conn):
        if self.pool.qsize() < self.max_conn:
            self.pool.put(conn)
        else:
            conn.close()


class MysqlManage(object):
    _instance_lock = threading.Lock()

    # 实现单例模式
    def __new__(cls, **kwargs):
        if not hasattr(MysqlManage, "_instance"):
            with MysqlManage._instance_lock:
                if not hasattr(MysqlManage, "_instance"):
                    MysqlManage._instance = object.__new__(cls)
        return MysqlManage._instance

    def __init__(self, **config):
        self.pool = MysqlPool(**config, cursorclass=DictCursor)

    def get_one(self, sql, param=None):
        conn = self.pool.get_conn()
        cursor = conn.cursor()
        if param is None:
            count = cursor.execute(sql)
        else:
            count = cursor.execute(sql, param)

        if count > 0:
            result = cursor.fetchone()
        else:
            result = False

        self.__close(cursor, conn)
        return result

    def get_all(self, sql, param=None):
        conn = self.pool.get_conn()
        cursor = conn.cursor()
        if param is None:
            count = cursor.execute(sql)
        else:
            count = cursor.execute(sql, param)

        if count > 0:
            result = cursor.fetchall()
        else:
            result = False

        self.__close(cursor, conn)
        return result

    def get_many(self, sql, num, param=None):
        conn = self.pool.get_conn()
        cursor = conn.cursor()
        if param is None:
            count = cursor.execute(sql)
        else:
            count = cursor.execute(sql, param)

        if count > 0:
            result = cursor.fetchmany(num)
        else:
            result = False

        self.__close(cursor, conn)
        return result

    def insert(self, sql):
        try:
            count = self.execute(sql)
        except MysqlError:
            raise MysqlError()

        return count

    def update(self, sql):
        try:
            count = self.execute(sql)
        except MysqlError:
            raise MysqlError()

        return count

    def delete(self, sql):
        try:
            count = self.execute(sql)
        except MysqlError:
            raise MysqlError()

        return count

    def execute(self, sql):
        conn = self.pool.get_conn()
        cursor = conn.cursor()
        try:
            count = cursor.execute(sql)
            conn.commit()
        except MysqlError:
            conn.rollback()
            raise MysqlError()
        except Exception:
            conn.rollback()
            raise MysqlError()
        finally:
            self.__close(cursor, conn)

        return count

    def __close(self, cursor, conn):
        cursor.close()
        self.pool.close_conn(conn)


if __name__ == '__main__':
    select_sql = 'select * from users'
    insert_sql = 'insert into users (username, password) values("admin", "admin")'
    update_sql = 'update users set password = "root" where id = 2'
    delete_sql = 'delete from users where id = 1'

    conn = MysqlManage(**mysqlConfig)
    print(conn.get_all(select_sql))
    # print(conn.insert(insert_sql))
    # print(conn.update(update_sql))
    # print(conn.delete(delete_sql))
