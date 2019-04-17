import re


class FiledsCheck(object):
    def __init__(self, content, msg, level=1, min_lenght=6, max_length=15):
        self.content = content
        self.msg = msg
        self.level = level
        self.min_length = min_lenght
        self.max_length = max_length
        self.check()

    def check(self):
        level = self.level
        if level == 1:
            return self.check_null() or None
        elif level == 2:
            return self.check_length() or None
        else:
            return self.check_special() or None

    def check_null(self):
        if not self.content:
            return '%s不能为空' % self.msg

    def check_length(self):
        self.check_null()
        if len(self.content) < self.min_length or len(self.content) > self.max_length:
            return '%s长度为%d~%d位' % (self.msg, self.min_length, self.max_length)

    def check_special(self):
        self.check_null()
        self.check_length()
        pattern = re.compile('[^a-zA-Z\d]')
        if re.search(pattern, self.content):
            return '%s不能包含特殊字符' % self.msg
