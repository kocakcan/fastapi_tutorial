from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Tutorial")

class Item(BaseModel):
    name: str
    price: float

items_db: dict[int, Item] = {}

@app.get("/")
def root():
    return {"message": "Hello from FastAPI tutorial!"}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"item_id": item_id, "item": item}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    return items_db[item_id]
