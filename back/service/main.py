from typing import List

from fastapi import APIRouter, Body, HTTPException, Request
from fastapi.responses import Response
from service.models import Service
from service.schemas import ServicePd
from pony.orm import db_session
from pony.orm.core import ObjectNotFound

router = APIRouter(prefix="/service", tags=["service"])

# creation - verification - modification


@router.post("/create")
async def create_service(service:ServicePd =Body()):
    try:
        with db_session:
            service_db = Service(**service.dict(exclude_unset=True))
        return Response(status_code=200)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=403, detail="Erreur lors de l'enregistrement")


@router.patch("/{service_id}")
async  def update_service(service_id:int, service:ServicePd = Body()):
    try:
        with db_session:
            service_db = Service[service_id]
            service_db.set(**service.dict(exclude_unset=True))
    except ObjectNotFound as ob:
        print(ob)
        raise HTTPException(status_code=404, detail="aucun enregistrement correspodant")

@router.get("/all", response_model=List[ServicePd])
async def get_all_service():
    with db_session:
        services = Service.select()
        result = [ServicePd.from_orm(s) for s in services]
    return result

@router.get("/{id}", response_model=ServicePd)
async def get_serice_by_id(id:int):
    try:
        with db_session:
            service = Service[id]
        return ServicePd.from_orm(service)
    except ObjectNotFound as e:
        raise HTTPException(status_code=404, detail="service introuvable")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

@router.delete("/delete/")
async def delete_service(service_id:int):
    try:
        with db_session:
            Service[service_id].delete()
        return Response(status_code=200)
    except ObjectNotFound:
        raise HTTPException(status_code=404, detail="service introuvable")
    except Exception as e:
        print(e)
