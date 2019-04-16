from common import db
from sql import tables

for table in tables:
    db.execute(table)
