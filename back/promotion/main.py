from typing import List

from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import Response
from promotion.schemas import PromoPd
from promotion.models import Promos
from pony.orm import db_session
from pony.orm.core import ObjectNotFound

router = APIRouter(prefix="/promos", tags=["promos"])
#get create updadte getall

@router.post("/create")
async def create_promo(promo:PromoPd = Body()):
    with db_session:
        Promos(**promo.dict(exclude_unset=True))
    return  Response(status_code=200)


@router.get("/", response_model=List[PromoPd])
async def get_all_promo():
    with db_session :
        promos = Promos.select()
        result = [PromoPd.from_orm(p) for p in promos]
    return result


@router.get("/{id}", response_model=PromoPd)
async def get_promo_by_id(id:int):
    try:
        with db_session:
            promo = Promos[id]
        return PromoPd.from_orm(promo)
    except ObjectNotFound as e:
        print("objet non trouver")
        print(e)
        raise HTTPException(status_code=404,detail="pazs trouvé")
