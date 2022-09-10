import uvicorn
from fastapi import FastAPI
from ocr.endpoints import video_router
from profiles.endpoints import user_router

app = FastAPI()
app.include_router(video_router)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
