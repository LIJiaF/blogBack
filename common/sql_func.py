import pymysql


class MysqlManage(object):
    def __init__(self, config):
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

    def get_one(self, sql):
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)

        return result

    def get_all(self, sql):
        list = ()
        try:
            self.cursor.execute(sql)
            list = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)

        return list

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            count = self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)

        return count

    def close(self):
        self.cursor.close()
        self.conn.close()
