from pydantic import BaseModel
from driver.schemas import DriverPd


class WalletPd(BaseModel):
    id: int
    amount: int
    types: str
    user_id: int
    user_type: str
    origin_id: str
    origin_type: str
    getDriver: DriverPd | None

    class Config:
        orm_mode = True