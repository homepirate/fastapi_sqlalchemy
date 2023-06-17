import time

from sqlalchemy import select, insert
from sqlalchemy.orm import with_polymorphic

from models import User, Status, Owner, Realtor, Company, Realestate, Address

from routers.router_orm import create_user
import asyncio

import requests


def test_add_users():
    headers = {'accept': 'application/json',
               'Content-Type': 'application/json'}
    lst = [{
        "title": "owner",
        "verified": "false",
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
             "verified": "false",
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
             "verified": "true",
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
             "verified": "false",
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
             "verified": "false",
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
             "verified": "true",
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
             "verified": "false",
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
             "verified": "false",
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
    for i in lst:
        r = requests.post('http://localhost:8000/api/orm/create-user', headers=headers, json=i)
        print(r)


def test_add_address():
   lst = [
      Address(city="Moscow", district="Perovo", street="Bratskaya", housenumber="44"),
     Address(city="Moscow", district="Perovo", street="Bratskaya", housenumber="3"),
     Address(city="Moscow", district="Perovo", street="Bratskaya", housenumber="46"),
     Address(city="Moscow", district="Perovo", street="Bratskaya", housenumber="10"),
     Address(city="Moscow", district="Perovo", street="Lazo", housenumber="3"),
     Address(city="Moscow", district="Perovo", street="Lazo", housenumber="3"),
     Address(city="Moscow", district="Perovo", street="Lazo", housenumber="5"),
     Address(city="Moscow", district="Perovo", street="Lazo", housenumber="7"),
     Address(city="Moscow", district="Donskoi", street="Leninsky Prospekt", housenumber="29"),
     Address(city="Moscow", district="Donskoi", street="Leninsky Prospekt", housenumber="21"),
     Address(city="Moscow", district="Donskoi", street="Stasovoy", housenumber="1"),
     Address(city="Moscow", district="Donskoi", street="Stasovoy", housenumber="7"),
     Address(city="Moscow", district="Danilovsky", street="3-y Paveletskiy proyezd", housenumber="3"),
     Address(city="Moscow", district="Zyuzino", street="Malaya Yushunskaya ulitsa", housenumber="6"),
     ]


def test_add_flats():
   lst = [
      Realestate(userid=1, addressid=2, name="Новая квартира", numberofrooms=3, price=11000000, floor=1, square=60, yearofconstruction=2022, numberofbathrooms=1, сeilingheight=2.3, balcony=1, numberofelevators=3, apartamentnumber=3),
     Realestate(userid=4, addressid=2, name="Квартира в Перово", numberofrooms=3, price=13000000, floor=3, square=78, yearofconstruction=2017, numberofbathrooms=1, сeilingheight=2.5, balcony=1, numberofelevators=2, apartamentnumber=23),
     Realestate(userid=2, addressid=9, name="Квартира", numberofrooms=3, price=11000000, floor=23, square=100, yearofconstruction=2012, numberofbathrooms=1, сeilingheight=2.1, balcony=1, numberofelevators=4, apartamentnumber=70),
     Realestate(userid=7, addressid=13, name="Продается квартира", numberofrooms=3, price=11000000, floor=13, square=79, yearofconstruction=1956, numberofbathrooms=1, сeilingheight=3, balcony=1, numberofelevators=2, apartamentnumber=60),
     Realestate(userid=4, addressid=13, name="Хорошая квартира", numberofrooms=3, price=23400000, floor=3, square=130, yearofconstruction=1977, numberofbathrooms=1, сeilingheight=2.7, balcony=1, numberofelevators=2, apartamentnumber=12),
     Realestate(userid=3, addressid=14, name="Новая квартира", numberofrooms=3, price=12000000, floor=2, square=132, yearofconstruction=1999, numberofbathrooms=1, сeilingheight=2.9, balcony=1, numberofelevators=2, apartamentnumber=5),
     Realestate(userid=5, addressid=9, name="Квартира в Москве", numberofrooms=6, price=17000000, floor=15, square=90, yearofconstruction=2023, numberofbathrooms=1, сeilingheight=2.6, balcony=1, numberofelevators=1, apartamentnumber=77),
     Realestate(userid=4, addressid=11, name="Большая двухкомнатная квартира", numberofrooms=2, price=13500000, floor=5, square=88, yearofconstruction=1981, numberofbathrooms=1, сeilingheight=2.2, balcony=1, numberofelevators=2, apartamentnumber=18),
     Realestate(userid=8, addressid=1, name="Квартира трехкомнатная", numberofrooms=3, price=9000000, floor=5, square=66, yearofconstruction=1966, numberofbathrooms=1, сeilingheight=2.2, balcony=1, numberofelevators=1, apartamentnumber=15),
     Realestate(userid=8, addressid=7, name="Далеко не новая квартира", numberofrooms=5, price=88800000, floor=1, square=155, yearofconstruction=1811, numberofbathrooms=1, сeilingheight=3.5, balcony=2, apartamentnumber=1),
     Realestate(userid=6, addressid=3, name="Новая квартира", numberofrooms=3, price=10000000, floor=5, square=49, yearofconstruction=2022, numberofbathrooms=1, сeilingheight=2, balcony=1, numberofelevators=3, apartamentnumber=19),

   ]


if __name__ == '__main__':
    test_add_users()
    