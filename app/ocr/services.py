from uuid import uuid4

import aiofiles as aiofiles
from fastapi import UploadFile, HTTPException, Depends
from sqlmodel import Session

from app.core.database import get_db
from app.ocr.models import Image
from app.profiles.models import User


async def save_image(
        user: User,
        file: UploadFile,
        title: str,
        extension: str,
        db: Session = Depends(get_db)
):
    file_name = f'media/{user.id}_{uuid4()}.mp4'
    if file.content_type == 'image/jpeg' or file.content_type == 'image/png':
        await write_image(file_name, file)
    else:
        raise HTTPException(status_code=418, detail="It isn't png or jpeg")
    img = Image(title=title, extension=extension, user_id=user.id)
    async with db as session:
        session.add(img)
        await session.commit()


async def write_image(file_name: str, file: UploadFile):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)
