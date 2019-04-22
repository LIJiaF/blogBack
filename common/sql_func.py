import pymysql
from pymysql.cursors import DictCursor

from config import mysqlConfig
from common.err_func import MysqlError
from common.log_print import logger


class MysqlManage(object):
    def __init__(self, **config):
        self.conn = None
        self.cursor = None
        self.db = config['db']
        self.host = config['host']
        self.user = config['user']
        self.password = config['password']
        self.port = config['port']
        self.charset = config['charset']
        self.cursorClass = DictCursor

    def connect(self):
        self.conn = pymysql.connect(db=self.db, host=self.host, user=self.user, password=self.password, port=self.port,
                                    cursorclass=self.cursorClass)
        self.cursor = self.conn.cursor()

    def get_one(self, sql):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            logger.info('[SUCCESS] 获取一条数据 %s' % sql)
        except MysqlError as e:
            logger.info('[ERROR] 获取数据失败 %s' % sql)
            raise MysqlError()
        except Exception as e:
            logger.info('[ERROR] 获取数据失败 %s' % sql)
            raise MysqlError()
        finally:
            self.close()

        return result

    def get_all(self, sql):
        result = []
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            logger.info('[SUCCESS] 获取 %d 条数据 %s' % (len(result), sql))
        except MysqlError as e:
            logger.info('[ERROR] 获取数据失败 %s' % sql)
            raise MysqlError()
        except Exception as e:
            logger.info('[ERROR] 获取数据失败 %s' % sql)
            raise MysqlError()
        finally:
            self.close()

        return result

    def insert(self, sql):
        try:
            count = self.execute(sql)
        except MysqlError as e:
            raise MysqlError()

        return count

    def update(self, sql):
        try:
            count = self.execute(sql)
        except MysqlError as e:
            raise MysqlError()

        return count

    def delete(self, sql):
        try:
            count = self.execute(sql)
        except MysqlError as e:
            raise MysqlError()

        return count

    def execute(self, sql):
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.conn.commit()
            print('[SUCCESS] 执行sql语句成功 ', sql)
        except MysqlError as e:
            self.rollback()
            print('[ERROR] 执行sql语句失败 ', sql)
            raise MysqlError()
        except Exception as e:
            self.rollback()
            print('[ERROR] 执行sql语句失败 ', sql)
            raise MysqlError()
        finally:
            self.close()

        return count

    def rollback(self):
        print('[ERROR] sql语句执行失败，事务回滚')
        self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()


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
