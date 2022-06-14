from fastapi import APIRouter, Request , Body, HTTPException, Depends, Response
from auth.schemas import AdminPd
from auth.models import Admin
from auth.utils import check_auth_token
from pony.orm import db_session, core

router = APIRouter(prefix="/auth", tags=["auth"])

routerApi = APIRouter(prefix="/user", tags=["auth","user"])



@router.post("/create", response_model=AdminPd, )
async def create_user(user:AdminPd = Body()):
    with db_session:
        user = Admin(**user.dict(exclude_unset=True))
    return Response(status_code=200)

@router.patch("/update/{id}", dependencies=[Depends(check_auth_token)])
async def update_user(id:int, user:AdminPd = Body()):
    try:
        with db_session:
            user_db =Admin[id]
            user_db.set(**user.dict(exclude_unset=True))
    except core.ObjectNotFound as e:
        print(e)
        raise HTTPException(status_code=404,detail="user introuvable")

@router.delete("/delete/{id}")
async def delete_user(id:int, user=Depends(check_auth_token)):
    with db_session:
        Admin[id].delete()
    return Response(status_code=200)

@router.get("/", dependencies=[Depends(check_auth_token)])
async def get_all_users():
    with db_session:
        users = Admin.select()
    return [AdminPd.from_orm(user) for user in users]

@router.get("/{id}")
async def get_user(id:int):
    with db_session:
        user = Admin[id]
    return AdminPd.from_orm(user)

@router.post("/login")
async def user_login(reponse:Response,username: str = Body(), password:str = Body()):
    try:
        with db_session:
            user = Admin.get(username=username, password=password)
            print(user)
            if user is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            reponse.set_cookie("z-token", user.token)
        return AdminPd.from_orm(user)
    except core.ObjectNotFound as e:
        print(e)
        raise HTTPException(403, "username ou mot de passe i,correctct")

@router.post("/logout")
async  def user_logout(reponse:Response):
    reponse.headers["z-token"] = ""
    return Response(status_code=200)

