import datetime

from pony.orm import Required, Optional, Set, PrimaryKey

from config.db import db


class Customers(db.Entity):
    id = PrimaryKey(int)
    created_at = Optional(datetime.datetime)
    token = Optional(str)
    firstname = Optional(str)
    lastname = Optional(str)
    phone = Optional(str)
    email = Optional(str)
    password = Optional(str)
    picture = Optional(str)
    note = Optional(float)
    order_id = Optional(int)
    promo_code = Optional(str)
