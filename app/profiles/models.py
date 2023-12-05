from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, Integer, DateTime, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.database import Base, get_session


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'users_profiles'
    __tableargs__ = {
        'comment': 'Пользователи'
    }
    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='Идентификатор')
    username = Column(String, unique=True, index=True, comment='Никнейм пользователя')
    email = Column(String, unique=True, index=True, comment='Email пользователя')
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True, comment='Активен')
    is_admin = Column(Boolean, default=False, comment='Администратор')
    created_at = Column(DateTime(timezone=True), comment='Дата и время создания', server_default=func.now())

    images = relationship('ExternalFile', back_populates='owner', lazy='subquery')
    docs = relationship('ResultFile', back_populates='owner', lazy='subquery')

    def __repr__(self):
        return f'{self.username} uuid: {self.id}'


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)
