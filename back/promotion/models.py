from pony.orm import Required, PrimaryKey, Optional
from config.db import db
import datetime


class Promos(db.Entity):
    _table_ = "promos"
    id = PrimaryKey(int)
    created_at = Optional(datetime.datetime)
    discount = Required(int)
    code = Required(str)
    start_at =Optional(datetime.datetime)
    end_at = Optional(datetime.datetime)

    @property
    def isActif(self):
        return self.end_at > datetime.datetime.now() and self.start_at < datetime.datetime.now()