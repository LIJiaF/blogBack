import os

BASE_DIR = os.path.dirname(__file__)
IMAGE_FORMAT = ['image/png', 'image/jpeg']

TORNADO_CONFIG = {
    'debug': True,
    'static_path': os.path.join(BASE_DIR, 'static')
}

MYSQL_CONFIG = {
    'db': 'myorder',
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'charset': 'utf8',
    'autocommit': True
}
