import json
from uuid import uuid4
from sqlalchemy.orm import Session
from api.chat.chat import generate_chat_response_home
from api.chat.home import generate_home_design_response
from api.chat.business import generate_bunisess_design_response
from api.common import models
from api.common.image import get_image
from api.common.schemas import Chat, HomeCreate, HomeUpdate, BusinessCreate
from api.common.summary import generate_prompt_for_image


async def create_business_home(db: Session, home: BusinessCreate, user_id: str = None):
    if home.type != "business":
        return None   
    
    user_ansewr = {
        "question1": home.question1,
        "question2": home.question2,
        "question3": home.question3,
        "question4": home.question4,
        "question5": home.question5,
        "question6": home.question6,
        "question7": home.question7,
        "question8": home.question8,
        "question9": home.question9,
        "question10": home.question10,
        "question11": home.question11,
        "question12": home.question12,
        "question13": home.question13, 
        "question14": home.question14,
        "question15": home.question15,
        
    }
    
    respose = generate_bunisess_design_response(user_ansewr) 
    if respose is None:
        return None
    db_home = models.Home(
        id=str(uuid4()),
        title=home.title,
        home_type=home.type,
        user_id=user_id,
        data=json.dumps(respose[0]),
        context=json.dumps(respose[1]),
    )
    db.add(db_home)
    db.commit()
    db.refresh(db_home)
    return db_home.toJSON()

async def create_home(db: Session, home: HomeCreate, user_id: str = None):
    
    
    if home.type != "home":
        return None
    
    user_ansewr = {
        "question1": home.question1,
        "question2": home.question2,
        "question3": home.question3,
        "question4": home.question4,
        "question5": home.question5,
        "question6": home.question6,
        "question7": home.question7,
        "question8": home.question8,
        "question9": home.question9,
        "question10": home.question10,
        "question11": home.question11,
        "question12": home.question12,
        "question13": home.question13, 
        "question14": home.question14
        
    }
        
    respose = generate_home_design_response(user_ansewr)
    
    if respose is None:
        return None
    db_home = models.Home(
        id=str(uuid4()),
        title=home.title,
        home_type=home.type,
        user_id=user_id,
        data=json.dumps(respose[0]),
        context=json.dumps(respose[1]),
    )
    db.add(db_home)
    db.commit()
    db.refresh(db_home)
    return db_home.toJSON()

async def get_home(db: Session, home_id: str):
    result = db.query(models.Home).filter(models.Home.id == home_id).first()
    if result is None:
        return None
    return result.toJSON()

async def get_homes(db: Session, skip: int = 0, limit: int = 100, user_id: str = None):
    return db.query(models.Home).filter(models.Home.user_id == user_id).offset(skip).limit(limit).all()

async def update_home(db: Session, home: HomeUpdate, home_id: str):
    user_ansewr = {
        "question1": home.question1,
        "question2": home.question2,
        "question3": home.question3,
        "question4": home.question4,
        "question5": home.question5,
        "question6": home.question6,
        "question7": home.question7,
        "question8": home.question8,
        "question9": home.question9,
        "question10": home.question10,
        "question11": home.question11,
        "question12": home.question12,
        "question13": home.question13, 
        "question14": home.question14

        
    }
    db_home = db.query(models.Home).filter(models.Home.id == home_id).first()
    response = generate_home_design_response(user_ansewr)
    if response is None:
        return None
    db_home.title = home.title
    db_home.data = json.dumps(response[0])
    db_home.context = json.dumps(response[1])
    db.commit()
    db.refresh(db_home)
    return db_home.toJSON()

async def update_business_home(db: Session, home: BusinessCreate, home_id: str):
    user_ansewr = {
        "question1": home.question1,
        "question2": home.question2,
        "question3": home.question3,
        "question4": home.question4,
        "question5": home.question5,
        "question6": home.question6,
        "question7": home.question7,
        "question8": home.question8,
        "question9": home.question9,
        "question10": home.question10,
        "question11": home.question11,
        "question12": home.question12,
        "question13": home.question13, 
        "question14": home.question14,
        "question15": home.question15,
        
    }
    db_home = db.query(models.Home).filter(models.Home.id == home_id).first()
    response = generate_bunisess_design_response(user_ansewr)
    if response is None:
        return None
    db_home.title = home.title
    db_home.data = json.dumps(response[0])
    db_home.context = json.dumps(response[1])
    db.commit()
    db.refresh(db_home)
    return db_home.toJSON()

async def delete_home(db: Session, home_id: str):
    db_home = db.query(models.Home).filter(models.Home.id == home_id).first()
    db.delete(db_home)
    db.commit()
    return db_home.toJSON()

async def get_home_image(db: Session, home_id: str):
    db_home = db.query(models.Home).filter(models.Home.id == home_id).first()
    if db_home is None:
        return None
    prompt =  generate_prompt_for_image(db_home.toJSON())
    image_url = await get_image(prompt)
    print(image_url)
    if image_url is None:
        return None
    db_home.images = json.dumps(image_url)
    db.commit()
    db.refresh(db_home)
    print(image_url)
    return db_home.toJSON()
    
    
async def get_home_chat(db: Session, home_id: str, chat: Chat):
    return await generate_chat_response_home(db=db, home_id=home_id, chat= chat.chat)
    
    