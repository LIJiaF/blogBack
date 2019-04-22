from config import mysqlConfig
from common.sql_pool import MysqlPool
from common.log_print import logger
from common.err_func import MysqlError, FiledsError
from common.fileds_check import FiledsCheck

db = MysqlPool(mysqlConfig)
