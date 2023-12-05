from uuid import uuid4

import aiofiles as aiofiles
from fastapi import UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.ocr.models import ExternalFile
from app.profiles.models import User
from app.settings import MEDIA_DIR_PATH


async def save_file(
        user: User,
        file: UploadFile,
        title: str,
        session: AsyncSession
):
    file_path = MEDIA_DIR_PATH / f'{user.id}_{uuid4()}.jpeg'  # TODO resolve problem with the file path creation
    if file.content_type == 'image/jpeg' or file.content_type == 'image/png':
        await write_file(file_path, file)
    else:
        raise HTTPException(status_code=418, detail="It isn't png or jpeg")
    img = ExternalFile(title=title, file_path=str(file_path), owner_id=user.id)
    session.add(img)
    await session.commit()


async def write_file(file_name: str, file: UploadFile):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)
