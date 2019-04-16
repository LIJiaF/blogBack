import tornado.web

from common import db, MysqlError


class LoginHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        res = {
            'code': 0,
        }

        if not username or not password:
            res['msg'] = '用户名或密码不能为空'
        elif username == '123' and password == '123':
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

        if not username or not password:
            res['msg'] = '用户名或密码不能为空!'
            return self.finish(res)

        sql = 'select id from users where username = "%s"' % (username)
        data = db.get_one(sql)
        if data:
            res['msg'] = '用户名已存在!'
        else:
            try:
                sql = 'insert into users (username, password) values ("%s", "%s")' % (username, password)
                count = db.insert(sql)
                if count:
                    res['msg'] = '注册成功!'
            except MysqlError as e:
                db.rollback()
                res['msg'] = '注册失败，请重新注册!'
                print(e)

        return self.finish(res)
