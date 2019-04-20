from config import mysqlConfig
from .sql_func import MysqlManage
from .log_print import logger
from .err_func import MysqlError, FiledsError
from .fileds_check import FiledsCheck

db = MysqlManage(**mysqlConfig)
