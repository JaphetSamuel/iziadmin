from typing import Optional, List

import pydantic.error_wrappers
from fastapi import APIRouter, Query, Body, HTTPException
from order.schemas import OrderPd
from order.models import Orders
from pony.orm import db_session
from pony.orm.core import ObjectNotFound, desc

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/create", response_model=OrderPd)
async  def create_order(order:OrderPd):
    with db_session:
        order_db = Orders(**order.dict())
        result = OrderPd.from_orm(order_db)
    return result

@router.get("/", response_model=list[OrderPd])
async def get_all_Orders(table = Query(False)):
    try:
        with db_session:

            orders = Orders.select()

            if table:
                orders = Orders.select()

            result = [OrderPd.from_orm(order) for order in orders]
        return result

    except pydantic.error_wrappers.ValidationError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}", response_model=OrderPd)
async def get_order_by_id(id:int):

    with db_session:

        order = Orders.get(id=id)
        result = OrderPd.from_orm(order)

    return result

@router.get("/driver_commande/{driver_id}", response_model=List[OrderPd])
async def get_order_by_driver_id(driver_id:int ):
    try:
        with db_session:
            orders = Orders.select(driver_id=driver_id).order_by(desc(Orders.created_at))
        return[OrderPd.from_orm(order) for order in orders]
    except ObjectNotFound as e:
        HTTPException(status_code=404, detail=str(e))
