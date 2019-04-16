import pymysql
from config import mysqlConfig


class MysqlError(Exception):
    pass


class MysqlManage(object):
    def __init__(self, config):
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

    def get_one(self, sql):
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print('[SUCCESS] 获取一条数据 ', result, 'SQL ', sql)
            self.__close()
        except Exception as e:
            print('[ERROR] 获取一条数据失败 ', 'SQL ', sql)
            print(e)

        return result

    def get_all(self, sql):
        result = []
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print('[SUCCESS] 获取%n条数据 ' % len(result), result, 'SQL ', sql)
            self.__close()
        except Exception as e:
            print('[ERROR] 获取多条数据失败 ', 'SQL ', sql)
            print(e)

        return result

    def insert(self, sql):
        try:
            count = self.__execute(sql)
            print('[SUCCESS] 插入%n条记录 ' % count, sql)
        except Exception as e:
            print('[ERROR] 插入记录失败 ', sql)
            print(e)

        return count

    def update(self, sql):
        try:
            count = self.__execute(sql)
            print('[SUCCESS] 更新%n条记录 ' % count, sql)
        except Exception as e:
            print('[ERROR] 更新记录失败 ', sql)
            print(e)

        return count

    def delete(self, sql):
        try:
            count = self.__execute(sql)
            print('[SUCCESS] 删除%n条记录 ' % count, sql)
        except Exception as e:
            print('[ERROR] 删除记录失败 ', sql)
            print(e)

        return count

    def execute(self, sql):
        try:
            self.__execute(sql)
            print('[SUCCESS] 执行sql语句成功 ', sql)
        except Exception as e:
            print('[ERROR] 执行sql语句失败 ', sql)
            print(e)

    def rollback(self):
        self.__rollback()

    def __execute(self, sql):
        count = 0
        try:
            count = self.cursor.execute(sql)
            self.conn.commit()
            self.__close()
        except Exception as e:
            print(e)

        return count

    def __rollback(self):
        print('sql语句执行失败，事务回滚')
        self.conn.rollback()

    def __close(self):
        print('关闭游标，关闭连接')
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    insert_sql = 'insert into users (username, password) values("admin", "admin")'
    update_sql = 'update users set password = "root" where id = 2'
    delete_sql = 'delete from users where id = 1'

    conn = MysqlManage(mysqlConfig)
    print(conn.insert(insert_sql))
    print(conn.update(update_sql))
    print(conn.delete(delete_sql))
