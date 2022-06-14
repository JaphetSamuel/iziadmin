from fastapi import Request, Header, HTTPException, Cookie
from auth.schemas import AdminPd
from auth.models import Admin
from pony.orm import db_session
from pony.orm.core import ObjectNotFound


async def check_auth_token(request: Request):
    if "z-token" in request.cookies:
        token = request.cookies["z-token"]
        with db_session:
            try:
                print("user search with token:", token)
                user = Admin.get(token=token)
                print("user found:", user)
                return AdminPd.from_orm(user)
            except ObjectNotFound as e:
                raise HTTPException(status_code=403, detail=str(e))
    else:
        raise HTTPException(status_code=403, detail="token introuvable")
