import asyncio
import contextlib
from contextlib import ExitStack

import pytest
from anyio import Path, open_file
from fastapi import Depends
from httpx import AsyncClient
from starlette.testclient import TestClient
from fastapi_users.exceptions import UserAlreadyExists
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

import app.settings as settings
from app.core.database import get_session, sessionmanager
from app.main import init_app
from app.profiles.manager import get_user_manager
from app.profiles.models import User
from app.profiles.schemas import UserCreate


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def app(event_loop):
    with ExitStack():
        yield init_app(init_db=False)


@pytest.fixture(scope="function")
async def client(app):
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
async def connection_test(event_loop):
    sessionmanager.init(settings.TEST_DATABASE_URL)
    yield
    await sessionmanager.close()


@pytest.fixture(scope="function", autouse=True)
async def create_tables(connection_test):
    async with sessionmanager.connect() as connection:
        await sessionmanager.drop_all(connection)
        await sessionmanager.create_all(connection)


@pytest.fixture(scope="function", autouse=True)
async def session_override(app, connection_test):
    async def get_db_override():
        async with sessionmanager.session() as session:
            yield session

    app.dependency_overrides[get_session] = get_db_override
    return get_db_override


@pytest.fixture
async def create_user_in_database(session_override):
    async def get_user_db(session: AsyncSession = Depends(session_override)):
        yield SQLAlchemyUserDatabase(session, User)

    get_async_session_context = contextlib.asynccontextmanager(session_override)
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
                        return user
        except UserAlreadyExists:
            print(f"User {email} already exists")

    return create_user


@pytest.fixture
async def cleanup():
    # TODO DANGEROUS refactor to a better solution
    yield
    path = Path(__file__).parent / 'media'
    async for image in path.glob('*.jpeg'):
        await image.unlink()
