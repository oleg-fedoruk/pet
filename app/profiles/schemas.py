from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None = None
    is_active: bool
    is_admin: bool


class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
