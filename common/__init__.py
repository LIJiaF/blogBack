from config import mysqlConfig
from .sql_func import MysqlManage, MysqlError
from .log_print import logger

db = MysqlManage(**mysqlConfig)
