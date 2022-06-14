import datetime

from pydantic import BaseModel


class CustomersPd(BaseModel):
    id: int | None
    created_at: datetime.datetime | None
    token: str | None
    firstname:str | None
    lastname: str | None
    phone: str | None
    email: str | None
    password: str | None
    picture: str | None
    note: str | None
    order_id: int | None
    promo_code: str | None

    class Config:
        orm_mode = True