import os
from pathlib import Path

APP_ABSOLUTE_ROOT_PATH = Path(__file__).resolve()
PARENT_DIRECTORY = APP_ABSOLUTE_ROOT_PATH.parent.parent.parent
MEDIA_DIR_PATH = Path('media')

SECRET_KEY = os.environ.get('SECRET_KEY', '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30)

DATABASE_URL = os.environ.get(
    'DATABASE_URL', 'postgresql+asyncpg://postgres:postgres@0.0.0.0:5431/postgres',
)  # connect string for the real database

TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL", "postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test",
)


if __name__ == '__main__':
    pass
