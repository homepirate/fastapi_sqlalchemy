from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from models import Realestate, Address, User
from schemas import ReModel

from routers.router import router_api

app = FastAPI()


app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")

app.include_router(router_api)


@app.get("/sql")
def get_sql_page(request: Request):
    return templates.TemplateResponse(
        "sql.html",
        {
            "request": request,
        },
        status_code=200
    )


@app.get("/orm")
def get_orm_page(request: Request):
    return templates.TemplateResponse(
        "orm.html",
        {
            "request": request,
        },
        status_code=200
    )
