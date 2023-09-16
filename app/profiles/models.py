from sqlalchemy import Column, String, Boolean, Integer, DateTime
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = 'users_profiles'
    __tableargs__ = {
        'comment': 'Пользователи'
    }

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, comment='Идентификатор')
    username = Column(String, unique=True, index=True, comment='Никнейм пользователя')
    email = Column(String, unique=True, index=True, comment='Email пользователя')
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True, comment='Активен')
    is_admin = Column(Boolean, default=False, comment='Администратор')
    created_at = Column(DateTime, comment='Дата и время создания')

    images = relationship('ExternalFile', back_populates='owner', lazy='subquery')
    docs = relationship('ResultFile', back_populates='owner', lazy='subquery')

    def __repr__(self):
        return f'{self.username} uuid: {self.id}'
