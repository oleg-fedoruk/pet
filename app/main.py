import uvicorn
from fastapi import FastAPI

from app.core.database import engine
from app.routers.clients import client_router
from app.routers.ocr import image_router
from app.routers.profiles import user_router
from app.routers.tpdf import tpdf_router

app = FastAPI()
app.include_router(image_router)
app.include_router(tpdf_router)
app.include_router(client_router)
app.include_router(user_router)


@app.on_event("startup")
async def startup():
    await engine.connect()


@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)

# TODO
#  - сделать создание пользователя/смену пароля
#  - использование системы аутентификации - зависимости для всех роутов
#  - создать привязку файла к пользователю
#  - сделать миграции
#  - создать crud для этих моделей
#  - сделать асинхронную работу с SQLAlchemy
#  - сделать страницу для внесения основных данных (PersonalData)
#  - сделать возможность внесения данных в pdf
# 1. Создание и авторизация пользователя
# 2. Возможность корректировки полей на анкете
# 3. Возможнось создания записи с данными клиента
# 4. Генерация анкеты по внесённым данным
# 5. Запуск проекта с поднятием БД (docker)

