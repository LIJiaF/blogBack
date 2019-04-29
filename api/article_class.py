import tornado.web

from common.fileds_check import FiledsCheck, FiledsError
from common.log_print import logger
from common import db, MysqlError


class ArticleClassHandle(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', '')

        res = {
            'code': 0
        }

        try:
            name_check = FiledsCheck(name, msg='分类名称', min_lenght=2, max_length=10)
            name_check.check_null()
            name_check.check_length()

        except FiledsError as msg:
            res['code'] = 1
            res['msg'] = str(msg)
            logger.warning('[ERROR] %s' % str(msg))
            return self.finish(res)

        try:
            sql = 'insert into article_class (name) values ("%s")' % name
            count = db.insert(sql)
            if count:
                logger.info('[SUCCESS] %s 添加成功' % name)
                res['msg'] = '添加成功!'
            else:
                raise MysqlError
        except MysqlError as e:
            logger.error('[ERROR] %s 添加失败' % name)
            res['code'] = 1
            res['msg'] = '添加失败，请重新添加!'
            print(e)
        except Exception as e:
            logger.error('[ERROR] %s 添加失败' % name)
            res['code'] = 1
            res['msg'] = '添加失败，请重新添加!'
            print(e)

        return self.finish(res)
