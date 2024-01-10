from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Depends
import app.settings as settings
from app.core.database import sessionmanager
from app.dependencies import current_user
from app.profiles.auth import auth_backend
from app.profiles.schemas import UserRead, UserRegister, UserUpdate
from app.routers.clients import client_router
from app.routers.ocr import image_router
from app.routers.profiles import fastapi_users
from app.routers.tpdf import tpdf_router


def init_app(init_db=True):
    lifespan = None
    if init_db:
        sessionmanager.init(settings.DATABASE_URL)

        @asynccontextmanager
        async def lifespan(application: FastAPI):
            yield
            if sessionmanager._engine is not None:  # noqa
                await sessionmanager.close()

    # app = FastAPI(dependencies=[Depends(current_user)])
    server = FastAPI(dependencies=[], title="Tesseract Server", lifespan=lifespan)
    server.include_router(image_router)
    server.include_router(tpdf_router)
    server.include_router(client_router)
    server.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth/jwt",
        tags=["auth"],
    )
    server.include_router(
        fastapi_users.get_register_router(UserRead, UserRegister),
        prefix="/auth",
        tags=["auth"],
    )
    server.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["users"],
    )

    return server


app = init_app(True)

if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)

# TODO
#  - добавить Pytests
#  - внести линтеры и прекоммит-хуки (4 часть)
#  - проект таблиц для работы с данными паспортов
#  - обработка картинки (чтение данных с картинки)
#  - создать привязку файла к пользователю
#  - создать crud для этих моделей
#  - сделать страницу для внесения основных данных (PersonalData)
#  - сделать возможность внесения данных в pdf
# 1. Доработать систему авторизации
# 2. Возможность корректировки полей на анкете
# 3. Возможнось создания записи с данными клиента
# 4. Генерация анкеты по внесённым данным
# 5. Запуск проекта с поднятием БД (docker)
