from sqlalchemy import select, insert
from sqlalchemy.orm import with_polymorphic

from models import User, Status, Owner, Realtor, Company, Realestate, Address

from routers.router_orm import create_user
import asyncio


async def atest_dd_users():
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
        "phonenumber": 8800553535,
        "email": "evg1@example.com",
        "password": "pass1313rsf"
      },
        {
             "title": "realtor",
             "verified": False,
             "yearsw": "1995",
             "companyname": "string",
             "website": "string",
             "statusid": 0,
             "login": "realt31",
             "page": 0,
             "name": "Viktor",
             "surname": "Polikov",
             "phonenumber": 88937651312,
             "email": "vp1@ramb.com",
             "password": "dfd1341"
        },
        {
             "title": "owner",
             "verified": True,
             "yearsw": "1986",
             "companyname": "string",
             "website": "string",
             "statusid": 0,
             "login": "topboy",
             "page": 0,
             "name": "Evgeniy",
             "surname": "Nikolaev",
             "phonenumber": 81347653451,
             "email": "evgnik@example.com",
             "password": "123456"
        },
        {
             "title": "company",
             "verified": False,
             "yearsw": "1996",
             "companyname": "cian",
             "website": "cian.ru",
             "statusid": 0,
             "login": "cian_login",
             "page": 0,
             "name": "Andrei",
             "surname": "Andreev",
             "phonenumber": 89996663322,
             "email": "and_cian_work@ci.an",
             "password": "adsf134fgg"
        },
        {
             "title": "realtor",
             "verified": False,
             "yearsw": "1953",
             "companyname": "string",
             "website": "string",
             "statusid": 0,
             "login": "realtor_pavel",
             "page": 0,
             "name": "Pavel",
             "surname": "Klimov",
             "phonenumber": 86574441234,
             "email": "pk@example.com",
             "password": "pk_pass_24_06_1935"
        },
        {
             "title": "owner",
             "verified": True,
             "yearsw": "string",
             "companyname": "string",
             "website": "string",
             "statusid": 0,
             "login": "KylieJenner",
             "page": 0,
             "name": "Kylie",
             "surname": "Jenner",
             "phonenumber": 87774442132,
             "email": "kyliejenner@inst.com",
             "password": "secret_pass_kylie!"
        },
        {
             "title": "owner",
             "verified": False,
             "yearsw": "1953",
             "companyname": "string",
             "website": "string",
             "statusid": 0,
             "login": "realtor_pavel",
             "page": 0,
             "name": "Kendall",
             "surname": "Jenner",
             "phonenumber": 85666561378,
             "email": "kendallJenn@example.com",
             "password": "pk_pass_24_06_1935"
        },
        {
             "title": "company",
             "verified": False,
             "yearsw": "2013",
             "companyname": "sale_flats",
             "website": "sale-flats.ru",
             "statusid": 0,
             "login": "sale_flats_admin",
             "page": 0,
             "name": "Ivan",
             "surname": "Petrov",
             "phonenumber": 87663563358,
             "email": "saleflats@info.ru",
             "password": "admin12345!"
        },
   ]

