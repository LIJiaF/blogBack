from pymysql import (DataError, OperationalError, IntegrityError, InternalError, NotSupportedError, ProgrammingError)


class MysqlError(DataError, OperationalError, IntegrityError, InternalError, NotSupportedError, ProgrammingError):
    __slots__ = ()
    pass


class FiledsError(Exception):
    __slots__ = ()
    pass
