from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    title: str
    verified: Optional[bool] = False
    yearsw: int = None
    companyname: str = None
    yearsw: int = None
    website: Optional[str] = None
    statusid: int
    login: str
    page: int
    name: str
    surname: str
    phonenumber: int
    email: str
    password: str
    # is_active: Optional[bool] = True
    # is_superuser: Optional[bool] = False
    # is_verified: Optional[bool] = False
