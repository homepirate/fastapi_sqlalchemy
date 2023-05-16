from fastapi import APIRouter

from . import router_orm
from . import router_sql

router_api = APIRouter(
    prefix='/api',
    tags=["API"]
)

router_api.include_router(router_orm.router_orm)
router_api.include_router(router_sql.router_sql)
