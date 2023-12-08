from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.orm_methods import save_file_to_uploads
from app.ocr.crud import ExternalFileCRUD
from app.ocr.schemas import FileCreate
from app.profiles.models import User


async def save_file(
        user: User,
        file: UploadFile,
        title: str,
        session: AsyncSession
):
    file_path = await save_file_to_uploads(file=file)
    img = FileCreate(id=file_path.stem, title=title, file_path=file_path.as_posix(), owner_id=user.id)
    file_manager = ExternalFileCRUD(session=session)
    created_file = await file_manager.create(img)
    return created_file
