from pydantic import BaseModel
import datetime
from typing import Optional, Union
from package.schemas import PackagePd



class DriverPd(BaseModel):
    id: int
    token: str
    created_at: datetime.datetime
    firstname: str
    lastname: str
    phone: str
    email: str
    password: str
    is_online: bool
    is_enabled: bool
    car_brand: str
    car_model: str
    immatriculation: Optional[str]
    note: Optional[float]
    order_id: Optional[int]
    amount: Optional[int]
    get_licence: Optional[str]
    get_picture : Optional[str]

    class Config:
        orm_mode = True

class SubscriptionPd(BaseModel):
    id : Optional[int]
    created_at : Optional[datetime.datetime]
    bundle_id : Optional[int]
    driver_id : Optional[int]
    amount : Optional[int]
    discount : Optional[int]
    start_at : Optional[datetime.datetime]
    end_at : Optional[datetime.datetime]
    reference :Optional[str]
    is_actif: bool
    bundle: Optional[PackagePd]

    class Config:
        orm_mode = True