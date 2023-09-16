from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.profiles.crud import UserCRUD


async def get_users_crud(
        session: AsyncSession = Depends(get_db)
) -> UserCRUD:
    return UserCRUD(session=session)
