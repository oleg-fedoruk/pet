from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


class File(BaseModel):
    id: Union[str, UUID]
    title: str
    file_path: str
    owner_id: int


class FileCreate(File):
    pass


class FileOut(File):
    created_at: Optional[datetime]
