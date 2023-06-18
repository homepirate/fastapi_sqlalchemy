from fastapi import APIRouter, Request, Depends, Body, Query
from sqlalchemy import select, delete, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import with_polymorphic

from pydantic import EmailStr
from database import get_async_session
from models import User, Status, Company, Address, Realtor, Owner
from starlette.templating import Jinja2Templates

import re

router_sql = APIRouter(
    prefix='/sql',
    tags=["Sql"]
)

templates = Jinja2Templates(directory="templates")


@router_sql.put("/email-change/{uid}")
# async def change_email(uid: int = Query(..., regex=r"^\d+$"), email: EmailStr, session=Depends(get_async_session)):
async def change_email(uid: int, email: EmailStr, session=Depends(get_async_session)):

    print(uid, type(uid), email, type(email))

    stmt = text("""UPDATE "user" SET email=:email WHERE id=:id""")
    data = {"id": uid, "email": email}

    await session.execute(stmt, params=data)
    await session.commit()
    

    stmt = text("""SELECT * FROM "user" WHERE id=:id""")
    resp = await session.execute(stmt, params={"id":uid})
    resp = resp.first()
    
    data = {"id":resp.id, "name":resp.name, "email":resp.email}
    return data


@router_sql.post("/count-indistrict")
async def count_in_district(session=Depends(get_async_session)):
    stmt = text("""SELECT address.district, COUNT(district) FROM 
            realestate JOIN address ON realestate.addressid=address.id GROUP BY district""")
    resp = await session.execute(stmt)
    resp = resp.all()
    data = [{"district":i[0], "count":i[1]}for i in resp]
    return data


@router_sql.post("/user-with-large-flats-in-city")
async def get_users_with_large_flats_incity(square: int, city: str, session=Depends(get_async_session)):
    stmt = text("""SELECT * FROM "user" us JOIN status st ON us.statusid=st.id WHERE EXISTS (SELECT re.name, re.square FROM realestate re JOIN address ad on re.addressid=ad.id WHERE re.userid=us.id AND re.square > :square and ad.city=:city)""")

    resp = await session.execute(stmt, params={"city": city, "square":square})
    resp = resp.all()
    print(resp)

    data = [{"id":i.id, "name":i.name, "surname":i.surname, "email":i.email, "title": i.title} for i in resp]
    return data    

