import tornado.web

from common import db, MysqlError, FiledsError, logger, login_check
from publit_func import encryption


def make_check(username, password):
    try:
        login_check(username, msg='用户名')
        login_check(password, msg='密码')
    except FiledsError as e:
        logger.warning('[ERROR] %s' % e)
        return str(e)
    except Exception as e:
        logger.error('[ERROR] %s' % str(e))
        raise

    return None


class LoginHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        res = {
            'code': 0,
        }

        msg = make_check(username, password)
        if msg:
            res['code'] = 1
            res['msg'] = msg
            return self.finish(res)

        sql = 'select password from users where username = "%s"' % (username)
        data = db.get_one(sql)
        if data and encryption(password) == data.get('password'):
            logger.info('[SUCCESS] %s 登录成功' % username)
            res['msg'] = '登录成功'
        else:
            logger.warning('[ERROR] 账号或密码错误')
            res['code'] = 1
            res['msg'] = '账号或密码错误'

        return self.finish(res)


class RegisterHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        res = {
            'code': 0,
        }

        msg = make_check(username, password)
        if msg:
            res['code'] = 1
            res['msg'] = msg
            return self.finish(res)

        sql = 'select username from users where username = "%s"' % (username)
        data = db.get_one(sql)
        if data:
            logger.warning('[ERROR] %s 用户名已存在' % username)
            res['msg'] = '用户名已存在!'
        else:
            try:
                sql = 'insert into users (username, password) values ("%s", "%s")' % (username, encryption(password))
                count = db.insert(sql)
                if count:
                    logger.info('[SUCCESS] %s 注册成功' % username)
                    res['msg'] = '注册成功!'
                else:
                    raise MysqlError
            except MysqlError as e:
                logger.error('[ERROR] %s 注册失败' % username)
                res['code'] = 1
                res['msg'] = '注册失败，请重新注册!'

        return self.finish(res)
