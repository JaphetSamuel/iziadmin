from config.db import db
from pony.orm import PrimaryKey, Required, Optional

class Service(db.Entity):
    _table_ = "services"

    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    categorie_id = Optional(str)
    description = Optional(str)
    base = Required(int, default=500)
    per_meter = Required(int, default=65)
    per_drive_time = Required(int, default=50)
    per_waiting_time = Optional(int)
    payment = Optional(str)
