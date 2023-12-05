from pathlib import Path


APP_ROOT_PATH = Path(__file__).resolve().parent.parent
MEDIA_DIR_PATH = APP_ROOT_PATH / 'app/media'


if __name__ == '__main__':
    print(MEDIA_DIR_PATH)
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
