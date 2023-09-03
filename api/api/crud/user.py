from sqlalchemy.orm import Session
from api.common import models, schemas
from uuid import uuid4

async def get_user(db: Session, user_id: str):
    result = db.query(models.User).filter(models.User.id == user_id).first()
    if result is None:
        return None
    return result.toJSON()

async def get_user_by_email(db: Session, email: str):
    result =  db.query(models.User).filter(models.User.email == email).first()
    if result is None:
        return None
    return result.toJSON()

async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

async def create_user(db: Session, user: schemas.UserCreate):
    
    if user.type not in ["architect", "client"]:
        return None
    
    db_user = models.User(
        id=str(uuid4()),
        email=user.email,
        firstname=user.firstname,
        lastname=user.lastname,
        user_type=user.type,
        password=user.password,
        profile_image=user.profile_image
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.toJSON()

async def update_user(db: Session, user: schemas.UserUpdate, user_id: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.firstname = user.firstname
    db_user.lastname = user.lastname
    db_user.profile_image = user.profile_image
    db.commit()
    return db_user.toJSON()

async def delete_user(db: Session, user_id: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user.toJSON()


