from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for request validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI on Render"}

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}
