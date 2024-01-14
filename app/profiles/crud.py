import contextlib
from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from fastapi_users.exceptions import UserAlreadyExists
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.profiles.manager import get_user_manager
from app.profiles.models import User, get_user_db
from app.profiles.schemas import UserCreate, UserUpdate


class UserCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **kwargs) -> User:

        user = User(**kwargs)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def get(self, user_id: str | int) -> User:
        statement = select(
            User
        ).where(
            User.id == user_id
        )
        results = await self.session.execute(statement=statement)
        user = results.scalar_one_or_none()

        if user is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The hero hasn't been found!"
            )

        return user

    async def get_by_username(self, username: str) -> User:
        statement = select(
            User
        ).where(
            User.username == username
        )
        results = await self.session.execute(statement=statement)
        user = results.scalar_one_or_none()

        if user is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The hero hasn't been found!"
            )

        return user

    async def patch(self, user_id: str | UUID, data: UserUpdate) -> User:
        user = await self.get(user_id=user_id)
        values = data.dict(exclude_unset=True)

        for k, v in values.items():
            setattr(user, k, v)

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def delete(self, user_id: str | int) -> bool:
        statement = delete(
            User
        ).where(
            User.id == user_id
        )

        await self.session.execute(statement=statement)
        await self.session.commit()

        return True


get_async_session_context = contextlib.asynccontextmanager(get_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(username: str, email: str, password: str, is_superuser: bool = False):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            email=email, password=password, is_superuser=is_superuser, username=username
                        )
                    )
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {email} already exists")
