from typing import List, Union
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from api import common
from api.common import schemas
from api.common import summary
from api.crud import user
from ..crud import home as crud  
from api.common.get_db import get_db
from fastapi import APIRouter

router = APIRouter()


@router.post("/users/{user_id}/homes/residential")
async def create_residentational_for_user(user_id: str, home: schemas.HomeCreate, db: Session = Depends(get_db)):
    db_user = await user.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    result = await crud.create_home(db=db, home=home, user_id=user_id)
    if result is None:
        raise HTTPException(status_code=400, detail="Home not created")
    return result

@router.post("/users/{user_id}/homes/business")
async def create_business_home_for_user(user_id: str, home: schemas.BusinessCreate, db: Session = Depends(get_db)):
    db_user = await user.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    result = await crud.create_business_home(db=db, home=home, user_id=user_id)
    if result is None:
        raise HTTPException(status_code=400, detail="Home not created")
    return result


@router.get("/homes/{home_id}")
async def read_home(home_id: str, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    return db_home

@router.post("/homes/{home_id}/chat")
async def get_home_chat(home_id: str, chat: schemas.Chat, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    result = await crud.get_home_chat(db=db, home_id=home_id, chat=chat)
    if result is None:
        raise HTTPException(status_code=400, detail="Chat not created")
    return result
    

@router.get("/users/{user_id}/homes")
async def read_homes(skip: int = 0, limit: int = 100, user_id: str = None, db: Session = Depends(get_db)):
    result =  await crud.get_homes(db, skip=skip, limit=limit, user_id=user_id)
    response = []
    for home in result:
        response.append(home.toJSON())
    return response
  

@router.put("/homes/{home_id}/residential")
async def update_home(home_id: str, home: schemas.HomeUpdate, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    response = await crud.update_home(db=db, home=home, home_id=home_id)
    if response is None:
        raise HTTPException(status_code=400, detail="Home not updated")
    return response

@router.put("/homes/{home_id}/business")
async def update_business_home(home_id: str, home: schemas.BusinessUpdate, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    response = await crud.update_business_home(db=db, home=home, home_id=home_id)
    if response is None:
        raise HTTPException(status_code=400, detail="Home not updated")
    return response



@router.get("/homes/{home_id}/image")
async def get_home_image(home_id: str, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found for image")
    return await crud.get_home_image(db=db, home_id=home_id)

@router.delete("/homes/{home_id}")
async def delete_home(home_id: str, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    return await crud.delete_home(db=db, home_id=home_id)

@router.get("/homes/{home_id}/summary")
async def get_home_summary(home_id: str, db: Session = Depends(get_db)):
    db_home = await crud.get_home(db, home_id=home_id)
    if db_home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    return await summary.get_home_summary(db=db, home_id=home_id) 





    
