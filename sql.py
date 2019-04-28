""" 角色表 role
name        角色名字
"""
ROLE = """
CREATE TABLE IF NOT EXISTS role(
    id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(15),
    UNIQUE INDEX role_name_uq_index(name ASC)
)
"""

""" 用户表 users
username    用户名
password    密码
email       邮箱
photo       头像
age         年龄
sex         性别
address     地址
summary     名言
role_id     角色ID
"""
USERS = """
CREATE TABLE IF NOT EXISTS users(
    id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    email VARCHAR(30),
    photo VARCHAR(200),
    age INT(3),
    sex INT(2),
    address VARCHAR(30),
    summary VARCHAR(30),
    role_id INT(11),
    UNIQUE INDEX users_username_uq_index(username ASC),
    UNIQUE INDEX users_email_uq_index(email ASC),
    CONSTRAINT users_role_id_fk_index FOREIGN KEY (role_id) REFERENCES role(id) on delete cascade on update cascade
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
summary    描述
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

tables = [ROLE, USERS]
