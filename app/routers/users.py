from database import connection
from dependencies import get_token_header
from models import User
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy import select


router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


# @router.get("/")
# async def get_users():
#         query = User.select()
#     return await con.fetch_all(query)

@router.get("/", response_model=List[User.Model])
async def get_users():
    query = select(User.User)
    return await connection.conn.fetch_all(query)


@router.post(
    "/",
)
async def create_user(user_id: str):
    if user_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": user_id, "name": "The great Plumbus"}


@router.get("/{item_id}")
async def read_item(user_id: str):
    if user_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[user_id]["name"], "item_id": user_id}


@router.put(
    "/{user_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(user_id: str):
    if user_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": user_id, "name": "The great Plumbus"}
