from random import random

from fastapi import APIRouter, Request, Depends, Body, Query
from fastapi.responses import JSONResponse
from sqlalchemy import select, delete, func, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import with_polymorphic

from database import get_async_session
from models import User, Status, Company, Address, Realtor, Owner, Realestate
from schemas import UserCreate
from starlette.templating import Jinja2Templates


router_orm = APIRouter(
    prefix='/orm',
    tags=["Orm"]
)

templates = Jinja2Templates(directory="templates")


@router_orm.post("/create-user")
async def create_user(user_dict: UserCreate, session=Depends(get_async_session)):
    user_dict = dict(user_dict)
    title = user_dict.pop("title")
    if title == "owner":
        user_dict.pop("companyname")
        user_dict.pop("website")
        user_dict.pop("yearsw")
        verified = user_dict.pop("verified")
        c = Owner(title=title, verified=verified)
        await session.add(c)
        await session.commit()
        await session.refresh(c)
        stid = c.id
    elif title == "realtor":
        user_dict.pop("companyname")
        user_dict.pop("website")
        user_dict.pop("verified")
        yearsw = user_dict.pop("yearsw")
        c = Realtor(title=title, yearsw=yearsw)
        await session.add(c)
        await session.commit()
        await session.refresh(c)
        stid = c.id
    else:
        user_dict.pop("verified")
        companyname = user_dict.pop("companyname")
        website = user_dict.pop("website")
        yearsw = user_dict.pop("yearsw")
        c = Company(title=title, companyname=companyname, website=website, yearsw=yearsw)
        await session.add(c)
        await session.commit()
        await session.refresh(c)
        stid = c.id

    user_dict["statusid"] = stid
    user_dict["page"] = random.randint(10000, 99999)
    session.commit()

    statusid = user_dict.pop("statusid")
    page = user_dict.pop("page")
    login = user_dict.pop("login")
    password = user_dict.pop("password")
    name = user_dict.pop("name")
    surname = user_dict.pop("surname")
    email = user_dict.pop("email")
    phonenumber = user_dict.pop("phone_number")

    user = User(statusid=statusid, page=page, login=login, password=password, name=name,
                surname=surname, email=email, phonenumber=phonenumber)

    await session.add(user)
    await session.commit()


@router_orm.post("/user-ads-byname")
async def get_user_ads(name: str, session=Depends(get_async_session)):
    if "delete from" in name.lower() or "drop table" in name.lower():
        return "ERROR"
    q = select(User, Realestate).where(User.name == name).join(User.realestate)
    resp = await session.execute(q)
    resp = resp.all()
    data = [{"id": i[0].id, "name":i[0].name, "surname": i[0].surname,
             "email":i[0].email, "rename":i[1].name}for i in resp]
    return data


@router_orm.post("/ads-incity-order-price")
async def get_re_in_city_order_price(session=Depends(get_async_session)):
    q = select(Realestate, Address).join(Address, Realestate.addressid == Address.id).order_by(Realestate.price)
    resp = await session.execute(q)
    resp = resp.all()
    data = [{"name":i[0].name, "price":i[0].price, "square":i[0].square,
             "floor":i[0].floor, "apartamentnumber":i[0].apartamentnumber,
             "city":i[1].city, "district":i[1].district, "sreet":i[1].street,
             "housenumber":i[1].housenumber} for i in resp]
    return data


@router_orm.delete("/delete-user/{uid}")
# async def delete_user(uid: int = Query(..., regex=r"^\d+$"), session=Depends(get_async_session)):
async def delete_user(uid: int, session=Depends(get_async_session)):
    q = select(User).where(User.id == uid)
    user = await session.execute(q)
    user = user.scalars().one()
    stid = user.statusid
    await session.delete(user)

    q = select(Status).where(Status.id == stid)
    status = await session.execute(q)
    status = status.scalars().one()
    await session.delete(status)

    await session.commit()
    q = select(User)
    resp = await session.execute(q)
    resp = resp.all()
    data = [{"id":i[0].id, "name":i[0].name, "surname":i[0].surname, "email":i[0].email} for i in resp]
    return data


@router_orm.post("/all_users")
def get_all_users(session=Depends(get_async_session)):
    q = select(User, with_polymorphic(Status, [Owner, Realtor, Company])) \
        .join(with_polymorphic(Status, [Owner, Realtor, Company]), User.statusid == Status.id)

    resp = session.execute(q)
    resp = resp.scalars().all()

    data = [i for i in resp]

    return data


