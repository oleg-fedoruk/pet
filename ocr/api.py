from fastapi import APIRouter, BackgroundTasks, Form, UploadFile, File
from starlette.templating import Jinja2Templates

video_router = APIRouter(prefix='/image', tags=["image"])
templates = Jinja2Templates(directory="templates")


@video_router.post('/')
async def upload_image(
        back_tasks: BackgroundTasks,
        title: str = Form(...),
        extension: str = Form(...),
        file: UploadFile = File(...)
):

    return await decode_image(file, title, extension, back_tasks)
