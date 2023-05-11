from random import random

from fastapi import APIRouter, Request, Depends, Body
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import with_polymorphic

from database import get_async_session
from models import User, Status, Company, Address, Realtor, Owner, Realestate
from schemas import UserCreate
from starlette.templating import Jinja2Templates


router_orm= APIRouter(
    prefix='/orm',
    tags=["Orm"]
)

templates = Jinja2Templates(directory="templates")


@router_orm.post("create-user")
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


async def get_user_abs(name: str, session= Depends(get_async_session)):
    q = select(User, Realestate.name).where(User.name == name).join(Realestate, User.id == Realestate.userid)
    resp = await session.execute(q)
    resp = resp.all()

