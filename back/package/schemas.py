import datetime

from pydantic import BaseModel
from typing import Optional


class PackagePd(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime.datetime]
    name: Optional[str]
    amount: Optional[str]
    description: Optional[str]
    duration: Optional[int]

    class Config:
        orm_mode = True
