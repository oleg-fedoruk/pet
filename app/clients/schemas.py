from pydantic import BaseModel


class ClientData(BaseModel):
    name: str
    surname: str
