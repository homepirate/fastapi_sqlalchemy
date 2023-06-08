from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    title: str
    verified: Optional[bool] = False
    yearsw: int = None
    companyname: str = None
    yearsw: str = None
    website: Optional[str] = None
    statusid: int
    login: str
    page: int
    name: str = Field(..., max_length=10)
    surname: str = Field(..., max_length=10)
    phonenumber: int
    email: EmailStr
    password: str
    # is_active: Optional[bool] = True
    # is_superuser: Optional[bool] = False
    # is_verified: Optional[bool] = False
