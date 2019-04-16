from config import mysqlConfig
from .sql_func import MysqlManage, MysqlError

db = MysqlManage(mysqlConfig)
