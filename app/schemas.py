from pydantic import BaseModel

class ItemSchema(BaseModel):
    id: int
    name: str

class ItemCreateSchema(BaseModel):
    name: str