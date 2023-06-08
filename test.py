from sqlalchemy import select, insert
from sqlalchemy.orm import with_polymorphic

from models import User, Status, Owner, Realtor, Company, Realestate, Address

q = User(statusid=1, page=1, login='fdfd', password='fddf', name='dfdf',
                surname='fddf', email='dfdf@rr.ru', phonenumber=1113)
print(insert(User))