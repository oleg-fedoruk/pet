import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, select, Relationship


class Image(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    title: str
    extension: str
    owner_id: Optional[int] = Field(default=None, foreign_key='userbase.id')
    owner: Optional['User'] = Relationship(back_populates="images")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)


class ResultFile(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    title: str
    path: str
    source_id: Optional[int] = Field(default=None, foreign_key="image.id")
    source: Optional[Image] = Relationship(sa_relationship_kwargs={'uselist': False}, back_populates="result")
    owner_id: Optional[int] = Field(default=None, foreign_key='userbase.id')
    owner: Optional['User'] = Relationship(back_populates="images")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)


# with Session(engine) as session:
#     statement = select(User).where(User.username == "Spider-Boy")
#     user = session.exec(statement).first()
#     print(user)
