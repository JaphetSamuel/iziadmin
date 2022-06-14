from typing import List

from fastapi import APIRouter, Body, HTTPException
from package.schemas import PackagePd
from package.models import Package
from pony.orm import db_session
from pony.orm.core import ObjectNotFound
from fastapi.responses import Response

router = APIRouter(prefix="/package", tags=["package"])

@router.post("/create", response_model=PackagePd)
async def create_package(package:PackagePd = Body()):
    try:
        with db_session:
            package_db = Package(**package.dict(exclude_unset=True))
        return Response(status_code=200)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="erreur lors de la creation")

@router.patch("/{package_id}", response_model=PackagePd)
async def update_package(package_id:int, package:PackagePd = Body()):
    try:
        with db_session:
            package_db = Package[package_id]
            package_db.set(**package.dict(exclude_unset=True))
        return package_db
    except ObjectNotFound as e:
        raise  HTTPException(status_code=404, detail=str(e))

@router.delete("/delete/{package_id}")
async def delete_package(package_id:int):
    try:
        with db_session:
            Package[package_id].delete()
        return  Response(status_code=200)
    except ObjectNotFound as e:
        raise  HTTPException(status_code=404, detail= str(e))

@router.get("/{id}", response_model=PackagePd)
async def get_package_by_id(id:int):
    try:
        with db_session:
            package = Package[id]
        return  PackagePd.from_orm(package)
    except ObjectNotFound as e:
        raise  HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=List[PackagePd])
async def get_all_package():
    with db_session:
        packages = Package.select()
    return [PackagePd.from_orm(package) for package in packages]

