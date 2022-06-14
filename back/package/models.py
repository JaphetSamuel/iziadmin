from config.db import db
from pony.orm import Required, Optional, PrimaryKey
import datetime

class Package(db.Entity):
    _table_ = 'bundles'

    id = PrimaryKey(int, auto=True)
    created_at = Optional(datetime.datetime)
    name = Optional(str)
    amount = Optional(int)
    description = Optional(str)
    duration = Optional(int)