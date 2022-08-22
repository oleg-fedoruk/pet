import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, select, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    age: Optional[int] = None
    images: List["Image"] = Relationship(back_populates="owner")
    result_files: List["ResultFile"] = Relationship(back_populates="owner")


class Image(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    title: str
    extension: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="images")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)


class ResultFile(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    title: str
    path: str
    source_id: int = Field(default=None, foreign_key="image.id")
    source: Image = Relationship(sa_relationship_kwargs={'uselist': False}, back_populates="result")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="images")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)


engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
    statement = select(User).where(User.username == "Spider-Boy")
    user = session.exec(statement).first()
    print(user)
