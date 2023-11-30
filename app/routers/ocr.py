from fastapi import APIRouter, Form, UploadFile, File
from starlette.templating import Jinja2Templates

from app.ocr.services import write_file
from app.profiles.models import User

image_router = APIRouter(prefix='/image', tags=["image"])
templates = Jinja2Templates(directory="templates")


@image_router.post('/')
async def upload_image(
        title: str = Form(...),
        extension: str = Form(...),
        file: UploadFile = File(...)
):
    user = User(id=1, username='Oleg')
    return await write_file(user=user, file=file, title=title, extension=extension)
