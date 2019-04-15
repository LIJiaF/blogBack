import tornado.web


class LoginHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        result = {
            'code': 0,
        }

        if not username or not password:
            result['msg'] = '用户名或密码不能为空'

        if username == '123' and password == '123':
            result['msg'] = '登录成功'
        else:
            result['msg'] = '账号或密码错误'

        return self.finish(result)


class RegisterHandle(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        result = {
            'code': 0,
        }

        if not username or not password:
            result['msg'] = '用户名或密码不能为空'

        result['msg'] = '注册成功'

        return self.finish(result)
