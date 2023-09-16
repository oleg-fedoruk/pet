from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base


class ExternalFile(Base):
    __tablename__ = 'external_files'
    __tableargs__ = {
        'comment': 'Внешние загруженные файлы'
    }

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, comment='Идентификатор')
    title = Column(String, index=True, comment='Наименование')
    file_path = Column(String, comment='Файл')

    owner_id = Column(Integer, ForeignKey('users_profiles.id'), comment='Владелец файла')
    owner = relationship('User', back_populates='files', lazy='subquery')

    created_at = Column(DateTime, comment='Дата и время создания')

    def __repr__(self):
        return f'{self.title} uuid: {self.id}'


class ResultFile(Base):
    __tablename__ = 'result_files'
    __tableargs__ = {
        'comment': 'Сгенерированные файлы'
    }

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, comment='Идентификатор')
    title = Column(String, index=True, comment='Наименование')
    file_path = Column(String, comment='Файл')

    owner_id = Column(Integer, ForeignKey('users_profiles.id'), comment='Владелец файла')
    owner = relationship('User', back_populates='files', lazy='subquery')

    created_at = Column(DateTime, comment='Дата и время создания')

    def __repr__(self):
        return f'{self.title} uuid: {self.id}'
