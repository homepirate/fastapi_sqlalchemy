from sqlalchemy import select, insert
from sqlalchemy.orm import with_polymorphic

from models import User, Status, Owner, Realtor, Company, Realestate, Address

from routers.router_orm import create_user
import asyncio


async def add_users():
   lst = [{
        "title": "owner",
        "verified": False,
        "yearsw": "1986",
        "companyname": "string",
        "website": "string",
        "statusid": 0,
        "login": "EVG1",
        "page": 0,
        "name": "Evgeniy",
        "surname": "Loginov",
        "phonenumber": 0,
        "email": "evg1@example.com",
        "password": "pass1313rsf"
      },
   ]

