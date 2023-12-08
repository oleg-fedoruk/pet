from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.ocr.models import ExternalFile
from app.ocr.schemas import FileCreate


class ExternalFileCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: FileCreate) -> ExternalFile:
        values = data.model_dump()

        external_file = ExternalFile(**values)
        self.session.add(external_file)
        await self.session.commit()
        await self.session.refresh(external_file)

        return external_file

    async def get(self, file_id: str | int) -> Optional[ExternalFile]:
        statement = select(
            ExternalFile
        ).where(
            ExternalFile.id == file_id
        )
        results = await self.session.execute(statement=statement)
        file = results.scalar_one_or_none()
        return file
