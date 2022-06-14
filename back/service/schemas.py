from pydantic import BaseModel
from typing import Optional


class ServicePd(BaseModel):

    id :Optional[int]
    name : Optional[str]
    categorie_id : Optional[str]
    description : Optional[str]
    base: Optional[int]
    per_meter : Optional[int]
    per_drive_time : Optional[int]
    per_waiting_time: Optional[int]
    payment: Optional[str]

    class Config:
        orm_mode = True