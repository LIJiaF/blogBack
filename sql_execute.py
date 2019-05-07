from common import db
from sql import tables

for table in tables:
    print('创建表%s' % table)
    db.execute(table)
