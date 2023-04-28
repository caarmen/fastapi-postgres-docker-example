from pydantic import BaseModel


class Greeting(BaseModel):
    text: str

    class Config:
        orm_mode = True
