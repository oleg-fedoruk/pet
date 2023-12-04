import datetime
from typing import Optional

from fastapi_users import schemas
from fastapi_users.schemas import CreateUpdateDictModel
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    username: Optional[str]
    is_active: bool
    is_admin: bool
    created_at: datetime.datetime


class UserCreate(schemas.BaseUserCreate):
    username: str
    is_admin: bool


class UserRegister(CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    is_admin: bool


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
