import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    age: Optional[int] = None


class Image(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    title: str
    extension: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="images")


class ResultFile(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    title: str
    path: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="images")


engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
    statement = select(User).where(User.username == "Spider-Boy")
    user = session.exec(statement).first()
    print(user)
