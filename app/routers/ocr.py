from fastapi import APIRouter, Form, UploadFile, File, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.core.database import get_session
from app.dependencies import current_user
from app.ocr.crud import ExternalFileCRUD
from app.ocr.schemas import FileOut
from app.ocr.services import save_file
from app.profiles.models import User

image_router = APIRouter(prefix='/image', tags=["image"])
templates = Jinja2Templates(directory="templates")


@image_router.post('/', response_model=FileOut)
async def upload_image(
        title: str = Form(...),
        file: UploadFile = File(...),
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_session),
):
    if not (file.content_type == 'image/jpeg' or file.content_type == 'image/png'):
        raise HTTPException(status_code=418, detail="It isn't png or jpeg")
    response = await save_file(user=user, file=file, title=title, session=session)
    return response


@image_router.get('/{file_id}', dependencies=[Depends(current_user)], response_model=FileOut)
async def upload_image(
        file_id: str,
        session: AsyncSession = Depends(get_session),
):
    file_manager = ExternalFileCRUD(session=session)
    response = await file_manager.get(file_id)
    return response
