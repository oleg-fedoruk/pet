from datetime import datetime

from pydantic import BaseModel


class File(BaseModel):
    title: str
    file_path: str
    created_at: datetime


class FileCreate(File):
    pass


class FileOut(File):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
