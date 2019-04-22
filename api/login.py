import tornado.web

from common import db, MysqlError, FiledsError, logger, FiledsCheck


def check(username, password):
    try:
        FiledsCheck(username, msg='用户名')
        FiledsCheck(password, msg='密码')
    except FiledsError as e:
        logger.info('[ERROR] %s' % e)
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

        msg = check(username, password)
        if msg:
            return self.finish(msg)

        if username == '123' and password == '123':
            res['msg'] = '登录成功'
        else:
            res['msg'] = '账号或密码错误'

        return self.finish(res)


class RegisterHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        res = {
            'code': 0,
        }

        msg = check(username, password)
        if msg:
            return self.finish(msg)

        sql = 'select id from users where username = "%s"' % (username)
        data = db.get_one(sql)
        if data:
            logger.info('[ERROR] %s 用户名已存在' % username)
            res['msg'] = '用户名已存在!'
        else:
            try:
                sql = 'insert into users (username, password) values ("%s", "%s")' % (username, password)
                count = db.insert(sql)
                if count:
                    logger.info('[SUCCESS] 注册成功')
                    res['msg'] = '注册成功!'
            except MysqlError as e:
                logger.error('[ERROR] 注册失败')
                res['msg'] = '注册失败，请重新注册!'
                print(e)

        return self.finish(res)
