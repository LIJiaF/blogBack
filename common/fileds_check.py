import re

from common import FiledsError


class FiledsCheck(object):
    __slots__ = ('__content', '__msg', '__min_length', '__max_length')

    def __init__(self, content, msg='', min_lenght=5, max_length=15):
        self.__content = content
        self.__msg = msg
        self.__min_length = min_lenght
        self.__max_length = max_length
        # self.check()

    def check(self):
        func_list = list(filter(lambda x: re.match(r'^check_', x), dir(self)))
        for f in func_list:
            eval('self.' + f + '()')

    @property
    def content(self):
        return self.__content

    @property
    def msg(self):
        return self.__msg

    @property
    def min_lenght(self):
        return self.__min_length

    @property
    def max_length(self):
        return self.__max_length

    def check_null(self):
        if not self.__content:
            raise FiledsError('%s不能为空' % self.__msg)

    def check_special(self):
        pattern = re.compile('[^a-zA-Z\d]')
        if re.search(pattern, self.__content):
            raise FiledsError('%s不能包含特殊字符' % self.__msg)

    def check_length(self):
        if len(self.__content) < self.__min_length or len(self.__content) > self.__max_length:
            raise FiledsError('%s长度为%d~%d位' % (self.__msg, self.__min_length, self.__max_length))

    def __str__(self):
        return 'check: %s level: %d' % (self.__msg, self.__level)

    __repr__ = __str__


def login_check(content, **kwargs):
    fileds_check = FiledsCheck(content, **kwargs)
    fileds_check.check_null()
    fileds_check.check_special()
    fileds_check.check_length()


if __name__ == '__main__':
    try:
        login_check('', msg='用户名')
    except FiledsError as e:
        print(e)
