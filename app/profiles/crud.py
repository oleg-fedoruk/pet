from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.profiles.schemas import UserInput, UserPatch


class UserCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: UserInput) -> User:
        values = data.dict()

        user = User(**values)
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

    async def patch(self, user_id: str | UUID, data: UserPatch) -> User:
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

#
#
#
# def select_all_users():
#     with Session(engine) as session:
#         statement = select(User)
#         res = session.exec(statement).all()
#         return res
#
#
# def find_user(name):
#     with Session(engine) as session:
#         statement = select(User).where(User.username == name)
#         return session.exec(statement).first()
