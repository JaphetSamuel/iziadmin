import datetime

from config.db import db
from pony.orm import Required, PrimaryKey, Optional
from driver.models import Drivers
from driver.schemas import DriverPd


class Wallet(db.Entity):
    _table_ = "wallets"
    id = PrimaryKey(int)
    created_at = Optional(datetime.datetime)
    amount = Required(float)
    types = Optional(str, column="type")
    user_id = Required(int)
    user_type = Optional(str)
    origin_id = Optional(str)
    origin_type = Optional(str)

    @property
    def getDriver(self):
        try:

            driver = Drivers[self.user_id]
            print(driver.id)
            result = DriverPd.from_orm(driver)
            return result
        except Exception as e:
            print(e)
