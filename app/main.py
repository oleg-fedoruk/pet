import uvicorn
from fastapi import FastAPI

from app.core.database import engine
from app.profiles.auth import auth_backend
from app.profiles.schemas import UserRead, UserRegister, UserUpdate
from app.routers.clients import client_router
from app.routers.ocr import image_router
from app.routers.profiles import fastapi_users
from app.routers.tpdf import tpdf_router

app = FastAPI()
app.include_router(image_router)
app.include_router(tpdf_router)
app.include_router(client_router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserRegister),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.on_event("startup")
async def startup():
    await engine.connect()


@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)

# TODO
#  - использование системы аутентификации - зависимости для всех роутов
#  - создать привязку файла к пользователю
#  - сделать миграции
#  - создать crud для этих моделей
#  - сделать страницу для внесения основных данных (PersonalData)
#  - сделать возможность внесения данных в pdf
# 1. Доработать систему авторизации
# 2. Возможность корректировки полей на анкете
# 3. Возможнось создания записи с данными клиента
# 4. Генерация анкеты по внесённым данным
# 5. Запуск проекта с поднятием БД (docker)

