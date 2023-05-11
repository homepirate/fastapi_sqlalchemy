from fastapi import APIRouter
from router_orm import router_orm
from router_sql import router_sql
from starlette.templating import Jinja2Templates


router_api = APIRouter(
    prefix='/api',
    tags=["API"]
)

router_api.include_router(router_orm)
router_api.include_router(router_sql)
