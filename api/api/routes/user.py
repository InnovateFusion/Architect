from typing import List, Union
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from api.common import schemas
from ..crud import user as crud
from api.common.get_db import get_db
from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    response = await crud.create_user(db=db, user=user)
    if response is None:
        raise HTTPException(status_code=400, detail="User not created")
    return response

@router.get("/users/{user_id}")
async def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users")
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    result =  await crud.get_users(db, skip=skip, limit=limit)
    response = []
    for user in result:
        response.append(user.toJSON())
    return response

@router.put("/users/{user_id}")
async def update_user(user_id: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.update_user(db=db, user=user, user_id=user_id)

@router.delete("/users/{user_id}")
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.delete_user(db=db, user_id=user_id)


