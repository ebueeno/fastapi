from fastapi import APIRouter, Depends, HTTPException
from models import Item
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/crud", tags=["crud"])
items = []


@router.get("/items")
async def get_items():
    return items


@router.post("/items", status_code=201)
async def create_item(item: Item):
    items.append(item.dict())
    return item


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if 0 <= item_id < len(items):
        items[item_id].update(item.dict())
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item não encontrado")


@router.delete("item/{item_id}")
async def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        removed_item = items.pop(item_id)
        return removed_item
    raise HTTPException(status_code=404, detail="Item não encontrado")
