from pydantic import BaseModel
from typing import Optional


class AdminPd(BaseModel):
    id: Optional[int]
    username: str
    password: str
    token:Optional[str]
    role:Optional[str]

    class Config:
        orm_mode = True