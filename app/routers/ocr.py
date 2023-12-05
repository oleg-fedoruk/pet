from fastapi import APIRouter, Form, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.core.database import get_session
from app.dependencies import current_user
from app.ocr.services import save_file
from app.profiles.models import User

image_router = APIRouter(prefix='/image', tags=["image"])
templates = Jinja2Templates(directory="templates")


@image_router.post('/')
async def upload_image(
        title: str = Form(...),
        file: UploadFile = File(...),
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_session)
):
    # TODO correct response
    return await save_file(user=user, file=file, title=title, session=session)
