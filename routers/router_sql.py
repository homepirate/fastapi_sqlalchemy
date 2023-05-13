from fastapi import APIRouter, Request, Depends, Body
from fastapi.responses import JSONResponse
from sqlalchemy import select, delete, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import with_polymorphic

from database import get_async_session
from models import User, Status, Company, Address, Realtor, Owner
from starlette.templating import Jinja2Templates


router_sql = APIRouter(
    prefix='/sql',
    tags=["Sql"]
)

templates = Jinja2Templates(directory="templates")


@router_sql.put("/email-change-{uid}")
async def change_email(uid:int, email: str, session=Depends(get_async_session)):
    stmt = text('UPDATE "user" SET email=:email WHERE id=:id')
    data = {"id":uid, "email":email}
    await session.execute(stmt, params=data)
    await session.commit()

    stmt = text('SELECT "user" WHERE id:id')
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
    return resp

