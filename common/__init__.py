from config import mysqlConfig
from .sql_func import MysqlManage
from .log_print import logger
from .define_err import MysqlError, FiledsError

db = MysqlManage(**mysqlConfig)
