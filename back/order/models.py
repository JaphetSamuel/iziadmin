from typing import Type

from config.db import db
from pony.orm import PrimaryKey, Required, Optional, db_session
from datetime import datetime
from driver.schemas import DriverPd
from customer.schemas import CustomersPd
from driver.models import Drivers
from customer.models import Customers


class Orders(db.Entity):
    id = PrimaryKey(int)
    created_at = Optional(datetime)
    customer_id = Required(int)
    driver_id = Optional(int)
    types = Optional(str, column="type")
    price = Optional(int)

    proposals = Optional(str)
    promo_code =Optional(str)
    promo_discount = Optional(int)
    from_name= Optional(str)
    from_latitude = Optional(float)
    from_longitude = Optional(float)
    to_name= Optional(str)
    to_latitude = Optional(float)
    to_longitude = Optional(float)
    duration = Optional(float)
    distance =Optional(float)
    path = Optional(bytes)
    status = Optional(str)
    customer_cancel_al = Optional(datetime)
    driver_take_at = Optional(datetime)
    driver_arrive_at = Optional(datetime)
    driver_start_at = Optional(datetime)
    driver_end_at = Optional(datetime)
    driver_review = Optional(int)
    customer_review = Optional(int)


    def after_insert(self):
        with db_session:
            driver = Drivers[self.driver_id]
        self.get_driver= DriverPd.from_orm(driver)

    @property
    def get_customer(self):
        customer = Customers.get(self.customer_id)
        return CustomersPd.from_orm(customer)

