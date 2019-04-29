import tornado.web
import datetime

from common.fileds_check import FiledsCheck, FiledsError
from common import db, logger, MysqlError


class ArticleHandle(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument('title', '')
        class_id = self.get_argument('class_id', '')
        photo = self.get_argument('photo', '')
        summary = self.get_argument('summary', '')

        res = {
            'code': 0
        }

        try:
            title_check = FiledsCheck(title, msg='文章标题', max_length=30)
            title_check.check_null()
            title_check.check_length()
            class_id_check = FiledsCheck(class_id, msg='所属分类')
            class_id_check.check_null()
        except FiledsError as msg:
            res['code'] = 1
            res['msg'] = str(msg)
            logger.warning('[ERROR] %s' % str(msg))
            return self.finish(res)

        data = {
            'title': title,
            'class_id': class_id,
            'photo': photo,
            'summary': summary,
            'author': 'admin',
            'create_time': datetime.datetime.now()
        }

        try:
            sql = 'insert into article (title, class_id, photo, summary, author, create_time) ' \
                  'values ("{title}", {class_id}, "{photo}", "{summary}", "{author}", "{create_time}")'
            count = db.insert(sql.format(**data))
            if count:
                logger.info('[SUCCESS] %s 添加成功' % title)
                res['msg'] = '添加成功!'
        except MysqlError as e:
            logger.error('[ERROR] %s 添加失败' % title)
            res['code'] = 1
            res['msg'] = '添加失败，请重新添加!'
            print(e)
        except Exception as e:
            logger.error('[ERROR] %s 添加失败' % title)
            res['code'] = 1
            res['msg'] = '添加失败，请重新添加!'
            print(e)

        return self.finish(res)
