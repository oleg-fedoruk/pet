from uuid import uuid4

import aiofiles
from fastapi import UploadFile

from app.settings import MEDIA_DIR_PATH


async def save_file_to_uploads(file: UploadFile):
    file_path = MEDIA_DIR_PATH / f'{uuid4()}.jpeg'
    file_path.parent.mkdir(parents=True, exist_ok=True)
    await write_file(file_path.as_posix(), file)
    return file_path


async def write_file(file_path: str, file: UploadFile):
    async with aiofiles.open(file_path, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)


def delete_file_from_uploads(file_name: str):
    file_path = MEDIA_DIR_PATH + file_name
    try:
        file_path.unlink()
    except Exception as e:
        print(e)
