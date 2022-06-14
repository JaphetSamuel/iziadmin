from pydantic import BaseModel
from typing import Optional
import datetime

class PromoPd(BaseModel):
    id: int
    created_at: Optional[datetime.datetime]
    discount : Optional[int]
    code : Optional[str]
    start_at: Optional[datetime.datetime]
    end_at : Optional[datetime.datetime]
    isActif:Optional[bool]

    class Config:
        orm_mode = True