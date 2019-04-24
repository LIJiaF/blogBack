import hashlib


# 字符串加密
def encryption(string):
    md5 = hashlib.md5()
    md5.update(string.encode(encoding='utf-8'))
    return md5.hexdigest()


if __name__ == '__main__':
    md5_str = encryption('admin')
    print(md5_str)
