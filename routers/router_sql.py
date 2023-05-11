from fastapi import APIRouter, Request, Depends, Body
from fastapi.responses import JSONResponse
from sqlalchemy import select
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
