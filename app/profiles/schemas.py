from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool
    is_admin: bool


class UserInput(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True
