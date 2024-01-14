from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column

from app.core.database import Base


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
