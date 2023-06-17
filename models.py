import asyncio

from database import Base, engine

from sqlalchemy import INTEGER, String, Column, FLOAT, ForeignKey, BOOLEAN, BigInteger
from sqlalchemy.orm import relationship, validates
from fastapi_users.db import SQLAlchemyBaseUserTable

import re
class Status(Base):
    __tablename__ = 'status'

    id = Column(INTEGER, primary_key=True)
    title = Column(String)
    rating = Column(INTEGER, nullable=True)
    user = relationship("User", back_populates="status", uselist=False, cascade="all, delete",
        passive_deletes=True)

    __mapper_args__ = {
        'polymorphic_identity': 'status',
        # 'concrete': True
        'polymorphic_on': 'title'

    }

    def __repr__(self):
        return str(self.__dict__)


class Company(Status):
    __tablename__ = "company"

    statusid = Column(INTEGER, ForeignKey("status.id", ondelete="CASCADE"), primary_key=True)
    companyname = Column(String, nullable=False)
    website = Column(String, nullable=True)
    yearsw = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'company',
        # 'concrete': True
    }


class Realtor(Status):
    __tablename__ = "realtor"

    statusid = Column(INTEGER, ForeignKey("status.id", ondelete="CASCADE"), primary_key=True)
    yearsw = Column(String, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'realtor'
    }

    def __repr__(self):
        return str(self.__dict__)


class Owner(Status):
    __tablename__ = "owner"

    statusid = Column(INTEGER, ForeignKey("status.id", ondelete="CASCADE"), primary_key=True)
    verified = Column(BOOLEAN, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'owner'
    }

    def __repr__(self):
        return str(self.__dict__)


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True)
    statusid = Column(INTEGER, ForeignKey("status.id", ondelete="CASCADE"))
    page = Column(INTEGER, nullable=False)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phonenumber = Column(BigInteger, nullable=False)
    status = relationship("Status", back_populates="user", uselist=False)
    realestate = relationship("Realestate", back_populates="user", cascade="all, delete",
        passive_deletes=True)

    @validates("email")
    def validate_email(self, key, address):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, address) is not None:
            return address
        else:
            raise ValueError("failed simple email validation")
        # if "@" not in address:
        #     raise ValueError("failed simple email validation")
        # return address

    def __repr__(self):
        return str(self.__dict__)


class Address(Base):
    __tablename__ = "address"

    id = Column(INTEGER, primary_key=True)
    city = Column(String, nullable=False)
    district = Column(String, nullable=True)
    street = Column(String, nullable=False)
    housenumber = Column(String, nullable=False)
    realestate = relationship("Realestate", back_populates="address", cascade="all, delete",
        passive_deletes=True)


class Realestate(Base):
    __tablename__ = "realestate"

    id = Column(INTEGER, primary_key=True)
    userid = Column(INTEGER, ForeignKey("user.id", ondelete="CASCADE"))
    addressid = Column(INTEGER, ForeignKey("address.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    numberofrooms = Column(INTEGER, nullable=False)
    price = Column(BigInteger, nullable=False)
    floor = Column(INTEGER, nullable=True)
    square = Column(INTEGER, nullable=False)
    yearofconstruction = Column(INTEGER, nullable=False)
    numberofbathrooms = Column(INTEGER, nullable=False)
    сeilingheight = Column(FLOAT, nullable=False)
    balcony = Column(INTEGER, nullable=True)
    numberofelevators = Column(INTEGER, nullable=True)
    apartamentnumber = Column(INTEGER, nullable=False)
    user = relationship("User", back_populates="realestate")
    address = relationship("Address", back_populates="realestate", uselist=False)


# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
# asyncio.run(init_models())