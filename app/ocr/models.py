from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from app.core.models import TimestampModel, UUIDModel


class ImageBase(SQLModel):
    title: str
    extension: str


class Image(TimestampModel, ImageBase, UUIDModel, table=True):
    owner_id: Optional[int] = Field(default=None, foreign_key='user.id')


class ImageRead(ImageBase, UUIDModel):
    owner: Optional['UserRead'] = Relationship(back_populates="images")


class ResultFileBase(SQLModel):
    title: str
    path: str


class ResultFile(TimestampModel, ResultFileBase, UUIDModel, table=True):
    source_id: Optional[str] = Field(default=None, foreign_key="image.uuid")
    owner_id: Optional[int] = Field(default=None, foreign_key='user.id')


class ResultFileRead(ResultFileBase, UUIDModel):
    owner: Optional['UserRead'] = Relationship(back_populates="images")
    source: Optional[ImageRead] = Relationship(sa_relationship_kwargs={'uselist': False}, back_populates="result")
