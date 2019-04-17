from pymysql import (DataError, OperationalError, IntegrityError, InternalError, NotSupportedError, ProgrammingError)


class MysqlError(DataError, OperationalError, IntegrityError, InternalError, NotSupportedError, ProgrammingError):
    pass
