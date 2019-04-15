from config import mysqlConfig
from .sql_func import MysqlManage

db = MysqlManage(mysqlConfig)
