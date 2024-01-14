from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.profiles.crud import UserCRUD


async def get_users_crud(
        session: AsyncSession = Depends(get_session)
) -> UserCRUD:
    return UserCRUD(session=session)
