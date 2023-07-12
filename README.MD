## Подготовка Alembic
```alembic init migrations```
- в script.py.mako после импорта sqlalchemy пишем ```import sqlmodel```
- в alembic.ini изменить sqlalchemy.url на актуальный
- в env.py после импорта sqlalchemy пишем ```from sqlmodel import SQLModel```
- в env.py после импорта sqlmodel импортируем все модели ```from profiles.models import *```
- в env.py ставим ```target_metadata = SQLModel.metadata```
- создаём первый файл миграций ```alembic revision --autogenerate -m "init"```
- применяем миграцию ```alembic upgrade head```


## Docker DataBase
run-db:
	docker run --name tesseract_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=tesseract -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres