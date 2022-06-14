from pydantic import BaseModel
from typing import Optional
from driver.schemas import DriverPd
import datetime


class OrderPd(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime.datetime]
    customer_id: Optional[int]
    driver_id :  Optional[int]
    types :  Optional[str]
    price :  Optional[int]
    taxe_rate :  Optional[int]
    proposals :  Optional[str]
    promo_code : Optional[str]
    promo_discount :  Optional[int]
    from_name:  Optional[str]
    from_latitude :  Optional[float]
    from_longitude :  Optional[float]
    to_name:  Optional[str]
    to_latitude :  Optional[float]
    to_longitude :  Optional[float]
    duration :  Optional[float]
    distance : Optional[float]
    path :  Optional[bytes]
    status :  Optional[str]
    customer_cancel_al :  Optional[datetime.datetime]
    driver_take_at: Optional[datetime.datetime]
    driver_arrive_at: Optional[datetime.datetime]
    driver_start_at: Optional[datetime.datetime]
    driver_end_at: Optional[datetime.datetime]
    driver_review: Optional[int]
    customer_review: Optional[int]
    get_driver:Optional[DriverPd]

    class Config:
        orm_mode = True
