from fastapi import APIRouter, Form, UploadFile, File
from starlette.templating import Jinja2Templates

from ocr.services import save_image
from profiles.models import User

video_router = APIRouter(prefix='/image', tags=["image"])
templates = Jinja2Templates(directory="templates")


@video_router.post('/')
async def upload_image(
        title: str = Form(...),
        extension: str = Form(...),
        file: UploadFile = File(...)
):
    user = User(id=1, username='Oleg')
    return await save_image(user=user, file=file, title=title, extension=extension)
