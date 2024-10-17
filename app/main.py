from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.models import Item, Base
from app.schemas import ItemSchema, ItemCreateSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
async def list_items(db: Session = Depends(get_db)) -> List[ItemSchema]:
    return db.query(Item).all()

@app.post("/items")
async def create_items(payload: ItemCreateSchema, db: Session = Depends(get_db)) -> ItemSchema:
    with db:
        item = Item(payload.model_dump())

        db.add(item)
        db.commit()
        db.refresh(item)
        return item