import io

from fastapi import APIRouter
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import Response, HTMLResponse
from starlette.templating import Jinja2Templates

from app.tpdf.tpdf import TPdf

tpdf_router = APIRouter(prefix="/pdf", tags=["pdf"])
templates = Jinja2Templates(directory="templates")


@tpdf_router.get("/file")
async def get_new_file(background_tasks: BackgroundTasks) -> Response:
    data = {
        "last_name": "Федорук",
        "first_name": "Кристина",
        "middle_name": "Дмитриевна",
        "gender": "Ж",
        "birth_date": "01.01.2000",
        "birth_place": "г.Москва",
        "registration": "г.Москва, ул. Полковника Исаева, дом 17, кв 43",
        "1_work": "Радистка 3 категории, в/ч 89031",
        "2_work": "Радистка 1 категории, в/ч 17043",
        "3_work": "Командир отделения радистов, в/ч 17043 главного управления"
        " разведки комитета государственной безопасности республики Беларусь.",
    }

    # перечень документов в комплекте
    complete = [
        ("spain", 1),
    ]

    # загружаем данные в основной класс и получаем комплект документов в pdf
    tpdf = TPdf(**data)
    # можно сгенерировать один файл или комплект документов
    # file = tpdf.get_pdf('ZayavlenieNaZagranpasport ', b64='False')
    file = tpdf.get_complete(complete, b64="False")
    buffer = io.BytesIO()
    buffer.write(file)
    background_tasks.add_task(buffer.close)
    headers = {"Content-Disposition": 'inline; filename="out.pdf"'}
    return Response(buffer.getvalue(), headers=headers, media_type="application/pdf")


@tpdf_router.get("/zagran")
async def get_zagran(background_tasks: BackgroundTasks) -> Response:
    data = {
        "last_name": "Федорук",
        "first_name": "Кристина",
        "middle_name": "Дмитриевна",
        "gender": "Ж",
        "birth_date": "05.11.1997",
        "birth_place": "г.Москва",
        "registration": "г.Пушкино, ул. Гоголя, дом 24, кв 109",
        "1_work": "Радистка 3 категории, в/ч 89031",
        "2_work": "Радистка 1 категории, в/ч 17043",
        "3_work": "Командир отделения радистов, в/ч 17043 главного управления разведки комитета"
        " государственной безопасности республики Беларусь.",
    }

    # перечень документов в комплекте
    complete = [
        ("ZayavlenieNaZagranpasport", 1),
    ]

    # загружаем данные в основной класс и получаем комплект документов в pdf
    tpdf = TPdf(**data)
    # можно сгенерировать один файл или комплект документов
    # file = tpdf.get_pdf('ZayavlenieNaZagranpasport ', b64='False')
    file = tpdf.get_complete(complete, b64="False")
    buffer = io.BytesIO()
    buffer.write(file)
    background_tasks.add_task(buffer.close)
    headers = {"Content-Disposition": 'inline; filename="out.pdf"'}
    return Response(buffer.getvalue(), headers=headers, media_type="application/pdf")


@tpdf_router.get("/positioning", response_class=HTMLResponse)
async def positioning(request: Request, pdf_name: str, page_num: int):
    tpdf = TPdf()
    # дефолтные параметры
    in_data = {
        "pdf_name": "ClearPage",
        "page_num": "1",
    }
    in_data.update(dict(pdf_name=pdf_name, page_num=page_num))
    fields = tpdf.load_fields_from_file(name=in_data["pdf_name"], to_front=True)
    in_data.update({"fields": fields})
    return templates.TemplateResponse(
        "positioning.html",
        {"request": request, "fields": fields, "pdf_name": pdf_name, **in_data},
    )


@tpdf_router.get("/get_file")
async def get_file(pdf_name: str):
    """Для примера в строку запроса можно передать ?pdf_name=ZayavlenieNaZagranpasport"""
    tpdf = TPdf()
    file = tpdf.get_pdf(pdf_name, b64="False", fill_x=True)
    buffer = io.BytesIO()
    buffer.write(file)
    # background_tasks.add_task(buffer.close)
    headers = {"Content-Disposition": 'inline; filename="out.pdf"'}
    return Response(buffer.getvalue(), headers=headers, media_type="application/pdf")
