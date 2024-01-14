from typing import Annotated

from fastapi import APIRouter, Form, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse

from app.core.database import get_session

client_router = APIRouter(prefix='/client', tags=["client"])


@client_router.get("/form")
async def main():
    content = """
                <body>
                    <form action="/client/files/" enctype="multipart/form-data" method="post">
                        <input name="file" type="file" multiple><br>
                        <label for="fname">First name:</label><br>
                        <input type="text" id="fname" name="first_name"><br>
                        <label for="lname">Last name:</label><br>
                        <input type="text" id="lname" name="last_name"><br>
                        <input type="submit">
                    </form>
                </body>
            """
    return HTMLResponse(content=content)


@client_router.post("/files/")
async def create_file(
        file: Annotated[UploadFile, File()],
        first_name: Annotated[str, Form()],
        last_name: Annotated[str, Form()],
        session: AsyncSession = Depends(get_session)
):
    # new_file = service.add_file(session, new_file.name, new_file.population)
    # try:
    #     await session.commit()
    #     return new_file
    # except IntegrityError as ex:
    #     await session.rollback()
    return {
        "first_name": first_name,
        "last_name": last_name,
        "fileb_content_type": file.content_type,
    }
