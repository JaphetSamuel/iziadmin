from typing import List

from fastapi import APIRouter, HTTPException, Header, Body, Request
from pony.orm import db_session
from pony.orm.core import ObjectNotFound, desc
from driver.models import Drivers, Subscription
from driver.schemas import DriverPd, SubscriptionPd



router = APIRouter(prefix="/driver", tags=["drivers"])

async def okStatus(header:Header = Header()):
    Header()


@router.get("/", response_model=list[DriverPd])
async def getAll():
    drivers = Drivers.select()
    return [DriverPd.from_orm(driver) for driver in drivers]


@router.get("/{id}", response_model=DriverPd)
async def get(id:int):
    try:
        with db_session:
            driver = Drivers[id]
        return DriverPd.from_orm(driver)
    except ObjectNotFound :
        print("driver introuvable")
        raise HTTPException(status_code=404, detail="driver introuvable")



@router.get("/{token}", response_model=DriverPd)
async def get_by_token(token: str):
    driver = Drivers.get(token=token)
    return DriverPd.from_orm(driver)

@router.post("/enable")
async def set_enable(request:Request,enable:bool = Body(), driver_id:int=Body()):
    print(await request.body())
    print(enable)
    with db_session:
        driver = Drivers[driver_id]
        driver.is_enabled = enable
    return driver.is_enabled

@router.get("/deactivate", response_model=List[DriverPd])
async def getAllDeactivate():
    try:
        with db_session:
            drivers = Drivers.select(is_enabled=False)
            result = [DriverPd.from_orm(driver) for driver in drivers]
        return result
    except ObjectNotFound as e:
        print(e)
        raise HTTPException(status_code=404, detail="aucun driver désactivé trouvé")


##########################Transaction AKA subscriptions ##############################
@router.get("/subscription/", response_model=List[SubscriptionPd])
async def get_all_subscription():
    with db_session:
        list = Subscription.select()
    return [SubscriptionPd.from_orm(s) for s in list]

@router.get("/subscription/{id}")
async def get_subscriptions_by_id(id:int):
    try:
        with db_session:
            subscription = Subscription[id]
        return SubscriptionPd.from_orm(subscription)
    except ObjectNotFound as e:
        print(e)
        raise HTTPException(status_code=404, detail="oBjets introuvable")

@router.get("/getsubscriptionfor/{driver_id}")
async def get_subscription_by_driver_id(driver_id:int):
    try:
        with db_session:
            subscriptions = Subscription.select(driver_id=driver_id).order_by(desc(Subscription.created_at))
        return [SubscriptionPd.from_orm(subs) for subs in subscriptions]
    except Exception as e:
        print(e)
