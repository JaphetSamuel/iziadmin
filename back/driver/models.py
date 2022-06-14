import datetime

from pony.orm import Optional, Required, PrimaryKey, db_session
from config.db import db
from config.minio_conf import client
import os
from package.models import Package
from package.schemas import PackagePd
from typing import List



class Drivers(db.Entity):
    id = PrimaryKey(int)
    token = Required(str)
    created_at = Optional(datetime.datetime)
    firstname= Optional(str)
    lastname= Optional(str)
    phone = Optional(str)
    email = Optional(str)
    password = Optional(str)
    picture = Optional(str)
    is_online = Optional(bool)
    is_enabled = Optional(bool)
    car_brand = Optional(str)
    car_model = Optional(str)
    immatriculation = Optional(str)
    note = Optional(str)
    order_id = Optional(int)
    amount = Optional (int)
    car_licence = Optional(str)

    @property
    def get_picture(self) -> Optional(str):
        try:
            result = client.get_presigned_url(method="GET",bucket_name="picture",
                                              object_name=self.picture,)
            print(result)
            return result
        except Exception as e:
            print(e)\

    @property
    def get_licence(self) -> Optional(str):
        try:
            result = client.get_presigned_url(method="GET",bucket_name="picture",
                                              object_name=self.car_licence,)
            print(result)
            return result
        except Exception as e:
            print(e)


class Subscription(db.Entity):
    _table_ = "subscriptions"
    id = PrimaryKey(int)
    created_at = Optional(datetime.datetime)
    bundle_id = Optional(int)
    driver_id = Optional(int)
    amount = Optional(int)
    discount = Optional(int)
    start_at = Optional(datetime.datetime)
    end_at = Optional(datetime.datetime)
    reference = Optional(str)

    @property
    def is_actif(self):
        if self.end_at > datetime.datetime.now() and  self.start_at < datetime.datetime.now() :
            return True
        return False

    @property
    def bundle(self) -> PackagePd:
        with db_session:
            package = Package[self.bundle_id]
        return PackagePd.from_orm(package)