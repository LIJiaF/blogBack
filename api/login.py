import tornado.web
import re

from common import db, MysqlError, logger
from publit_func import FiledsCheck


class LoginHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None).strip()
        password = self.get_argument('password', None).strip()

        res = {
            'code': 0,
        }

        msg = FiledsCheck(username, msg='用户名', level=3).check()
        if msg:
            logger.info('[ERROR] %s' % msg)
            res['msg'] = msg
            return self.finish(res)

        if username == '123' and password == '123':
            res['msg'] = '登录成功'
        else:
            res['msg'] = '账号或密码错误'

        return self.finish(res)


class RegisterHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None).strip()
        password = self.get_argument('password', None).strip()

        res = {
            'code': 0,
        }

        if not username or not password:
            logger.info('[ERROR] 用户名或密码不能为空')
            res['msg'] = '用户名或密码不能为空!'
            return self.finish(res)

        if len(username) < 6 or len(username) > 15:
            logger.info('[ERROR] 用户名长度为6~15位')
            res['msg'] = '用户名长度为6~15位!'
            return self.finish(res)

        if len(username) < 6 or len(username) > 15:
            logger.info('[ERROR] 密码长度为6~15位')
            res['msg'] = '密码长度为6~15位!'
            return self.finish(res)

        pattern = re.compile('[^a-zA-Z\d]')
        if re.search(pattern, username):
            logger.info('[ERROR] 用户名不能包含特殊字符')
            res['msg'] = '用户名不能包含特殊字符!'
            return self.finish(res)

        if re.search(pattern, password):
            logger.info('[ERROR] 密码不能包含特殊字符')
            res['msg'] = '密码不能包含特殊字符!'
            return self.finish(res)

        sql = 'select id from users where username = "%s"' % (username)
        data = db.get_one(sql)
        if data:
            logger.info('[ERROR] 用户名已存在')
            res['msg'] = '用户名已存在!'
        else:
            try:
                sql = 'insert into users (username, password) values ("%s", "%s")' % (username, password)
                count = db.insert(sql)
                if count:
                    logger.info('[SUCCESS] 注册成功')
                    res['msg'] = '注册成功!'
            except MysqlError as e:
                logger.error('[ERROR] 注册成功')
                res['msg'] = '注册失败，请重新注册!'
                print(e)

        return self.finish(res)
