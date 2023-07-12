import uvicorn
from fastapi import FastAPI

from app.ocr.api import image_router
from app.tpdf.api import tpdf_router

app = FastAPI()
app.include_router(image_router)
app.include_router(tpdf_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
