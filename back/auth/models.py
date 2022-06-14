from config.db import db
from pony.orm import PrimaryKey, Required, Optional
from uuid import uuid4

def get_uuid() -> str :
    return str(uuid4())

class Admin(db.Entity):
    _table_ = "admin"

    id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(str)
    token = Required(str,default=get_uuid)
    role = Optional(str)