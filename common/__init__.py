from config import MYSQL_CONFIG
from common.sql_func import MysqlManage
from common.log_print import logger
from common.err_func import MysqlError, FiledsError
from common.fileds_check import login_check

db = MysqlManage(**MYSQL_CONFIG)
