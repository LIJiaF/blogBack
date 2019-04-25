""" 用户表 users
username    用户名
password    密码
email       邮箱
photo       头像
age         年龄
sex         性别
address     地址
describe    名言
role_id     角色ID
"""
USERS = """
CREATE TABLE IF NOT EXISTS users(
    id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    photo VARCHAR(255),
    age INT(3),
    sex INT(2),
    address VARCHAR(255),
    describe VARCHAR(255),
    UNIQUE INDEX username_index(username ASC)
)
"""

""" 角色表 role
name        角色名字
"""
ROLE = """
CREATE TABLE IF NOT EXISTS role(
    id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    UNIQUE INDEX role_name_index(name ASC)
)
"""

""" 权限表 auth
url         路由地址
role_id     角色ID
"""

""" 文章分类 article_class
name        分类名称
"""

""" 文章
title       标题
photo       照片
describe    描述
author      作者
create_time 创建时间
read_num    阅读次数
class_id    分类ID
content     文章内容
"""

""" 文章标签 article_label
name        标签名字
article_id  文章ID
"""

tables = [USERS]
